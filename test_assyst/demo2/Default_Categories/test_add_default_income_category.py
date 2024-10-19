import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_default_income_category(customer_id,data, data_sys, create_client, post_system_manager_data,
                                     post_default_income_category):

    post_income_category = post_system_manager_data(data_sys, 'income_category', True)
    post_income_category_response = post_income_category.json()
    logger.info( post_income_category_response)
    common.check_reponse_message(post_income_category_response, constants.get_incomecategory_sucess_message)
    logger.info("Income Category Details Added Successfully")


    income_category_id = post_income_category_response['data']['id']
    logger.info(income_category_id)
    #
    post_default_income = post_default_income_category(customer_id, income_category_id)
    post_default_income_response = post_default_income.json()
    common.check_reponse_message(post_default_income_response, constants.add_default_income_category)
    logger.info("Default Income Category Details Added Successfully")

    logger.info("Default Income Category Test Passed!")