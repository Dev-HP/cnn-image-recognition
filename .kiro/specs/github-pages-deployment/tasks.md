# Implementation Plan

- [x] 1. Reorganizar estrutura do projeto





  - Criar diretório `backend/` e mover `cnn_api.py` para lá
  - Criar diretório `docs/` para arquivos do frontend
  - Mover `requirements.txt` para `backend/requirements.txt`
  - Criar `requirements.txt` na raiz apenas com dependências de desenvolvimento
  - _Requirements: 1.4, 7.1, 7.2, 7.4_

- [x] 2. Implementar CNN.DEMO.py (CLI script)







  - Implementar carregamento do modelo MobileNetV2
  - Implementar processamento de imagem via linha de comando
  - Implementar exibição de top 5 predições
  - Implementar tratamento de erros (arquivo não encontrado, formato inválido)
  - Implementar mensagens de uso e ajuda
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [ ]* 2.1 Write property test for CLI prediction output
  - **Property 9: CLI Prediction Output**
  - **Validates: Requirements 6.1, 6.2**

- [ ]* 2.2 Write property test for CLI error handling
  - **Property 10: CLI Error Handling**
  - **Validates: Requirements 6.3, 6.4**

- [x] 3. Configurar backend com CORS



  - Adicionar middleware CORS ao FastAPI
  - Configurar origens permitidas (localhost e GitHub Pages)
  - Adicionar suporte para variável de ambiente ALLOWED_ORIGINS
  - Adicionar logging de origens permitidas no startup
  - Atualizar endpoint /health para retornar informações de CORS
  - _Requirements: 1.3, 4.1, 4.2, 4.3, 4.4, 4.5_

- [ ]* 3.1 Write property test for CORS headers
  - **Property 2: CORS Header Presence**
  - **Validates: Requirements 1.3, 4.1, 4.2**

- [ ]* 3.2 Write property test for preflight requests
  - **Property 8: Preflight Request Handling**
  - **Validates: Requirements 4.3**

- [ ]* 3.3 Write property test for multiple origins support
  - **Property: Multiple Origins Configuration**
  - **Validates: Requirements 4.5**

- [ ]* 3.4 Write unit tests for backend endpoints
  - Test /predict endpoint with valid image
  - Test /predict endpoint with invalid data
  - Test /health endpoint response format
  - Test error responses have correct structure
  - _Requirements: 1.2_

- [x] 4. Criar frontend estático


  - Criar `docs/index.html` com interface de upload completa
  - Criar `docs/config.js` com configuração de URL da API
  - Implementar lógica de upload de imagem
  - Implementar chamadas à API backend
  - Implementar exibição de resultados
  - Implementar indicador de loading
  - Implementar verificação de conectividade (health check)
  - Implementar tratamento de erros com mensagens amigáveis
  - _Requirements: 1.1, 1.5, 2.1, 2.2, 2.3, 2.4, 2.5_

- [ ]* 4.1 Write property test for configuration flexibility
  - **Property 12: Configuration Flexibility**
  - **Validates: Requirements 1.5**

- [ ]* 4.2 Write property test for health check on page load
  - **Property 5: Backend Connectivity Check**
  - **Validates: Requirements 2.4**

- [ ]* 4.3 Write property test for loading indicator display
  - **Property: Loading Indicator Visibility**
  - **Validates: Requirements 2.5**

- [x] 5. Configurar GitHub Actions para deploy


  - Criar diretório `.github/workflows/`
  - Criar arquivo `deploy.yml` com workflow de deploy
  - Configurar trigger em push para branch main
  - Configurar steps: checkout, setup pages, upload artifact, deploy
  - Adicionar logging de sucesso/falha
  - _Requirements: 3.1, 3.2, 3.3, 3.4, 3.5, 7.5_

- [ ]* 5.1 Write property test for workflow trigger
  - **Property 6: GitHub Actions Trigger**
  - **Validates: Requirements 3.1**

- [ ]* 5.2 Write property test for deployment success
  - **Property 7: Deployment Success Verification**
  - **Validates: Requirements 3.3**

- [x] 6. Criar documentação de deploy


  - Criar arquivo `DEPLOY.md` com instruções completas
  - Documentar deploy do frontend no GitHub Pages
  - Documentar deploy do backend em serviços cloud (Render, Railway)
  - Documentar configuração de variáveis de ambiente
  - Documentar como configurar URL da API no frontend
  - Adicionar seção de troubleshooting com problemas comuns
  - Adicionar lista de pré-requisitos
  - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [x] 7. Atualizar README.md



  - Atualizar estrutura do projeto no README
  - Adicionar seção sobre arquitetura (frontend + backend)
  - Adicionar instruções de deploy
  - Adicionar link para DEPLOY.md
  - Adicionar informações sobre CORS e configuração
  - Atualizar diagramas se necessário
  - _Requirements: 7.3_

- [ ] 8. Checkpoint - Verificar testes e funcionalidade
  - Ensure all tests pass, ask the user if questions arise.

- [ ]* 9. Testes de integração end-to-end
  - Testar upload de imagem através da UI
  - Testar exibição de resultados
  - Testar tratamento de erros
  - Testar health check
  - Verificar CORS em ambiente real
  - _Requirements: 2.2, 2.3, 2.4_
