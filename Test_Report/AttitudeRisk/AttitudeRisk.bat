@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\AttitudeRisk" mkdir "C:\APITestAutomation\Test_Report\AttitudeRisk"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\AttitudeRisk --html=C:\APITestAutomation\Test_Report\AttitudeRisk\report.html