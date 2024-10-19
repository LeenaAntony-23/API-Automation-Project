import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_payment_asset_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_payment_asset_share_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # provider post
    customer_id = create_client_response['data']['customer_id']

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

    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset ShareHolding Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset ShareHolding Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_payment_asset_bank_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_asset_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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

    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset BankBuilding Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset BankBuilding Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_liability_payment_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_liability_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    case_id =post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'liabilities_mortgages_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilty Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Liability Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_liability_loan_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_liability_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    case_id =post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None,'liabilities_loan_hire_purchase_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilty Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Liability Loan Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_liability_credit_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_liability_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    case_id =post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None,'liabilities_credit_cards_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilty Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Liability Liabiliity Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policy_payment_casesummary_data_with_valid_case_id(post_partner_data,data, post_system_manager_data, dataa,create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_life_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_pensions_payment_casesummary_data_with_valid_case_id(post_partner_data,data, create_client, post_policy_data,
                                               post_asset_payment_data,post_system_manager_data, dataa, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_pensions_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_investments_payment_casesummary_data_with_valid_case_id(post_partner_data,data, post_system_manager_data, dataa,create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_investments_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_savings_plans_payment_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_savings_plans_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_income_protection_payment_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_income_protection_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_health_assurance_payment_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_health_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_policies_general_payment_casesummary_data_with_valid_case_id(post_partner_data,data,post_system_manager_data, dataa, create_client, post_policy_data,
                                               post_asset_payment_data, get_payment_casesummary_data_with_case_id):
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
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_general_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id,case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_payment_casesummary_data_with_invalid_case_id(data, create_client, get_payment_casesummary_data_with_case_id):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id, 'd37fcd87-1881-4798-af93-802fea5027b9')
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.invalid_payment_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_payment_casesummary_data_with_invalid_customer_id(data,post_asset_payment_data,post_policy_data,post_system_manager_data,dataa, create_client, get_payment_casesummary_data_with_case_id):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # provider post
    customer_id = create_client_response['data']['customer_id']
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_policy = post_policy_data(customer_id, provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_general_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    get_payment_data = get_payment_casesummary_data_with_case_id(customer_id, case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")
    get_payment_data = get_payment_casesummary_data_with_case_id('d37fcd87-1881-4798-af93-802fea5027b9', case_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.invalid_payment_message)
    logger.info("Fetch Policy Payment Case Summary Data With Valid Case ID Test Passed!")

