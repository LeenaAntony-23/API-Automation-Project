import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_policy_schedule(post_partner_data,dataa,post_policy_schedule,post_asset_listing,post_fund_data,post_system_manager_data,create_client, post_asset_data, data, post_client_data,post_policy_data):
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
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_life_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy pensions Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_pensions_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy investments Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_investments_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy savings_plans Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_savings_plans_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")


    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy income_protection Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_income_protection_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy health_assurance Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_health_assurance_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy general Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    policy_id = post_policy_response['data']['policy_id']
    if policyholder == 0:
        customer_id = customer_id
    else:
        customer_id = partner_cust_id
    post_policy_fund = post_fund_data(customer_id, policy_id, None, 'policies_general_funds', True)
    post_policy_fund_response = post_policy_fund.json()
    # logger.info(post_policy_withdrawal_response)
    common.check_reponse_message(post_policy_fund_response, constants.add_asset_fund_success_message)
    logger.info("Fund Details  Added Successfully")

    post_policy_schedule
    post_policy_schedule_info = post_policy_schedule(customer_id,policyholder,partner_cust_id)
    logger.info(post_policy_schedule_info)
    logger.info("All Details Fetched Successfully")

# @pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
# def test_add_policy_schedule_multitenanttesting(dataa,post_policy_schedule,post_system_manager_data,post_policy_data):
#     customer_id = "19a3b122-3f00-4236-b2fe-90a47b9b6c33"
#
#
#
#     post_asset_listing_info = post_policy_schedule(customer_id)
#     logger.info(post_asset_listing_info)
#     logger.info("All Details Fetched Successfully")
