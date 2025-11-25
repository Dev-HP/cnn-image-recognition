# Design Document

## Overview

Este documento descreve o design para separar a aplicação CNN Image Recognition em uma arquitetura cliente-servidor, com frontend estático hospedado no GitHub Pages e backend API hospedado em serviço cloud. A solução inclui automação de deploy via GitHub Actions e configuração CORS para comunicação cross-origin.

## Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        GitHub Pages                          │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Frontend (Static Files)                           │    │
│  │  - index.html                                      │    │
│  │  - config.js (API URL configuration)              │    │
│  │  - styles.css                                      │    │
│  │  - app.js (API client logic)                      │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTPS Requests
                            │ (with CORS)
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    Vercel (Serverless Functions)             │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Backend API (FastAPI)                             │    │
│  │  - CORS middleware configured                      │    │
│  │  - /predict endpoint                               │    │
│  │  - /health endpoint                                │    │
│  │  - MobileNetV2 CNN model                          │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### Deployment Flow

```
Developer Push → GitHub → GitHub Actions → Build → Deploy to GitHub Pages
                            │
                            └──→ Vercel (Auto Deploy) → Backend API
                                                          │
                                                          ▼
                                                   Live Frontend
                                                          │
                                                          │ API Calls
                                                          ▼
                                              Backend API (Vercel Serverless)
```

## Components and Interfaces

### Frontend Components

#### 1. Static HTML Page (`docs/index.html`)
- Single-page application with upload interface
- Embedded CSS for styling
- References external JavaScript files

#### 2. Configuration Module (`docs/config.js`)
- Exports API base URL
- Allows easy switching between development and production
- Format:
```javascript
const API_CONFIG = {
    baseURL: 'https://your-backend-url.com',
    endpoints: {
        predict: '/predict',
        health: '/health'
    }
};
```

#### 3. Application Logic (`docs/app.js`)
- Handles file upload and preview
- Makes API requests to backend
- Displays results and error handling
- Implements retry logic for failed requests

### Backend Components

#### 1. FastAPI Application (`backend/cnn_api.py`)
- CORS middleware configuration
- Endpoints:
  - `GET /` - Health check with CORS info
  - `POST /predict` - Image prediction endpoint
  - `GET /health` - Service health status

#### 2. CORS Configuration
```python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://username.github.io",
    "http://localhost:8080",  # for local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### 3. CNN Demo Script (`CNN.DEMO.py`)
- Command-line interface for testing
- Loads MobileNetV2 model
- Processes single image
- Displays top 5 predictions

### GitHub Actions Workflow

#### Workflow File (`.github/workflows/deploy.yml`)
- Triggers on push to main branch
- Steps:
  1. Checkout code
  2. Setup GitHub Pages
  3. Upload artifacts from `docs/` directory
  4. Deploy to GitHub Pages

## Data Models

### API Request/Response Models

#### Prediction Request
```
POST /predict
Content-Type: multipart/form-data

file: <binary image data>
```

#### Prediction Response
```json
{
    "success": true,
    "predictions": [
        {
            "class_id": "n02123045",
            "name": "Tabby Cat",
            "confidence": 87.45
        },
        {
            "class_id": "n02123159",
            "name": "Tiger Cat",
            "confidence": 8.32
        }
    ]
}
```

#### Error Response
```json
{
    "success": false,
    "error": "Error message description"
}
```

#### Health Check Response
```json
{
    "status": "ok",
    "model": "MobileNetV2",
    "cors_origins": ["https://username.github.io"]
}
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Static Asset Serving
*For any* file in the `docs/` directory, when the frontend is deployed to GitHub Pages, that file should be accessible via HTTPS at the corresponding GitHub Pages URL.
**Validates: Requirements 1.1**

### Property 2: CORS Header Presence
*For any* request from the GitHub Pages origin to the backend API, the response should include the `Access-Control-Allow-Origin` header with the appropriate value.
**Validates: Requirements 1.3, 4.1, 4.2**

### Property 3: API Endpoint Accessibility
*For any* valid image upload request to the `/predict` endpoint, the backend should return a response with status code 200 and a valid JSON payload containing predictions.
**Validates: Requirements 1.2, 2.2**

### Property 4: Error Message Display
*For any* failed API request (network error, 4xx, or 5xx response), the frontend should display a user-friendly error message to the user.
**Validates: Requirements 2.3**

### Property 5: Backend Connectivity Check
*For any* page load, the frontend should make a request to the `/health` endpoint and inform the user whether the backend is available.
**Validates: Requirements 2.4**

### Property 6: GitHub Actions Trigger
*For any* push to the main branch, the GitHub Actions workflow should automatically trigger and attempt to deploy the frontend.
**Validates: Requirements 3.1**

