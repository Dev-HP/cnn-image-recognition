# 🚀 Guia de Deploy - CNN Image Recognition

Este guia fornece instruções completas para fazer deploy da aplicação CNN Image Recognition, com frontend no GitHub Pages e backend no Vercel.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:

- ✅ Conta no GitHub
- ✅ Conta no Vercel (gratuita)
- ✅ Git instalado localmente
- ✅ Node.js instalado (para Vercel CLI - opcional)
- ✅ Repositório Git com o código da aplicação

## 🎯 Arquitetura de Deploy

```
Frontend (GitHub Pages)  →  Backend (Vercel)
    docs/index.html      →  backend/cnn_api.py
    docs/config.js       →  MobileNetV2 Model
```

---

## 📦 Parte 1: Deploy do Frontend (GitHub Pages)

### Passo 1: Habilitar GitHub Pages

1. Acesse seu repositório no GitHub
2. Vá em **Settings** → **Pages**
3. Em **Source**, selecione **GitHub Actions**
4. Salve as configurações

### Passo 2: Fazer Push do Código

```bash
git add .
git commit -m "Setup GitHub Pages deployment"
git push origin main
```

### Passo 3: Verificar Deploy

1. Vá em **Actions** no seu repositório
2. Aguarde o workflow "Deploy to GitHub Pages" completar
3. Acesse a URL do GitHub Pages (será algo como `https://seu-usuario.github.io/seu-repo/`)

✅ **Frontend está no ar!** Mas ainda não funciona porque o backend não está configurado.

---

## 🔧 Parte 2: Deploy do Backend (Vercel)

### Opção A: Deploy via Vercel Dashboard (Recomendado)

#### Passo 1: Criar Conta no Vercel

