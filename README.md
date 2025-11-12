# 🧠 CNN Image Recognition

Sistema de reconhecimento de imagens usando Redes Neurais Convolucionais (CNN) com interface web interativa.

## 🎯 Funcionalidades

- ✅ Reconhecimento de imagens usando MobileNetV2 pré-treinado
- ✅ Interface web moderna com drag & drop
- ✅ API REST com FastAPI
- ✅ Suporte para mais de 1000 categorias de objetos
- ✅ Análise em tempo real
- ✅ Top 5 previsões com porcentagem de confiança

## 🚀 Como Usar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar o Servidor Web

```bash
python cnn_api.py
```

Acesse: **http://localhost:8080**

### 3. Usar via Linha de Comando

```bash
python CNN.DEMO.py sua_imagem.jpg
```

## 📦 Dependências

- Python 3.8+
- TensorFlow 2.x
- FastAPI
- Pillow
- Uvicorn

## 🖼️ Interface Web

A interface permite:
- Upload de imagens via drag & drop ou clique
- Preview da imagem antes da análise
- Resultados visuais com barras de confiança
- Design responsivo e moderno

## 🧪 Testes

Execute o script de teste:

```bash
python test_cnn.py
python test_cnn_simple.py test_image.jpg
```

## 📊 Modelo

Utiliza o **MobileNetV2** treinado no dataset ImageNet:
- Mais de 1000 categorias
- Otimizado para performance
- Precisão de reconhecimento de classe mundial

## 🛠️ Tecnologias

- **Backend**: FastAPI + Uvicorn
- **IA**: TensorFlow + Keras
- **Frontend**: HTML5 + CSS3 + JavaScript Vanilla
- **Modelo**: MobileNetV2 (ImageNet)

## 📝 Estrutura do Projeto

```
.
├── cnn_api.py              # API FastAPI
├── CNN.DEMO.py             # Script CLI
├── requirements.txt        # Dependências
├── templates/
│   └── cnn_upload.html    # Interface web
├── test_cnn.py            # Criar imagem de teste
└── test_cnn_simple.py     # Teste simples
```

## 🎓 Uso Educacional

Este projeto foi desenvolvido para demonstrar o poder das Redes Neurais Convolucionais de forma prática e acessível.

## 📄 Licença

MIT License

## 👨‍💻 Autor

Desenvolvido para a palestra "Desvendando as Redes Neurais"
