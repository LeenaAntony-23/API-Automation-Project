import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

#
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_search_client(data,get_search_client,create_client):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    # logger.info(create_client_response)
    first_name = create_client_response['data']['NameAndAddress']['first_name']
    last_name =  create_client_response['data']['NameAndAddress']['last_name']


    get_search_client = get_search_client(first_name,last_name)
    get_search_client = get_search_client.json()
    common.check_reponse_message(get_search_client, constants.get_search_success_message)
    assert get_search_client["isError"] is False
    logger.info(get_search_client)
    logger.info("Customer details fetch successfully")
    # created_by = get_search_client['data'][0]['NameAndAddress']['created_by']

    # logger.info(created_by)
def test_fetch_search_client2(get_search_client):
    first_name = "STRINGG"
    last_name = "STRINGG"
    get_search_client = get_search_client(first_name, last_name)
    get_search_client = get_search_client.json()
    common.check_reponse_message(get_search_client, constants.get_search_success_message)
    assert get_search_client["isError"] is False
    logger.info(get_search_client)
    logger.info("Customer details fetch successfully")


def test_fetch_search_client1(get_search_client):
    first_name = "STRINGG,"
    last_name = "STRINGG"
    get_search_client = get_search_client(first_name, last_name)
    get_search_client = get_search_client.json()
    common.check_reponse_message(get_search_client, constants.get_search_success_message)
    assert get_search_client["isError"] is False
    logger.info(get_search_client)
    logger.info("Customer details fetch successfully")


def test_fetch_search_invalid_client(get_search_client):
    first_name = "xyz"
    last_name = "klm"
    get_search_client = get_search_client(first_name, last_name)
    get_search_client = get_search_client.json()
    common.check_reponse_message(get_search_client, constants.get_search_fail_message)
    assert get_search_client["isError"] is False
    logger.info(get_search_client)
    logger.info("Customer not found")

# def test_fetch_search_client1(get_search_client):
#     first_name = ",STRINGG"
#     last_name = "STRINGG"
#     get_search_client = get_search_client(first_name, last_name)
#     get_search_client = get_search_client.json()
#     common.check_reponse_message(get_search_client, constants.get_search_success_message)
#     assert get_search_client["isError"] is False
#     logger.info(get_search_client)
#     logger.info("Customer details fetch successfully")