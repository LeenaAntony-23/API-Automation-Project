import pytest
import logging

from test_assyst.conftest import post_notes_data_with_customer_id
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_contact_note_data_with_valid_doc_id(customer_id,data, create_client, post_client_note_data,get_notes_data_with_doc_id):


    create_notes = post_client_note_data(customer_id, None, True)
    post_note_response = create_notes.json()
    logger.info(post_note_response)
    common.check_reponse_message(post_note_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    doc_id = post_note_response["data"]["notes"]["file_link"]
    get_notes_data = get_notes_data_with_doc_id(doc_id)
    get_client_response = get_notes_data.json()
    logger.info(get_client_response)

    #common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Contact Note Details Fetched Successfully")

