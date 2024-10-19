import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

def test_fetch_user_details_with_valid_user_id( get_user_id_details):

    user_id= "82b8f31c-81b2-403c-87ff-176129d1b64f"
    get_roles_details = get_user_id_details(user_id)
    get_roles_details_response = get_roles_details.json()
    common.check_reponse_message(get_roles_details_response, constants.get_user_id_details_success_message)
    logger.info(get_roles_details_response)
    logger.info("Roles Details Fetched Successfully")
