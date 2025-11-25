# 🧠 CNN Image Recognition

Sistema de reconhecimento de imagens usando Redes Neurais Convolucionais (CNN) com arquitetura moderna de frontend/backend separados.

## 🎯 Funcionalidades

- ✅ Reconhecimento de imagens usando MobileNetV2 pré-treinado
- ✅ Interface web moderna com drag & drop
- ✅ API REST com FastAPI
- ✅ Suporte para mais de 1000 categorias de objetos
- ✅ Análise em tempo real
- ✅ Top 5 previsões com porcentagem de confiança
- ✅ Deploy automatizado via GitHub Actions
- ✅ Frontend hospedado no GitHub Pages
- ✅ Backend hospedado no Vercel
- ✅ CORS configurado para comunicação cross-origin
- ✅ Health check e verificação de conectividade

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────┐
│     Frontend (GitHub Pages)             │
│  - Interface HTML/CSS/JS                │
│  - Configuração via config.js           │
│  - Deploy automático via Actions        │
└─────────────────────────────────────────┘
                  │
                  │ HTTPS + CORS
                  ▼
┌─────────────────────────────────────────┐
│     Backend (Vercel Serverless)         │
│  - FastAPI + MobileNetV2                │
│  - Endpoints: /predict, /health         │
│  - Deploy automático via Git            │
└─────────────────────────────────────────┘
```

## 🚀 Como Usar

### Opção 1: Usar a Aplicação Online (Recomendado)

Acesse a aplicação já deployada:
- **Frontend**: `https://seu-usuario.github.io/seu-repo/`
- Faça upload de uma imagem e veja a mágica acontecer!

### Opção 2: Desenvolvimento Local

#### 1. Instalar Dependências

```bash
# Backend
pip install -r backend/requirements.txt

# Frontend (apenas abrir no navegador)
```

#### 2. Iniciar o Backend

```bash
python backend/cnn_api.py
```

#### 3. Configurar Frontend para Local

Edite `docs/config.js`:
```javascript
baseURL: 'http://localhost:8080',
```

#### 4. Abrir Frontend

Abra `docs/index.html` no navegador ou use um servidor local:
```bash
# Python
python -m http.server 3000 --directory docs

# Node.js
npx serve docs
```

### Opção 3: Usar via Linha de Comando

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
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions para deploy automático
├── backend/
│   ├── cnn_api.py             # API FastAPI com CORS
│   └── requirements.txt        # Dependências do backend
├── docs/                       # Frontend (GitHub Pages)
│   ├── index.html             # Interface web principal
│   └── config.js              # Configuração da API
├── templates/
│   └── cnn_upload.html        # Template original (legado)
├── CNN.DEMO.py                # Script CLI para testes
├── test_cnn.py                # Criar imagem de teste
├── test_cnn_simple.py         # Teste simples
├── vercel.json                # Configuração do Vercel
├── requirements.txt           # Dependências raiz
├── DEPLOY.md                  # 📚 Guia completo de deploy
└── README.md                  # Este arquivo
```

## 🚀 Deploy

### Deploy Rápido

1. **Frontend (GitHub Pages)**:
   - Habilite GitHub Pages nas configurações do repositório
   - Selecione "GitHub Actions" como source
   - Push para `main` → Deploy automático!

2. **Backend (Vercel)**:
   - Conecte seu repositório no [Vercel](https://vercel.com)
   - Configure `ALLOWED_ORIGINS` com sua URL do GitHub Pages
   - Deploy automático a cada push!

3. **Conectar**:
   - Atualize `docs/config.js` com a URL do Vercel
   - Push → Pronto! 🎉

📚 **Guia completo**: Veja [DEPLOY.md](DEPLOY.md) para instruções detalhadas

### Configuração de CORS

O backend está configurado para aceitar requisições de:
- `http://localhost:8080` (desenvolvimento)
- `http://localhost:3000` (desenvolvimento)
- `https://*.github.io` (GitHub Pages)

Configure origens adicionais via variável de ambiente `ALLOWED_ORIGINS` no Vercel.

## 🔧 Configuração

### Variáveis de Ambiente (Backend)

```bash
# Vercel Dashboard → Settings → Environment Variables
ALLOWED_ORIGINS=https://seu-usuario.github.io,https://outro-dominio.com
```

### Configuração do Frontend

Edite `docs/config.js`:
```javascript
const API_CONFIG = {
    baseURL: 'https://seu-projeto.vercel.app',
    // ...
};
```

## 🧪 Testes

### Testar Backend Localmente

```bash
# Iniciar servidor
python backend/cnn_api.py

# Testar health check
curl http://localhost:8080/health

# Testar predição
curl -X POST -F "file=@test_image.jpg" http://localhost:8080/predict
```

### Testar CLI

```bash
# Criar imagem de teste
python test_cnn.py

# Testar reconhecimento
python CNN.DEMO.py test_image.jpg
```

### Testar Frontend

1. Abra `docs/index.html` no navegador
2. Verifique se o banner mostra "✅ Servidor online"
3. Faça upload de uma imagem
4. Verifique as predições

## 🐛 Troubleshooting

### CORS Error
- Verifique `ALLOWED_ORIGINS` no Vercel
- Certifique-se de usar HTTPS na URL do GitHub Pages
- Veja logs no Console do navegador (F12)

### Backend Timeout
- Vercel free tier tem limite de 10s
- Considere Render ou Railway para processos mais longos

### Frontend não atualiza
- Limpe cache do navegador (Ctrl+Shift+R)
- Verifique GitHub Actions para erros
- Aguarde 1-2 minutos para propagação

📚 Mais soluções em [DEPLOY.md](DEPLOY.md)

## 🎓 Uso Educacional

Este projeto foi desenvolvido para demonstrar o poder das Redes Neurais Convolucionais de forma prática e acessível, com arquitetura moderna de microserviços.

## 📄 Licença

MIT License

## 👨‍💻 Autor

Desenvolvido para a palestra "Desvendando as Redes Neurais"

## 🌟 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

## 📚 Recursos

- [Documentação FastAPI](https://fastapi.tiangolo.com/)
- [TensorFlow/Keras](https://www.tensorflow.org/)
- [GitHub Pages](https://pages.github.com/)
- [Vercel](https://vercel.com/docs)
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)
