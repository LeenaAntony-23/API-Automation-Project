import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_valuations_data_with_customer_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_policy_data, post_valuation_data ,get_valuation_data_with_customer_id ):
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

    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']



    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_valuation_data = post_valuation_data(customer_id, policy_id, None, 'policies_general_valuation', True)
    post_valuation_data_response = post_valuation_data.json()
    logger.info(post_valuation_data_response)
    common.check_reponse_message(post_valuation_data_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy General Added Successfully")

    get_valuation_data = get_valuation_data_with_customer_id(customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Valuations Details For Policy General Fetched Successfully")

    #common.compare_dicts(post_valuation_data_response['data'], get_valuation_response['data'])
    logger.info("Fetch Valuations Details For Policy General With Customer ID Test Passed!")

def test_fetch_policies_general_valuations_data_with_invalid_customer_id(get_valuation_data_with_customer_id):
    get_valuation_data = get_valuation_data_with_customer_id('aff44303-74fa-4ba6-b18d-b6bd68f0725a')
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_invalid_customer_id_success_message)
    assert get_valuation_response["isError"] is False
    logger.info("Fetch Valuations Data With Invalid Customer ID Test Passed!")