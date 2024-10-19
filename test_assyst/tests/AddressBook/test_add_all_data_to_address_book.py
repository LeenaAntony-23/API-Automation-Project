import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/AddressBook/test_data_addressbook.csv"))
def test_add_all_data_to_addressbook(data, field_values, create_client, post_addressbook_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
           for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_addressbook = post_addressbook_data(customer_id, data, 'address_book', False)
    post_addressbook_response = post_addressbook.json()
    common.check_reponse_message(post_addressbook_response, expected_message)
    logger.info("AddressBook Details Added Successfully")
    logger.info(post_addressbook_response)
    logger.info("Add Data To Address Book Test Passed!")

