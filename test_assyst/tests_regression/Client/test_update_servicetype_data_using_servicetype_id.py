import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
def test_add_all_data_to_servicetype(get_client_data_with_customer_id,data, field_values, create_client, post_client_data, patch_clientservicetype_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)

    customer_id = create_client_response['data']['customer_id']

    servicetype_data = common.read_json("./jsons/create_new_servicetype.json")
    client_servicetype = post_client_data(customer_id, servicetype_data, 'service_type', True)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.add_servicetype_success_message)
    logger.info("Client Details For Service Type Added Successfully")

    customer_id = client_servicetype_data['data']['servicetype']['customer_id']
    servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
     for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_client_data = patch_clientservicetype_data(customer_id, servicetype_id, values, 'service_type', None)
    patch_client_data_response = patch_client_data.json()
    logger.info(expected_message)
    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response,expected_message)
    logger.info("Client Details For Service Type Updated Successfully")
    logger.info("Update Service Type Data To Client Test Passed!")

    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")
