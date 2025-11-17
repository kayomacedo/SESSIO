@echo off
title Main SESSIO

echo ============================================
echo            INICIANDO O SESSIO
echo ============================================

REM ===== Diretório raiz do projeto (onde este BAT está)
set PROJECT_DIR=%~dp0

REM ===== Caminho do Python dentro do venv
set VENV_PY=%PROJECT_DIR%venv\Scripts\python.exe

REM ===== Script principal
set MAIN_SCRIPT=%PROJECT_DIR%main.py

echo.
echo 🔧 Ativando ambiente virtual...
echo.

REM ===== Verificar existência do Python
if not exist "%VENV_PY%" (
    echo ❌ ERRO: Python do venv não foi encontrado em:
    echo     %VENV_PY%
    echo.
    pause
    exit /b
)

echo 🚀 Executando o SESSIO...
echo ============================================
"%VENV_PY%" "%MAIN_SCRIPT%"

echo.
echo ============================================
echo       Sessio finalizado.
echo   Pressione qualquer tecla para sair.
echo ============================================
pause >nul
