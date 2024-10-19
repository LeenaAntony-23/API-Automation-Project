import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_fetch_actionlist_all_category_thisyear_date(user_id,get_search_client_userid,get_actionlist_with_user_id_this_year_overdue):
#  for getting user_id
#     get_search_client = get_search_client_userid()
#     get_search_client = get_search_client.json()
#     user_id = get_search_client['data']['user_id']
#     logger.info(user_id)


    # for calling get function
    get_action_data = get_actionlist_with_user_id_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_review_thisyear_date(user_id,get_actionlist_with_case_review_this_year_overdue):

    # for calling get function
    get_action_data = get_actionlist_with_case_review_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_review_thisyear_date(user_id,get_actionlist_with_client_review_this_year_overdue):

    # for calling get function
    get_action_data = get_actionlist_with_client_review_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_action_thisyear_date(user_id,get_actionlist_with_case_action_this_year_overdue):

    # for calling get function
    get_action_data = get_actionlist_with_case_action_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_action_thisyear_date(user_id,get_actionlist_with_client_action_this_year_overdue):

    # for calling get function
    get_action_data = get_actionlist_with_client_action_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_all_category_thisyear_date_invalid_user_id(get_actionlist_all_category_thisyear_date_invalid_user_id):
    # for calling get function
    get_action_data = get_actionlist_all_category_thisyear_date_invalid_user_id("bbf47558-ac94-4456-8b45-c8aa09118e3c")
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.invalid_user_id_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("User not found")