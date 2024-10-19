@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\CaseSummary" mkdir "C:\APITestAutomation\Test_Report\CaseSummary"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Case_summary --html=C:\APITestAutomation\Test_Report\CaseSummary\report.html