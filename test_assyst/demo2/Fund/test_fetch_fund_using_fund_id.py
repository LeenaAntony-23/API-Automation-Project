import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data,post_fund_data,get_fund_data_with_fund_id):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']

    post_policy_fund = post_fund_data(customer_id, asset_id, None, 'asset_investment_fund', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details For Asset Investment Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Investment Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Investment With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_life_assurance_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_life_assurance_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Life Assurance Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Life Assurance Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Life Assurance With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_pensions_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_pensions_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Pensions Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Pensions Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Pensions With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_investments_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_investments_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Investments Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Investments Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Investments With Fund_Id Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_savings_plans_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_savings_plans_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Savings Plan Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Savings Plan Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Savings Plan With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_income_protection_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_income_protection_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Income Protection Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Income Protection Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Income Protection With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_health_assurance_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_health_assurance_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Health Assurance Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For Health Assurance Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For Health Assurance With Fund_Id Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_fund_data_with_fund_id(customer_id,partner_cust_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']

    post_asset_fund = post_fund_data(customer_id, policy_id, None, 'policies_general_funds', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For General Added Successfully")

    fund_id = post_asset_fund_response['dataValues']['FundId']
    logger.info(fund_id)

    get_fund_data = get_fund_data_with_fund_id(fund_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")

    # common.compare_dicts(post_asset_fund_response['data'], get_fund_response['data'])
    logger.info("Fetch Fund Details For General With Fund_Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policies_general_fund_data_with_invalid_fund_id(customer_id,data, create_client, post_policy_data,post_fund_data,get_fund_data_with_fund_id):


    get_fund_data = get_fund_data_with_fund_id("517aca64-7a06-4849-b77b-e91332e35606", customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_invalid_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")

    logger.info("Fetch Fund Details For General With Invalid Fund_Id Test Passed!")
