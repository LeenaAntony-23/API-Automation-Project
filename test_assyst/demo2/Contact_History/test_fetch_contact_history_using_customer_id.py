import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_contact_history_data_with_valid_customer_id(customer_id,partner_cust_id,provider_correspondence_id,post_client_fact_note_data,post_system_manager_data,dataa,data, create_client, post_fact_findnotes_outgoing_data_with_customer_id,post_asset_data, post_business_data,post_client_data, get_contact_history_data_with_customer_id):

    create_notes = post_client_fact_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")


    client_asset = post_asset_data(customer_id,partner_cust_id,provider_correspondence_id, None, 'asset_investment_asset', True)
    post_asset_response = client_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")

    asset_id = post_asset_response['data']['asset_id']
    post_asset_investment = post_business_data(customer_id, asset_id, None, 'asset_investment_actions', True)
    post_asset_investment_response = post_asset_investment.json()
    common.check_reponse_message(post_asset_investment_response, constants.add_business_success_message)
    logger.info("Action Details For Investment Added Successfully")
    logger.info(post_asset_investment_response)
    logger.info("Add Data To Asset Investment Actions Test Passed!")


    contact_action = common.read_json("./jsons/create_client_contexts.json")
    client_contact_action = post_client_data(customer_id, contact_action, 'contacts_client_action', True)
    client_contact_action_data = client_contact_action.json()
    logger.info(client_contact_action_data)
    common.check_reponse_message(client_contact_action_data, constants.add_client_success_message)
    logger.info("Client Details For Contact Client Action Added Successfully")

    client_history_details = get_contact_history_data_with_customer_id(customer_id)
    client_history_response = client_history_details.json()
    common.check_reponse_message(client_history_response, constants.get_client_note_success_message)
    logger.info("Contact history details fetched successfully")
    logger.info(client_history_response)

    logger.info("Fetch Contact History Details Of One Customer Test Passed!")


def test_fetch_fetch_contact_data_with_invalid_customer_id(get_contact_history_data_with_customer_id):
    get_client_data = get_contact_history_data_with_customer_id('5f6e7568-f2e2-4fbf-a3d2-a2c246544a08')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_Contact_message)

    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")
