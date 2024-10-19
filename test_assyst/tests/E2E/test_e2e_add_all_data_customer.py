import pytest
import logging
import json
from test_assyst import constants

logger = logging.getLogger('my_logger')
contexts = ['employment', 'identity', 'objectives', 'service_type', 'contact', 'nationality', 'personal',
            'health_note', 'administration', 'compliance', 'fact_find_notes', 'fees_charges', 'contacts_time_allocation',
            'contacts_notes', 'contacts_client_action']


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_all_data_to_client(data, create_client, post_client_data, patch_client_data,
                                get_client_data_with_customer_id, post_dependant_data, post_outgoing_data,
                                post_income_data, post_addressbook_data, post_attituderisk_data,
                                post_asset_data, post_liability_data, post_policy_data):

    json_file_path = "./jsons/create_client_e2e.json"
    with open(json_file_path, "r") as file:
        json_data = json.load(file)

    create_client = create_client(json_data, 'name_and_address', 'e2e')
    create_client_response = create_client.json()
    assert create_client_response["message"] == constants.add_client_success_message, \
        f"API call failed with message: {create_client_response['message']}"
    logger.info("Client Name And Address Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    for context in contexts:
        if context in ['employment', 'identity', 'objectives', 'service_type', 'fact_find_notes', 'fees_charges',
                       'contacts_time_allocation', 'contacts_notes', 'contacts_client_action']:
            client_create = post_client_data(customer_id, json_data, context, 'e2e')
            client_create_data = client_create.json()
            if context == 'fact_find_notes' or context == 'contacts_notes':
                assert client_create_data["message"] == constants.add_fact_find_success_message, \
                    f"API call failed with message: {client_create_data['message']}"
            elif context == 'fees_charges':
                assert client_create_data["message"] == constants.add_fees_charges_success_message, \
                    f"API call failed with message: {client_create_data['message']}"
            else:
                assert client_create_data["message"] == constants.add_client_success_message, \
                    f"API call failed with message: {client_create_data['message']}"
        elif context in ['contact', 'nationality', 'personal', 'health_note', 'administration', 'compliance']:
            client_create = patch_client_data(customer_id, json_data, context, 'e2e')
            client_create_data = client_create.json()
            logger.info(client_create_data)
            assert client_create_data["message"] == constants.patch_client_success_message, \
                f"API call failed with message: {client_create_data['message']}"
        logger.info("Client %s Added Successfully" % context)

#     # Add data to Attitude Risk
#     post_attitude_risk = post_attituderisk_data(customer_id, 'attituderisk', json_data, 'e2e', 'attitude_to_risk')
#     post_attitude_risk_response = post_attitude_risk.json()
#     assert post_attitude_risk_response["message"] == constants.add_attitude_to_risk_success_message, \
#         f"API call failed with message: {post_attitude_risk_response['message']}"
#     logger.info("Attitude Risk Details Added Successfully")
#
#     get_client_details = get_client_data_with_customer_id(customer_id)
#     logger.info("Client Details: %ss" % get_client_details.text)
#
#     # Add data to Dependant
#     post_dependant = post_dependant_data(customer_id, json_data, 'dependants', 'e2e')
#     post_dependant_response = post_dependant.json()
#     assert post_dependant_response["message"] == constants.dependant_add_success_message, \
#         f"API call failed with message: {post_dependant_response['message']}"
#     logger.info("Dependant Details Added Successfully")
#
#     # Add data to Income
#     post_income = post_income_data(customer_id, json_data, 'income', 'e2e')
#     post_income_response = post_income.json()
#     assert post_income_response["message"] == constants.add_income_success_message, \
#         f"API call failed with message: {post_income_response['message']}"
#     logger.info("Income Details Added Successfully")
#
#     # Add data to Outgoing
#     post_outgoing = post_outgoing_data(customer_id, json_data, 'outgoings', 'e2e')
#     post_outgoing_response = post_outgoing.json()
#     assert post_outgoing_response["message"] == constants.outgoing_add_success_message, \
#         f"API call failed with message: {post_outgoing_response['message']}"
#     logger.info("Outgoing Details Added Successfully")
#
#     # Add data to AddressBook
#     post_address = post_addressbook_data(customer_id, json_data, 'address_book', 'e2e')
#     post_address_response = post_address.json()
#     assert post_address_response["message"] == constants.add_address_success_message, \
#         f"API call failed with message: {post_address_response['message']}"
#     logger.info("AddressBook Details Added Successfully")
#
#     # Add data to Asset: Investment
#     client_asset = post_asset_data(customer_id, json_data, 'asset_investment_asset', 'e2e')
#     client_asset_data = client_asset.json()
#     assert client_asset_data["message"] == constants.add_asset_success_message, \
#         f"API call failed with message: {client_asset_data['message']}"
#     logger.info("Asset Details For Investemnt Added Successfully")
#
#     # Add data to Liability: Mortgages
#     post_liability = post_liability_data(customer_id, json_data, 'liabilities_mortgages_liability', 'e2e')
#     post_liability_response = post_liability.json()
#     assert post_liability_response["message"] == constants.add_liability_success_message, \
#         f"API call failed with message: {post_liability_response['message']}"
#     logger.info("Mortgage Details For Liability Test Passed!")
#
#     # Add data to Policy: Life Assurance
#     post_policy = post_policy_data(customer_id, json_data, 'policies_life_assurance_policy', 'e2e')
#     post_policy_response = post_policy.json()
#     assert post_policy_response["message"] == constants.add_policy_success_message, \
#         f"API call failed with message: {post_policy_response['message']}"
#     logger.info("Policy Details For Life Assurance Added Successfully")
#
#     logger.info("Client Details Added Successfully")
