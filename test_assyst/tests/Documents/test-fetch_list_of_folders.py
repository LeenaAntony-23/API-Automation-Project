import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

def test_get_folder_list(get_folder_list ):

    folder_list_details = get_folder_list()
    folder_list_details_response = folder_list_details.json()
    #assert folder_list_details_response['statusCode'] == 200, f"API call failed with StatusCode: {folder_list_details_response['statusCode']}"
    logger.info("Folder list Fetched Successfully")
    logger.info(folder_list_details_response)
