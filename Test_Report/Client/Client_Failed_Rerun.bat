@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Client" mkdir "C:\APITestAutomation\Test_Report\Client"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Client --html=C:\APITestAutomation\Test_Report\Client\report_failed_rerun.html --lf