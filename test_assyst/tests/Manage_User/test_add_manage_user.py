import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

#@pytest.mark.parametrize("field_values1", common.read_csv("./test_data/Manage_user/test_create_new_manage_user_patch.csv"))
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Manage_user/test_create_new_manage_user.csv"))
def test_add_manage_user(field_values, post_manage_user_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    #logger.info(data)
    #logger.info(expected_message)
    post_manage_user = post_manage_user_data(data,False)
    post_manage_user_response = post_manage_user.json()
    logger.info(post_manage_user_response)
    common.check_reponse_message(post_manage_user_response, expected_message)
    logger.info("User Details Added Successfully")

    logger.info("Add Data To Manage User Test Passed!")

    # data = {field: int(field_values1.get(field)) if field_values1.get(field).isdigit() else field_values1.get(field)
    #         for field in field_values1.keys() if field_values1.get(field) is not None and field_values1.get(field) != ''}
    # expected_message = data.get(list(data)[-1])
    # data.popitem()
    # patch_manage_user = patch_manage_user_data(data, True, user_id)
    # patch_manage_user_response = patch_manage_user.json()
    # logger.info(patch_manage_user_response)
    # common.check_reponse_message(patch_manage_user_response, expected_message)
    # logger.info("User Details Updated Successfully")