import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_mortgages_liability.csv"))
def test_update_data_to_liabilities_mortgages_liability(partner_cust_id,customer_id,provider_correspondence_id,get_liability_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_data):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Mortgages Liability Details For Liability Added Successfully")

    customer_id = post_liability_response['data']['customer_id']
    liability_id = post_liability_response['data']['liability_id']
    #provider_id = post_liability_response['data']['provider_id']
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_liability_data = patch_liability_data(customer_id,provider_correspondence_id, liability_id, values, 'liabilities_mortgages_liability', False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response,expected_message)
    logger.info("Mortgages Liability Details For Liability Updated Successfully")

    logger.info("Update Mortgages Liability Data Test Passed!")
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_loan_hire_purchase_liability.csv"))
def test_update_data_to_loan_hire_purchase(partner_cust_id,customer_id,provider_correspondence_id,get_liability_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_data):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Loan Hire Purchase Details For Liability Added Successfully")
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")
    customer_id = post_liability_response['data']['customer_id']
    liability_id = post_liability_response['data']['liability_id']
    #provider_id = post_liability_response['data']['provider_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_liability_data = patch_liability_data(customer_id,provider_correspondence_id, liability_id, values, 'liabilities_loan_hire_purchase_liability', False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response,expected_message)
    logger.info("Loan Hire Purchase Details For Liability Updated Successfully")

    logger.info("Update Loan Hire Purchase Data Test Passed!")
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_credit_cards_liability.csv"))
def test_update_data_to_credit_cards_liability(partner_cust_id,customer_id,provider_correspondence_id,get_liability_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_data):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Credit cards Details For Liability Added Successfully")
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    customer_id = post_liability_response['data']['customer_id']
    liability_id = post_liability_response['data']['liability_id']
    #provider_id = post_liability_response['data']['provider_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_liability_data = patch_liability_data(customer_id,provider_correspondence_id, liability_id, values, 'liabilities_credit_cards_liability', False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response,expected_message)
    logger.info("Credit cards Details For Liability Updated Successfully")

    logger.info("Update Credit cards Data Test Passed!")
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")