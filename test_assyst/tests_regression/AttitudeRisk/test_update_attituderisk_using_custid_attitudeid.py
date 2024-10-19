import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/AttitudeRisk/test_data_attitude_risk.csv"))
def test_update_attituderisk_data(get_attituderisk_data,data,field_values, create_client, post_client_data, patch_attitude_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    employment_data = common.read_json("./jsons/create_new_attituderisk.json")

    client_att = post_client_data(customer_id, employment_data, 'attitude_to_risk', True)
    client_att_data = client_att.json()
    logger.info(client_att_data)
    common.check_reponse_message(client_att_data, constants.add_client_success_message)
    logger.info("Client Attitude to risk Added Successfully")

    attitude_id = client_att_data['attitude_to_risk']['attituderisk_id']

    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    patch_attitude = patch_attitude_data(customer_id, attitude_id, data, 'attitude_to_risk',False)
    patch_attitude_response = patch_attitude.json()
    common.check_reponse_message(patch_attitude_response, expected_message)
    logger.info("Attitude to risk Details Updated Successfully")
    logger.info(patch_attitude_response)
    logger.info("Update Data To Attitude risk Test Passed!")
    get_attituderisk_details = get_attituderisk_data(customer_id)
    get_attituderisk_response = get_attituderisk_details.json()
    logger.info(get_attituderisk_response)
    common.check_reponse_message(get_attituderisk_response, constants.get_attitude_to_risk_success_message)
    assert get_attituderisk_response["isError"] is False
    logger.info("Attitude Risk Details Fetched Successfully")