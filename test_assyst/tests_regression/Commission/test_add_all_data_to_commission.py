import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_add_data_to_asset_investment_payment_commission(post_partner_data,data,dataa,post_system_manager_data, field_values, create_client, post_asset_data,
                                                         post_asset_payment_data, post_asset_commission_data):
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

    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create Payment for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, asset_id, payment_id, values,
                                                    'asset_investment_payment_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Payment Commission Details For Investment Added Successfully")

    logger.info("Commission Details For Asset Investment Added Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_add_data_to_asset_share_holdings_commission(post_partner_data,data, field_values, create_client, post_asset_data,
                                                         post_asset_payment_data,post_system_manager_data, dataa, post_asset_commission_data):
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
    logger.info("Asset Details For Share Holdings Added Successfully")

    # Create Payment for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Share Holdings Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, asset_id, payment_id, values,
                                                    'asset_share_holdings_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Payment Commission Details For Share Holdings Added Successfully")

    logger.info("Commission Details For Asset Share Holdings Added Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_add_data_to_asset_banks_building_commission(post_partner_data,data, field_values, create_client, post_asset_data,post_system_manager_data, dataa,
                                                     post_asset_payment_data, post_asset_commission_data):
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

    client_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Banks Building Societies Added Successfully")

    # Create Payment for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Banks Building Societies Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, asset_id, payment_id, values,
                                                    'asset_banks_building_societies_payment_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Asset Payment Commission Details For Banks Building Societies Added Successfully")

    logger.info("Commission Details For Asset Banks Building Societies Added Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_liabilities_mortgages_payment_commission(post_partner_data,data, field_values, create_client, post_liability_data,post_system_manager_data, dataa,
                                                       post_asset_payment_data, post_asset_commission_data):
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


    post_mortgage = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_mortgages_payment', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Mortgages Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, liability_id, payment_id, values,
                                                    'liabilities_mortgages_payment_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Liability Payment Commission Details For Mortgages Added Successfully")

    logger.info("Add Data To Liability Payment Commission Details For Mortgages Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_liabilities_loan_hire_payment_commission(post_partner_data,data, field_values, create_client, post_liability_data,post_system_manager_data, dataa ,
                                                       post_asset_payment_data, post_asset_commission_data):
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

    post_mortgage = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Loan Hire Purchase Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Loan Hire Purchase Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, liability_id, payment_id, values,
                                                    'liabilities_loan_hire_purchase_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Liability Payment Commission Details For Loan Hire Purchase Added Successfully")

    logger.info("Add Data To Liability Payment Commission Details For Loan Hire Purchase Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_liabilities_credit_card_payment_commission(post_partner_data,data, field_values, create_client, post_liability_data,post_system_manager_data, dataa,
                                                       post_asset_payment_data, post_asset_commission_data):
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
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Credit Card Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_credit_cards_payments', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Credit Card Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    logger.info(payment_id)
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, liability_id, payment_id, values,
                                                    'liabilities_credit_cards_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Liability Payment Commission Details For Credit Card Added Successfully")

    logger.info("Add Data To Liability Payment Commission Details For Credit Card Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_life_assurance_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                         post_asset_payment_data, post_asset_commission_data):
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
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_life_assurance_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For Life Assurance Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_life_assurance_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For Life Assurance Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For Life Assurance Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_pension_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data,
                                                              post_asset_payment_data, post_asset_commission_data):
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
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_pensions_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For Pensions Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_pensions_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For Pensions Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For Pensions Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_investment_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data,
                                                              post_asset_payment_data, post_asset_commission_data):
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


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id , None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investments Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_investments_payments', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For Investments Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_investments_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For Investments Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For Investments Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_savingsplan_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data,
                                                              post_asset_payment_data, post_asset_commission_data):
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
    logger.info("Policy Details For Savings Plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_savings_plans_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For Savings Plan Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_savings_plans_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For Savings Plan Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For Savings Plan Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_income_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data,
                                                              post_asset_payment_data, post_asset_commission_data):
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
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_income_protection_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For Income Protection Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_income_protection_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For Income Protection Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For Income Protection Test Passed!")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/"
                                                         "test_data_asset_payment_commission.csv"))
def test_add_all_data_to_policies_general_payment_commission(post_partner_data,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data,
                                                              post_asset_payment_data, post_asset_commission_data):
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
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None, 'policies_general_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Asset Payment Details For General Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    post_asset_payment = post_asset_commission_data(customer_id, policy_id, payment_id, values,
                                                    'policies_general_payments_commission', False)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, expected_message)
    logger.info("Policy Payment Commission Details For General Added Successfully")

    logger.info("Add Data To Policy Payment Commission Details For General Test Passed!")
