@echo off
REM run_viewer.bat

REM 第一个参数是传递给脚本的目录
SET DIR=%1

REM 执行命令，启动程序并传递目录参数
"%~dp0\..\viewer\bin\SIBR_gaussianViewer_app.exe" -m "%DIR%"