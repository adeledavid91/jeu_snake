@echo off

:: Check if 'venv' folder exists
IF NOT EXIST "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

:: Activate the virtual environment
echo Activating virtual environment...
call .\venv\Scripts\activate

:: Upgrade pip and install dependencies
echo Installing and upgrading dependencies...
python -m pip install --upgrade pip
pip install --upgrade -r .\requirements.txt


echo Done!