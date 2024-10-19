@echo off
:: Create Test Report Directory to store output
if not exist "C:\APITestAutomation\Test_Report\ContactHistory" mkdir "C:\APITestAutomation\Test_Report\ContactHistory"

:: Run the test scripts
cd C:\APITestAutomation\test_assyst
pytest --env=qa .\tests\Contact_History\test_fetch_contact_note_only.py --html=C:\APITestAutomation\Test_Report\ContactHistory\report.html