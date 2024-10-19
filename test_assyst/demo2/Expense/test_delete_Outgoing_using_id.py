import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
def test_delete_all_data_to_single_Expense(data,create_client,post_outgoing_data,delete_client_details,get_outgoing_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create expense using json data
    outgoing_data = common.read_json("./jsons/create_new_outgoing.json")
    post_outgoing = post_outgoing_data(customer_id, outgoing_data, 'outgoings', True)
    post_outgoing_response = post_outgoing.json()
    logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully")
    expense_id = post_outgoing_response['data']['expense_id']


    #  Fetch client data before deletion
    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.outgoing_fetch_success_message)
    logger.info("Outgoing Details Fetched Successfully")

    #  Delete first expense details
    delete_client_data = delete_client_details('expense',expense_id)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_expense_success_message)
    logger.info("Expense Details Deleted Successfully")

    #  Fetch client data after deletion
    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_outgoing_invalid_message)
    logger.info("Outgoing Details Fetched Successfully")

    # Extract 'expense' data after responses
    expense_after = get_client_response_after['data']

    # Assert that the expense_id_1 is NOT present in the 'after' data
    assert expense_id not in [['expense_id'] for data in
                               expense_after], "Expense ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that expense data has been deleted successfully.")

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Expense/test_data_expense.csv"))
def test_delete_all_data_to_multiple_Expense(field_values,data,create_client,post_outgoing_data,delete_client_details,get_outgoing_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create expense using json data
    outgoing_data = common.read_json("./jsons/create_new_outgoing.json")
    post_outgoing = post_outgoing_data(customer_id, outgoing_data, 'outgoings', True)
    post_outgoing_response = post_outgoing.json()
    logger.info(post_outgoing_response)
    common.check_reponse_message(post_outgoing_response, constants.outgoing_add_success_message)
    logger.info("Outgoing Details Added Successfully Using JSON Data")
    expense_id_1 = post_outgoing_response['data']['expense_id']

    # Create expense using csv data
    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_outgoing = post_outgoing_data(customer_id, data, 'outgoings', False)
    post_outgoing_response = post_outgoing.json()
    common.check_reponse_message(post_outgoing_response, expected_message)
    logger.info("Outgoing Details Added Successfully Using CSV Data")
    expense_id_2 = post_outgoing_response['data']['expense_id']

    #  Fetch client data before deletion
    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response_before = get_client_data.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.outgoing_fetch_success_message)
    logger.info("Outgoing Details Fetched Successfully")

    #  Delete first expense details
    delete_client_data = delete_client_details('expense',expense_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_expense_success_message)
    logger.info("Expense Details Deleted Successfully")

    #  Fetch client data after deletion
    get_client_data = get_outgoing_data_with_customer_id(customer_id)
    get_client_response_after = get_client_data.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.outgoing_fetch_success_message)
    logger.info("Outgoing Details Fetched Successfully")


    # Extract 'expense' data after responses
    expense_after = get_client_response_after['data']

    # Assert that the expense_id_1 is NOT present in the 'after' data
    assert expense_id_1 not in [['expense_id'] for data in
                               expense_after], "Expense ID should be deleted from the response"

    # Log that the expense was deleted successfully
    logger.info("Confirmed that expense data has been deleted successfully.")
