import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Client/test_data_fees_charges.csv"))
def test_update_commission_data(get_commission_data_with_customer_id,data, field_values, create_client, post_client_data,patch_commission_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    commission_data = common.read_json("./jsons/create_new_commission.json")
    client_commission = post_client_data(customer_id, commission_data, 'fees_charges', True)
    client_commission_data = client_commission.json()
    logger.info(client_commission_data)
    common.check_reponse_message(client_commission_data, constants.add_commission_success_message)
    logger.info("Client Details For Commission Added Successfully")

    commission_id = client_commission_data['data']['fees_charges']['commission_id']

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_commission_data = patch_commission_data(customer_id, commission_id, data, 'fees_charges', False)
    patch_commission_data_response = patch_commission_data.json()
    logger.info(patch_commission_data_response)
    common.check_reponse_message(patch_commission_data_response, expected_message)
    logger.info("Client Commission Updated Successfully")
    get_commission_data = get_commission_data_with_customer_id(customer_id)
    get_commission_response = get_commission_data.json()
    logger.info(get_commission_response)
    common.check_reponse_message(get_commission_response, constants.get_client_success_message)
    assert get_commission_response["isError"] is False
    logger.info("Commission Details Fetched Successfully")