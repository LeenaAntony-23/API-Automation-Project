import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_asset_details_with_asset_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None,'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    get_asset_details = get_asset_details_with_asset_id(asset_id, customer_id)
    get_asset_response = get_asset_details.json()
    common.check_reponse_message(get_asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(get_asset_response)
    #common.compare_dicts(post_asset_response['data'], get_asset_response['data'])

    logger.info("Fetch Asset Data With valid Asset ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_share_holdings_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_asset_details_with_asset_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None,'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    get_asset_details = get_asset_details_with_asset_id(asset_id, customer_id)
    get_asset_response = get_asset_details.json()
    common.check_reponse_message(get_asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(get_asset_response)
    #common.compare_dicts(post_asset_response['data'], get_asset_response['data'])

    logger.info("Fetch Asset Data With valid Asset ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_home_personal_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_asset_details_with_asset_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None,'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    get_asset_details = get_asset_details_with_asset_id(asset_id, customer_id)
    get_asset_response = get_asset_details.json()
    common.check_reponse_message(get_asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(get_asset_response)
    #common.compare_dicts(post_asset_response['data'], get_asset_response['data'])

    logger.info("Fetch Asset Data With valid Asset ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_banks_building_societies_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_asset_details_with_asset_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None,'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    get_asset_details = get_asset_details_with_asset_id(asset_id, customer_id)
    get_asset_response = get_asset_details.json()
    common.check_reponse_message(get_asset_response, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")
    logger.info(get_asset_response)
    #common.compare_dicts(post_asset_response['data'], get_asset_response['data'])

    logger.info("Fetch Asset Data With valid Asset ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_data_with_invalid_asset_id(data, create_client, get_asset_details_with_asset_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    get_asset_data = get_asset_details_with_asset_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0', customer_id)
    get_asset_response = get_asset_data.json()
    common.check_reponse_message(get_asset_response, constants.asset_invlaid_customer_message)
    assert get_asset_response["isError"] is False
    logger.info("Fetch Asset Data With Invalid Asset ID Test Passed!")