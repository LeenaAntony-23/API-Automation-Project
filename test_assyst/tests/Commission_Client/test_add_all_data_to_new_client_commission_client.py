import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_add_all_data_to_name_address_commission_client(data, create_commission_client):


    client_name_addres = create_commission_client(data, 'commission_client', True)
    client_name_addres_data = client_name_addres.json()
    common.check_reponse_message(client_name_addres_data, constants.add_client_commission_success_message)
    logger.info("Commission for client created successfully")
    logger.info(client_name_addres_data)
    logger.info("Add NameAndAddress With Valid Data for commission client Test Passed!")

