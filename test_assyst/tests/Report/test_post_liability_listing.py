import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liability_listing(post_asset_payment_data,post_partner_data,dataa,post_liability_listing,post_system_manager_data,create_client, data,post_liability_data):
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
    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']
    # post liability
    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    liability_id= post_liability_response['data']['liability_id']
    logger.info(liability_id)

    if jointindicator == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None, 'liabilities_loan_hire_purchase_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liability Loan Hire purchase Added Successfully")


    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    liability_id = post_liability_response['data']['liability_id']
    logger.info(jointindicator)

    if jointindicator == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
                                                 'liabilities_credit_cards_payments', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liability Credit Card Added Successfully")

    post_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    liability_id = post_liability_response['data']['liability_id']
    logger.info(jointindicator)

    if jointindicator == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_asset_payment = post_asset_payment_data(customer_id, liability_id, None,
                                                 'liabilities_mortgages_payment', True)
    post_asset_payment_response = post_asset_payment.json()
    logger.info(post_asset_payment_response)
    common.check_reponse_message(post_asset_payment_response, constants.add_asset_payment_success_message)
    logger.info("Payment Details For Liability Mortgage Added Successfully")

    #get function
    post_user_info = post_liability_listing(customer_id,jointindicator,partner_cust_id)

    logger.info(post_user_info)
    logger.info("All Details Fetched Successfully")
#
# @pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
# def test_fetch_liability_listing_multitenanttesting(dataa,post_liability_listing,post_system_manager_data,post_liability_data):
#
#     customer_id = "19a3b122-3f00-4236-b2fe-90a47b9b6c33"
#     # post provider
#
#
#     # get function
#     post_user_info = post_liability_listing(customer_id)
#
#     logger.info(post_user_info)
#     logger.info("No customer found, blank report")
