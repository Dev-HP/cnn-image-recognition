/**
 * Configuração da API Backend
 * 
 * Para desenvolvimento local:
 * - Descomente a linha localhost
 * 
 * Para produção (Vercel):
 * - Atualize com sua URL do Vercel
 */

const API_CONFIG = {
    // URL base da API (atualize com sua URL do Vercel)
    baseURL: 'https://your-project.vercel.app',
    
    // Para desenvolvimento local, descomente a linha abaixo:
    // baseURL: 'http://localhost:8080',
    
    // Endpoints disponíveis
    endpoints: {
        predict: '/predict',
        health: '/health'
    },
    
    // Timeout para requisições (em ms)
    timeout: 30000,
    
    // Configurações de upload
    upload: {
        maxSize: 10 * 1024 * 1024, // 10MB
        acceptedTypes: ['image/jpeg', 'image/png', 'image/gif', 'image/bmp', 'image/webp']
    }
};

// Exportar configuração
if (typeof module !== 'undefined' && module.exports) {
    module.exports = API_CONFIG;
}
