@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Dependants" mkdir "C:\APITestAutomation\Test_Report\Dependants"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Dependants --html=C:\APITestAutomation\Test_Report\Dependants\report.html