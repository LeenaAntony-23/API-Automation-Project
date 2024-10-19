import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_post_addressphone(post_addressphone,create_client,data):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")

    # provider post
    customer_id = create_client_response['data']['customer_id']


    post_addressphone_info = post_addressphone()

    logger.info(post_addressphone_info)
    logger.info("Report fetched successsfully")
