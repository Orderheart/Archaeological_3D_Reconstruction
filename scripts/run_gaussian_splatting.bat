@echo off
CALL conda activate gaussian_splatting
python "%~dp0\..\gaussian_splatting\convert.py" -s %1 2> error_log.txt
if %ERRORLEVEL% neq 0 (
    echo Error occurred. Check error_log.txt for details.
    pause
)
REM 启动监视程序
echo Starting the monitoring program...
start "" "%~dp0..\viewer\bin\SIBR_remoteGaussian_app.exe"

echo Running train.py script...
python "%~dp0..\gaussian_splatting\train.py" -s %1 2>> error_log.txt
if %ERRORLEVEL% neq 0 (
    echo Error occurred during train.py execution. Check error_log.txt for details.
    pause
    exit /b %ERRORLEVEL%
)

echo Both scripts executed successfully.
pause


