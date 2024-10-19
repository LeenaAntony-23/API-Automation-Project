@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Income" mkdir "C:\APITestAutomation\Test_Report\Income"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Income  --lf --html=C:\APITestAutomation\Test_Report\Income\report_failed_rerun.html