import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_asset_investment_commission(post_partner_data,get_asset_commission_data_with_commission_id,data, field_values,post_system_manager_data,dataa, create_client,post_asset_data,post_asset_payment_data,
    post_asset_commission_data,patch_payment_commission_data):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    #logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    #logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    post_asset_commission = post_asset_commission_data(customer_id, asset_id, payment_id,None,'asset_investment_payment_commission', True)
    post_asset_commission_response = post_asset_commission.json()
    logger.info(post_asset_commission_response)
    common.check_reponse_message(post_asset_commission_response,constants.add_asset_commission_success_message )
    logger.info("Asset Payment Commission Details For Investment Added Successfully")

    commission_id = post_asset_commission_response['data']['commission_id']
    logger.info(commission_id)
    logger.info(payment_id)
    logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id,asset_id ,payment_id, values,
                                                   'asset_investment_payment_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for asset Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_asset_share_holdings_investment(post_partner_data,get_asset_commission_data_with_commission_id,data, field_values,post_system_manager_data,dataa, create_client,post_asset_data,post_asset_payment_data, post_asset_commission_data,patch_payment_commission_data ):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']
    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = client_asset.json()
    #logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Share Holdings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    #logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Share Holdings Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    post_asset_commission = post_asset_commission_data(customer_id, asset_id, payment_id,None,'asset_share_holdings_commission', True)
    post_asset_commission_response = post_asset_commission.json()
    logger.info(post_asset_commission_response)
    common.check_reponse_message(post_asset_commission_response,constants.add_asset_commission_success_message )
    logger.info("Asset Payment Commission Details For Share Holdings Added Successfully")

    commission_id = post_asset_commission_response['data']['commission_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id,asset_id ,payment_id, values,'asset_share_holdings_commission', False)
    update_commission_data_response = update_commission_data.json()
    logger.info(update_commission_data_response)
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info("Commission Details for Asset Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_asset_banks_building_societies_commission(post_partner_data,get_asset_commission_data_with_commission_id,data, field_values, create_client, post_asset_data, post_asset_payment_data,
                                                dataa,post_asset_commission_data,post_system_manager_data, patch_payment_commission_data):
    # Create Client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    #
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = client_asset.json()
    #logger.info(post_asset_response)
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Bank Buildings Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Bank Buildings Added Successfully")

    payment_id = post_asset_payment_response['data']['Payment_id']
    post_asset_commission = post_asset_commission_data(customer_id, asset_id, payment_id, None,
                                                       'asset_banks_building_societies_payment_commission', True)
    post_asset_commission_response = post_asset_commission.json()
    logger.info(post_asset_commission_response)
    common.check_reponse_message(post_asset_commission_response, constants.add_asset_commission_success_message)
    logger.info("Asset Payment Commission Details For Bank Buildings Added Successfully")

    commission_id = post_asset_commission_response['data']['commission_id']
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, asset_id, payment_id, values,
                                                           'asset_banks_building_societies_payment_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Asset Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_liabilities_mortgages_payment_commission(post_partner_data,get_asset_commission_data_with_commission_id,data, post_system_manager_data,dataa, field_values, create_client,post_liability_data,post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
    #Create Client
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
    post_liability_commission = post_asset_commission_data(customer_id, liability_id, payment_id,None,'liabilities_mortgages_payment_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response,constants.add_asset_commission_success_message )
    logger.info("liability Payment Commission Details For Mortages Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id,liability_id ,payment_id, values,
                                                   'liabilities_mortgages_payment_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for liability Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_liabilities_loan_hire_purchase_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,data,dataa,post_system_manager_data, field_values, create_client,post_liability_data,post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_mortgage = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Loan Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, liability_id, payment_id,None,'liabilities_loan_hire_purchase_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response,constants.add_asset_commission_success_message )
    logger.info("liability Payment Commission Details For Loan Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id,liability_id ,payment_id, values,
                                                   'liabilities_loan_hire_purchase_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Loan liability Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_liabilities_credit_cards_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,data,post_system_manager_data,dataa, field_values, create_client,post_liability_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    post_mortgage = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_credit_cards_liability', True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")

    liability_id = post_mortgage_response['data']['liability_id']
    post_mortgage = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_credit_cards_payments',True)
    post_mortgage_response = post_mortgage.json()
    common.check_reponse_message(post_mortgage_response, constants.add_asset_payment_success_message)
    logger.info("Liability Payment Details For Loan Added Successfully")

    payment_id = post_mortgage_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, liability_id, payment_id, None,
                                                           'liabilities_credit_cards_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("liability Payment Commission Details For Credit card Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, liability_id, payment_id, values,
                                                           'liabilities_credit_cards_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Credit card liability Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_life_assurance_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
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
    logger.info("policy Payment Details For Life Assurance Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_life_assurance_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For life assurance Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_life_assurance_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for life assurance Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_pensions_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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


    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_pensions_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Pension Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_pensions_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For Pension Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_pensions_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Pension Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_investments_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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


    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_pensions_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Investment Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_investments_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For Investment Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_investments_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Investment Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_savings_plans_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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

    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings plan Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_savings_plans_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Savings plan Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_savings_plans_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For Savings plan Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_savings_plans_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Savings plan Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_income_protection_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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


    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income protection Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_income_protection_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For Income protection Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_income_protection_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For Income protection Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_income_protection_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for Income protection Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values",
                         common.read_csv("./test_data_regression/Commission/test_data_asset_payment_commission.csv"))
def test_update_policies_general_payments_commission(post_partner_data,get_asset_commission_data_with_commission_id,post_system_manager_data,dataa,data, field_values, create_client,post_policy_data, post_asset_payment_data,post_asset_commission_data,patch_payment_commission_data):
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


    #customer_id = "20f99fde-b5a1-4a2b-99c9-25f924f4da27"
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = post_policy_response['data']['policy_id']
    post_life_assurance = post_asset_payment_data(customer_id, policy_id, None,'policies_general_payment', True)
    post_life_assurance_response = post_life_assurance.json()
    common.check_reponse_message(post_life_assurance_response, constants.add_asset_payment_success_message)
    logger.info("Policy Payment Details For General protection Added Successfully")

    payment_id = post_life_assurance_response['data']['Payment_id']
    post_liability_commission = post_asset_commission_data(customer_id, policy_id, payment_id, None,
                                                           'policies_general_payments_commission', True)
    post_liability_commission_response = post_liability_commission.json()
    logger.info(post_liability_commission_response)
    common.check_reponse_message(post_liability_commission_response, constants.add_asset_commission_success_message)
    logger.info("Policy Payment Commission Details For General Added Successfully")

    commission_id = post_liability_commission_response['data']['commission_id']
    # logger.info(commission_id)
    # logger.info(payment_id)
    # logger.info(asset_id)
    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
    field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    update_commission_data = patch_payment_commission_data(customer_id, commission_id, policy_id, payment_id, values,
                                                           'policies_general_payments_commission', False)
    update_commission_data_response = update_commission_data.json()
    common.check_reponse_message(update_commission_data_response, expected_message)
    logger.info(update_commission_data_response)
    logger.info("Commission Details for General Policy Updated Successfully")

    logger.info("Update Commission Test Passed!")
    get_commission_data = get_asset_commission_data_with_commission_id(customer_id, commission_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_commission_customer_id_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details For Asset Investment Fetched Successfully")


