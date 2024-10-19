@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Valuations" mkdir "C:\APITestAutomation\Test_Report\Valuations"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Valuations\test_add_all_data_to_valuation.py --html=C:\APITestAutomation\Test_Report\Valuations\report.html