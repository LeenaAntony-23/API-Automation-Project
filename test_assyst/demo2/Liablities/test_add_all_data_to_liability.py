import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_mortgages_liability.csv"))
def test_add_data_to_mortgages_liability(partner_cust_id,customer_id,provider_correspondence_id,data,dataa, field_values, create_client, post_liability_data,post_system_manager_data):

    logger.info(provider_correspondence_id)

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_mortgage = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'liabilities_mortgages_liability', False)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, expected_message)
    logger.info("Liability Details For Mortgage Added Successfully")

    logger.info("Add Data To Mortgage Liability Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/"
                                                         "test_data_loan_hire_purchase_liability.csv"))
def test_add_data_to_loan_hire_purchase_liability(partner_cust_id,customer_id,provider_correspondence_id,data,dataa, field_values,post_system_manager_data, create_client, post_liability_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_loan_hire = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, values, 'liabilities_loan_hire_purchase_liability', False)
    post_loan_hire_response = post_loan_hire.json()
    common.check_reponse_message(post_loan_hire_response, expected_message)
    logger.info("Liability Details For Loan Hire Purchase Added Successfully")

    logger.info("Add Data To Loan Hire Purchase Liability Test Passed!")
# #
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_credit_cards_liability.csv"))
def test_add_data_to_credit_cards_liability(customer_id,partner_cust_id,provider_correspondence_id,data, field_values,dataa,post_system_manager_data, create_client, post_liability_data):

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_credit_card = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id , values, 'liabilities_credit_cards_liability', False)
    post_credit_card_response = post_credit_card.json()
    common.check_reponse_message(post_credit_card_response, expected_message)
    logger.info("Liability Details For Credit Cards Added Successfully")

    logger.info("Add Data To Credit Card Liability Test Passed!")
