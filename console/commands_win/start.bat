@echo off
python ..\commands_py\startup.py

:start
rem echo start
set getCommand=
set tmp=
set command=
set modi=
set mmodi=
set mmmodi=
set /p getCommand=">> "
set t=%getCommand%
if defined getCommand if not "%getCommand: =%"=="" goto valid
rem echo variable is either undefined or contains only spaces
goto :start

:valid

:loop1
for /f "tokens=1*" %%a in ("%t%") do (
    rem echo %%a
    set t=%%b
    set tmp=%%a
)
if not defined command goto :setCommand
if not defined modi goto :setModi
if not defined mmodi goto :setMmodi
if not defined mmmodi goto :setMmmodi

:weiter
if defined t goto :loop1

echo(%command%
if defined modi echo(%modi%
if defined mmodi echo(%mmodi%
if defined mmmodi echo(%mmmodi%

::pause
If exist ../commands_py/%command%.py python ../commands_py/%command%.py
If not exist ../commands_py/%command%.py echo Command not found!    For help type 'help'.
goto start

:setCommand
rem echo Command
set command=%tmp%
goto :weiter

:setModi
set modi=%tmp%
goto :weiter

:setMmodi
set mmodi=%tmp%
goto :weiter

:setMmmodi
set mmmodi=%tmp%
goto :weiter
