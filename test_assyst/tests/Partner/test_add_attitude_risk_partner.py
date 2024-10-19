import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common


logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/AttitudeRisk/test_data_attitude_risk_partner.csv"))
def test_add_all_data_to_attitude_risk(data, field_values, create_client,post_partner_data, post_client_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")

    partner_cust_id = partner_data_response['data']['customer_id']
    logger.info(customer_id)
    logger.info(partner_cust_id)

    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_attitude_risk = post_client_data(partner_cust_id, data, 'attitude_to_risk', False)
    post_attitude_response = post_attitude_risk.json()
    common.check_reponse_message(post_attitude_response, expected_message)
    logger.info("Attitude Risk Details Added Successfully")
    logger.info(post_attitude_response)
    logger.info("Add Data To Attitude Risk Test Passed!")