import pytest
import logging

logger = logging.getLogger('my_logger')

def test_fetch_template(get_template):

    get_template_data = get_template()
    get_template_data_response = get_template_data.json()
    logger.info(get_template_data_response)
    logger.info("Template Details Fetched Successfully")

def test_fetch_template_invalid_url(get_template_invalid_url):

    get_template_data = get_template_invalid_url()
    get_template_data_response = get_template_data.json()
    logger.info(get_template_data_response)

    logger.info("Template Details Fetched Successfully")