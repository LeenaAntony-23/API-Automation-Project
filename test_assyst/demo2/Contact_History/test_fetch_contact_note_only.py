import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_note_client_history_using_valid_customerid(customer_id,data, create_client, post_client_note_data, get_note_client_history_with_customer_id):

    create_notes = post_client_note_data(customer_id, None, True)
    post_note_response = create_notes.json()
    logger.info(post_note_response)
    common.check_reponse_message(post_note_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    notes_id = post_note_response['data']['notes']['note_id']
    logger.info(notes_id)
    get_note_data = get_note_client_history_with_customer_id(customer_id)
    get_note_response = get_note_data.json()
    logger.info(get_note_response)
    common.check_reponse_message(get_note_response, constants.get_client_note_success_message)
    logger.info("Fetch Contact Note Client History Data With Valid Case ID Test Passed!")



def test_fetch_fetch_note_data_with_invalid_customer_id(get_note_client_history_with_customer_id):
    get_client_data = get_note_client_history_with_customer_id('5f6e7568-f2e2-4fbf-a3d2-a2c246544a08')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_contact_note_message )

    assert get_client_response["isError"] is True
    logger.info("Fetch Customer Data With Invalid Customer ID Test Passed!")

