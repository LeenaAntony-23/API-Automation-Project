import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_asset_investment_payment(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data, field_values,post_system_manager_data, dataa, create_client, post_asset_data,
                                                    post_asset_payment_data, patch_asset_payment_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create Payment for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,asset_id, payment_id, values,'asset_investment_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment  Details For Asset Investment Updated Successfully")

    logger.info("Update Payment  Details For Asset Investment Test Passed!")

    get_payment_data = get_payment_data_with_case_id(asset_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_asset_share_holdings_payment(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data, post_system_manager_data, dataa, field_values, create_client, post_asset_data,post_asset_payment_data, patch_asset_payment_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create Payment for the asset investment
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Share Holdings Added Successfully")

    # Create Complaince for the asset investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,asset_id, payment_id, values, 'asset_share_holdings_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Asset Share Holdings Updated Successfully")

    logger.info("Update Payment  Details For Asset Share Holdings Test Passed!")
    get_payment_data = get_payment_data_with_case_id(asset_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_asset_banks_building_societies(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data, field_values, create_client, post_asset_data,post_system_manager_data, dataa,
                                                          post_asset_payment_data, patch_asset_payment_data):


    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    # Create Payment for the asset banks and building
    asset_id = post_asset_response['data']['asset_id']
    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None,
                                                 'asset_banks_building_societies_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Banks Building Societies Added Successfully")

    # Create Complaince for the asset banks and building
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,asset_id, payment_id, values,
                                                    'asset_banks_building_societies_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Asset Banks Building Societies Updated Successfully")

    logger.info("Update Payment  Details For Asset Banks Building Societies Test Passed!")
    get_payment_data = get_payment_data_with_case_id(asset_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")
#

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_liability_mortgages_payment(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data, field_values,post_system_manager_data, dataa, create_client, post_liability_data,
                                                       post_asset_payment_data, patch_asset_payment_data):


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the mortgage liability
    liability_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_mortgages_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Mortgages Added Successfully")

    # Create Complaince for the mortgage liability
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,liability_id, payment_id, values,
                                                    'liabilities_mortgages_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    logger.info(update_asset_payment_response)
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment Details For Liabilities Mortgages Updated Successfully")

    logger.info("Update Payment Details For Liabilities Mortgages Test Passed!")
    get_payment_data = get_payment_data_with_case_id(liability_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_liability_loan_hire_purchase_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                                 post_asset_payment_data, patch_asset_payment_data):


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the loan hire purchase liability
    liability_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
                                                 'liabilities_loan_hire_purchase_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Loan Hire Purchase Added Successfully")

    # Create Complaince for the loan hire purchase liability
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,liability_id, payment_id, values,
                                                    'liabilities_loan_hire_purchase_payments', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Liabilities Loan Hire Purchase Updated Successfully")

    logger.info("Update Payment  Details For Liabilities Loan Hire Purchase Test Passed!")
    get_payment_data = get_payment_data_with_case_id(liability_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_liability_credit_cards_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_liability_data,
                                                           post_asset_payment_data, patch_asset_payment_data):


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    # Create Payment for the credit card liability
    liability_id = post_liability_response['data']['liability_id']
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_credit_cards_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liabilities Credit Card Added Successfully")

    # Create Complaince for the credit card liability
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,liability_id, payment_id, values,
                                                    'liabilities_credit_cards_payments', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment Complaince Details For Liabilities Credit Card Updated Successfully")

    logger.info("Update Payment Complaince Details For Liabilities Credit Card Test Passed!")
    get_payment_data = get_payment_data_with_case_id(liability_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_life_assurance_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                            post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the life assurance policy
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_life_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Life Assurance Added Successfully")

    # Create Complaince for the life assurance policy
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_life_assurance_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies Life Assurance Updated Successfully")

    logger.info("Update Payment Details For Policies Life Assurance Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_pensions_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                      post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the pensions policies
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_pensions_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Pensions Added Successfully")

    # Create Complaince for the pensions policies
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_pensions_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    logger.info(update_asset_payment_response)
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies Pensions Updated Successfully")
    logger.info("Update Payment  Details For Policies Pensions Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_investments_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                         post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the policies investment
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_investments_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Investment Added Successfully")

    # Create Complaince for the policies investment
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_investments_payments', False)
    update_asset_payment_response = update_asset_payment.json()
    logger.info(update_asset_payment_response)
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies Investment Updated Successfully")

    logger.info("Update Payment  Details For Policies Investment Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_savings_plans_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data,dataa, field_values, create_client, post_policy_data,
                                                           post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the savings plan policies
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_savings_plans_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Savings Plan Added Successfully")

    # Create Complaince for the savings plan policies
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_savings_plans_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies Savings Plan Updated Successfully")

    logger.info("Update Payment  Details For Policies Savings Plan Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_income_protection_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                               post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the income protection
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_income_protection_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Income Protection Added Successfully")

    # Create Complaince for the income protection
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_income_protection_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment Details For Policies Income Protection Updated Successfully")

    logger.info("Update Payment Details For Policies Income Protection Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_health_assurance(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                     post_asset_payment_data, patch_asset_payment_data):


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the health assurance policies
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_health_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Health Assurance Added Successfully")

    # Create Complaince for the health assurance policies
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_health_assurance_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies Health Assurance Updated Successfully")

    logger.info("Update Payment Details For Policies Health Assurance Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/test_data_asset_payment.csv"))
def test_update_policies_general_payments(customer_id,partner_cust_id,provider_correspondence_id,get_payment_data_with_case_id,data,post_system_manager_data, dataa, field_values, create_client, post_policy_data,
                                                     post_asset_payment_data, patch_asset_payment_data):

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")

    # Create Payment for the general policies
    policy_id = post_policy_response['data']['policy_id']
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_general_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies General Added Successfully")

    # Create Complaince for the general policies
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
                                                    'policies_general_payment', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info("Payment  Details For Policies General Updated Successfully")

    logger.info("Update Payment  Details For Policies General Test Passed!")
    get_payment_data = get_payment_data_with_case_id(policy_id, customer_id)
    get_payment_response = get_payment_data.json()
    logger.info(get_payment_response)
    common.check_reponse_message(get_payment_response, constants.get_asset_payment_success_message)
    logger.info("Fetch Asset Investment Payment Data With Valid Case ID Test Passed!")