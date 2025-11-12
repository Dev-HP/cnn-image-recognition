#!/usr/bin/env python3
"""
Script de teste para CNN.DEMO.py
Cria uma imagem de teste simples
"""

from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Criar uma imagem de teste simples (um círculo vermelho)
print("🎨 Criando imagem de teste...")

# Criar imagem 224x224 com fundo branco
img = Image.new('RGB', (224, 224), color='white')
draw = ImageDraw.Draw(img)

# Desenhar um círculo vermelho (simulando uma bola)
draw.ellipse([50, 50, 174, 174], fill='red', outline='darkred', width=3)

# Salvar imagem
img.save('test_image.jpg')
print("✅ Imagem de teste criada: test_image.jpg")

print("\n🚀 Agora execute:")
print("   python CNN.DEMO.py test_image.jpg")
