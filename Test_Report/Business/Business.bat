@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Business" mkdir "C:\APITestAutomation\Test_Report\Business"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Business --html=C:\APITestAutomation\Test_Report\Business\report.html