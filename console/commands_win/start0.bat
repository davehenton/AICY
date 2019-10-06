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
if not defined getCommand goto :start

:loop
for /f "tokens=1*" %%a in ("%t%") do (
    ::echo %%a
    set t=%%b
    set tmp=%%a
)
if not defined command goto :setCommand
:weiter
if defined t goto :loop
echo(%command%

::python ..\commands_py\%getFile%.rpy
::pause
goto start

:setCommand
set command=%tmp%
goto :weiter
