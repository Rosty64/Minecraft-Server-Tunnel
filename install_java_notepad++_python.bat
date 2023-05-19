@echo off
echo Installing Java...
winget install --id Oracle.JavaRuntimeEnvironment

echo Installing Notepad++ silently...
winget install --id=Notepad++.Notepad++ -e -h --scope "machine"

echo.
echo Installing Python 3.10.6...
winget install --id=Python.Python.3.10 -v "3.10.6"

echo.
echo Notepad++ and Python 3.10.6 installation completed.
pause
