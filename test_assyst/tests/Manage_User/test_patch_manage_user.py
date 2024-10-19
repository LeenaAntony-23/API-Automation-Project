import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_patch_manage_user( patch_manage_user_data):

    data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
    user_id= "7fe77b21-0814-493d-a2df-dd1da872ce77"                     #apiautomation
    patch_manage_user = patch_manage_user_data(data, True, user_id)
    patch_manage_user_response = patch_manage_user.json()
    logger.info(patch_manage_user_response)
    common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
    logger.info("User Details Updated Successfully")

#
#
# def test_patch_manage_user_2( patch_manage_user_data):
#
#     data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
#     user_id= "a9cd39f8-827f-4058-8e92-5aa9f745fb71"                     #apiautomation
#     patch_manage_user = patch_manage_user_data(data, True, user_id)
#     patch_manage_user_response = patch_manage_user.json()
#     logger.info(patch_manage_user_response)
#     common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
#     logger.info("User Details Updated Successfully")
#
#
#
#
# def test_patch_manage_user_3(patch_manage_user_data):
#     data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
#     user_id = "1b198705-079a-4ad8-b8da-6c74265d231b"  # apiautomation
#     patch_manage_user = patch_manage_user_data(data, True, user_id)
#     patch_manage_user_response = patch_manage_user.json()
#     logger.info(patch_manage_user_response)
#     common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
#     logger.info("User Details Updated Successfully")
#
#
#
#
#
# def test_patch_manage_user_4(patch_manage_user_data):
#     data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
#     user_id = "ae2392b2-517d-418b-94d5-39b618508bea"  # apiautomation
#     patch_manage_user = patch_manage_user_data(data, True, user_id)
#     patch_manage_user_response = patch_manage_user.json()
#     logger.info(patch_manage_user_response)
#     common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
#     logger.info("User Details Updated Successfully")
#
# def test_patch_manage_user_5(patch_manage_user_data):
#     data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
#     user_id = "c32aa1bb-e2b1-4780-b4a1-0756d7976016"  # apiautomation
#     patch_manage_user = patch_manage_user_data(data, True, user_id)
#     patch_manage_user_response = patch_manage_user.json()
#     logger.info(patch_manage_user_response)
#     common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
#     logger.info("User Details Updated Successfully")
#
# def test_patch_manage_user_6(patch_manage_user_data):
#     data = common.read_json("./jsons/create_new_manage_user_for_patch.json")
#     user_id = "cb45c55c-9786-4dc3-9a89-3c9a612aee34"  # apiautomation
#     patch_manage_user = patch_manage_user_data(data, True, user_id)
#     patch_manage_user_response = patch_manage_user.json()
#     logger.info(patch_manage_user_response)
#     common.check_reponse_message(patch_manage_user_response, constants.patch_manage_user_success_message)
#     logger.info("User Details Updated Successfully")