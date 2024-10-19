import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_user_details_with_valid_user_id( get_user_id_details):

    user_id= "7fe77b21-0814-493d-a2df-dd1da872ce77"
    get_roles_details = get_user_id_details(user_id)
    get_roles_details_response = get_roles_details.json()
    common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
    logger.info(get_roles_details_response)
    logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_valid_user_id_2(get_user_id_details):
#
#     user_id = "a9cd39f8-827f-4058-8e92-5aa9f745fb71"
#     get_roles_details = get_user_id_details(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_valid_user_id_3(get_user_id_details):
#
#     user_id = "1b198705-079a-4ad8-b8da-6c74265d231b"
#     get_roles_details = get_user_id_details(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_valid_user_id_4(get_user_id_details):
#
#     user_id = "ae2392b2-517d-418b-94d5-39b618508bea"
#     get_roles_details = get_user_id_details(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_valid_user_id_5(get_user_id_details):
#
#     user_id = "c32aa1bb-e2b1-4780-b4a1-0756d7976016"
#     get_roles_details = get_user_id_details(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# def test_fetch_user_details_with_valid_user_id_6(get_user_id_details):
#
#     user_id = "cb45c55c-9786-4dc3-9a89-3c9a612aee34"
#     get_roles_details = get_user_id_details(user_id)
#     get_roles_details_response = get_roles_details.json()
#     common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
#     logger.info(get_roles_details_response)
#     logger.info("Roles Details Fetched Successfully")
#
# # def test_fetch_user_details_with_invalid_user_id( get_user_id_details):
# #
# #     user_id= "12900183-cb8a-40d7-8ec8-ee78d02b1ef1"
# #     # 12900183-cb8a-40d7-8ec8-ee78d02b1ef1 -asset id
# #     get_roles_details = get_user_id_details(user_id)
# #     get_roles_details_response = get_roles_details.json()
# #     common.check_reponse_message(get_roles_details_response, constants.get_invalid_user_id_details_message)
# #     logger.info(get_roles_details_response)
# #     logger.info("Roles Details Fetched Successfully")
# #
# # def test_fetch_user_details_with_expired_bearer_token(get_user_id_details_invalid_token):
# #
# #     user_id= "d0454086-a5a5-4cd2-974d-ceaa1f4d0560"
# #     get_id_details = get_user_id_details_invalid_token(user_id)
# #     # get_id_details_response= get_id_details.json()
# #     # common.check_reponse_message(get_id_details_response, constants.get_case_success_message)
# #     logger.info(get_id_details)
#
