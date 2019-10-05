@echo off
python ..\commands_py\startup.py
:start
set /p getFile=">> "
python ..\commands_py\%getFile%.rpy
pause
goto start
