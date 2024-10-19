@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Fund" mkdir "C:\APITestAutomation\Test_Report\Fund"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Fund\test_update_fund_using_fundid.py --html=C:\APITestAutomation\Test_Report\Fund\report.html