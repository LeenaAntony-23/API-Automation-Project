@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Valuations" mkdir "C:\APITestAutomation\Test_Report\Valuations"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Valuations --lf  --html=C:\APITestAutomation\Test_Report\Valuations\report_failed_rerun.html