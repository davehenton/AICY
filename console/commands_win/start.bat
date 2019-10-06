@echo off
python ..\commands_py\startup.py
:start
set /p getCommand=">> "
For %%a in (%getCommand%) do echo %%a
python ..\commands_py\%getFile%.rpy
pause
goto start
