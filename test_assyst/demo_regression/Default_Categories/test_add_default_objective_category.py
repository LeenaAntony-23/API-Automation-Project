import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_default_objective_category(customer_id,data, data_sys, create_client, post_system_manager_data,
                                     post_default_objective_category):


    post_objective_category = post_system_manager_data(data_sys, 'objectives_detail', True)
    post_objective_category_response = post_objective_category.json()
    common.check_reponse_message(post_objective_category_response, constants.get_objective_sucess_message)
    logger.info("Objective Category Details Added Successfully")

    objective_category_id = post_objective_category_response['data']['id']

    post_default_objective = post_default_objective_category(customer_id, objective_category_id)
    post_default_objective_response = post_default_objective.json()
    logger.info(post_default_objective_response)
    common.check_reponse_message(post_default_objective_response, constants.add_default_objective_category)
    logger.info("Default Objective Category Details Added Successfully")

    logger.info("Default Objective Category Test Passed!")