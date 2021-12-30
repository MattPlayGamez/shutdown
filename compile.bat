@echo off
cls
pyinstaller --onefile -i downloads.ico down-shutter.py --dist .
