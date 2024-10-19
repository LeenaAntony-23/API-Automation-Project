import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_fetch_contact_history(post_partner_data,post_client_data,post_contact_history,post_policy_data,post_liability_data,create_client,data,dataa,post_system_manager_data,post_asset_data,post_business_data):
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

    # adding client action

    appointment_data = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, appointment_data, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("Client Details For Contact Client Action Added Successfully")
    # provider post

    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']
#asset investment action
    client_asset = post_asset_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")
#
# #liability mortgage and loan action
#
    create_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                           'liabilities_mortgages_liability', True)
    create_liability_response = create_liability.json()
    common.check_reponse_message(create_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Mortgages Added Successfully")

    liability_id = create_liability_response['data']['liability_id']
    post_liability_mortage = post_business_data(customer_id, liability_id, None, 'liabilities_mortgages_actions', True)
    post_liability_mortage_response = post_liability_mortage.json()
    common.check_reponse_message(post_liability_mortage_response, constants.add_business_success_message)
    logger.info("Action Details For Mortgages Added Successfully")

    create_liability = post_liability_data(customer_id,partner_cust_id, provider_correspondence_id, None,
                                           'liabilities_loan_hire_purchase_liability', True)
    create_liability_response = create_liability.json()
    common.check_reponse_message(create_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details For Loan Hire Added Successfully")

    liability_id = create_liability_response['data']['liability_id']
    post_liability_loan_hire = post_business_data(customer_id,liability_id, None,
                                                  'liabilities_loan_hire_purchase_actions', True)
    post_liability_loan_hire_response = post_liability_loan_hire.json()
    common.check_reponse_message(post_liability_loan_hire_response, constants.add_business_success_message)
    logger.info("Action Details For Loan Hire Added Successfully")

#policy action

    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_life_assurance_policy',
                                     True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Life Assurance Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_life_assurance = post_business_data(customer_id, policy_id, None,
                                                    'policies_life_assurance_actions', True)
    post_policy_life_assurance_response = post_policy_life_assurance.json()
    common.check_reponse_message(post_policy_life_assurance_response, constants.add_business_success_message)
    logger.info("Action Details For Life Assurance Added Successfully")

    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_pensions_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Pensions Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_pensions = post_business_data(customer_id, policy_id, None, 'policies_pensions_actions', True)
    post_policy_pensions_response = post_policy_pensions.json()
    common.check_reponse_message(post_policy_pensions_response, constants.add_business_success_message)
    logger.info("Action Details For Pensions Added Successfully")

    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_investments_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Investment Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_pensions = post_business_data(customer_id, policy_id, None, 'policies_investments_actions', True)
    post_policy_pensions_response = post_policy_pensions.json()
    common.check_reponse_message(post_policy_pensions_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")

    create_policy = post_policy_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'policies_general_policy', True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For General Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_general = post_business_data(customer_id, policy_id, None, 'policies_general_actions', True)
    post_policy_general_response = post_policy_general.json()
    common.check_reponse_message(post_policy_general_response, constants.add_business_success_message)
    logger.info("Action Details For General Added Successfully")

    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_savings_plans_policy',
                                     True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Savings Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_general = post_business_data(customer_id, policy_id, None, 'policies_savings_plans_actions', True)
    post_policy_general_response = post_policy_general.json()
    common.check_reponse_message(post_policy_general_response, constants.add_business_success_message)
    logger.info("Action Details For Savings Added Successfully")

    create_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_income_protection_policy',
                                     True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Income Protection Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_general = post_business_data(customer_id, policy_id, None, 'policies_income_protection_actions', True)
    post_policy_general_response = post_policy_general.json()
    common.check_reponse_message(post_policy_general_response, constants.add_business_success_message)
    logger.info("Action Details For Income Protection Added Successfully")
    create_policy = post_policy_data(customer_id, partner_cust_id,provider_correspondence_id, None, 'policies_health_assurance_policy',
                                     True)
    create_policy_response = create_policy.json()
    common.check_reponse_message(create_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details For Health Assurance Added Successfully")

    policy_id = create_policy_response['data']['policy_id']
    post_policy_general = post_business_data(customer_id, policy_id, None, 'policies_health_assurance_actions', True)
    post_policy_general_response = post_policy_general.json()
    common.check_reponse_message(post_policy_general_response, constants.add_business_success_message)
    logger.info("Action Details For Health Assurance Added Successfully")

    # post_contact_history
    post_asset_listing_info = post_contact_history()

    logger.info(post_asset_listing_info)
    logger.info("All Details Fetched Successfully")