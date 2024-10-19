import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_get_folder_list(data, create_client,post_folder_data,get_folder_list_with_customer_id ,post_client_note_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']


    post_folder = post_folder_data(customer_id, None, True)
    post_folder_response = post_folder.json()
    assert post_folder_response['message'] == "folder created sucessfully", f"API call failed with message: {post_folder_response['message']}"
    logger.info("Folder Details Added Successfully")

#post notes

    create_notes = post_client_note_data(customer_id, None, True)
    post_note_response = create_notes.json()
    # logger.info(post_note_response)
    common.check_reponse_message(post_note_response, constants.add_fact_find_success_message)
    logger.info("Note Details Added Successfully")



    folder_list_details = get_folder_list_with_customer_id(customer_id)
    folder_list_details_response = folder_list_details.json()
    #assert folder_list_details_response['statusCode'] == 200, f"API call failed with StatusCode: {folder_list_details_response['statusCode']}"
    logger.info("Folder list Fetched Successfully")
    logger.info(folder_list_details_response)
