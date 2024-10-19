@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Regression" mkdir "C:\APITestAutomation\Test_Report\Regression"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Client  --lf --html=C:\APITestAutomation\Test_Report\Regression\regression_rerun16_report1.html 