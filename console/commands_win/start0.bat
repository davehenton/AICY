@echo off
python ..\commands_py\startup.py
:start
set "tmp= "
set "command= "
set "modi= "
set "mmodi= "
set "mmmodi= "
set /p getCommand=">> "
set t=%getCommand%
if defined getCommand if not "%getCommand: =%"=="" goto valid
echo variable is either undefined or contains only spaces
goto :start

:valid

:loop1
for /f "tokens=1*" %%a in ("%t%") do (
    echo %%a
    set t=%%b
    set tmp=%%a
)
if not defined command goto :setCommand
:weiter
if defined t goto :loop1

echo(%command%

::python ..\commands_py\%getFile%.rpy
::pause
goto start

:setCommand
set command=%tmp%
goto :weiter
