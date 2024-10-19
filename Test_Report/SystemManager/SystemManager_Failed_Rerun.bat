@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\SystemManager" mkdir "C:\APITestAutomation\Test_Report\SystemManager"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\System_Manager --html=C:\APITestAutomation\Test_Report\SystemManager\report_failed_rerun.html --lf