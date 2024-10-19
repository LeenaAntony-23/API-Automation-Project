import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_asset_Investment_case_action( post_system_manager_data, data, data_sys, create_client, post_asset_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_asset = post_asset_data(customer_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_asset_response['data']['asset_id']
    tracking_id = post_case_action_response ['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id,tracking_id, 'asset_investment_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response, constants.add_default_load_standard_case_action_category)
    logger.info("Default Case Action Added Successfully")

    logger.info("Default Case Action Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_liabilities_mortgages_case_action( post_system_manager_data, data, data_sys, create_client, post_liability_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_liability = post_liability_data(customer_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_liability_response['data']['liability_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'liabilities_mortgages_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response, constants.add_default_load_standard_case_action_category)
    logger.info("Default Case Action Details Added Successfully")

    logger.info("Default Case Action Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_liabilities_loan_hire_purchase_case_action( post_system_manager_data, data, data_sys, create_client, post_liability_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_liability = post_liability_data(customer_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Loan Hire Purchase Details For Liability Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_liability_response['data']['liability_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action_response = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'liabilities_loan_hire_purchase_actions')
    post_default_case_action_response_response = post_default_case_action_response.json()
    logger.info(post_default_case_action_response_response)
    common.check_reponse_message(post_default_case_action_response_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Case Action Details Added Successfully")

    logger.info("Default Case Action Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_life_assurance_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action_response = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_life_assurance_actions')
    post_default_case_action_response_response = post_default_case_action_response.json()
    logger.info(post_default_case_action_response_response)
    common.check_reponse_message(post_default_case_action_response_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_pensions_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action_response = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_pensions_actions')
    post_default_case_action_response_response = post_default_case_action_response.json()
    logger.info(post_default_case_action_response_response)
    common.check_reponse_message(post_default_case_action_response_response,
                                 constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_investments_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action_response = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_investments_actions')
    post_default_case_action_response_response = post_default_case_action_response.json()
    logger.info(post_default_case_action_response_response)
    common.check_reponse_message(post_default_case_action_response_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_savings_plans_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_savings_plans_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_income_protection_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_income_protection_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_health_assurance_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_health_assurance_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_load_standard_policies_general_case_action( post_system_manager_data, data, data_sys, create_client, post_policy_data,
                                     post_default_load_standard_case_action ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    customer_id = create_client_response['data']['customer_id']
    post_policy = post_policy_data(customer_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    post_case_action = post_system_manager_data(data_sys, 'tracking_case_actions', True)
    post_case_action_response = post_case_action.json()
    common.check_reponse_message(post_case_action_response, constants.post_case_success_message)
    logger.info("Case actions Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    case_id = post_policy_response['data']['policy_id']
    tracking_id = post_case_action_response['data']['id']

    post_default_case_action = post_default_load_standard_case_action(customer_id, case_id, tracking_id,'policies_general_actions')
    post_default_case_action_response = post_default_case_action.json()
    logger.info(post_default_case_action_response)
    common.check_reponse_message(post_default_case_action_response,constants.add_default_load_standard_case_action_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")
