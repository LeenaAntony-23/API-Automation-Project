import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_create_and_fetch_case_summary_liability_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_liability_data, get_casesummary_liability_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # provider post
    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    get_liability_details = get_casesummary_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Mortgage Casesummary Details Fetched Successfully")

    logger.info("Fetch Liability Casesummary Data Of One Customer Test Passed!")


def test_fetch_liability_data_with_invalid_customer_id(get_casesummary_liability_data_with_customer_id):
    get_client_data = get_casesummary_liability_data_with_customer_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_liability_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Liability Data With Invalid Customer ID Test Passed!")
