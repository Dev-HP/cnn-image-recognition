# Script PowerShell para manter o servidor CNN sempre ativo
$Host.UI.RawUI.WindowTitle = "CNN Image Recognition Server"

Write-Host "========================================" -ForegroundColor Green
Write-Host "   CNN Image Recognition Server" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Iniciando servidor..." -ForegroundColor Yellow
Write-Host "Acesse: http://localhost:8080" -ForegroundColor White
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Gray
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

while ($true) {
    try {
        python cnn_api.py
    }
    catch {
        Write-Host ""
        Write-Host "========================================" -ForegroundColor Red
        Write-Host "   Erro detectado! Reiniciando..." -ForegroundColor Yellow
        Write-Host "========================================" -ForegroundColor Red
        Start-Sleep -Seconds 3
    }
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Yellow
    Write-Host "   Servidor parou! Reiniciando em 3s..." -ForegroundColor Yellow
    Write-Host "========================================" -ForegroundColor Yellow
    Start-Sleep -Seconds 3
}
