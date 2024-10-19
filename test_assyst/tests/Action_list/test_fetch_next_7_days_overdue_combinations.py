import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_fetch_actionlist_all_category_next_7_date(user_id,get_search_client_userid,get_actionlist_with_user_id_next_7_days_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_user_id_next_7_days_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_review_next_7_date(user_id,get_actionlist_case_review_next_7_days_overdue):


    # for calling get function
    get_action_data = get_actionlist_case_review_next_7_days_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_review_next_7_date(user_id,get_actionlist_client_review_next_7_days_overdue):


    # for calling get function
    get_action_data = get_actionlist_client_review_next_7_days_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_action_next_7_date(user_id,get_actionlist_client_action_next_7_days_overdue):


    # for calling get function
    get_action_data = get_actionlist_client_action_next_7_days_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_action_next_7_date(user_id,get_actionlist_case_action_next_7_days_overdue):


    # for calling get function
    get_action_data = get_actionlist_case_action_next_7_days_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_all_category_all_date_invalid_user_id(get_actionlist_with_user_id_next_7_days_overdue):
    # for calling get function
    get_action_data = get_actionlist_with_user_id_next_7_days_overdue("bbf47558-ac94-4456-8b45-c8aa09118e3c")
    get_action_response = get_action_data.json()
    # assert get_action_response['statusCode'] == 200, f"API call failed with StatusCode: {get_action_response['statusCode']}"
    # assert get_action_response["isError"] is False
    common.check_reponse_message(get_action_response, constants.invalid_user_id_message)
    assert get_action_response["isError"] is False

    logger.info(get_action_response)
    logger.info("Action list not found")

def test_fetch_actionlist_all_category_all_date_empty_user_id(get_actionlist_with_user_id_next_7_days_overdue_empty_userid):
    # for calling get function

    get_action_data = get_actionlist_with_user_id_next_7_days_overdue_empty_userid("")
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    logger.info("Not Found")

def test_fetch_actionlist_all_category_all_date_invalid_bearer_token(get_user_info,get_actionlist_with_user_id_next_7_days_overdue_invalid_token):
     #for getting user_id
     get_search_client = get_user_info()
     get_search_client = get_search_client.json()
     user_id = get_search_client['data']['user_id']
     logger.info(user_id)

     get_action_data = get_actionlist_with_user_id_next_7_days_overdue_invalid_token(user_id)
     logger.info(get_action_data)
     logger.info("UnAuthorised")