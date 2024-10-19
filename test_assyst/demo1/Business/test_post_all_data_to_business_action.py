import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_investment_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data, post_business_data):

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_investment = post_business_data(customer_id, asset_id,  values, 'asset_investment_actions', False)
    post_asset_investment_response = post_asset_investment.json()
    common.check_reponse_message(post_asset_investment_response, expected_message)
    logger.info("Action Details For Investment Added Successfully")
    logger.info(post_asset_investment_response)
    logger.info("Add Data To Asset Investment Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_liabilities_mortgages_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                   post_business_data):


    client_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = client_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgage Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_mortgage = post_business_data(customer_id, liability_id, values, 'liabilities_mortgages_actions', False)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, expected_message)
    logger.info("Action Details For Mortgage Added Successfully")

    logger.info("Add Data To Liability Mortgage Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_liabilities_loan_hire_purchase_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                            post_business_data):



    client_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = client_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Loan Hire Purchase Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_investment = post_business_data(customer_id, liability_id, values,
                                               'liabilities_loan_hire_purchase_actions', False)
    post_asset_investment_response = post_asset_investment.json()
    common.check_reponse_message(post_asset_investment_response, expected_message)
    logger.info("Action Details For Loan Hire Purchase Added Successfully")

    logger.info("Add Data To Liability Loan Purchase Actions Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_life_assurance_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                                     post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy_life_assurance = post_business_data(customer_id, policy_id, values,
                                                    'policies_life_assurance_actions', False)
    post_policy_life_assurance_response = post_policy_life_assurance.json()
    common.check_reponse_message(post_policy_life_assurance_response, expected_message)
    logger.info("Action Details For Life Assurance Added Successfully")

    logger.info("Add Data To Policy Life Assurance Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_pensions_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy_pension = post_business_data(customer_id, policy_id, values, 'policies_pensions_actions', False)
    post_policy_pension_response = post_policy_pension.json()
    common.check_reponse_message(post_policy_pension_response, expected_message)
    logger.info("Action Details For Pensions Added Successfully")

    logger.info("Add Data To Policy Pensions Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_investments_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                  post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy_investment = post_business_data(customer_id, policy_id, values, 'policies_investments_actions', False)
    post_policy_investment_response = post_policy_investment.json()
    common.check_reponse_message(post_policy_investment_response, expected_message)
    logger.info("Action Details For Investments Added Successfully")

    logger.info("Add Data To Policy Investement Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_savings_plans_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                    post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_policy_savings = post_business_data(customer_id, policy_id, values, 'policies_savings_plans_actions', False)
    post_policy_savings_response = post_policy_savings.json()
    common.check_reponse_message(post_policy_savings_response, expected_message)
    logger.info("Action Details For Savings Plan Added Successfully")

    logger.info("Add Data To Policy Savings Plan Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_income_protection_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                        post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_income_protection = post_business_data(customer_id, policy_id, values,
                                                'policies_income_protection_actions', False)
    post_income_protection_response = post_income_protection.json()
    common.check_reponse_message(post_income_protection_response, expected_message)
    logger.info("Action Details For Income Protection Added Successfully")

    logger.info("Add Data To Policy Income Protection Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_health_assurance_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                       post_business_data):

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_health_assurance = post_business_data(customer_id, policy_id, values,
                                               'policies_health_assurance_actions', False)
    post_health_assurance_response = post_health_assurance.json()
    common.check_reponse_message(post_health_assurance_response, expected_message)
    logger.info("Action Details For Health Assurance Added Successfully")

    logger.info("Add Data To Policy Health Assurance Actions Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_add_data_to_policies_general_actions(customer_id,partner_cust_id,provider_correspondence_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data, post_business_data):


    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_general_policy = post_business_data(customer_id, policy_id, values, 'policies_general_actions', False)
    post_general_policy_response = post_general_policy.json()
    common.check_reponse_message(post_general_policy_response, expected_message)
    logger.info("Action Details For General Added Successfully")

    logger.info("Add Data To Policy General Actions Test Passed!")

