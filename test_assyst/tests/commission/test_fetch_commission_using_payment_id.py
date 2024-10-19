import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                    'asset_investment_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Asset Investment Added Successfully")

    case_id=post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_payment_id(customer_id,payment_id,case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Investment using Payment ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_share_holdings_commission_data_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,get_asset_commission_data_with_payment_id, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset share holding Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                    'asset_share_holdings_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Asset share holding Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    payment_id = post_commission_response['data']['payment_id']
    case_id=post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_payment_id(customer_id,payment_id,case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset share holding Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset share holding using Payment ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_asset_banks_building_data_using_payment_id(post_partner_data,data,post_system_manager_data,dataa, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For banks and buildings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset banks and buildings Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                    'asset_banks_building_societies_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Asset banks and buildings Added Successfully")

    commission_id = post_commission_response['data']['commission_id']
    customer_id = post_commission_response['data']['customer_id']
    payment_id = post_commission_response['data']['payment_id']
    case_id=post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_payment_id(customer_id,payment_id,case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset banks and buildings Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset banks and buildings using Payment ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liab_mortgage_data_using_payment_id(post_partner_data,data,post_system_manager_data,dataa, create_client, post_liability_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_mortgage = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                        'liabilities_mortgages_liability', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")
    liability_id = post_mortgage_response['data']['liability_id']

    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_mortgages_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For liability Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                 'liabilities_mortgages_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For liability Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Liability mortgage Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Liability mortgage using Payment ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liab_loan_hire_using_payment_id(post_partner_data,data,post_system_manager_data,dataa, create_client, post_liability_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_mortgage = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                        'liabilities_loan_hire_purchase_liability', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")
    liability_id = post_mortgage_response['data']['liability_id']

    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For liability Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                 'liabilities_loan_hire_purchase_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For liability Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Liability loan hire purchase Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Liability loan hire purchase using Payment ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_all_data_from_liabilities_credit_card_data_using_payment_id(post_partner_data,data, post_system_manager_data, dataa, create_client, post_liability_data,
                                                       post_asset_payment_data, post_asset_commission_data,get_asset_commission_data_with_payment_id):
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
    post_mortgage = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_credit_cards_liability', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For credit card Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_credit_cards_payments', True)
    post_mortgage_response = post_mortgage.json()
    logger.info(post_mortgage_response)
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For credit card Added Successfully")
    payment_id = post_mortgage_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                 'liabilities_credit_cards_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For liability credit card Added Successfully")


    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For liability credit card Fetched Successfully")
    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For liability credit card using Payment ID Test Passed!")



@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_pension_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_pensions_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_pensions_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_pensions_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy pension Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy pension using Payment ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_investment_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_investments_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_investments_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy pension Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy pension using Payment ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_savings_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_savings_plans_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_savings_plans_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_savings_plans_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy pension Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy pension using Payment ID Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_income_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_income_protection_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_income_protection_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_income_protection_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy pension Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy pension using Payment ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_general_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_general_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_general_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy pension Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy pension using Payment ID Test Passed!")



@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_policy_life_commission_using_payment_id(post_partner_data,data,post_system_manager_data,dataa,post_policy_data, create_client, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_life_assurance_policy',
                                   True)
    post_policy_response = post_policy.json()
    logger.info(post_policy_response)
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_life_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policy Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None, 'policies_life_assurance_payments_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Policy Added Successfully")

    case_id = post_commission_response['data']['case_id']
    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, payment_id, case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Policy life assurance Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Policy life assurance using Payment ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_all_data_of_commission_using_invalid_payment_id(post_partner_data,post_system_manager_data,dataa,data, create_client, post_asset_data, post_asset_payment_data,post_asset_commission_data,get_asset_commission_data_with_payment_id ):
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
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id , None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']

    post_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                 'asset_investment_payment_commission', True)
    post_commission_response = post_commission.json()
    logger.info(post_commission_response)
    common.check_reponse_message(post_commission_response, constants.add_as_pol_liab_commission_success_message)
    logger.info("Commission Details For Asset Investment Added Successfully")


    case_id = post_commission_response['data']['case_id']

    get_commission_data = get_asset_commission_data_with_payment_id(customer_id, "882a5379-42cc-4ae2-9e36-fc81a9cda055", case_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_invalid_payment_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

    #common.compare_dicts(post_commission_response['data'], get_commission_response['data'])
    logger.info("Fetch Commission Details For Asset Investment using Invalid Payment ID Test Passed!")