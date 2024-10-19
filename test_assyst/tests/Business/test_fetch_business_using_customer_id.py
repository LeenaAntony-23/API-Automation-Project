import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])

def test_fetch_asset_action_data_with_customer_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, post_business_data,
                                                  get_business_data_with_customer_id):
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

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

# business assigned
#     post_user = post_user_data_for_business_assigned(customer_id, datas, True)
#     post_user = post_user.json()
#     common.check_reponse_message(post_user, constants.add_user_success_message)
#     logger.info(post_user)
#     logger.info("User Details Added Successfully")


    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    logger.info(post_asset_investment_response)
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")

    get_action_data = get_business_data_with_customer_id(customer_id)
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    common.check_reponse_message(get_action_response, constants.get_business_customer_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    common.compare_dicts(post_asset_investment_response['data'], get_action_response['data'])
    logger.info("Fetch Asset Investment Action Data With Customer Id Test Passed!")

def test_fetch_asset_action_data_with_invalid_customer_id(get_business_data_with_customer_id):
    get_action_data = get_business_data_with_customer_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    common.check_reponse_message(get_action_response, constants.get_business_invalid_customer_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Fetch Asset Investment Action Data With Invalid Customer Id Test Passed!")




