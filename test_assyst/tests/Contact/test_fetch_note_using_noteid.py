import pytest
import logging
from test_assyst import constants

from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_note_data_with_note_id(data, create_client, post_client_note_data, get_fact_find_notes_data_with_notes_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    create_notes = post_client_note_data(customer_id, None, True)
    post_note_response = create_notes.json()
    # logger.info(post_note_response)
    common.check_reponse_message(post_note_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    notes_id = post_note_response['data']['notes']['note_id']
    get_note = get_fact_find_notes_data_with_notes_id(customer_id)
    get_note_response = get_note.json()
    logger.info(get_note_response)
    common.check_reponse_message(get_note_response, constants.get_fact_find_success_message)
    logger.info("Note Details Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_note_data_with_invalid_note_id(data, create_client, get_fact_find_notes_data_with_notes_id):

    get_client_data = get_fact_find_notes_data_with_notes_id('a65e1912-2260-437e-8448-63bd3a54b37d')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_note_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Note ID Test Passed!")