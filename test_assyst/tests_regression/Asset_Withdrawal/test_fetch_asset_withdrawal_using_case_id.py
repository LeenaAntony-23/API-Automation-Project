import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_create_and_fetch_assetwithdrwal_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    case_id=post_asset_response['data']['asset_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'asset_investment_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Investment Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Asset Withdrawal  Data using Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_asset_share_holdings_withdrawal_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details  Added Successfully")

    case_id=post_asset_response['data']['asset_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'asset_share_holdings_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Shareholdings Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Asset Withdrawal  Data using Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_asset_banks_building_societies_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details  Added Successfully")

    case_id=post_asset_response['data']['asset_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'asset_banks_building_societies_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Asset Withdrawal Details For Bank building Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Asset Withdrawal  Data using Case ID Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_life_assurance_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_life_assurance_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Life assurance Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_pensions_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_pensions_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Life assurance Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_general_policy_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_general_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Pension Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_investments_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_investments_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Investment Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_savings_plans_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_savings_plans_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Savings Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_income_protection_withdrawals_data(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_income_protection_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Income protection Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_policies_health_assurance_withdrawals_data(post_partner_data,data,post_system_manager_data,dataa, create_client, post_policy_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']

    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, case_id, None, 'policies_health_assurance_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    logger.info(post_asset_withdrawal_response)
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_assetwithdrawal_success_message)
    logger.info("Policy Withdrawal Details For Health Assurance Added Successfully")

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,case_id)
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    logger.info(get_assetwithdrawal_response)
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_success_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Policy Withdrawal  Details Fetched Successfully")

    logger.info("Fetch Policy Withdrawal  Data using Case ID Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_invalid_assetwithdrawal_data(data, create_client, post_asset_data, get_assetwithdrawal_with_asset_id,post_asset_withdrawal_data ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    get_assetwithdrawal_details = get_assetwithdrawal_with_asset_id(customer_id,'a9129a87-5c6c-45bb-914f-a2b1bd567171')
    get_assetwithdrawal_response = get_assetwithdrawal_details.json()
    common.check_reponse_message(get_assetwithdrawal_response, constants.get_assetwithdrawal_invalid_message)
    assert get_assetwithdrawal_response["isError"] is False
    logger.info("Asset Withdrawal Details Fetched Successfully")

    logger.info("Fetch Asset Withdrawal Data using Invalid Case ID Passed!")