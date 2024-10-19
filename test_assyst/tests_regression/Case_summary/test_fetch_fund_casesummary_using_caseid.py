import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_investment_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    logger.info(case_id)
    post_asset_fund = post_fund_data(customer_id, case_id, None, 'asset_investment_fund', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details For Asset Investment Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Asset Investment Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_life_assurance_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data,dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_life_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Policy Life Insurance Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_pensions_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # provider post
    customer_id = create_client_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Pensions Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_pensions_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Policy pensions Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Pensions Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_investments_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Investments Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_investments_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Policy Investments Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Investments Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_savings_plans_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Savings Plans Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_savings_plans_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Policy Savings Plans Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Savings Plans Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_income_protection_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Income Protection Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_income_protection_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Income Protection Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Income Protection Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_health_assurance_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Health Assurance Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_health_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For Health Assurance Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch Health Assurance Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_general_fund_casesummary_data_with_valid_asset_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,  post_fund_data, get_fund_casesummary_data_with_case_id):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy General Details Added Successfully")

    case_id = post_policy_response ['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_general_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For General Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_asset_fund_success_message)
    logger.info("Fetch General Policy Fund Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_fund_casesummary_data_with_invalid_case_id(data, create_client, get_fund_casesummary_data_with_case_id):

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

    get_fund_data = get_fund_casesummary_data_with_case_id('d37fcd87-1881-4798-af93-802fea5027b9', customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_invalid_fund_message)
    logger.info("Fetch Policy Fund Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_fund_casesummary_data_with_invalid_customer_id(post_partner_data,data,post_fund_data,post_policy_data, post_system_manager_data, dataa,create_client, get_fund_casesummary_data_with_case_id):

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
    customer_id = create_client_response['data']['customer_id']

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy General Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    logger.info(case_id)
    post_policy_fund = post_fund_data(customer_id, case_id, data, 'policies_general_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    logger.info(post_policy_fund_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_fund_success_message)
    logger.info("Fund Details For General Added Successfully")

    get_fund_data = get_fund_casesummary_data_with_case_id(case_id, 'd37fcd87-1881-4798-af93-802fea5027b9')
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.invalid_customer_id_message)
    logger.info("Fetch Policy Fund Case Summary Data With Valid Case ID Test Passed!")
