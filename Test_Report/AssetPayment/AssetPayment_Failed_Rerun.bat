@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\AssetPayment" mkdir "C:\APITestAutomation\Test_Report\AssetPayment"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Asset_Payment --html=C:\APITestAutomation\Test_Report\AssetPayment\report_failed_rerun.html --lf