1. Acesse [vercel.com](https://vercel.com)
2. Faça login com sua conta GitHub
3. Autorize o Vercel a acessar seus repositórios

#### Passo 2: Importar Projeto

1. Clique em **"Add New..."** → **"Project"**
2. Selecione seu repositório
3. Clique em **"Import"**

#### Passo 3: Configurar Projeto

1. **Framework Preset**: Other
2. **Root Directory**: `./` (raiz do projeto)
3. **Build Command**: (deixe vazio)
4. **Output Directory**: (deixe vazio)

#### Passo 4: Configurar Variáveis de Ambiente

Clique em **"Environment Variables"** e adicione:

```
ALLOWED_ORIGINS = https://seu-usuario.github.io
```

> ⚠️ **Importante**: Substitua `seu-usuario.github.io` pela URL real do seu GitHub Pages!

#### Passo 5: Deploy

1. Clique em **"Deploy"**
2. Aguarde o build completar (pode levar 2-3 minutos)
3. Copie a URL do projeto (será algo como `https://seu-projeto.vercel.app`)

### Opção B: Deploy via Vercel CLI

```bash
# Instalar Vercel CLI
npm i -g vercel

# Fazer login
vercel login

# Deploy
vercel

# Seguir os prompts:
# - Set up and deploy? Yes
# - Which scope? (sua conta)
# - Link to existing project? No
# - Project name? (nome do seu projeto)
# - In which directory is your code located? ./
# - Want to override settings? No

# Configurar variável de ambiente
vercel env add ALLOWED_ORIGINS
# Digite: https://seu-usuario.github.io

# Deploy para produção
vercel --prod
```

---

## 🔗 Parte 3: Conectar Frontend ao Backend

### Passo 1: Atualizar config.js

Edite o arquivo `docs/config.js`:

```javascript
const API_CONFIG = {
    // Substitua pela URL do seu Vercel
    baseURL: 'https://seu-projeto.vercel.app',
    
    // ... resto do arquivo
};
```

### Passo 2: Fazer Push das Alterações

```bash
git add docs/config.js
git commit -m "Update API URL to Vercel"
git push origin main
```

### Passo 3: Aguardar Re-deploy

O GitHub Actions irá automaticamente fazer re-deploy do frontend com a nova configuração.

---

## ✅ Parte 4: Testar a Aplicação

1. Acesse sua URL do GitHub Pages
2. Verifique se o banner mostra "✅ Servidor online"
3. Faça upload de uma imagem de teste
4. Verifique se as predições aparecem

### Troubleshooting

Se o banner mostrar "❌ Servidor offline":

1. Verifique se a URL no `config.js` está correta
2. Verifique se o backend no Vercel está rodando
3. Abra o Console do navegador (F12) e verifique erros CORS
4. Verifique se `ALLOWED_ORIGINS` no Vercel está correto

---

## 🔄 Atualizações Futuras

### Atualizar Frontend

```bash
# Edite os arquivos em docs/
git add docs/
git commit -m "Update frontend"
git push origin main
# GitHub Actions fará deploy automaticamente
```

### Atualizar Backend

```bash
# Edite os arquivos em backend/
git add backend/
git commit -m "Update backend"
git push origin main
# Vercel fará deploy automaticamente
```

---

## 🐛 Troubleshooting Comum

### Problema: CORS Error no Console

**Sintoma**: Erro "Access to fetch has been blocked by CORS policy"

**Solução**:
1. Verifique se `ALLOWED_ORIGINS` no Vercel inclui sua URL do GitHub Pages
2. Certifique-se de usar HTTPS (não HTTP) na URL
3. Não inclua barra final na URL (use `https://user.github.io`, não `https://user.github.io/`)

### Problema: Backend Timeout no Vercel

**Sintoma**: Erro "Function execution timed out"

**Solução**:
- O plano gratuito do Vercel tem limite de 10s
- O modelo pode demorar para carregar no cold start
- Considere usar Render ou Railway para processos mais longos

### Problema: GitHub Pages não atualiza

**Sintoma**: Mudanças não aparecem no site

**Solução**:
1. Verifique se o workflow completou em Actions
2. Limpe o cache do navegador (Ctrl+Shift+R)
3. Aguarde 1-2 minutos para propagação do CDN

### Problema: Imagem muito grande

**Sintoma**: Erro ao fazer upload

**Solução**:
- Limite atual: 10MB
- Redimensione a imagem antes do upload
- Use ferramentas como TinyPNG para comprimir

### Problema: Modelo não carrega no Vercel

**Sintoma**: Erro 500 ao fazer predição

**Solução**:
1. Verifique os logs no Vercel Dashboard
2. Certifique-se de que `tensorflow` está em `requirements.txt`
3. Verifique se o deployment size não excede 50MB

---

## 📊 Monitoramento

### Vercel Dashboard

- Acesse [vercel.com/dashboard](https://vercel.com/dashboard)
- Veja logs em tempo real
- Monitore uso de recursos
- Verifique erros e performance

### GitHub Actions

- Acesse a aba **Actions** no repositório
- Veja histórico de deploys
- Verifique logs de build

---

## 🔐 Segurança

### Boas Práticas

1. ✅ Sempre use HTTPS
2. ✅ Configure CORS apenas para origens específicas
3. ✅ Não exponha chaves de API no frontend
4. ✅ Valide tamanho e tipo de arquivo no upload
5. ✅ Monitore uso para detectar abusos

### Variáveis de Ambiente

Nunca commite variáveis sensíveis no Git. Use:
- Vercel Environment Variables para o backend
- GitHub Secrets para workflows (se necessário)

---

## 💰 Custos

### GitHub Pages
- ✅ **Gratuito** para repositórios públicos
- ✅ 100GB bandwidth/mês
- ✅ 1GB storage

### Vercel (Free Tier)
- ✅ **Gratuito** para projetos pessoais
- ✅ 100GB bandwidth/mês
- ✅ Execuções serverless ilimitadas
- ⚠️ 10s timeout por função
- ⚠️ 50MB deployment size

---

## 🚀 Serviços Alternativos

Se o Vercel não atender suas necessidades:

### Render.com
- ✅ Free tier disponível
- ✅ Sem timeout de 10s
- ✅ Melhor para processos longos
- ❌ Cold start mais lento

### Railway.app
- ✅ $5 crédito gratuito/mês
- ✅ Suporte a Docker
- ✅ Bom para ML models
- ❌ Requer cartão de crédito

### Hugging Face Spaces
- ✅ Otimizado para ML
- ✅ GPU disponível
- ✅ Comunidade ativa
- ❌ Configuração mais complexa

---

## 📚 Recursos Adicionais

- [Documentação GitHub Pages](https://docs.github.com/pages)
- [Documentação Vercel](https://vercel.com/docs)
- [FastAPI Deployment](https://fastapi.tiangolo.com/deployment/)
- [TensorFlow.js](https://www.tensorflow.org/js) (alternativa client-side)

---

## 🆘 Suporte

Se encontrar problemas:

1. Verifique a seção de Troubleshooting acima
2. Consulte os logs no Vercel e GitHub Actions
3. Abra uma issue no repositório
4. Consulte a documentação oficial dos serviços

---

## ✨ Próximos Passos

Após o deploy bem-sucedido:

1. 🎨 Personalize o design do frontend
2. 📊 Adicione analytics (Google Analytics, Plausible)
3. 🔍 Implemente SEO (meta tags, sitemap)
4. 🌐 Adicione suporte a múltiplos idiomas
5. 📱 Otimize para mobile
6. 🧪 Adicione testes automatizados
7. 📈 Configure monitoramento de erros (Sentry)

---

**🎉 Parabéns! Sua aplicação CNN está no ar!**

Compartilhe sua URL e mostre o poder da IA para o mundo! 🚀
