@echo off
echo ========================================
echo   Enviando projeto para o GitHub
echo ========================================
echo.

set /p USERNAME="Digite seu username do GitHub: "
set REPO_NAME=cnn-image-recognition

echo.
echo Configurando repositorio remoto...
git remote add origin https://github.com/%USERNAME%/%REPO_NAME%.git

echo.
echo Renomeando branch para main...
git branch -M main

echo.
echo Enviando codigo para o GitHub...
git push -u origin main

echo.
echo ========================================
echo   Concluido!
echo ========================================
echo.
echo Acesse seu repositorio em:
echo https://github.com/%USERNAME%/%REPO_NAME%
echo.
pause
