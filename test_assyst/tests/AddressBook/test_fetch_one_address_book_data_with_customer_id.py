import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_addressbook_data(data, create_client, post_addressbook_data,
                                           get_addressbook_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_address = post_addressbook_data(customer_id, None, 'address_book', True)
    post_address_response = post_address.json()
    common.check_reponse_message(post_address_response, constants.add_address_success_message)
    logger.info("Address Book Details Added Successfully")

    get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
    get_addressbook_response = get_addressbook_details.json()
    common.check_reponse_message(get_addressbook_response, constants.get_addressbook_customer_id_success_message)
    assert get_addressbook_response["isError"] is False
    logger.info("Address Book Details Fetched Successfully")
    logger.info(get_addressbook_response)
    logger.info("Fetch AddressBook Data Of One Customer Test Passed!")


def test_fetch_addressbook_data_invalid_customer_id(get_addressbook_data_with_customer_id):
    get_addressbook_data = get_addressbook_data_with_customer_id('fd8c7057-3fe8-4424-9f84-bcc77ed92665')
    get_addressbook_response = get_addressbook_data.json()
    common.check_reponse_message(get_addressbook_response, constants.invalid_adress_customer_id_message)
    assert get_addressbook_response["isError"] is False

    logger.info("Fetch AddressBook Data With Invalid Customer ID Test Passed!")
