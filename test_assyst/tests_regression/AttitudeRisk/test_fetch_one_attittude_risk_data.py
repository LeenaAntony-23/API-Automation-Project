import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_and_fetch_attituderisk_data(data, create_client, post_attituderisk_data, get_attituderisk_data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    post_attitude_risk = post_attituderisk_data(customer_id, 'attituderisk', None, None, None)
    post_attitude_risk_response = post_attitude_risk.json()
    common.check_reponse_message(post_attitude_risk_response, constants.add_attitude_to_risk_success_message)
    logger.info("Attitude Risk Details Added Successfully")

    get_attituderisk_details = get_attituderisk_data(customer_id)
    get_attituderisk_response = get_attituderisk_details.json()
    common.check_reponse_message(get_attituderisk_response, constants.get_attitude_to_risk_success_message)
    assert get_attituderisk_response["isError"] is False
    logger.info("Attitude Risk Details Fetched Successfully")

    logger.info("Fetch Attitude To Risk Data Of One Customer Test Passed!")


def test_fetch_attituderisk_with_invalid_customer_id(get_attituderisk_data):
    get_client_data = get_attituderisk_data('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0')
    get_client_response = get_client_data.json()
    common.check_reponse_message(get_client_response, constants.invalid_customer_id_message)
    assert get_client_response["isError"] is False

    logger.info("Fetch Attitude To Risk Data With Invalid Customer ID Test Passed!")
