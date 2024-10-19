import pytest
import logging
from test_assyst.utils import common
from test_assyst import constants

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data",["./jsons/create_client.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Income/test_data_income.csv"))
def test_delete_all_data_to_income(field_values,data,create_client,post_income_data,delete_client_details,get_income_data_with_customer_id):
    # Create client
    create_client = create_client(data, None, True)
    create_client_response = create_client.json()
    logger.info(create_client_response)
    common.check_reponse_message(create_client_response, constants.add_client_success_message)
    logger.info("Client Details Added Successfully")
    customer_id = create_client_response['data']['customer_id']

    # Create income using json data
    income_data = common.read_json("./jsons/create_new_income.json")
    post_income = post_income_data(customer_id, income_data, 'income', True)
    post_income_response = post_income.json()
    logger.info(post_income_response)
    common.check_reponse_message(post_income_response, constants.add_income_success_message)
    logger.info("Income Details Added Successfully using JSON Data")
    income_id_1 = post_income_response['data']['income_id']

    # Create income using csv data for different payload
    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_income = post_income_data(customer_id, data, 'income', False)
    post_income_response = post_income.json()
    logger.info(post_income_response)
    common.check_reponse_message(post_income_response, expected_message)
    logger.info("Income Details Added Successfully Using CSV Data")
    income_id_2 = post_income_response['data']['income_id']

    #  Fetch client data before deletion
    get_income_details = get_income_data_with_customer_id(customer_id)
    get_client_response_before = get_income_details.json()
    logger.info(get_client_response_before)
    common.check_reponse_message(get_client_response_before, constants.get_income_success_message)
    logger.info("Income Details Fetched Successfully")

    #  Delete first income details
    delete_client_data = delete_client_details('income',income_id_1)
    delete_client_response = delete_client_data.json()
    logger.info(delete_client_response)
    common.check_reponse_message(delete_client_response, constants.delete_income_success_message)
    logger.info("Income Details Deleted Successfully")

    #  Fetch client data after deletion
    get_income_details = get_income_data_with_customer_id(customer_id)
    get_client_response_after = get_income_details.json()
    logger.info(get_client_response_after)
    common.check_reponse_message(get_client_response_after, constants.get_income_success_message)
    logger.info("Income Details Fetched Successfully")


    # Extract 'income' data from before and after responses
    income_before = get_client_response_before['data'].get('result', [])
    income_after = get_client_response_after['data'].get('result', [])

    # Assert that the income_id_1 is present in the 'before' data
    assert income_id_1 in [income['income_id'] for income in
                           income_before], "Income ID should be in the initial response"

    # Assert that the income_id_1 is NOT present in the 'after' data
    assert income_id_1 not in [income['income_id'] for income in
                               income_after], "Income ID should be deleted from the response"

    # Log that the income was deleted successfully
    logger.info("Confirmed that income data has been deleted successfully.")

    # Verify that the totals have been updated correctly
    total_before = get_client_response_before['data']['total']
    total_after = get_client_response_after['data']['total']

    # Ensure that the ClientAnnualGrossAmount, ClientMonthlyGrossAmount, etc., reflect the change
    assert total_before['ClientAnnualGrossAmount'] > total_after[
        'ClientAnnualGrossAmount'], "ClientAnnualGrossAmount should decrease after deletion"
    assert total_before['ClientMonthlyGrossAmount'] > total_after[
        'ClientMonthlyGrossAmount'], "ClientMonthlyGrossAmount should decrease after deletion"

    # Log that the totals have been updated correctly
    logger.info("Totals have been updated correctly after income deletion.")