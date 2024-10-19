import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')
#
@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_liabilities_loan_hire_purchase_single_data_liability_id(get_liability_data_with_customer_id,delete_case_details,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    logger.info(post_liability_response)


    liability_id = post_liability_response['data']['liability_id']
    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_invalid_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_delete_liabilities_loan_hire_purchase_multiple_data_liability_id(get_liability_data_with_customer_id,delete_case_details,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    logger.info(post_liability_response)


    liability_id_1 = post_liability_response['data']['liability_id']

    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    logger.info(post_liability_response)

    liability_id_2 = post_liability_response['data']['liability_id']

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id_2)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    liability_after = get_liability_response['data']

    # Assert that the liability_id_2 is NOT present in the 'after' data
    assert liability_id_2 not in [data['liability_id'] for data in
                             liability_after], "Liability ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that second liability data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_credit_cards_single_data_liability_id(delete_case_details,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id_1 = post_liability_response['data']['liability_id']

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_invalid_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_credit_cards_multiple_data_liability_id(delete_case_details,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_customer_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id_1 = post_liability_response['data']['liability_id']

    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Second Liability Details Added Successfully")

    liability_id_2 = post_liability_response['data']['liability_id']

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id_2)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Second Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    liability_after = get_liability_response['data']

    # Assert that the liability_id_2 is NOT present in the 'after' data
    assert liability_id_2 not in [data['liability_id'] for data in
                                  liability_after], "Liability ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that second liability data has been deleted successfully.")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_mortgages_liability_single_data_id(delete_case_details,get_liability_data_with_customer_id,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id = post_liability_response['data']['liability_id']

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info("Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_invalid_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_mortgages_liability_multiple_data_id(delete_case_details,get_liability_data_with_customer_id,post_partner_data,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    partner_data = post_partner_data(customer_id, None, "name_and_address", True)
    partner_data_response = partner_data.json()
    logger.info(partner_data_response)
    common.check_reponse_message(partner_data_response, constants.add_partner_success_message)
    logger.info("Partner Details Added Successfully")
    partner_cust_id = partner_data_response['data']['customer_id']

    # post provider
    post_expense_category = post_system_manager_data(dataa, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    provider_correspondence_id = post_expense_category_response['data']['id']


    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id_1 = post_liability_response['data']['liability_id']

    post_liability = post_liability_data(customer_id, partner_cust_id, provider_correspondence_id, None,
                                         'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Second Liability Details Added Successfully")

    liability_id_2 = post_liability_response['data']['liability_id']

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    delete_client_data = delete_case_details('liability', liability_id_2)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_liability_success_message)
    logger.info(" Second Liability Details Deleted Successfully")

    get_liability_details = get_liability_data_with_customer_id(customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    logger.info(get_liability_response)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    liability_after = get_liability_response['data']

    # Assert that the liability_id_2 is NOT present in the 'after' data
    assert liability_id_2 not in [data['liability_id'] for data in
                                  liability_after], "Liability ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that second liability data has been deleted successfully.")
