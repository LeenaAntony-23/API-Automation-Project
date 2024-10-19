import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_attitude_risk_with_valid_customer_id(get_attitude_with_partner_customer_id,data,post_client_data, create_client,post_partner_data, get_client_data_with_partner_customer_id):

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
    att_data = common.read_json("./jsons/create_new_attituderisk.json")
    post_attitude_risk = post_client_data(partner_cust_id, att_data, 'attitude_to_risk', True)
    post_attitude_response = post_attitude_risk.json()
    common.check_reponse_message(post_attitude_response, constants.add_partner_success_message)
    logger.info("Attitude Risk Details Added Successfully")
    logger.info(post_attitude_response)

    attitude_id = post_attitude_response['attitude_to_risk']['attituderisk_id']

    get_client_data = get_attitude_with_partner_customer_id(partner_cust_id)
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.get_client_success_message)
    logger.info("Attitude risk Details Fetched Successfully")
    logger.info(get_client_response)


def test_fetch_attitude_risk_data_with_invalid_customer_id(get_attitude_with_partner_customer_id):
    get_client_data = get_attitude_with_partner_customer_id('65386379-3d11-48bb-ae08-2932639910be')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_partner_customer_id_message)
    assert get_client_response["isError"] is False
    logger.info("Fetch Customer Data With Invalid Partner customer ID Test Passed!")
