import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_investment.csv"))
def test_add_data_to_asset_investment(customer_id,partner_cust_id,provider_correspondence_id,data, field_values,post_system_manager_data,dataa, create_client, post_asset_data,
                                      get_asset_details_with_asset_id):


    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_asset = post_asset_data(customer_id, partner_cust_id,provider_correspondence_id,values, 'asset_investment_asset', False)
    client_asset_data = client_asset.json()
    common.check_reponse_message(client_asset_data, expected_message)
    logger.info("Asset Details For Investemnt Added Successfully")
    logger.info(client_asset_data)
    logger.info("Add Asset Investment Data Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_share_holdings.csv"))
def test_add_data_to_asset_share_holdings(customer_id,partner_cust_id,provider_correspondence_id,data, field_values, post_system_manager_data, dataa, create_client, post_asset_data,
                                          get_asset_details_with_asset_id):


    logger.info(provider_correspondence_id)

    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    client_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id,values, 'asset_share_holdings_asset', False)
    client_asset_data = client_asset.json()
    common.check_reponse_message(client_asset_data, expected_message)
    logger.info("Asset Details For Share Holdings Added Successfully")
    # logger.info(client_asset_data)

    logger.info("Add Asset Share Holdings Data Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/test_data_asset_home_personal.csv"))
def test_add_data_to_asset_home_personal(customer_id,partner_cust_id,provider_correspondence_id,data, field_values, post_system_manager_data,dataa, create_client, post_asset_data,
                                         get_asset_details_with_asset_id):


    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    create_asset = post_asset_data(customer_id,partner_cust_id, provider_correspondence_id,values, 'asset_home_personal_asset', False)
    client_asset_data = create_asset.json()
    common.check_reponse_message(client_asset_data, expected_message)
    logger.info("Asset Details For Home And Personal Added Successfully")

    logger.info("Add Asset Home Personal Data Test Passed!")

# #
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Asset/"
                                                         "test_data_asset_banks_building_societies.csv"))
def test_add_data_to_asset_banks_building_societies(customer_id,partner_cust_id,provider_correspondence_id,data, field_values, post_system_manager_data,dataa, create_client, post_asset_data,
                                                    get_asset_details_with_asset_id):


    values = {field: int(field_values.get(field)) if (field_values.get(field).isdigit() and field != 'case_type') else
              field_values.get(field) for field in field_values.keys() if field_values.get(field) is not None and
              field_values.get(field) != ''}
    expected_message = values.get(list(values)[-2])
    values.popitem()
    values.popitem()
    create_asset = post_asset_data(customer_id, partner_cust_id,provider_correspondence_id,values, 'asset_banks_building_societies_asset', False)
    client_asset_data = create_asset.json()
    common.check_reponse_message(client_asset_data, expected_message)
    logger.info("Asset Details For Banks/Building Societies Added Successfully")

    logger.info("Add Asset Bank And Building Socities Data Test Passed!")