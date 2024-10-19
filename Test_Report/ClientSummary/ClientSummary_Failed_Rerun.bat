@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\ClientSummary" mkdir "C:\APITestAutomation\Test_Report\ClientSummary"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Client_Summary --html=C:\APITestAutomation\Test_Report\ClientSummary\report_failed_rerun.html --lf