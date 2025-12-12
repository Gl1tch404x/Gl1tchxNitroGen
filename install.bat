@echo off
set packages=aiohttp

echo Starting installation of Python packages...
echo.

for %%p in (%packages%) do (
    echo Installing %%p...
    python -m pip install %%p
)

echo.
echo All packages have been installed!
pause