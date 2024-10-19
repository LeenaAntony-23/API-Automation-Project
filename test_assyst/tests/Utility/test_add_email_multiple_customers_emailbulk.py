import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("field_values_a, field_values_b", zip(
    common.read_csv("./test_data/Utility/test_data_name_and_address.csv"),
    common.read_csv("./test_data/Utility/test_data_contact.csv")
))
def test_add_customers_and_post_contacts(field_values_a, field_values_b, create_client, patch_client_data,post_email_data):
    # Step 1: Add customer based on field_values1 (name and address details)
    data1 = {field: field_values_a.get(field) for field in field_values_a.keys() if
             field_values_a.get(field) is not None and field_values_a.get(field) != ''}

    expected_message_name_address = data1.get(list(data1)[-2])  # Adjusted for expected message
    data1.popitem()  # Remove the last field (assuming it's not required for customer creation)
    data1.popitem()  # Remove the second last field (if necessary)

    client_name_address = create_client(data1, 'name_and_address', False)
    client_name_address_data = client_name_address.json()
    common.check_reponse_message(client_name_address_data, expected_message_name_address)
    logger.info("Client Details For Name And Address Added Successfully")
    logger.info(client_name_address_data)

    customer_id = client_name_address_data['data']['customer_id']

    # Step 2: Post contact details based on field_values2
    data2 = {field: field_values_b.get(field) for field in field_values_b.keys() if
             field_values_b.get(field) is not None and field_values_b.get(field) != ''}

    expected_message_contact = data2.get(list(data2)[-1])  # Assuming the expected message is the last field value
    data2.popitem()  # Remove the last field

    patch_client_data_response = patch_client_data(customer_id, data2, 'contact', None).json()
    logger.info(patch_client_data_response)

    # Step 3: Check the response message for the patch operation
    common.check_reponse_message(patch_client_data_response, expected_message_contact)
    logger.info(f"Contact details added for Customer ID: {customer_id}")

    data = common.read_json("./jsons/create_new_email_post.json")
    post_mail = post_email_data(customer_id, data, True)
    post_mail_response = post_mail.json()
    common.check_reponse_message(post_mail_response, constants.add_mail_success_message)
    logger.info(post_mail_response)
    logger.info("Utility email test passed")