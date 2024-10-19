import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_default_client_action(customer_id,data, data_sys, create_client, post_system_manager_data,
                                     post_default_client_action_category):

    post_clientactn_category = post_system_manager_data(data_sys, 'tracking_client_actions', True)
    post_clientactn_category_response = post_clientactn_category.json()
    logger.info(post_clientactn_category_response)
    common.check_reponse_message(post_clientactn_category_response, constants.get_appointmentcategory_sucess_message)
    logger.info("Appointment  Category Details Added Successfully")


    tracking_id = post_clientactn_category_response['data']['id']

    post_default_client_action = post_default_client_action_category(customer_id,tracking_id)
    post_default_client_action_response = post_default_client_action.json()
    logger.info(post_default_client_action_response)
    common.check_reponse_message(post_default_client_action_response, constants.add_default_clientaction_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")
