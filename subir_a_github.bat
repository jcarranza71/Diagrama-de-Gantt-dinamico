@echo off
REM Inicializa repositorio Git y sube a GitHub

REM Usuario de GitHub
set GITHUB_USER=jcarranza71

REM Nombre del repositorio (ya debe existir en GitHub)
set REPO_NAME=Diagrama-de-Gantt-dinamico

REM Inicializar repositorio local
git init
git add .
git commit -m "Primer commit - Generador de diagrama de Gantt dinámico"

REM Establecer repositorio remoto
git remote add origin https://github.com/%GITHUB_USER%/%REPO_NAME%.git
git branch -M main
git push -u origin main

pause