### Property 7: Deployment Success Verification
*For any* successful GitHub Actions workflow run, the updated files should be accessible at the GitHub Pages URL within a reasonable time (< 5 minutes).
**Validates: Requirements 3.3**

### Property 8: Preflight Request Handling
*For any* OPTIONS preflight request from an allowed origin, the backend should respond with appropriate CORS headers including `Access-Control-Allow-Methods` and `Access-Control-Allow-Headers`.
**Validates: Requirements 4.3**

### Property 9: CLI Prediction Output
*For any* valid image file path provided to CNN.DEMO.py, the script should output exactly 5 predictions with class names and confidence percentages.
**Validates: Requirements 6.1, 6.2**

### Property 10: CLI Error Handling
*For any* invalid or missing image path provided to CNN.DEMO.py, the script should display an appropriate error message without crashing.
**Validates: Requirements 6.3, 6.4**

### Property 11: Directory Structure Separation
*For any* file in the project, it should be located in either the frontend directory (`docs/`), backend directory (`backend/`), or root configuration directory, with no mixing of concerns.
**Validates: Requirements 1.4, 7.1, 7.2**

### Property 12: Configuration Flexibility
*For any* change to the backend API URL in the configuration file, the frontend should use the new URL for all subsequent API requests without requiring code changes.
**Validates: Requirements 1.5**

## Error Handling

### Frontend Error Scenarios

1. **Network Errors**
   - Display: "Não foi possível conectar ao servidor. Verifique sua conexão."
   - Action: Show retry button

2. **Backend Unavailable (Health Check Fails)**
   - Display: "Servidor temporariamente indisponível. Tente novamente mais tarde."
   - Action: Disable upload functionality, show status banner

3. **Invalid Image Format**
   - Display: "Formato de imagem inválido. Use JPG, PNG ou GIF."
   - Action: Clear file input, allow new selection

4. **File Too Large**
   - Display: "Arquivo muito grande. Tamanho máximo: 10MB."
   - Action: Clear file input, allow new selection

5. **API Error Response**
   - Display: Error message from API or generic "Erro ao processar imagem"
   - Action: Allow retry with same or different image

### Backend Error Scenarios

1. **Invalid Image Data**
   - Return: 400 Bad Request with error message
   - Log: Error details for debugging

2. **Model Prediction Failure**
   - Return: 500 Internal Server Error
   - Log: Full stack trace

3. **CORS Violation**
   - Return: 403 Forbidden (automatically handled by middleware)
   - Log: Origin that was rejected

4. **File Processing Error**
   - Return: 500 Internal Server Error with sanitized message
   - Log: Detailed error information

### CLI Error Scenarios

1. **No Arguments Provided**
   - Display: Usage instructions
   - Exit: Code 1

2. **File Not Found**
   - Display: "Erro: Arquivo não encontrado: {path}"
   - Exit: Code 1

3. **Invalid Image File**
   - Display: "Erro: Arquivo inválido ou corrompido"
   - Exit: Code 1

4. **Model Loading Failure**
   - Display: "Erro ao carregar modelo CNN"
   - Exit: Code 1

## Testing Strategy

### Unit Testing

Unit tests will verify specific functionality and edge cases:

1. **Backend API Tests**
   - Test CORS headers are present in responses
   - Test /health endpoint returns correct status
   - Test /predict endpoint with valid image
   - Test /predict endpoint with invalid data
   - Test error responses have correct format

2. **Frontend Tests** (Manual/Browser-based)
   - Test file upload UI interaction
   - Test drag-and-drop functionality
   - Test error message display
   - Test results rendering
   - Test configuration loading

3. **CLI Tests**
   - Test with valid image file
   - Test with missing file
   - Test with invalid file
   - Test output format
   - Test error messages

### Property-Based Testing

Property-based tests will use **Hypothesis** (Python) for backend testing.

Each property test should run a minimum of 100 iterations to ensure robustness.

Property tests will be tagged with comments referencing the design document:
- Format: `# Feature: github-pages-deployment, Property {number}: {property_text}`

### Integration Testing

1. **End-to-End Flow**
   - Deploy frontend to test GitHub Pages
   - Deploy backend to test environment
   - Upload test image through UI
   - Verify prediction results display correctly

2. **CORS Integration**
   - Make requests from GitHub Pages domain
   - Verify no CORS errors in browser console
   - Test preflight requests

3. **GitHub Actions**
   - Test workflow triggers on push
   - Verify deployment completes successfully
   - Check deployed files are accessible

### Manual Testing Checklist

