import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


def test_fetch_all_expense_category_data(get_expense_category_details):

    get_expense_category_details_data = get_expense_category_details()
    get_expense_category_details_response = get_expense_category_details_data.json()
    common.check_reponse_message(get_expense_category_details_response, constants.get_expense_category_success_message)
    logger.info(get_expense_category_details_response)
    logger.info("All Expense Category Details Fetched Successfully")