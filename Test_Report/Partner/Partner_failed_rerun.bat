@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\Partner" mkdir "C:\APITestAutomation\Test_Report\Partner"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Partner\test_add_all_data_to_partner.py --lf --html=C:\APITestAutomation\Test_Report\Partner\report_failed_rerun.html