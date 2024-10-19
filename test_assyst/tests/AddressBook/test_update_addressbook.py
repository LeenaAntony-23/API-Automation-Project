import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/AddressBook/test_data_addressbook.csv"))
def test_update_addressbook_data(get_addressbook_data_with_customer_id,data,  field_values, create_client, post_addressbook_data, patch_addressbook_data):

    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']

    post_address = post_addressbook_data(customer_id, data, 'address_book', True)
    post_address_response = post_address.json()
    common.check_reponse_message(post_address_response,constants.add_address_success_message )
    logger.info(post_address_response)
    logger.info("Address Book Details Added Successfully")

    address_id = post_address_response['data']['address_book']['address_id']
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_address = patch_addressbook_data(customer_id, address_id, data, 'address_book', False)
    patch_address_response = patch_address.json()
    common.check_reponse_message(patch_address_response, expected_message)
    logger.info("Addressbook Details Updated Successfully")
    logger.info(patch_address_response)
    logger.info("Update Data To Addressbook Test Passed!")

    get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
    get_addressbook_response = get_addressbook_details.json()
    common.check_reponse_message(get_addressbook_response, constants.get_addressbook_customer_id_success_message)
    assert get_addressbook_response["isError"] is False
    logger.info("Address Book Details Fetched Successfully")
