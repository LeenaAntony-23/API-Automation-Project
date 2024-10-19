import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_asset_investment_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_investment_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Asset Investment Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Investment withdrawal Data With Valid Withdrawal ID Test Passed!")



@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_asset_sharehold_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_share_holdings_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Asset Shareholdings Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Shareholding withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_asset_bank_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data, post_asset_withdrawal_data,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment asset
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create withdrawal for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, asset_id, None, 'asset_banks_building_societies_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Asset Bank Building Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Asset Bank Building withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policy_life_assurance_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_life_assurance_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Policy Life Assurance Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy Life Assurance withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_pension_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pension Policy Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_pensions_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For Pension Policy Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch  Pension Policy withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policies_investments_withdrawals(post_partner_data,data,post_system_manager_data,dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Policy Investment Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_investments_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For  Policy Investment Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy Investment  withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policies_savings_plans_withdrawals(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Policy Savings Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_savings_plans_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For  Policy Savings Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy Savings  withdrawal Data With Valid Withdrawal ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policies_income_protection_withdrawal(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Policy Income Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_income_protection_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For  Policy Income Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy Income  withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policies_health_assurance_withdrawals(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data,post_policy_data ,get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Policy Health Assurance Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id , None, 'policies_health_assurance_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For  Policy Health Assurance Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy Health Assurance  withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_update_policies_general_withdrawals(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_withdrawal_data, post_policy_data,
                                                      get_withdrawal_data_with_withdrawal_id):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # # Create Investment policy
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

    create_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Policy General Added Successfully")

    # Create withdrawal for the policy investment
    policy_id = create_policy_response['data']['policy_id']
    post_asset_withdrawal = post_asset_withdrawal_data(customer_id, policy_id, None,
                                                       'policies_general_withdrawals', True)
    post_asset_withdrawal_response = post_asset_withdrawal.json()
    common.check_reponse_message(post_asset_withdrawal_response, constants.add_asset_withdrawal_success_message)
    logger.info("Withdrawal Details For  Policy  General Added Successfully")
    logger.info(post_asset_withdrawal_response)

    withdrawal_id = post_asset_withdrawal_response['data']['withdrawal']['withdrawal_id']

    get_withdrawal_data = get_withdrawal_data_with_withdrawal_id(withdrawal_id, customer_id)
    get_withdrawal_response = get_withdrawal_data.json()
    logger.info(get_withdrawal_response)
    common.check_reponse_message(get_withdrawal_response, constants.add_asset_withdrawal_fetch_message)
    logger.info("Fetch Policy General  withdrawal Data With Valid Withdrawal ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_withdrawal_data_with_invalid_withdrawal_id(data, create_client, get_withdrawal_data_with_withdrawal_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    get_asset_data = get_withdrawal_data_with_withdrawal_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0', customer_id)
    get_asset_response = get_asset_data.json()
    common.check_reponse_message(get_asset_response, constants.get_assetwithdrawal_invalid_message)
    assert get_asset_response["isError"] is False
    logger.info("Fetch Asset Investment withdrawal Data With Invalid Case ID Test Passed!")

