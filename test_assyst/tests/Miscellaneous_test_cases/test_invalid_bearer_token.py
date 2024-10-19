import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_create_client_data(data, create_client_test):
    create_client_test(data, None, True)

    logger.info("Unauthorised Bearer token")

