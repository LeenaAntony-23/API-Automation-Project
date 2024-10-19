import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("data_sys", ["./jsons/create_new_systemmanager.json"])
def test_add_default_expense_category(data, data_sys, create_client, post_system_manager_data,
                                     post_default_expense_category):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info(create_client_response)
    logger.info("Client Details Added Successfully")

    post_expense_category = post_system_manager_data(data_sys, 'expense_category', True)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, constants.get_expensecategory_sucess_message)
    logger.info("Expense Category Details Added Successfully")

    customer_id = create_client_response['data']['customer_id']
    expense_category_id = post_expense_category_response['data']['id']

    post_default_expense = post_default_expense_category(customer_id, expense_category_id)
    post_default_expense_response = post_default_expense.json()
    logger.info(post_default_expense_response)
    common.check_reponse_message(post_default_expense_response, constants.add_default_expense_category)
    logger.info("Default Expense Category Details Added Successfully")

    logger.info("Default Expense Category Test Passed!")