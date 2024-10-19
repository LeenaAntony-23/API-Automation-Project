import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_user_details_with_valid_user_id( get_user_role_details_using_user_id):

    user_id= "7fe77b21-0814-493d-a2df-dd1da872ce77"
    #"FullName": "akhil","UserEmail": "akhil@myvedtekk.com",
    get_roles_details = get_user_role_details_using_user_id(user_id)
    get_roles_details_response = get_roles_details.json()
    #common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
    logger.info(get_roles_details_response)
    logger.info("Roles Details Fetched Successfully")

# def test_fetch_user_details_with_invalid_user_id( get_user_role_details_using_user_id):
#
#     user_id= "12900183-cb8a-40d7-8ec8-ee78d02b1ef1"
#     # 12900183-cb8a-40d7-8ec8-ee78d02b1ef1 -asset id
#     get_roles_details = get_user_role_details_using_user_id(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_invalid_user_id_details_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_expired_bearer_token(get_user_role_details_with_invalid_token):
#
#     user_id= "d0454086-a5a5-4cd2-974d-ceaa1f4d0560"
#     get_id_details = get_user_role_details_with_invalid_token(user_id)
#     # get_id_details_response= get_id_details.json()
#     # common.check_reponse_message(get_id_details_response, constants.get_case_success_message)
#     logger.info(get_id_details)
#
