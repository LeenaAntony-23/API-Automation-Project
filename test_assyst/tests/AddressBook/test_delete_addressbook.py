import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

# @pytest.mark.parametrize("data",["./jsons/create_client.json"])
# @pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/AddressBook/test_data_addressbook.csv"))
# def test_delete_all_data_to_addressbook_multiple_records(delete_client_details,get_addressbook_data_with_customer_id,field_values,data,create_client,post_addressbook_data,get_income_data_with_customer_id):
#     # Create client
#     create_client = create_client(data, None, True)
#     create_client_response = create_client.json()
#     logger.info(create_client_response)
#     common.check_reponse_message(create_client_response, constants.add_client_success_message)
#     logger.info("Client Details Added Successfully")
#     customer_id = create_client_response['data']['customer_id']
#
#     post_address = post_addressbook_data(customer_id, None, 'address_book', True)
#     post_address_response = post_address.json()
#     logger.info(post_address_response)
#     common.check_reponse_message(post_address_response, constants.add_address_success_message)
#     logger.info("Address Book Details Added Successfully")
#     address_id_1 = post_address_response['data']['address_book']['address_id']
#
#     data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
#             for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
#     expected_message = data.get(list(data)[-2])
#     data.popitem()
#     data.popitem()
#     post_addressbook = post_addressbook_data(customer_id, data, 'address_book', False)
#     post_addressbook_response = post_addressbook.json()
#     logger.info(post_addressbook_response)
#     common.check_reponse_message(post_addressbook_response, expected_message)
#     logger.info("AddressBook Details Added Successfully")
#     address_id_2 = post_address_response['data']['address_book']['address_id']
#
#     get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
#     get_addressbook_response = get_addressbook_details.json()
#     common.check_reponse_message(get_addressbook_response, constants.get_addressbook_customer_id_success_message)
#     assert get_addressbook_response["isError"] is False
#     logger.info(get_addressbook_response)
#     logger.info("Address Book Details Fetched Successfully")
#
#
#
#     delete_client_data = delete_client_details('addressbook',address_id_2 )
#     delete_client_response = delete_client_data.json()
#     logger.info(delete_client_response)
#     common.check_reponse_message(delete_client_response, constants.delete_address_success_message)
#     logger.info(" Second Address Details Deleted Successfully")
#
#     get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
#     get_addressbook_response = get_addressbook_details.json()
#     common.check_reponse_message(get_addressbook_response, constants.get_addressbook_customer_id_success_message)
#     assert get_addressbook_response["isError"] is False
#     logger.info(get_addressbook_response)
#     logger.info("Address Book Details Fetched Successfully")
#     address_after = get_addressbook_response['data']
#
#     assert address_id_2 not in [data['address_id'] for data in
#                                 address_after], "second address ID should be deleted from the response"
#
#     logger.info(" Second Addressbook data is deleted successfully")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/AddressBook/test_data_addressbook.csv"))
def test_delete_all_data_to_addressbook_single_records(delete_client_details,get_addressbook_data_with_customer_id,field_values,data,create_client,post_addressbook_data,get_income_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    post_address = post_addressbook_data(customer_id, None, 'address_book', True)
    post_address_response = post_address.json()
    logger.info(post_address_response)
    common.check_reponse_message(post_address_response, constants.add_address_success_message)
    logger.info("Address Book Details Added Successfully")
    address_id_1 = post_address_response['data']['address_book']['address_id']

    get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
    get_addressbook_response = get_addressbook_details.json()
    common.check_reponse_message(get_addressbook_response, constants.get_addressbook_customer_id_success_message)
    assert get_addressbook_response["isError"] is False
    logger.info(get_addressbook_response)
    logger.info("Address Book Details Fetched Successfully")

    delete_client_data = delete_client_details('addressbook', address_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_address_success_message)
    logger.info("  Address Details Deleted Successfully")

    get_addressbook_details = get_addressbook_data_with_customer_id(customer_id)
    get_addressbook_response = get_addressbook_details.json()
    common.check_reponse_message(get_addressbook_response, constants.get_addressbook_not_found)
    assert get_addressbook_response["isError"] is False
    logger.info(get_addressbook_response)
    logger.info("No Address details fetched")