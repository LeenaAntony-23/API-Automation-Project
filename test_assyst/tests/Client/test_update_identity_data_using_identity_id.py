import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Client/test_data_identity.csv"))
def test_add_all_data_to_identitytype(get_client_data_with_customer_id,data, field_values, create_client, post_client_data, patch_clientidentity_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    logger.info(create_client_response)

    customer_id = create_client_response['data']['customer_id']

    identity_data = common.read_json("./jsons/create_new_identity.json")
    client_identity = post_client_data(customer_id, identity_data, 'identity', True)
    client_identity_data = client_identity.json()
    logger.info(client_identity_data)
    common.check_reponse_message(client_identity_data, constants.add_identity_success_message)
    logger.info("Client Details For identity Added Successfully")

    customer_id = client_identity_data['data']['identity']['customer_id']
    identity_id = client_identity_data['data']['identity']['identity_id']

    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
     for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_identity_data = patch_clientidentity_data(customer_id, identity_id, values, 'identity', None)
    patch_identity_data_response = patch_identity_data.json()
    logger.info(patch_identity_data_response)
    common.check_reponse_message(patch_identity_data_response,expected_message)
    logger.info("Client Details For Identity Updated Successfully")
    logger.info("Update Identity Data To Client Test Passed!")

    get_client_data = get_client_data_with_customer_id(customer_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Client Details Fetched Successfully")