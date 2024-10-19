import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
@pytest.mark.parametrize("data", common.read_csv("./test_data_regression/Client/test_data_name_and_address.csv"))
def test_update_client_commission_data(data,dataa, create_client,patch_clientservicetype_data, patch_client_commission_data,post_client_data):

    customer_id = "de1d16e1-6ac9-456c-9042-a022761e8d6c"     # gopika api

    patch_client_data = patch_client_commission_data(customer_id, data, 'commission_client', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, constants.patch_client_commission_success_message)
    logger.info("Client Details For Name And Address Updated Successfully")

@pytest.mark.parametrize("dataa", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
def test_update_client_commission_data(data,dataa, create_client,patch_clientservicetype_data, patch_client_commission_data,post_client_data):


    servicetype_data = common.read_json("./jsons/create_new_servicetype.json")

    client_servicetype = post_client_data(customer_id, servicetype_data, 'service_type', False)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.add_client_success_message)
    logger.info("Client Commission Details For Service Type Added Successfully")

    servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']
    patch_client_data = patch_clientservicetype_data(customer_id, servicetype_id, dataa, 'service_type', None)
    patch_client_data_response = patch_client_data.json()

    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response, constants.patch_client_success_message)
    logger.info("Client Details For Service Type Updated Successfully")
    logger.info("Update Service Type Data To Client Test Passed!")