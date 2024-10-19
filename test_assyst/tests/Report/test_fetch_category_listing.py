import pytest
import logging


logger = logging.getLogger('my_logger')


def test_fetch_category_listing(get_category_listing):

    get_client_data = get_category_listing()
    get_client_response = get_client_data.json()
    logger.info(get_client_response)
    logger.info("Category listing fetched successfully")