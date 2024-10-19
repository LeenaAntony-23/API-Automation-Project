import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_provider_data_with_provider_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data,get_provider_casesummary_data_with_provider_id):

    # asset investment post
    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")
    # asset_id = post_asset_response['data']['asset_id']

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Asset Investment CaseSummary Fetched Successfully")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_liability_mortgage_provider_data_with_provider_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa, create_client, post_liability_data,
                                                  get_provider_casesummary_data_with_provider_id):


    # liability post
    create_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    create_liability_response = create_liability.json()
    common.check_reponse_message(create_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")
    # liability_id = create_liability_response['data']['liability_id']

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Liability Mortgages CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_life_assurance_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                                       get_provider_casesummary_data_with_provider_id):


    # policy post
    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")
    # policy_id = create_policy_response['data']['policy_id']

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_pensions_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa,create_client, post_policy_data,
                                                 get_provider_casesummary_data_with_provider_id):


    # post policy
    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_Policy_investment_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa,create_client, post_policy_data,
                                                   get_provider_casesummary_data_with_provider_id):

    # policy post
    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investment Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_savings_plan_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                                     get_provider_casesummary_data_with_provider_id):


    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_income_protection_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                                          post_business_data, get_provider_casesummary_data_with_provider_id):


    # policy post
    post_policy = post_policy_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_health_assurance_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                                         post_business_data, get_provider_casesummary_data_with_provider_id):


    # policy post
    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_general_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa,create_client, post_policy_data,
                                                get_provider_casesummary_data_with_provider_id):


    # policy post
    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    # get
    get_provider_data = get_provider_casesummary_data_with_provider_id(provider_correspondence_id)
    get_provider_response = get_provider_data.json()
    logger.info(get_provider_response)
    common.check_reponse_message(get_provider_response, constants.get_providers_success_message)
    assert get_provider_response["isError"] is False
    logger.info("Provider Details For Policy Life Assurance CaseSummary Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_business_action_with_invalid_provider_id(customer_id,data, create_client, get_provider_casesummary_data_with_provider_id):

    get_action_data = get_provider_casesummary_data_with_provider_id('e34960f1-ce23-4985-a5df-d497193be3ab')
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.invalid_provider_id_message)
    assert get_action_response["isError"] is False
    logger.info("Fetch Action Data CaseSummary With Invalid Case ID Test Passed!")
