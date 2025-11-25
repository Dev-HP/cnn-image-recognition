#!/usr/bin/env python3
"""
API FastAPI para reconhecimento de imagens com CNN
"""

import io
import os
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

# Criar aplicação FastAPI
app = FastAPI(title="CNN Image Recognition")

# Configurar CORS
# Obter origens permitidas da variável de ambiente ou usar padrões
allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "")
if allowed_origins_env:
    # Se houver variável de ambiente, dividir por vírgula
    allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]
else:
    # Origens padrão para desenvolvimento e GitHub Pages
    allowed_origins = [
        "http://localhost:8080",
        "http://localhost:3000",
        "http://127.0.0.1:8080",
        "https://*.github.io",  # Permite qualquer subdomínio do GitHub Pages
    ]

# Adicionar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Log das origens permitidas
print("🌐 CORS configurado!")
print(f"📋 Origens permitidas: {', '.join(allowed_origins)}")

# Configurar templates
templates = Jinja2Templates(directory="templates")

# Carregar modelo CNN (uma única vez na inicialização)
print("🧠 Carregando modelo CNN...")
model = MobileNetV2(weights='imagenet')
print("✅ Modelo carregado!")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Página inicial com interface de upload"""
    return templates.TemplateResponse("cnn_upload.html", {"request": request})

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint para fazer previsão em uma imagem enviada
    """
    try:
        # Ler imagem do upload
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        
        # Converter para RGB se necessário
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Redimensionar para 224x224
        img_resized = img.resize((224, 224))
        
        # Converter para array numpy e preprocessar
        img_array = np.array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        # Fazer previsão
        predictions = model.predict(img_array, verbose=0)
        
        # Decodificar top 5 previsões
        results = decode_predictions(predictions, top=5)[0]
        
        # Formatar resultados
        formatted_results = [
            {
                "class_id": class_id,
                "name": name.replace("_", " ").title(),
                "confidence": float(confidence * 100)
            }
            for class_id, name, confidence in results
        ]
        
        return JSONResponse({
            "success": True,
            "predictions": formatted_results
        })
        
    except Exception as e:
        return JSONResponse({
            "success": False,
            "error": str(e)
        }, status_code=500)

@app.get("/health")
async def health():
    """Health check endpoint com informações de CORS"""
    return {
        "status": "ok",
        "model": "MobileNetV2",
        "cors_enabled": True,
        "allowed_origins": allowed_origins
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
