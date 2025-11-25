#!/usr/bin/env python3
"""
CNN.DEMO.py - Script CLI para reconhecimento de imagens usando MobileNetV2

Uso:
    python CNN.DEMO.py <caminho_da_imagem>

Exemplo:
    python CNN.DEMO.py test_image.jpg
"""

import sys
import os
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions


def print_usage():
    """Exibe instruções de uso do script"""
    print("=" * 60)
    print("CNN Image Recognition - Demo CLI")
    print("=" * 60)
    print("\nUso:")
    print("    python CNN.DEMO.py <caminho_da_imagem>")
    print("\nExemplo:")
    print("    python CNN.DEMO.py test_image.jpg")
    print("\nFormatos suportados: JPG, JPEG, PNG, BMP, GIF")
    print("=" * 60)


def load_and_preprocess_image(image_path):
    """
    Carrega e preprocessa uma imagem para o modelo MobileNetV2
    
    Args:
        image_path: Caminho para o arquivo de imagem
        
    Returns:
        Array numpy preprocessado pronto para predição
        
    Raises:
        FileNotFoundError: Se o arquivo não existir
        Exception: Se o arquivo não for uma imagem válida
    """
    # Verificar se o arquivo existe
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")
    
    try:
        # Carregar imagem
        img = Image.open(image_path)
        
        # Converter para RGB se necessário
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Redimensionar para 224x224 (tamanho esperado pelo MobileNetV2)
        img_resized = img.resize((224, 224))
        
        # Converter para array numpy
        img_array = np.array(img_resized)
        
        # Adicionar dimensão de batch
        img_array = np.expand_dims(img_array, axis=0)
        
        # Preprocessar para MobileNetV2
        img_array = preprocess_input(img_array)
        
        return img_array
        
    except Exception as e:
        raise Exception(f"Erro ao processar imagem: {str(e)}")


def main():
    """Função principal do script CLI"""
    
    # Verificar argumentos
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    try:
        # Carregar modelo
        print("🧠 Carregando modelo MobileNetV2...")
        model = MobileNetV2(weights='imagenet')
        print("✅ Modelo carregado com sucesso!\n")
        
        # Carregar e preprocessar imagem
        print(f"📸 Processando imagem: {image_path}")
        img_array = load_and_preprocess_image(image_path)
        print("✅ Imagem processada!\n")
        
        # Fazer predição
        print("🔍 Analisando imagem...")
        predictions = model.predict(img_array, verbose=0)
        
        # Decodificar top 5 predições
        results = decode_predictions(predictions, top=5)[0]
        
        # Exibir resultados
        print("\n" + "=" * 60)
        print("🎯 TOP 5 PREDIÇÕES")
        print("=" * 60)
        
        for i, (class_id, name, confidence) in enumerate(results, 1):
            # Formatar nome (substituir underscores e capitalizar)
            formatted_name = name.replace("_", " ").title()
            confidence_percent = confidence * 100
            
            # Criar barra de progresso visual
            bar_length = int(confidence_percent / 2)  # 50 caracteres = 100%
            bar = "█" * bar_length + "░" * (50 - bar_length)
            
            print(f"\n{i}. {formatted_name}")
            print(f"   [{bar}] {confidence_percent:.2f}%")
        
        print("\n" + "=" * 60)
        print("✅ Análise concluída!")
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"\n❌ Erro: {e}")
        print("\nVerifique se o caminho do arquivo está correto.")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        print("\nVerifique se o arquivo é uma imagem válida.")
        sys.exit(1)


if __name__ == "__main__":
    main()