- [ ] Frontend loads correctly on GitHub Pages
- [ ] Backend health check succeeds from frontend
- [ ] Image upload and prediction works end-to-end
- [ ] Error messages display correctly
- [ ] Loading indicators appear during processing
- [ ] Results display with correct formatting
- [ ] CLI script works with test images
- [ ] GitHub Actions workflow deploys successfully

## Deployment Strategy

### Frontend Deployment (GitHub Pages)

1. **Repository Setup**
   - Enable GitHub Pages in repository settings
   - Set source to GitHub Actions
   - Configure custom domain (optional)

2. **Directory Structure**
   - All frontend files in `docs/` directory
   - GitHub Actions deploys from `docs/`

3. **Configuration**
   - Update `config.js` with production backend URL
   - Commit and push to main branch
   - GitHub Actions automatically deploys

### Backend Deployment (Vercel - Recommended)

**Why Vercel:**
- ✅ Automatic deployment via Git
- ✅ Free tier with generous limits
- ✅ Native Python/FastAPI support
- ✅ Built-in HTTPS and CDN
- ✅ Easy environment variable management
- ✅ Public URL automatically generated

**Deployment Steps:**
1. Install Vercel CLI: `npm i -g vercel`
2. Create `vercel.json` configuration file
3. Run `vercel` in project root
4. Follow prompts to link repository
5. Set environment variables via Vercel dashboard
6. Get public URL (e.g., `https://your-project.vercel.app`)
7. Update frontend `config.js` with Vercel URL

**Alternative Services:**
- Render.com (Better for long-running processes)
- Railway.app (Good for containerized apps)
- Hugging Face Spaces (Optimized for ML models)

### Environment Variables

Backend may use:
- `ALLOWED_ORIGINS`: Comma-separated list of allowed CORS origins
- `PORT`: Port number (usually provided by hosting service)
- `ENV`: Environment name (development/production)

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow
├── backend/
│   ├── cnn_api.py             # FastAPI backend
│   └── requirements.txt        # Backend dependencies
├── docs/                       # Frontend (GitHub Pages)
│   ├── index.html             # Main HTML page
│   ├── config.js              # API configuration
│   └── app.js                 # Application logic (optional separate file)
├── CNN.DEMO.py                # CLI demo script
├── test_cnn.py                # Test image generator
├── test_cnn_simple.py         # Simple CLI test
├── vercel.json                # Vercel configuration
├── requirements.txt           # Root dependencies
├── README.md                  # Updated documentation
└── DEPLOY.md                  # Deployment guide
```

## Vercel Configuration

### vercel.json Structure

```json
{
  "version": 2,
  "builds": [
    {
      "src": "backend/cnn_api.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "backend/cnn_api.py"
    }
  ],
  "env": {
    "ALLOWED_ORIGINS": "https://your-username.github.io"
  }
}
```

### Vercel Considerations

**Advantages:**
- Automatic HTTPS
- Global CDN
- Zero-config deployment
- Built-in analytics

**Limitations:**
- 10s execution timeout (free tier)
- 50MB deployment size limit
- Cold starts for infrequent requests
- Memory limits (1024MB free tier)

**Optimization Tips:**
- Model loads on cold start (~2-3s)
- Consider model caching strategies
- Use lightweight model versions if needed
- Monitor function execution time

## Security Considerations

1. **CORS Configuration**
   - Only allow specific origins (GitHub Pages URL)
   - Don't use wildcard (*) in production
   - Configure via environment variables in Vercel

2. **File Upload Validation**
   - Validate file type and size
   - Sanitize file names
   - Limit upload size to prevent DoS

3. **Error Messages**
   - Don't expose internal paths or stack traces to frontend
   - Log detailed errors server-side only

4. **Rate Limiting** (Future Enhancement)
   - Consider adding rate limiting to prevent abuse
   - Use Vercel's built-in rate limiting features

## Performance Considerations

1. **Model Loading**
   - Load model once at startup, not per request
   - Consider model caching strategies

2. **Image Processing**
   - Resize images efficiently
   - Use appropriate image formats

3. **Frontend**
   - Minimize JavaScript bundle size
   - Use CDN for any external libraries
   - Implement client-side image validation before upload

4. **Backend**
   - Use async/await for I/O operations
   - Consider request queuing for high load
   - Monitor memory usage with TensorFlow

## Future Enhancements

1. **Progressive Web App (PWA)**
   - Add service worker for offline capability
   - Cache model predictions

2. **Multiple Model Support**
   - Allow users to select different CNN models
   - Compare predictions across models

3. **Batch Processing**
   - Support multiple image uploads
   - Process images in parallel

4. **User Accounts**
   - Save prediction history
   - Track usage statistics

5. **WebSocket Support**
   - Real-time prediction updates
   - Progress indicators for large images
