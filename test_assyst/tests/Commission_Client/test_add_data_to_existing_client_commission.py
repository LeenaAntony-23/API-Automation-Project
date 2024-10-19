import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", common.read_csv("./test_data_regression/Client/test_data_service_type.csv"))
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_all_data_to__client(dataa,data,post_client_data):


    customer_id = "de1d16e1-6ac9-456c-9042-a022761e8d6c"    #gopika api

    client_servicetype = post_client_data(customer_id, dataa, 'service_type', False)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.add_client_success_message)
    logger.info("Client Commission Details For Service Type Added Successfully")
