@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Test_assyst_complete_run" mkdir "C:\APITestAutomation\Test_Report\Test_assyst_complete_run"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa  --html=C:\APITestAutomation\Test_Report\Test_assyst_complete_run\report.html