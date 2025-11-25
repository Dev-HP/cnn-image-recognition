# Requirements Document

## Introduction

Este documento especifica os requisitos para separar a aplicação CNN Image Recognition em frontend estático (hospedado no GitHub Pages) e backend API (hospedado em serviço cloud), permitindo deploy automatizado via GitHub Actions.

## Glossary

- **Frontend**: Interface web estática (HTML/CSS/JS) que roda no navegador do usuário
- **Backend**: API FastAPI que processa imagens usando o modelo CNN
- **GitHub Pages**: Serviço de hospedagem gratuita do GitHub para sites estáticos
- **GitHub Actions**: Sistema de CI/CD do GitHub para automação de workflows
- **CORS**: Cross-Origin Resource Sharing - mecanismo que permite requisições entre domínios diferentes
- **Sistema**: A aplicação completa de reconhecimento de imagens CNN

## Requirements

### Requirement 1

**User Story:** Como desenvolvedor, eu quero separar o frontend do backend, para que o frontend possa ser hospedado no GitHub Pages e o backend em um serviço cloud.

#### Acceptance Criteria

1. WHEN the frontend is deployed THEN the Sistema SHALL serve all HTML, CSS, and JavaScript files as static assets
2. WHEN the backend is deployed THEN the Sistema SHALL expose API endpoints accessible via HTTP
3. WHEN the frontend makes requests to the backend THEN the Sistema SHALL handle CORS properly to allow cross-origin requests
4. WHEN the project structure is organized THEN the Sistema SHALL separate frontend files from backend files in distinct directories
5. WHERE the backend URL is configured THEN the Sistema SHALL allow easy configuration of the API endpoint URL in the frontend

### Requirement 2

**User Story:** Como usuário, eu quero acessar a aplicação via GitHub Pages, para que eu possa usar o reconhecimento de imagens sem instalar nada localmente.

#### Acceptance Criteria

1. WHEN a user visits the GitHub Pages URL THEN the Sistema SHALL display the complete web interface
2. WHEN a user uploads an image THEN the Sistema SHALL send the image to the backend API and display results
3. WHEN the backend is unavailable THEN the Sistema SHALL display a clear error message to the user
4. WHEN the page loads THEN the Sistema SHALL verify backend connectivity and inform the user of the status
5. WHILE the image is being processed THEN the Sistema SHALL show a loading indicator to the user

### Requirement 3

**User Story:** Como desenvolvedor, eu quero deploy automatizado via GitHub Actions, para que o frontend seja publicado automaticamente no GitHub Pages quando eu fizer push.

#### Acceptance Criteria

1. WHEN code is pushed to the main branch THEN the Sistema SHALL trigger the GitHub Actions workflow automatically
2. WHEN the workflow runs THEN the Sistema SHALL build and deploy the frontend to GitHub Pages
3. WHEN the deployment completes THEN the Sistema SHALL make the updated site available at the GitHub Pages URL
4. IF the deployment fails THEN the Sistema SHALL report the error in the GitHub Actions log
5. WHEN the workflow succeeds THEN the Sistema SHALL confirm successful deployment in the Actions log

### Requirement 4

**User Story:** Como desenvolvedor, eu quero configurar o backend com CORS, para que o frontend hospedado no GitHub Pages possa fazer requisições à API.

#### Acceptance Criteria

1. WHEN the backend receives a request from the GitHub Pages domain THEN the Sistema SHALL accept the request with proper CORS headers
2. WHEN CORS is configured THEN the Sistema SHALL allow requests from the GitHub Pages URL
3. WHEN preflight OPTIONS requests are received THEN the Sistema SHALL respond with appropriate CORS headers
4. WHEN the backend starts THEN the Sistema SHALL log the allowed CORS origins for verification
5. WHERE multiple origins are needed THEN the Sistema SHALL support configuration of multiple allowed origins

### Requirement 5

**User Story:** Como desenvolvedor, eu quero documentação clara de deploy, para que eu possa configurar e hospedar tanto o frontend quanto o backend facilmente.

#### Acceptance Criteria

1. WHEN reading the documentation THEN the Sistema SHALL provide step-by-step instructions for deploying the frontend to GitHub Pages
2. WHEN reading the documentation THEN the Sistema SHALL provide step-by-step instructions for deploying the backend to a cloud service
3. WHEN configuring the frontend THEN the Sistema SHALL document how to set the backend API URL
4. WHEN troubleshooting THEN the Sistema SHALL provide common issues and solutions in the documentation
5. WHEN deploying for the first time THEN the Sistema SHALL include all prerequisites and requirements in the documentation

### Requirement 6

**User Story:** Como desenvolvedor, eu quero o arquivo CNN.DEMO.py implementado, para que eu possa testar o modelo via linha de comando.

#### Acceptance Criteria

1. WHEN CNN.DEMO.py is executed with an image path THEN the Sistema SHALL load the image and process it with the CNN model
2. WHEN the prediction completes THEN the Sistema SHALL display the top 5 predictions with confidence percentages
3. WHEN no image path is provided THEN the Sistema SHALL display usage instructions
4. WHEN an invalid image path is provided THEN the Sistema SHALL display a clear error message
5. WHEN the model loads THEN the Sistema SHALL display a loading message to inform the user

### Requirement 7

**User Story:** Como desenvolvedor, eu quero uma estrutura de projeto organizada, para que seja fácil entender e manter o código.

#### Acceptance Criteria

1. WHEN viewing the project structure THEN the Sistema SHALL organize frontend files in a dedicated directory
2. WHEN viewing the project structure THEN the Sistema SHALL organize backend files in a dedicated directory
3. WHEN viewing the project structure THEN the Sistema SHALL include a clear README with architecture overview
4. WHEN viewing the project structure THEN the Sistema SHALL separate configuration files appropriately
5. WHEN viewing the project structure THEN the Sistema SHALL include GitHub Actions workflow files in the .github/workflows directory
