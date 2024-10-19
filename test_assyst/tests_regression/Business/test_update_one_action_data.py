import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_asset_investment_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_asset_data,
                                              post_business_data, patch_business_data):
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
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    logger.info(post_asset_investment_response)
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")
    get_action_data = get_business_data_with_case_id(asset_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_asset_investment_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_asset_investment = patch_business_data(customer_id, asset_id, business_id, values,
                                                 'asset_investment_actions', False)
    patch_asset_investment_response = patch_asset_investment.json()
    common.check_reponse_message(patch_asset_investment_response, expected_message)
    logger.info("Action Details For Investment Updated Successfully")

    logger.info("Update Data To Asset Investment Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(asset_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_liabilities_mortgages_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                   post_business_data, patch_business_data):
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

    client_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = client_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgage Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    post_mortgage = post_business_data(customer_id, liability_id, None, 'liabilities_mortgages_actions', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_business_success_message)
    logger.info("Action Details For Mortgage Added Successfully")
    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_mortgage_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_mortgage = patch_business_data(customer_id, liability_id, business_id, values,
                                         'liabilities_mortgages_actions', False)
    patch_mortgage_response = patch_mortgage.json()
    common.check_reponse_message(patch_mortgage_response, expected_message)
    logger.info("Action Details For Mortgage Updated Successfully")

    logger.info("Update Data To Liability Mortgage Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_liabilities_loan_hire_purchase_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                            post_business_data, patch_business_data):
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

    client_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = client_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Loan Hire Purchase Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    post_loan_hire = post_business_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_actions', True)
    post_loan_hire_response = post_loan_hire.json()
    logger.info(post_loan_hire_response)
    common.check_reponse_message(post_loan_hire_response, constants.add_business_success_message)
    logger.info("Action Details For Loan Hire Purchase Added Successfully")
    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_loan_hire_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_loan_hire = patch_business_data(customer_id, liability_id, business_id, values,
                                          'liabilities_loan_hire_purchase_actions', False)
    patch_loan_hire_response = patch_loan_hire.json()
    common.check_reponse_message(patch_loan_hire_response, expected_message)
    logger.info("Action Details For Loan Hire Purchase Updated Successfully")

    logger.info("Update Data To Liability Loan Purchase Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(liability_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_life_assurance_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                     post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_business_data(customer_id, policy_id, None, 'policies_life_assurance_actions', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_business_success_message)
    logger.info("Action Details For Life Assurance Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_life_assurance_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_life_assurance = patch_business_data(customer_id, policy_id, business_id, values,
                                               'policies_life_assurance_actions', False)
    patch_life_assurance_response = patch_life_assurance.json()
    common.check_reponse_message(patch_life_assurance_response, expected_message)
    logger.info("Action Details For Life Assurance Updated Successfully")

    logger.info("Update Data To Policy Life Assurance Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_pensions_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                               post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_pensions = post_business_data(customer_id, policy_id, None, 'policies_pensions_actions', True)
    post_pensions_response = post_pensions.json()
    common.check_reponse_message(post_pensions_response, constants.add_business_success_message)
    logger.info("Action Details For Pensions Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_pensions_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_pensions = patch_business_data(customer_id, policy_id, business_id, values, 'policies_pensions_actions', False)
    patch_pensions_response = patch_pensions.json()
    common.check_reponse_message(patch_pensions_response, expected_message)
    logger.info("Action Details For Pensions Updated Successfully")

    logger.info("Update Data To Policy Pensions Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_investments_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                  post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_investment = post_business_data(customer_id, policy_id, None, 'policies_investments_actions', True)
    post_investment_response = post_investment.json()
    common.check_reponse_message(post_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investments Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_investment_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_investment = patch_business_data(customer_id, policy_id, business_id, values,
                                           'policies_investments_actions', False)
    patch_investment_response = patch_investment.json()
    common.check_reponse_message(patch_investment_response, expected_message)
    logger.info("Action Details For Investments Updated Successfully")

    logger.info("Update Data To Policy Investment Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_savings_plans_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                    post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_savings_plan = post_business_data(customer_id, policy_id, None, 'policies_savings_plans_actions', True)
    post_savings_plan_response = post_savings_plan.json()
    common.check_reponse_message(post_savings_plan_response, constants.add_business_success_message)
    logger.info("Action Details For Savings Plan Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_savings_plan_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_savings_plan = patch_business_data(customer_id, policy_id, business_id, values,
                                             'policies_savings_plans_actions', False)
    patch_savings_plan_response = patch_savings_plan.json()
    common.check_reponse_message(patch_savings_plan_response, expected_message)
    logger.info(patch_savings_plan_response)
    logger.info("Action Details For Savings Plan Updated Successfully")

    logger.info("Update Data To Policy Savings Plan Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_income_protection_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                        post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id,  None, 'policies_income_protection_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_income_protection = post_business_data(customer_id, policy_id, None, 'policies_income_protection_actions', True)
    post_income_protection_response = post_income_protection.json()
    common.check_reponse_message(post_income_protection_response, constants.add_business_success_message)
    logger.info("Action Details For Income Protection Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_income_protection_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_income_protection = patch_business_data(customer_id, policy_id, business_id, values,
                                                  'policies_income_protection_actions', False)
    patch_income_protection_response = patch_income_protection.json()
    common.check_reponse_message(patch_income_protection_response, expected_message)
    logger.info("Action Details For Income Protection Updated Successfully")

    logger.info("Update Data To Policy Income Protection Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_health_assurance_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                       post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_business_data(customer_id, policy_id, None, 'policies_health_assurance_actions', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_business_success_message)
    logger.info("Action Details For Health Assurance Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_life_assurance_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_health_assurance = patch_business_data(customer_id, policy_id, business_id, values,
                                                 'policies_health_assurance_actions', False)
    patch_health_assurance_response = patch_health_assurance.json()
    common.check_reponse_message(patch_health_assurance_response, expected_message)
    logger.info("Action Details For Health Assurance Updated Successfully")

    logger.info("Update Data To Policy Health Assurance Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Business/test_data_business.csv"))
def test_update_data_policies_general_actions(post_partner_data,get_business_data_with_case_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                              post_business_data, patch_business_data):
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

    client_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = client_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_general = post_business_data(customer_id, policy_id, None, 'policies_general_actions', True)
    post_general_response = post_general.json()
    common.check_reponse_message(post_general_response, constants.add_business_success_message)
    logger.info("Action Details For General Added Successfully")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")

    business_id = post_general_response['data']['business_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_general = patch_business_data(customer_id, policy_id, business_id, values, 'policies_general_actions', False)
    patch_general_response = patch_general.json()
    common.check_reponse_message(patch_general_response, expected_message)
    logger.info("Action Details For General Updated Successfully")

    logger.info("Update Data To Policy General Actions Test Passed!")
    get_action_data = get_business_data_with_case_id(policy_id, customer_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_business_case_id_success_message)
    assert get_action_response["isError"] is False
    logger.info("Action Details For Investment Fetched Successfully")
