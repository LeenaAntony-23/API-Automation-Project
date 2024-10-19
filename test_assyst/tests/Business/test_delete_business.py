import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')
#
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_action_delete_asset_investment(data,dataa,create_client,delete_case_details,post_system_manager_data,post_asset_data,post_business_data,get_business_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    client_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                   'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")
    asset_id = post_asset_response['data']['asset_id']

    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    logger.info(post_asset_investment_response)
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")
    action_id = post_asset_investment_response['data']['business_id']

    get_action_data = get_business_data_with_customer_id(customer_id)
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    common.check_reponse_message(get_action_response, constants.get_business_customer_id_success_message)
    logger.info("Action Details For Investment Fetched Successfully")

    delete_client_data = delete_case_details('action', action_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Action Details Deleted Successfully")

    get_action_data = get_business_data_with_customer_id(customer_id)
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    common.check_reponse_message(get_action_response, constants.get_business_customer_id_success_message)
    logger.info("Action Details For Investment Fetched Successfully")
