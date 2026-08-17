# Publicação da Space CNN no Hugging Face

A Space antiga deste projeto entrou em `Runtime error` porque o runtime Gradio tentou gerar o schema de uma saída `gr.Label` com uma combinação incompatível de versões e porque o processo não declarava explicitamente o endereço/porta esperados pelo ambiente.

A implementação corrigida está em [`space/app.py`](space/app.py), com dependências fixadas em [`space/requirements.txt`](space/requirements.txt). A função retorna Markdown simples, o que elimina a conversão problemática de dicionários para `gr.Label`; o modelo continua sendo MobileNetV2 com pesos ImageNet.

## Sincronização manual

A Space precisa conter estes arquivos na raiz:

```text
app.py
requirements.txt
README.md
```

Copie os três arquivos de `space/` para a raiz da Space e faça commit na branch `main`. O README da Space deve manter o front matter:

```yaml
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
```

O processo de publicação requer autenticação no Hugging Face. Depois do push, aguarde o rebuild da Space e confirme que o upload de imagem retorna cinco previsões em Markdown.

## Validação local

A sintaxe do aplicativo pode ser validada sem carregar o modelo:

```bash
python -m py_compile space/app.py
```

Para testar a interface completa, instale as dependências da Space em um ambiente isolado:

```bash
python -m venv .venv-space
source .venv-space/bin/activate
pip install -r space/requirements.txt
python space/app.py
```

O projeto principal continua documentando a arquitetura FastAPI + frontend estático em `backend/` e `docs/`. A pasta `space/` é uma vitrine independente para o Hugging Face.
