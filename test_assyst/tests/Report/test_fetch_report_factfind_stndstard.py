import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_identity.csv"))

def test_fetch_factfind_standard(post_system_manager_data,dataa,get_factfind_standard_report,field_values,post_policy_data,post_liability_data, create_client,post_asset_data,post_outgoing_data,post_income_data,data,post_partner_data,post_dependant_data,post_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)
#post partner
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']
#post dependant
    post_dependant = post_dependant_data(customer_id, None, 'dependants', True)
    post_dependant_response = post_dependant.json()
    common.check_reponse_message(post_dependant_response, constants.dependant_add_success_message)
    logger.info("Dependant Details Added Successfully")
#post employment
    employment_data = common.read_json("./jsons/create_client_employment.json")
    # logger.info(employment_data)
    # logger.info(customer_id)
    client_employment = post_client_data(customer_id, employment_data, 'employment', True)
    client_employment_data = client_employment.json()
    # logger.info(client_employment_data)
    common.check_reponse_message(client_employment_data, constants.add_client_success_message)
    logger.info("Client employment Added Successfully")
#post income
    post_income = post_income_data(customer_id, data, 'income', True)
    post_income_response = post_income.json()
    common.check_reponse_message(post_income_response, constants.add_income_success_message)
    # logger.info(post_income_response)
    # logger.info(data)
    logger.info("Income Details Added Successfully")
#post outgoing
    post_outgoing = post_outgoing_data(customer_id, None, 'outgoings', True)
    post_outgoing_response = post_outgoing.json()
    #logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully")
#     # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    #post asset
    post_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")
    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")
    post_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'asset_banks_building_societies_asset',
                                 True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details Added Successfully")

    #post policy
    post_policy = post_policy_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'policies_life_assurance_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_pensions_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_investments_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_savings_plans_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_income_protection_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_health_assurance_policy',
                                   True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
    post_policy = post_policy_data(customer_id,partner_cust_id, provider_correspondence_id, None, 'policies_general_policy', True)
    post_policy_response = post_policy.json()
    common.check_reponse_message(post_policy_response, constants.add_policy_success_message)
    logger.info("Policy Details Added Successfully")
#post liability
    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    post_liability = post_liability_data(customer_id, partner_cust_id,provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    post_liability = post_liability_data(customer_id, partner_cust_id,provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
#post identity
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_identity = post_client_data(customer_id, values, 'identity', False)
    client_identity_data = client_identity.json()
    common.check_reponse_message(client_identity_data, expected_message)
    logger.info("Client Details For Identity Added Successfully")


    get_user_info = get_factfind_standard_report(customer_id)

    logger.info(get_user_info)
    logger.info("All Details Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_fact_standard_invalid_context(get_fact_standard_invalid_context,data,create_client,post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

# post partner
    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()

    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    get_user_info = get_fact_standard_invalid_context(customer_id)
    get_user_details_response = get_user_info.json()
    logger.info("Invalid Context")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_fact_standard_invalid_custid(get_fact_standard_invalid_custid,data,create_client,post_partner_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # post partner
    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()

    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    get_user_info = get_fact_standard_invalid_custid()
    get_user_details_response = get_user_info.json()
    logger.info(get_user_details_response)
    logger.info("Invalid Customer Id")

def test_fetch_fact_standard_multitenant_custid(get_factfind_standard_report,post_partner_data):

    # post partner
    customer_id = "19a3b122-3f00-4236-b2fe-90a47b9b6c33"


    get_user_info = get_factfind_standard_report(customer_id)
    get_user_details_response = get_user_info.json()
    logger.info(get_user_details_response)
    logger.info("Invalid Customer Id")