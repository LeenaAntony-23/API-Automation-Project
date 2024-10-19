import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_one_folder(data, create_client,post_folder_data ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']


    post_folder = post_folder_data(customer_id, None, True)
    post_folder_response = post_folder.json()
    assert post_folder_response['message'] == "folder created sucessfully", f"API call failed with message: {post_folder_response['message']}"
    logger.info("Folder Details Added Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_one_folder_invalid_url(data, create_client,post_folder_data_invalid_url ):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']


    post_folder = post_folder_data_invalid_url(customer_id, None, True)
    post_folder_response = post_folder.json()
    logger.info("invalid url")

