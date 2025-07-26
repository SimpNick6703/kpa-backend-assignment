@echo off
echo KPA Backend Assignment Setup
echo ============================

echo.
echo 1. Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 2. Setting up environment file...
if not exist .env (
    copy .env.example .env
    echo Environment file created. Please update .env with your database credentials.
) else (
    echo Environment file already exists.
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Update .env file with your PostgreSQL database credentials
echo 2. Ensure PostgreSQL is running
echo 3. Run: python run_server.py
echo.
echo Or use Docker:
echo 1. Run: docker-compose up --build
echo.
pause
