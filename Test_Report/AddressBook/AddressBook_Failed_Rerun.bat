@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\AddressBook" mkdir "C:\APITestAutomation\Test_Report\AddressBook"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\AddressBook --html=C:\APITestAutomation\Test_Report\AddressBook\report_failed_rerun.html --lf 