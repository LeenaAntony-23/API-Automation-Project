@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\AssetWithdrawal" mkdir "C:\APITestAutomation\Test_Report\AssetWithdrawal"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Asset_Withdrawal --html=C:\APITestAutomation\Test_Report\AssetWithdrawal\report.html