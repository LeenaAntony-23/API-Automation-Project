import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset_Payment/"
                                                         "test_data_payment_complaince.csv"))
def test_post_replacement_register(post_replacement_register_report,post_liability_data,patch_asset_payment_data,field_values,post_partner_data,post_asset_payment_data,post_asset_withdrawal_data,post_policy_payment_withdrawal,dataa,post_policy_schedule,post_asset_listing,post_fund_data,post_system_manager_data,create_client, post_asset_data, data, post_client_data,post_policy_data):
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

# policy payment compliance adding part


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy life_assurance Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_life_assurance_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Policies Life Assurance Added Successfully")


    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
                                                    'policies_life_assurance_payments_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Policies Life Assurance Updated Successfully")


#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_pensions_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy pensions Details Added Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_pensions_payment', True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies Pensions Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
#                                                     'policies_pensions_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies Pensions Updated Successfully")
#
#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_investments_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy investments Details Added Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_investments_payments', True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies Investment Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
#                                                     'policies_investments_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies Investment Updated Successfully")
#
#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_savings_plans_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy savings_plans Details Added Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#     #
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_savings_plans_payment', True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies Savings Plan Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
#                                                     'policies_savings_plans_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies Savings plan Updated Successfully")
#
#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_income_protection_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy income_protection Details A`dded Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#     #
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_income_protection_payment',
#                                                  True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies Income Protection Added Successfully")
#
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id,policy_id, payment_id, values,
#                                                     'policies_income_protection_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies Income Protection Updated Successfully")
#
#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_health_assurance_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy health_assurance Details Added Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#     #
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_health_assurance_payment',
#                                                  True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies Health Assurance Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
#                                                     'policies_health_assurance_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies Health Assurance Updated Successfully")
#
#     post_policy = post_policy_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                    'policies_general_policy', True)
#     post_policy_response = post_policy.json()
#     common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
#     logger.info("Policy general Details Added Successfully")
#     policyholder = post_policy_response['data']['policy_holder']
#     logger.info(policyholder)
#     #
#     policy_id = post_policy_response['data']['policy_id']
#     if policyholder == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, policy_id, None, 'policies_general_payment', True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Policies General Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, policy_id, payment_id, values,
#                                                     'policies_general_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Policies General Updated Successfully")
#
# #asset payment compliance adding part
#
    post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Investment Details Added Successfully")
    logger.info(post_asset_response)
    jointindicator = post_asset_response['data']['joint_indicator']
    logger.info(jointindicator)

    asset_id = post_asset_response['data']['asset_id']
    if jointindicator == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id

    post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_investment_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Asset Investment Added Successfully")
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    payment_id = post_asset_payment_response['data']['Payment_id']
    update_asset_payment = patch_asset_payment_data(customer_id, asset_id, payment_id, values,
                                                    'asset_investment_payment_complaince', False)
    update_asset_payment_response = update_asset_payment.json()
    common.check_reponse_message(update_asset_payment_response, expected_message)
    logger.info(update_asset_payment_response)
    logger.info("Payment Complaince Details For Asset Investment Updated Successfully")

#     post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                  'asset_share_holdings_asset', True)
#     post_asset_response = post_asset.json()
#     common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
#     logger.info("Asset share_holdings Details Added Successfully")
#     jointindicator = post_asset_response['data']['joint_indicator']
#
#     logger.info(jointindicator)
#
#     asset_id = post_asset_response['data']['asset_id']
#     if jointindicator == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#
#     post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_share_holdings_payment', True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Asset Shareholding Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, asset_id, payment_id, values,
#                                                     'asset_share_holdings_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Asset Share holdings Updated Successfully")
#
#     post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                  'asset_banks_building_societies_asset', True)
#     post_asset_response = post_asset.json()
#     common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
#     logger.info("Asset banks_building_societies Details Added Successfully")
#     jointindicator = post_asset_response['data']['joint_indicator']
#     logger.info(jointindicator)
#
#
#     asset_id = post_asset_response['data']['asset_id']
#     if jointindicator == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, asset_id, None, 'asset_banks_building_societies_payment',
#                                                  True)
#     post_asset_payment_response = post_asset_payment.json()
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Asset Bank building Added Successfully")
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, asset_id, payment_id, values,
#                                                     'asset_banks_building_societies_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Asset Bank buildings Updated Successfully")
#
#     #################### chk home prsnl having paymnt or not
# #adding liability payment and compliance
#
#     post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                          'liabilities_loan_hire_purchase_liability', True)
#     post_liability_response = post_liability.json()
#     common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
#     logger.info("Liability Details Added Successfully")
#     jointindicator = post_liability_response['data']['joint_indicator']
#     liability_id = post_liability_response['data']['liability_id']
#     logger.info(liability_id)
#
#     if jointindicator == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
#                                                  'liabilities_loan_hire_purchase_payments', True)
#     post_asset_payment_response = post_asset_payment.json()
#     logger.info(post_asset_payment_response)
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Liability Loan Hire purchase Added Successfully")
#
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, liability_id, payment_id, values,
#                                                     'liabilities_loan_hire_purchase_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Liabilities Loan hire purchase Updated Successfully")
#
#     post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                          'liabilities_credit_cards_liability', True)
#     post_liability_response = post_liability.json()
#     common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
#     logger.info("Liability Details Added Successfully")
#     jointindicator = post_liability_response['data']['joint_indicator']
#     liability_id = post_liability_response['data']['liability_id']
#     logger.info(jointindicator)
#
#     if jointindicator == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
#                                                  'liabilities_credit_cards_payments', True)
#     post_asset_payment_response = post_asset_payment.json()
#     logger.info(post_asset_payment_response)
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Liability Credit Card Added Successfully")
#
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, liability_id, payment_id, values,
#                                                     'liabilities_credit_cards_payments_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Liabilities Credit cards Updated Successfully")
#
#     post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
#                                          'liabilities_mortgages_liability', True)
#     post_liability_response = post_liability.json()
#     common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
#     logger.info("Liability Details Added Successfully")
#     jointindicator = post_liability_response['data']['joint_indicator']
#     liability_id = post_liability_response['data']['liability_id']
#     logger.info(jointindicator)
#
#     if jointindicator == 0:
#         customer_id = customer_id
#     else:
#         customer_id = partner_cust_id
#     post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
#                                                  'liabilities_mortgages_payment', True)
#     post_asset_payment_response = post_asset_payment.json()
#     logger.info(post_asset_payment_response)
#     common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
#     logger.info("Payment Details For Liability Mortgage Added Successfully")
#
#     values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#               for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = values.get(list(values)[-1])
#     values.popitem()
#     payment_id = post_asset_payment_response['data']['Payment_id']
#     update_asset_payment = patch_asset_payment_data(customer_id, liability_id, payment_id, values,
#                                                     'liabilities_mortgages_payment_complaince', False)
#     update_asset_payment_response = update_asset_payment.json()
#     common.check_reponse_message(update_asset_payment_response, expected_message)
#     logger.info(update_asset_payment_response)
#     logger.info("Payment Complaince Details For Liabilities Mortgages Updated Successfully")

    post_user_info = post_replacement_register_report(policyholder, jointindicator)

    logger.info(post_user_info)
    logger.info("All Details Fetched Successfully")