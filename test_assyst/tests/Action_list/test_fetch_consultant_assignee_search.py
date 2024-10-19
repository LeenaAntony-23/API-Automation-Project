
import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_fetch_actionlist_only_assignee_thisyear_date(user_id,get_actionlist_with_only_assignee_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_only_assignee_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_invalid_assignee_thisyear_date(user_id,get_actionlist_with_invalid_assignee_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_invalid_assignee_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_invalid_search_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)



def test_fetch_actionlist_only_consultant_thisyear_date(user_id,get_actionlist_with_only_consultant_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_only_consultant_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_invalid_consultant_thisyear_date(user_id,get_actionlist_with_invalid_consultant_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_invalid_consultant_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_invalid_search_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)

def test_fetch_actionlist_only_search_thisyear_date(user_id,get_actionlist_with_only_search_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_only_search_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")

def test_fetch_actionlist_invalid_search_thisyear_date(user_id,get_actionlist_with_invalid_search_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_invalid_search_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_invalid_search_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)

def test_fetch_actionlist_consultant_assignee_search_thisyear_date(user_id,get_actionlist_with_all_search_this_year_overdue):


    # for calling get function
    get_action_data = get_actionlist_with_all_search_this_year_overdue(user_id)
    get_action_response = get_action_data.json()
    common.check_reponse_message(get_action_response, constants.get_actionlist_success_message)
    assert get_action_response["isError"] is False
    logger.info(get_action_response)
    logger.info("Action List Fetched Successfully")
