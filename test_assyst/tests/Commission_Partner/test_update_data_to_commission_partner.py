import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Commission_Partner/test_data_name_and_address_partner.csv"))
def test_update_commission_partner_name_address_data(field_values,  patch_name_address_commission_partner_data):
    customer_id = "de1d16e1-6ac9-456c-9042-a022761e8d6c" # username =gopika api
    partner_cust_id = "fa0e9014-ee32-4e37-ad5f-95a6d631a9b3"

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    patch_client_data = patch_name_address_commission_partner_data(partner_cust_id, data, 'name_and_address', None)
    patch_client_data_response = patch_client_data.json()
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Commission Partner Details For Name And Address Updated Successfully")

    logger.info("Update Data To Commission Partner Test Passed!")

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Commission_Partner/test_data_service_type.csv"))
def test_update_commission_partner_service_type_data(field_values,post_client_data,  patch_clientservicetype_data):
    customer_id = "fa0e9014-ee32-4e37-ad5f-95a6d631a9b3" # username =gopika api
    # Servicetype post
    servicetype_data = common.read_json("./jsons/create_new_servicetype.json")
    client_servicetype = post_client_data(customer_id, servicetype_data, 'service_type', True)
    client_servicetype_data = client_servicetype.json()
    logger.info(client_servicetype_data)
    common.check_reponse_message(client_servicetype_data, constants.post_servicetype_partner_success_message)
    logger.info("Partner Details For Service Type Added Successfully")

    customer_id = client_servicetype_data['data']['servicetype']['customer_id']
    servicetype_id = client_servicetype_data['data']['servicetype']['servicetype_id']

    # service type patch
    values = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = values.get(list(values)[-1])
    values.popitem()
    values.popitem()
    patch_client_data = patch_clientservicetype_data(customer_id, servicetype_id, values, 'service_type', None)
    patch_client_data_response = patch_client_data.json()
    logger.info(expected_message)
    logger.info(patch_client_data_response)
    common.check_reponse_message(patch_client_data_response, expected_message)
    logger.info("Client Details For Service Type Commission Partner Updated Successfully")
    logger.info("Update Service Type Commission Partner Data Test Passed!")
    # data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
    #           for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    # expected_message = data.get(list(data)[-1])
    # data.popitem()
    # patch_client_data = patch_clientservicetype_data(customer_id,servicetype_id, data, 'service_type', False)
    # patch_client_data_response = patch_client_data.json()
    # common.check_reponse_message(patch_client_data_response, expected_message)
    # logger.info(patch_client_data_response)
    # logger.info("Commission Partner Details For Name And Address Updated Successfully")
    #
    # logger.info("Update Data To Commission Partner Test Passed!")
