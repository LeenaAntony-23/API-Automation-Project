import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Commission_Partner/test_data_name_and_address_partner.csv"))
def test_add_all_data_to_name_address_commission_partner(field_values, create_commission_partner):
    customer_id = "de1d16e1-6ac9-456c-9042-a022761e8d6c" # username =gopika api
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    Partner_name_addres = create_commission_partner(customer_id,data, 'name_and_address', False)
    Partner_name_addres_data = Partner_name_addres.json()
    common.check_reponse_message(Partner_name_addres_data, expected_message)
    logger.info("Commission for partner created successfully")
    logger.info(Partner_name_addres_data)
    logger.info("Add NameAndAddress With Valid Data for commission partner Test Passed!")

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Commission_Partner/test_data_service_type.csv"))
def test_add_all_data_to_servicetype_commission_partner(field_values, post_client_data):

    customer_id = "de1d16e1-6ac9-456c-9042-a022761e8d6c" # username =gopika api
    partner_cust_id = "fa0e9014-ee32-4e37-ad5f-95a6d631a9b3"

    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    client_servicetype = post_client_data(partner_cust_id, data, 'service_type', False)
    client_servicetype_data = client_servicetype.json()
    common.check_reponse_message(client_servicetype_data, expected_message)
    logger.info(client_servicetype_data)
    logger.info("Commission Partner Details For Service Type Added Successfully")

    logger.info("Add Commission Servicetype Data To Partner Test Passed!")