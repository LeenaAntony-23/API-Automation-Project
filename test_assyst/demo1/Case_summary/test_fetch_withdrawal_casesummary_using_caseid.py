import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

#  Asset - investment,share-holdings, banks building societies
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_investment_withdrawal_casesummary_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    case_id = post_asset_response['data']['asset_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'asset_investment_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Investment Added Successfully")

    get_assetwithdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_assetwithdrawal_response = get_assetwithdrawal_data.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal Details Fetched Successfully")

    logger.info("Fetch Asset Withdrawal Data using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_share_holdings_withdrawal_casesummary_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'asset_share_holdings_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Share Holdings Added Successfully")

    get_assetwithdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_assetwithdrawal_response = get_assetwithdrawal_data.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal Details For Share Holdings Fetched Successfully")

    logger.info("Fetch Asset Withdrawal Data for share holdings using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_banks_building_societies_withdrawal_casesummary_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks Building Societies Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None,'asset_banks_building_societies_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Banks Building Societies Added Successfully")

    get_assetwithdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_assetwithdrawal_response = get_assetwithdrawal_data.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal Details For Banks Building Societies Fetched Successfully")

    logger.info("Fetch Asset Withdrawal Data for Banks Building Societies using valid Case ID Passed!")

#  Policies - Life assurance, Pensions, Investments, Health assurance, Savings plans, Income protection, General
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_life_assurance_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client,post_policy_data,post_asset_withdrawal_data,get_assetwithdrawal_casesummary_data_with_case_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None,'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_withdrawal_data(customer_id, case_id, None,'policies_life_assurance_withdrawals', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Life Assurance Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Life Assurance Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Life Assurance using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_pensions_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_pensions = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_pensions_withdrawals',True)
    post_pensions_response = post_pensions.json()
    common.check_reponse_message(post_pensions_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Pensions Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Pensions Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Pensions using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_investments_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_investments = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_investments_withdrawals', True)
    post_investments_response = post_investments.json()
    common.check_reponse_message(post_investments_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Investments Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Investments Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Investments using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_savings_plans_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plans Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_savings = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_savings_plans_withdrawals', True)
    post_savings_response = post_savings.json()
    common.check_reponse_message(post_savings_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Savings Plans Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Savings Plans Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Savings Plans using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_income_protection_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_protection = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_health_assurance_withdrawals', True)
    post_protection_response = post_protection.json()
    logger.info(post_protection_response)
    common.check_reponse_message(post_protection_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Income Protection Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Income Protection Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Income Protection using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_health_assurance_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_health_assurance = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_health_assurance_withdrawals', True)
    post_health_assurance_response = post_health_assurance.json()
    common.check_reponse_message(post_health_assurance_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Health Assurance Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For Health Assurance Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For Health Assurance using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_general_data_with_valid_asset_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_asset_withdrawal_data, get_assetwithdrawal_casesummary_data_with_case_id):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_general = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_general_withdrawals', True)
    post_general_response = post_general.json()
    common.check_reponse_message(post_general_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For General Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For General Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For General using valid Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_withdrawal_casesummary_data_with_invalid_case_id(customer_id,data, create_client, get_assetwithdrawal_casesummary_data_with_case_id):


    get_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id('e34960f1-ce23-4985-a5df-d497193be3ab', customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.get_assetwithdrawal_invalid_message)
    logger.info("Fetch Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_withdrawal_casesummary_data_with_invalid_customer_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_asset_withdrawal_data,post_policy_data,post_system_manager_data,dataa, create_client, get_assetwithdrawal_casesummary_data_with_case_id):



    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_general = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_general_withdrawals', True)
    post_general_response = post_general.json()
    common.check_reponse_message(post_general_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For General Added Successfully")

    get_policy_life_assurance_withdrawal_data = get_assetwithdrawal_casesummary_data_with_case_id(case_id, customer_id)
    get_policy_life_assurance_withdrawal_response = get_policy_life_assurance_withdrawal_data.json()
    logger.info(get_policy_life_assurance_withdrawal_response)
    common.check_reponse_message(get_policy_life_assurance_withdrawal_response,
                                 constants.get_assetwithdrawal_success_message)
    assert get_policy_life_assurance_withdrawal_response["isError"] is False
    logger.info("Policy Withdrawal Details For General Fetched Successfully")

    logger.info("Fetch Policy Withdrawal Details For General using valid Case ID Passed!")
