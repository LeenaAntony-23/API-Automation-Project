import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/AttitudeRisk/test_data_attitude_risk.csv"))
def test_add_all_data_to_attitude_risk(get_attituderisk_data,data, field_values, create_client, post_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_att = post_client_data(customer_id, values, 'attitude_to_risk', False)
    client_att_data = client_att.json()
    common.check_reponse_message(client_att_data, expected_message)
    logger.info("Client Details For Attitude Risk Added Successfully")

    logger.info("Add Data To Attitude Risk Test Passed!")
    get_attituderisk_details = get_attituderisk_data(customer_id)
    get_attituderisk_response = get_attituderisk_details.json()
    common.check_reponse_message(get_attituderisk_response, constants.get_attitude_to_risk_success_message)
    assert get_attituderisk_response["isError"] is False
    logger.info("Attitude Risk Details Fetched Successfully")