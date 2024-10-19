import pytest
import logging

from test_assyst.conftest import post_notes_data_with_customer_id
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_one_note_data_with_valid_customer_id(customer_id,data, create_client, post_client_note_data,get_notes_data_with_customer_id):


    create_notes = post_client_note_data(customer_id, None, True)
    post_note_response = create_notes.json()
    logger.info(post_note_response)
    common.check_reponse_message(post_note_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    get_client_data = get_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)

    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Contact Note Details Fetched Successfully")



def test_fetch_one_customer_data_with_invalid_customer_id(get_notes_data_with_customer_id):
    get_client_data = get_notes_data_with_customer_id('0006f028-ea52-4eec-94d8-e995e1c80ffc')
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Notes Data With Invalid Customer ID Test Passed!")






