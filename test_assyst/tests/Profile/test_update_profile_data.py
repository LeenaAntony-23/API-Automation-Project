import pytest
import logging
from test_assyst import constants
from test_assyst.conftest import patch_income_data
from test_assyst.utils import common

logger = logging.getLogger('my_logger')



@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Profile/test_data_profile.csv"))
def test_patch_profile_data( create_client,field_values,patch_profile_data):

    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    id = "82b8f31c-81b2-403c-87ff-176129d1b64f"
    update_profile_data = patch_profile_data( values,id,  False)
    update_profile_data_response = update_profile_data.json()
    logger.info(update_profile_data_response)
    common.check_reponse_message(update_profile_data_response, expected_message)


    logger.info("Update profile details Test Passed!")