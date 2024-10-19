@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Expense" mkdir "C:\APITestAutomation\Test_Report\Expense"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests_regression\Expense --html=C:\APITestAutomation\Test_Report\Expense\report.html