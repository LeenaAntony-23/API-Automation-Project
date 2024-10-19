import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_asset_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_asset_data, post_business_data,
                                              get_business_data_with_case_id):


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")

    get_action_data = get_business_data_with_case_id(asset_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    common.compare_dicts(post_asset_investment_response['data'], get_action_response['data'])
    logger.info("Fetch Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_mortgages_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_liability_data, post_business_data,
                                                  get_business_data_with_case_id):

    create_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    create_liability_response = create_liability.json()
    common.check_reponse_message(create_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")

    liability_id = create_liability_response['data']['liability_id']
    post_liability_mortgage = post_business_data(customer_id, liability_id, None, 'liabilities_mortgages_actions', True)
    post_liability_mortgage_response = post_liability_mortgage.json()
    common.check_reponse_message(post_liability_mortgage_response, constants.add_business_success_message)
    logger.info("Action Details For Mortgages Added Successfully")

    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Mortgages Fetched Successfully")

    common.compare_dicts(post_liability_mortgage_response['data'], get_action_response['data'])
    logger.info("Fetch Mortgages Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_loan_hire_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_liability_data, post_business_data,
                                                  get_business_data_with_case_id):


    create_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    create_liability_response = create_liability.json()
    common.check_reponse_message(create_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Loan Hire Added Successfully")

    liability_id = create_liability_response['data']['liability_id']
    post_liability_loan_hire = post_business_data(customer_id, liability_id, None,
                                                  'liabilities_loan_hire_purchase_actions', True)
    post_liability_loan_hire_response = post_liability_loan_hire.json()
    common.check_reponse_message(post_liability_loan_hire_response, constants.add_business_success_message)
    logger.info("Action Details For Loan Hire Added Successfully")

    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Loan Hire Fetched Successfully")

    common.compare_dicts(post_liability_loan_hire_response['data'], get_action_response['data'])
    logger.info("Fetch Loan Hire Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_life_assurance_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_business_data,
                                                       get_business_data_with_case_id):


    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_life_assurance = post_business_data(customer_id, policy_id, None, 'policies_life_assurance_actions', True)
    post_policy_life_assurance_response = post_policy_life_assurance.json()
    common.check_reponse_message(post_policy_life_assurance_response, constants.add_business_success_message)
    logger.info("Action Details For Life Assurance Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Life Assurance Fetched Successfully")

    common.compare_dicts(post_policy_life_assurance_response['data'], get_action_response['data'])
    logger.info("Fetch Life Assurance Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_pensions_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_business_data,
                                                 get_business_data_with_case_id):



    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_pensions = post_business_data(customer_id, policy_id, None, 'policies_pensions_actions', True)
    post_policy_pensions_response = post_policy_pensions.json()
    common.check_reponse_message(post_policy_pensions_response, constants.add_business_success_message)
    logger.info("Action Details For Pensions Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Pensions Fetched Successfully")

    common.compare_dicts(post_policy_pensions_response['data'], get_action_response['data'])
    logger.info("Fetch Pensions Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_investment_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa,create_client, post_policy_data, post_business_data,
                                                   get_business_data_with_case_id):

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investment Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_investment = post_business_data(customer_id, policy_id, None, 'policies_investments_actions', True)
    post_policy_investment_response = post_policy_investment.json()
    common.check_reponse_message(post_policy_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    common.compare_dicts(post_policy_investment_response['data'], get_action_response['data'])
    logger.info("Fetch Investment Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_savings_plan_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_business_data,
                                                     get_business_data_with_case_id):


    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id,None, 'policies_savings_plans_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_investment = post_business_data(customer_id, policy_id, None, 'policies_savings_plans_actions', True)
    post_policy_investment_response = post_policy_investment.json()
    common.check_reponse_message(post_policy_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Savings Plan Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Savings Plan Fetched Successfully")

    common.compare_dicts(post_policy_investment_response['data'], get_action_response['data'])
    logger.info("Fetch Savings Plan Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_income_protection_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data, post_system_manager_data, dataa, create_client, post_policy_data,
                                                          post_business_data, get_business_data_with_case_id):


    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_income_protection = post_business_data(customer_id, policy_id, None,
                                                       'policies_income_protection_actions', True)
    post_policy_income_protection_response = post_policy_income_protection.json()
    common.check_reponse_message(post_policy_income_protection_response, constants.add_business_success_message)
    logger.info("Action Details For Income Protection Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Income Protection Fetched Successfully")

    common.compare_dicts(post_policy_income_protection_response['data'], get_action_response['data'])
    logger.info("Fetch Income Protection Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_health_assurance_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                                         post_business_data, get_business_data_with_case_id):


    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_health_assurance = post_business_data(customer_id, policy_id, None,
                                                      'policies_health_assurance_actions', True)
    post_policy_health_assurance_response = post_policy_health_assurance.json()
    common.check_reponse_message(post_policy_health_assurance_response, constants.add_business_success_message)
    logger.info("Action Details For Health Assurance Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Health Assurance Fetched Successfully")

    common.compare_dicts(post_policy_health_assurance_response['data'], get_action_response['data'])
    logger.info("Fetch Health Assurance Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_general_action_data_with_case_id(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, create_client, post_policy_data, post_business_data,
                                                get_business_data_with_case_id):


    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_general = post_business_data(customer_id, policy_id, None, 'policies_general_actions', True)
    post_policy_general_response = post_policy_general.json()
    common.check_reponse_message(post_policy_general_response, constants.add_business_success_message)
    logger.info("Action Details For Health Assurance Added Successfully")

    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Health Assurance Fetched Successfully")

    common.compare_dicts(post_policy_general_response['data'], get_action_response['data'])
    logger.info("Fetch Health Assurance Action Data With Case Id Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_business_action_with_invalid_case_id(customer_id,data, create_client, get_business_data_with_case_id):

    get_action_data = get_business_data_with_case_id('e34960f1-ce23-4985-a5df-d497193be3ab', customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.invalid_case_id_message)
    assert get_action_response["isError"] is False
    logger.info("Fetch Action Data With Invalid Case ID Test Passed!")