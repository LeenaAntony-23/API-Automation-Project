import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contact.csv"))
def test_post_email(data, create_client, post_email_data,field_values,patch_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    #logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']


    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    # data.popitem()
    patch_client_data = patch_client_data(customer_id, data, 'contact', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)




    data= common.read_json("./jsons/create_new_email_post.json")
    post_mail = post_email_data(customer_id,data, True)
    post_mail_response = post_mail.json()
    common.check_reponse_message(post_mail_response, constants.add_mail_success_message)
    logger.info(post_mail_response)
    logger.info("Utility email test passed")

