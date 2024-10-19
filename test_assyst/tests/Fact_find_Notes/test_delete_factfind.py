import pytest
import logging

from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_one_factnote_data_with_one_note_(delete_client_details,post_client_fact_note_data,data, create_client,get_fact_find_notes_data_with_customer_id,post_fact_findnotes_outgoing_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    logger.info(create_client_response)
    customer_id = create_client_response['data']['customer_id']
    create_notes = post_client_fact_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message( post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")

    get_client_data = get_fact_find_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Fact find Notes Details Fetched Successfully")
    note_id = post_factnotes_response['data']['notes']['note_id']

  #for deleting file

    delete_client_data = delete_client_details('factfindnotesfile', note_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_factfind_file_success_message)
    logger.info("Associated file Details Deleted Successfully")

  #for deleting note

    delete_client_data = delete_client_details('factfindnotes', note_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_factfind_success_message)
    logger.info("Note Details Deleted Successfully")

    get_client_data = get_fact_find_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.invalid_note_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fact find Notes Details Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_one_factnote_data_with_one_note_(delete_client_details,post_client_fact_note_data,data, create_client,get_fact_find_notes_data_with_customer_id,post_fact_findnotes_outgoing_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    logger.info(create_client_response)
    customer_id = create_client_response['data']['customer_id']
    create_notes = post_client_fact_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message( post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")
    note_id_1 = post_factnotes_response['data']['notes']['note_id']

    create_notes = post_client_fact_note_data(customer_id, None, True)
    post_factnotes_response = create_notes.json()
    logger.info(post_factnotes_response)
    common.check_reponse_message(post_factnotes_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")
    note_id_2 = post_factnotes_response['data']['notes']['note_id']

    get_client_data = get_fact_find_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Fact find Notes Details Fetched Successfully")

    # for deleting file

    delete_client_data = delete_client_details('factfindnotesfile', note_id_2)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_factfind_file_success_message)
    logger.info("Associated file Details for second note Deleted Successfully")

    # for deleting note

    delete_client_data = delete_client_details('factfindnotes', note_id_2)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_factfind_success_message)
    logger.info(" Second Note Details Deleted Successfully")

    get_client_data = get_fact_find_notes_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.customer_success_message)
    assert get_client_response["isError"] is False
    logger.info("Fact find Notes Details Fetched Successfully")

    note_after = get_client_response['data']

    # Assert that the note_id_2 is NOT present in the 'after' data
    assert note_id_2 not in [['note_id'] for data in
                                note_after], "Note ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that second note data has been deleted successfully.")
