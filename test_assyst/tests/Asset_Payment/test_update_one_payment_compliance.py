import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_asset_investment_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_asset_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    # Create Payment for the asset investment
    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'asset_investment_payment_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Asset Investment Updated Successfully")

    logger.info("Update Payment Complaince Details For Asset Investment Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_asset_share_holdings_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_asset_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    # Create Payment for the asset investment
    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Share holdings Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'asset_share_holdings_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Asset Share holdings Updated Successfully")

    logger.info("Update Payment Complaince Details For Asset Share holdings Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_asset_banks_building_societies_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_asset_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    # Create Payment for the asset investment
    case_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Bank buildings Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'asset_banks_building_societies_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Asset Bank buildings Updated Successfully")

    logger.info("Update Payment Complaince Details For Asset Bank buildings Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_liabilities_mortgages_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the mortgage liability
    case_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'liabilities_mortgages_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Mortgages Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'liabilities_mortgages_payment_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Liabilities Mortgages Updated Successfully")

    logger.info("Update Payment Complaince Details For Liabilities Mortgages Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_liabilities_loan_hire_purchase_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the mortgage liability
    case_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Loan hire purchase Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'liabilities_loan_hire_purchase_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Liabilities Loan hire purchase Updated Successfully")

    logger.info("Update Payment Complaince Details For Liabilities Loan hire purchase Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_Credit_cards_payment_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_liability_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the mortgage liability
    case_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'liabilities_credit_cards_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Credit cards Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'liabilities_credit_cards_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Liabilities Credit cards Updated Successfully")

    logger.info("Update Payment Complaince Details For Liabilities Credit cards Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_life_assurance_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_life_assurance_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_life_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Life Assurance Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_life_assurance_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Life Assurance Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Life Assurance Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_pensions_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_pensions_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_pensions_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Pensions Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_pensions_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Pensions Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Pensions Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_investments_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_investments_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_investments_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Investment Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_investments_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Investment Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Investment Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_savings_plans_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_savings_plans_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_savings_plans_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Savings plan Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_savings_plans_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Savings plan Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Savings plan Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_income_protection_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_income_protection_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_income_protection_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Income Protection Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_income_protection_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Income Protection Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Income Protection Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_health_assurance_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_health_assurance_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_health_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Health Assurance Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,case_id, payment_id, values,
                                                    'policies_health_assurance_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Health Assurance Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies Health Assurance Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_update_policies_general_payments_complaince(post_partner_data,get_payment_data_with_case_id,post_system_manager_data,dataa,data, field_values, create_client, post_policy_data,
                                                    post_asset_payment_data, patch_asset_payment_data):
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

    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    case_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, case_id, None, 'policies_general_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies General Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id, case_id, payment_id, values,
                                                    'policies_general_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies General Updated Successfully")

    logger.info("Update Payment Complaince Details For Policies General Test Passed!")
    get_payment_data = get_payment_data_with_case_id(case_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")
