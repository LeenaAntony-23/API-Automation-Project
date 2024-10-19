@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\commission" mkdir "C:\APITestAutomation\Test_Report\commission"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Commission --html=C:\APITestAutomation\Test_Report\commission\report_failed_rerun.html --lf