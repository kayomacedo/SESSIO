@echo off
title Sessio - Session Manager
echo ============================================
echo        SESSIO - Session Manager
echo ============================================

REM ===== Diretório raiz do projeto (onde o .bat está)
set PROJECT_DIR=%~dp0

REM ===== Caminho do Python no venv
set VENV_PY=%PROJECT_DIR%venv\Scripts\python.exe

REM ===== Caminho do script do manager
set MANAGER_SCRIPT=%PROJECT_DIR%session_manager\manager.py

echo.
echo 🔧 Ativando ambiente virtual...
echo.

if not exist "%VENV_PY%" (
    echo ❌ ERRO: Python do venv não encontrado em:
    echo %VENV_PY%
    pause
    exit /b
)

echo 🚀 Executando Session Manager no terminal...
echo ============================================
"%VENV_PY%" "%MANAGER_SCRIPT%"

echo.
echo ============================================
echo   Sessio Manager finalizado.
echo   Pressione qualquer tecla para sair.
echo ============================================
pause >nul
