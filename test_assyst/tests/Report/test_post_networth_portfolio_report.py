import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_portfolio_summary(post_liability_data,post_partner_data,dataa,post_networth_portfolio,post_system_manager_data,create_client, post_asset_data, data, post_client_data,post_policy_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']
    # post provider
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
# post asset

    post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Investment Details Added Successfully")
    logger.info(post_asset_response)
    jointindicator = post_asset_response['data']['joint_indicator']
    logger.info(jointindicator)


    post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset share_holdings Details Added Successfully")
    jointindicator = post_asset_response['data']['joint_indicator']
    logger.info(jointindicator)
    # #
    post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset home_personal Details Added Successfully")
    jointindicator = post_asset_response['data']['joint_indicator']
    logger.info(jointindicator)

    post_asset = post_asset_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset banks_building_societies Details Added Successfully")
    jointindicator = post_asset_response['data']['joint_indicator']
    logger.info(jointindicator)
#post policy
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy life_assurance Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy pensions Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy investments Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy savings_plans Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_income_protection_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy income_protection Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)

    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy health_assurance Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)
#
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy general Details Added Successfully")
    policyholder = post_policy_response['data']['policy_holder']
    logger.info(policyholder)
#
# # post liability
    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    logger.info(jointindicator)

    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    logger.info(jointindicator)

    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    jointindicator = post_liability_response['data']['joint_indicator']
    logger.info(jointindicator)

    #get function
    post_user_info = post_networth_portfolio(customer_id,jointindicator,policyholder,partner_cust_id)

    logger.info(post_user_info)
    logger.info("All Details Fetched Successfully")

# @pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
# def test_fetch_portfolio_summary_multitenanttesting(dataa,post_networth_portfolio,post_system_manager_data, post_asset_data):
#
#     customer_id = "19a3b122-3f00-4236-b2fe-90a47b9b6c33"
#
#
#     post_user_info = post_networth_portfolio(customer_id)
#
#     logger.info(post_user_info)
#     logger.info("All Details Fetched Successfully")