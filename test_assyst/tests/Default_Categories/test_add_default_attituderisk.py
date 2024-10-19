import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_default_attituderisk(data, data_sys, create_client, post_system_manager_data,
                                     post_default_attituderisk):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    post_attituderisk_category = post_system_manager_data(data_sys, 'attitude_to_risk_category', True)
    post_attituderisk_category_response = post_attituderisk_category.json()
    common.check_reponse_message(post_attituderisk_category_response, constants.get_attitude_sucess_message)
    logger.info("Attitude Risk Category Details Added Successfully")

    post_attituderisk_rating_category = post_system_manager_data(data_sys, 'attitude_to_risk_rating', True)
    post_attituderisk_rating_category_response = post_attituderisk_rating_category.json()
    common.check_reponse_message(post_attituderisk_rating_category_response, constants.get_attitude_rating_sucess_message)
    logger.info("Attitude Risk Rating Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    category_id = post_attituderisk_category_response['data']['id']
    rating_id = post_attituderisk_rating_category_response['data']['id']

    post_default_attitude_risk = post_default_attituderisk(customer_id, category_id, rating_id)
    post_default_attitude_risk_response = post_default_attitude_risk.json()
    logger.info(post_default_attitude_risk_response)
    common.check_reponse_message(post_default_attitude_risk_response, constants.add_default_objective_category)
    logger.info("Default Attitude Risk Details Added Successfully")

    logger.info("Default Attitude Risk Test Passed!")