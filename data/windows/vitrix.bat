chcp 65001
set PYTHONIOENCODING=utf-8
title Vitrix

call "python\python.exe" "src\vitrix\menu.pyc" > "log.txt" 2>&1
