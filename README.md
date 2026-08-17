# CNN Image Recognition

> Aplicação educacional para reconhecer imagens com uma Rede Neural Convolucional usando MobileNetV2, com interface web, API FastAPI e alternativa de execução por linha de comando.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Status

**Projeto demonstrativo.** A interface e a API são adequadas para estudo de classificação de imagens. A demonstração hospedada externamente está temporariamente em validação; por isso, o caminho reproduzível abaixo é a execução local.

## O que o projeto demonstra

- Classificação com MobileNetV2 pré-treinada no ImageNet.
- Até cinco previsões acompanhadas de porcentagens de confiança.
- Interface com upload e pré-visualização de imagem.
- API REST com FastAPI e endpoint de verificação de saúde.
- Separação entre frontend estático e backend Python.
- Execução alternativa pela linha de comando.

## Arquitetura

```text
Frontend estático (docs/)
          │ HTTP + CORS
          ▼
Backend FastAPI (backend/)
          │
          ▼
MobileNetV2 + TensorFlow/Keras
```

## Demonstração visual

Adicione aqui uma captura real do fluxo de upload, processamento e resultado antes de publicar uma URL de demonstração. Não mantenha links genéricos ou uma URL externa quebrada como se fossem uma demo funcional.

## Execução local

### Backend

```bash
git clone https://github.com/Dev-HP/cnn-image-recognition.git
cd cnn-image-recognition
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
python backend/cnn_api.py
```

### Frontend

Em outro terminal, sirva a pasta `docs/` por HTTP para que o navegador possa carregar os arquivos corretamente:

```bash
python -m http.server 3000 --directory docs
```

Acesse `http://localhost:3000`. Para apontar a interface para um backend local, confira a configuração em `docs/config.js`.

## Uso pela linha de comando

```bash
python CNN.DEMO.py caminho/para/imagem.jpg
```

## Testes

```bash
python test_cnn.py
python test_cnn_simple.py test_image.jpg
```

Para testar a API manualmente:

```bash
curl http://localhost:8080/health
curl -X POST -F "file=@test_image.jpg" http://localhost:8080/predict
```

## Estrutura

```text
backend/                 API FastAPI e dependências
 docs/                   frontend estático e configuração da API
CNN.DEMO.py              execução por linha de comando
test_cnn.py              geração de imagem de teste
test_cnn_simple.py       teste simples de reconhecimento
DEPLOY.md                notas de publicação
LICENSE                  licença MIT
```

## Limitações

O modelo foi treinado no ImageNet e pode produzir previsões incorretas para imagens fora do domínio esperado. A porcentagem apresentada é confiança do modelo, não garantia de acerto. Registre exemplos de entrada, limitações e resultados reais em uma seção de avaliação quando houver benchmark reproduzível.

## Licença e autor

O projeto está sob a licença [MIT](LICENSE). Desenvolvido por **Hélio Paulo Leite de Lima** para a palestra “Desvendando as Redes Neurais”.
