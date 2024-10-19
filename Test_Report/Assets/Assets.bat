@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Assets" mkdir "C:\APITestAutomation\Test_Report\Assets"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Assets --html=C:\APITestAutomation\Test_Report\Assets\report.html