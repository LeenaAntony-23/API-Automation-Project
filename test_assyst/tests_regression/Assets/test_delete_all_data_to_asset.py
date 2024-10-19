import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_single_asset_investment(dataa,data,post_system_manager_data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")
    asset_id = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.asset_invlaid_customer_message)
    logger.info("Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']
    assert asset_id not in [data['asset_id'] for data in
                                 asset_after], "Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_multiple_asset_investment(dataa,post_system_manager_data,data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create first asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")
    asset_id_1 = post_asset_response['data']['asset_id']

    # Create second asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_investment_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For Investment Added Successfully")
    asset_id_2 = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("First Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_asset_details_success_message)
    logger.info("Second Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']

    assert asset_id_1 not in [data['appointment_id'] for data in
                                 asset_after], "First Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_single_asset_share_holding(dataa,data,post_system_manager_data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For share holding Added Successfully")
    asset_id = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.asset_invlaid_customer_message)
    logger.info("Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']
    assert asset_id not in [data['asset_id'] for data in
                                 asset_after], "Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_multiple_asset_share_holding(dataa,post_system_manager_data,data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create first asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For share holding Added Successfully")
    asset_id_1 = post_asset_response['data']['asset_id']

    # Create second asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_share_holdings_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For share holding Added Successfully")
    asset_id_2 = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("First Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_asset_details_success_message)
    logger.info("Second Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']

    assert asset_id_1 not in [data['appointment_id'] for data in
                                 asset_after], "First Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_single_asset_home_personal(dataa,data,post_system_manager_data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For home personal Added Successfully")
    asset_id = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.asset_invlaid_customer_message)
    logger.info("Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']
    assert asset_id not in [data['asset_id'] for data in
                                 asset_after], "Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_multiple_asset_home_personal(dataa,post_system_manager_data,data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create first asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For home personal Added Successfully")
    asset_id_1 = post_asset_response['data']['asset_id']

    # Create second asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_home_personal_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For home personal Added Successfully")
    asset_id_2 = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("First Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_asset_details_success_message)
    logger.info("Second Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']

    assert asset_id_1 not in [data['appointment_id'] for data in
                                 asset_after], "First Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_single_asset_banks_building_societies(dataa,data,post_system_manager_data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For banks building societies Added Successfully")
    asset_id = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.asset_invlaid_customer_message)
    logger.info("Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']
    assert asset_id not in [data['asset_id'] for data in
                                 asset_after], "Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
def test_delete_all_data_to_multiple_asset_banks_building_societies(dataa,post_system_manager_data,data,create_client,post_asset_data,delete_client_details,get_asset_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']

    # Create first asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For banks building societies Added Successfully")
    asset_id_1 = post_asset_response['data']['asset_id']

    # Create second asset using json data
    asset_data = common.read_json("./jsons/create_new_asset.json")
    post_asset = post_asset_data(customer_id,None, provider_correspondence_id, asset_data, 'asset_banks_building_societies_asset', True)
    post_asset_response = post_asset.json()
    common.check_reponse_message(post_asset_response, constants.add_asset_success_message)
    logger.info("Asset Details For banks building societies Added Successfully")
    asset_id_2 = post_asset_response['data']['asset_id']

    #  Fetch asset data before deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_before = asset_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_asset_details_success_message)
    logger.info("Asset Details Fetched Successfully")

    #  Delete first client action details
    delete_client_data = delete_client_details('asset',asset_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_asset_success_message)
    logger.info("First Asset Details Deleted Successfully")

    #  Fetch client action data after deletion
    asset_details = get_asset_data_with_customer_id(customer_id)
    get_client_response_after = asset_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_asset_details_success_message)
    logger.info("Second Asset Details Fetched Successfully")

    asset_after = get_client_response_after['data']

    assert asset_id_1 not in [data['appointment_id'] for data in
                                 asset_after], "First Asset ID is not deleted from the response"

    logger.info("Confirmed that Asset data has been deleted successfully.")
