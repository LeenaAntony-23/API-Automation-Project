@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Liabilities" mkdir "C:\APITestAutomation\Test_Report\Liabilities"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Liablities --html=C:\APITestAutomation\Test_Report\Liabilities\report.html