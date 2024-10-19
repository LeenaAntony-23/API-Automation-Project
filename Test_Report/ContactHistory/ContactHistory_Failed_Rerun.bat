@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\ContactHistory" mkdir "C:\APITestAutomation\Test_Report\ContactHistory"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Contact_History --html=C:\APITestAutomation\Test_Report\ContactHistory\report_failed_rerun.html --lf