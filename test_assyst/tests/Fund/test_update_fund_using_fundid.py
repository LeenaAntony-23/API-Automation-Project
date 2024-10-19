import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_asset_investment_fund(post_partner_data,get_fund_data_with_customer_id,data, field_values,post_system_manager_data,dataa, create_client, post_asset_data, post_fund_data, patch_fund_data):
    # Create Client
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

    # # Create Investment asset

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create fund for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_fund = post_fund_data(customer_id, asset_id, None, 'asset_investment_fund', True)
    post_asset_fund_response = post_asset_fund.json()
    logger.info(post_asset_fund_response)
    common.check_reponse_message(post_asset_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details For Asset Investment Added Successfully")
    #logger.info(post_asset_withdrawal_response)

    fund_id = post_asset_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_fund_data = patch_fund_data(customer_id, fund_id,asset_id, values,'asset_investment_fund', False)
    update_fund_data_response = update_fund_data.json()
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info(update_fund_data_response)
    logger.info("Fund Details for life assurance Updated Successfully")

    logger.info("Update Investment Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_life_assurance_policy(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data,patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None,'policies_life_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values,
                                                   'policies_life_assurance_funds', False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Life assurance policy Updated Successfully")

    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_pensions_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data, patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None,'policies_pensions_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_pensions_funds', False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Pension policy Updated Successfully")

    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_investments_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data, patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None,'policies_investments_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_investments_funds', False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Investment policy Updated Successfully")

    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_savings_plans_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data, patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None,'policies_savings_plans_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_savings_plans_funds', False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Savings policy Updated Successfully")

    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_income_protection_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data, patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None,'policies_income_protection_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
             field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_income_protection_funds', False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Income Protection policy Updated Successfully")
    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_health_assurance_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data,
                                                 patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_health_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_health_assurance_funds',
                                       False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for Health Assurance policy Updated Successfully")
    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Fund/test_data_fund.csv"))
def test_update_policies_general_funds(post_partner_data,get_fund_data_with_customer_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data, post_fund_data,
                                                 patch_fund_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    # logger.info(post_policy_response )

    policy_id = post_policy_response['data']['policy_id']
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_general_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    fund_id = post_policy_fund_response['dataValues']['FundId']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_id') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    logger.info(values)
    update_fund_data = patch_fund_data(customer_id, fund_id, policy_id, values, 'policies_general_funds',
                                       False)
    update_fund_data_response = update_fund_data.json()
    logger.info(update_fund_data_response)
    common.check_reponse_message(update_fund_data_response, expected_message)
    logger.info("fund Details for General policy Updated Successfully")
    logger.info("Update policy Fund Test Passed!")
    get_fund_data = get_fund_data_with_customer_id(customer_id)
    get_fund_response = get_fund_data.json()
    logger.info(get_fund_response)
    common.check_reponse_message(get_fund_response, constants.get_fund_fund_id_success_message)
    assert get_fund_response["isError"] is False
    logger.info("Fund Details For General Fetched Successfully")





