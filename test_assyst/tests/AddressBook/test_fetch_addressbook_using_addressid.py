import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_addressbook_data(data, create_client, post_addressbook_data,
                                           get_addressbook_data_with_address_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)

    customer_id = create_client_response['data']['customer_id']
    post_address = post_addressbook_data(customer_id, None, 'address_book', True)
    post_address_response = post_address.json()
    common.check_reponse_message(post_address_response, constants.add_address_success_message)
    logger.info("Address Book Details Added Successfully")
    logger.info(post_address_response)

    address_id = post_address_response['data']['address_book']['address_id']
    get_addressbook_details = get_addressbook_data_with_address_id(customer_id, address_id)
    get_addressbook_response = get_addressbook_details.json()
    common.check_reponse_message(get_addressbook_response, constants.get_address_success_message)

    assert get_addressbook_response["isError"] is False
    logger.info("Address Book Details Fetched Successfully")
    logger.info(get_addressbook_response)
    logger.info("Fetch AddressBook Data Of One Customer Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_addressbook_data_with_invalid_id(data, create_client, get_addressbook_data_with_address_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    get_addressbook_data = get_addressbook_data_with_address_id('d37fcd87-1881-4798-af93-802fea5027b9',customer_id)
    get_addressbook_response = get_addressbook_data.json()
    common.check_reponse_message(get_addressbook_response, constants.addressbook_invalid_message)
    assert get_addressbook_response["isError"] is False
    logger.info("Fetch AddressBook Data With Invalid Customer ID Test Passed!")