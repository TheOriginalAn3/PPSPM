@echo off

setlocal enabledelayedexpansion

set command=%1
set args=%2

if "%command%"=="create" (
    python "D:\Coding\CustomSysPATHVars\create.py" %args%
) else if "%command%"=="remove" (
    python "D:\Coding\CustomSysPATHVars\remove.py" %args%
) else if "%command%"=="open" (
    python "D:\Coding\CustomSysPATHVars\open.py" %args%
) else if "%command%"=="resume" (
    python "D:\Coding\CustomSysPATHVars\resume.py" %args%
) else (
    echo "Invalid command. Use 'pj create [Folder]', 'pj remove [Folder]', 'pj open [Folder]' or 'pj resume [Folder]'."
)

endlocal
