@echo off
cd /d "%~dp0"
start python app.py
timeout /t 2
start http://localhost:5000
pause
