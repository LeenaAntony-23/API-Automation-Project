import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_contact.csv"))
def test_post_email(data, create_client, post_email_data,field_values,patch_client_data,get_email_using_templateid_custid):
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
    template_id = "161c469a-cac3-4802-9d9b-e3d767cdb7ea"
    get_email = get_email_using_templateid_custid(template_id, customer_id)
    get_income_response = get_email.json()


    logger.info(get_income_response)
    logger.info("Template Details Fetched Successfully")