import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_liability_review.csv"))
def test_update_data_to_liabilities_mortgages_liability_review(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_review_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']



    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Mortgages Liability Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    case_id=liability_id

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()

    update_liability_data = patch_liability_review_data(customer_id,case_id, values, 'liabilities_mortgages_review',
                                                 False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response, expected_message)
    logger.info("Mortgages Liability Details For Liability Review Updated Successfully")

    logger.info("Update Mortgages Liability Review Data Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_liability_review.csv"))
def test_update_data_to_liabilities_loan_hire_purchase_liability_review(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_review_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Loan Hire Purchase Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    case_id=liability_id

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()

    update_liability_data = patch_liability_review_data(customer_id,case_id, values, 'liabilities_loan_hire_purchase_review',
                                                 False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response, expected_message)
    logger.info("Loan Hire Purchase Details For Liability Review Updated Successfully")

    logger.info("Update Mortgages Liability Loan Hire Purchase Review Data Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Liability/test_data_liability_review.csv"))
def test_update_data_to_liabilities_credit_cards_liability_review(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,patch_liability_review_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']
    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']



    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    logger.info(post_liability_response)
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Credit cards Details For Liability Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    case_id=liability_id

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()

    update_liability_data = patch_liability_review_data(customer_id,case_id, values, 'liabilities_credit_cards_review',
                                                 False)
    update_liability_data_response = update_liability_data.json()
    logger.info(update_liability_data_response)
    common.check_reponse_message(update_liability_data_response, expected_message)
    logger.info("Credit cards Details For Liability Review Updated Successfully")

    logger.info("Update Mortgages Liability Credit cards Review Data Test Passed!")