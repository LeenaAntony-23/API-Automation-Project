import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_fetch_actionlist_all_category_all_date(user_id,get_actionlist_with_user_id):

    # for calling get function
    get_action_data = get_actionlist_with_user_id(user_id)  #actionlistapi

    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_review_all_date(user_id,get_actionlist_case_review):

    # for calling get function
    get_action_data = get_actionlist_case_review(user_id)  #actionlistapi

    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_action_all_date(user_id,get_actionlist_client_action):

    # for calling get function
    get_action_data = get_actionlist_client_action(user_id)  #actionlistapi

    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_action_all_date(user_id,get_actionlist_case_action):

    # for calling get function
    get_action_data = get_actionlist_case_action(user_id)  #actionlistapi

    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_review_all_date(user_id,get_actionlist_client_review):

    # for calling get function
    get_action_data = get_actionlist_client_review(user_id)  #actionlistapi

    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_all_category_all_date_invalid_user_id(get_actionlist_with_user_id):
    # for calling get function
    get_action_data = get_actionlist_with_user_id("bbf47558-ac94-4456-8b45-c8aa09118e3c")
    get_action_response = get_action_data.json()
    # assert get_action_response['statusCode'] == 200, f"API call failed with StatusCode: {get_action_response['statusCode']}"
    # assert get_action_response["isError"] is False
    common.check_reponse_message(get_action_response, constants.invalid_user_id_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Invalid user id test passed")

def test_fetch_actionlist_all_category_all_date_empty_user_id(get_actionlist_with_empty_user_id):
    # for calling get function

    get_action_data = get_actionlist_with_empty_user_id("")
    get_action_response = get_action_data.json()
    logger.info(get_action_response)
    logger.info("Not Found")

def test_fetch_actionlist_all_category_all_date_invalid_bearer_token(get_user_info,get_actionlist_with_invalid_bearertoken):
     #for getting user_id
     get_search_client = get_user_info()
     get_search_client = get_search_client.json()
     user_id = get_search_client['data']['user_id']
     logger.info(user_id)

     get_actionlist_with_invalid_bearertoken(user_id)
     logger.info("UnAuthorised")