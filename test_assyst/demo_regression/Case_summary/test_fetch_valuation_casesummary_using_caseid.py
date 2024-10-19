import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

#  Asset - investment,share-holdings, banks building societies, home personal
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_life_assurance_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_life_assurance_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Life Assurance Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy Life Assurance Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_pensions_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_pensions_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Pensions Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy Pensions Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_investments_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_investments_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Investments Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy Investments Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_income_protection_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_income_protection_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Income Protection Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy Income Protection Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_health_assurance_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_health_assurance_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy Health Assurance Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy Health Assurance Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_general_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_policy_data,post_valuation_data,get_valuation_casesummary_data_with_case_id ):

    post_policy = post_policy_data(customer_id ,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_valuation_policy = post_valuation_data(customer_id, case_id, None, 'policies_general_valuation', True)
    post_valuation_policy_response = post_valuation_policy.json()
    common.check_reponse_message(post_valuation_policy_response, constants.add_valuations_success_message)
    logger.info("Valuations Details For Policy General Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_valuations_customer_id_success_message)
    logger.info("Fetch Policy General Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_investment_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_asset_data,post_valuation_data, get_valuation_casesummary_data_with_case_id):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_valuation_asset = post_valuation_data(customer_id, case_id, None, 'asset_investment_valuation', True)
    post_valuation_asset_response = post_valuation_asset.json()
    common.check_reponse_message(post_valuation_asset_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Asset Investment Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_policy_valuation_success_message)
    logger.info("Fetch Asset Investment Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_share_holdings_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_asset_data,post_valuation_data, get_valuation_casesummary_data_with_case_id):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Share Holdings Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_valuation_asset = post_valuation_data(customer_id, case_id, None, 'asset_share_holdings_valuation', True)
    post_valuation_asset_response = post_valuation_asset.json()
    common.check_reponse_message(post_valuation_asset_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Asset Share Holdings Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_policy_valuation_success_message)
    logger.info("Fetch Asset Share Holdings Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_home_personal_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_asset_data,post_valuation_data, get_valuation_casesummary_data_with_case_id):

    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Home Personal Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_valuation_asset = post_valuation_data(customer_id, case_id, None, 'asset_home_personal_valuation', True)
    post_valuation_asset_response = post_valuation_asset.json()
    common.check_reponse_message(post_valuation_asset_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Asset Home Personal Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info(get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_policy_valuation_success_message)
    logger.info("Fetch Asset Home Personal Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_banks_building_societies_valuation_casesummary_data_with_valid_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, create_client, post_asset_data,post_valuation_data, get_valuation_casesummary_data_with_case_id):

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Banks Building Societies Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_valuation_asset = post_valuation_data(customer_id, case_id, None, 'asset_banks_building_societies_valuation' , True)
    post_valuation_asset_response = post_valuation_asset.json()
    common.check_reponse_message(post_valuation_asset_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Asset Banks Building Societies Added Successfully")

    get_valuation_data = get_valuation_casesummary_data_with_case_id(case_id, customer_id)
    get_valuation_response = get_valuation_data.json()
    logger.info( get_valuation_response)
    common.check_reponse_message(get_valuation_response, constants.get_policy_valuation_success_message)
    logger.info("Fetch Asset Banks Building Societies Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_valuation_casesummary_data_with_invalid_case_id(customer_id,data, create_client, get_valuation_casesummary_data_with_case_id):


    get_fund_data = get_valuation_casesummary_data_with_case_id('d37fcd87-1881-4798-af93-802fea5027b9', customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_invalid_valuation_message)
    assert get_fund_response["isError"] is False
    logger.info("Fetch Valuation Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_valuation_casesummary_data_with_invalid_customer_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_valuation_data, post_asset_data,post_system_manager_data, dataa, create_client, get_valuation_casesummary_data_with_case_id):



    post_asset = post_asset_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset',
                                 True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Banks Building Societies Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_valuation_asset = post_valuation_data(customer_id, case_id, None, 'asset_banks_building_societies_valuation',
                                               True)
    post_valuation_asset_response = post_valuation_asset.json()
    common.check_reponse_message(post_valuation_asset_response, constants.add_valuations_success_message)
    logger.info("Valuation Details For Asset Banks Building Societies Added Successfully")

    get_fund_data = get_valuation_casesummary_data_with_case_id(case_id, 'd37fcd87-1881-4798-af93-802fea5027b9')
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.invalid_customer_id_message)
    assert get_fund_response["isError"] is False
    logger.info("Fetch Valuation Case Summary Data With Valid Case ID Test Passed!")