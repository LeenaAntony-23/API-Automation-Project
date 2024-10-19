import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_fetch_actionlist_all_category_past_date(user_id,get_actionlist_with_user_id_pastdates):

    # for calling get function
    get_action_data = get_actionlist_with_user_id_pastdates(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_review_past_date(user_id,get_actionlist_case_review_pastdates):

    # for calling get function
    get_action_data = get_actionlist_case_review_pastdates(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_review_past_date(user_id,get_actionlist_client_review_pastdates):

    # for calling get function
    get_action_data = get_actionlist_client_review_pastdates(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_client_action_past_date(user_id,get_actionlist_client_action_pastdates):

    # for calling get function
    get_action_data = get_actionlist_client_action_pastdates(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_case_action_past_date(user_id,get_actionlist_case_action_pastdates):
    # for calling get function
    get_action_data = get_actionlist_case_action_pastdates(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_all_category_past_date_invalid_user_id(get_actionlist_all_category_past_date_invalid_user_id):
    # for calling get function
    get_action_data = get_actionlist_all_category_past_date_invalid_user_id("bbf47558-ac94-4456-8b45-c8aa09118e3c")
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.invalid_user_id_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("User not found")



