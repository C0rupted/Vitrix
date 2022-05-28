chcp 65001
set PYTHONIOENCODING=utf-8
title Vitrix

call "python\python.exe" "vitrix\menu.py" > "log.txt" 2>&1
