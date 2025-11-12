#!/usr/bin/env python3
import sys
import os

print("Iniciando teste...", flush=True)
print(f"Python version: {sys.version}", flush=True)
print(f"Argumentos: {sys.argv}", flush=True)

try:
    import tensorflow as tf
    print(f"TensorFlow version: {tf.__version__}", flush=True)
    
    from tensorflow.keras.applications import MobileNetV2
    from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
    from PIL import Image
    import numpy as np
    
    print("Carregando modelo...", flush=True)
    model = MobileNetV2(weights='imagenet')
    print("Modelo carregado!", flush=True)
    
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
        print(f"Processando imagem: {img_path}", flush=True)
        
        img = Image.open(img_path)
        img = img.convert('RGB')
        img = img.resize((224, 224))
        
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        print("Fazendo previsão...", flush=True)
        predictions = model.predict(img_array, verbose=1)
        
        results = decode_predictions(predictions, top=3)[0]
        
        print("\nResultados:", flush=True)
        for i, (class_id, name, confidence) in enumerate(results, 1):
            print(f"{i}. {name}: {confidence*100:.2f}%", flush=True)
    else:
        print("Uso: python test_cnn_simple.py <imagem>", flush=True)
        
except Exception as e:
    print(f"ERRO: {e}", flush=True)
    import traceback
    traceback.print_exc()
