@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Policy" mkdir "C:\APITestAutomation\Test_Report\Policy"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Policies --html=C:\APITestAutomation\Test_Report\Policy\report.html