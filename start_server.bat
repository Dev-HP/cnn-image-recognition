@echo off
title CNN Image Recognition Server
color 0A
echo ========================================
echo   CNN Image Recognition Server
echo ========================================
echo.
echo Iniciando servidor...
echo Acesse: http://localhost:8080
echo.
echo Pressione Ctrl+C para parar o servidor
echo ========================================
echo.

:loop
python cnn_api.py
echo.
echo ========================================
echo   Servidor parou! Reiniciando em 3s...
echo ========================================
timeout /t 3 /nobreak
goto loop
