@echo off
:start
set /p variable=">> "

if defined variable if not "%variable: =%"=="" goto valid
echo variable is either undefined or contains only spaces
goto :start

:valid
echo %variable%
pause
goto :start
