import pytest
import logging
from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_loan_hire_purchase_liability_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_loan_hire_purchase_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")
    logger.info(post_liability_response)


    liability_id = post_liability_response['data']['liability_id']
    get_liability_details = get_liability_data_with_liability_id(liability_id, customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")
    logger.info(get_liability_response)
    #common.compare_dicts(post_liability_response['data'], get_liability_response['data'])
    logger.info("Fetch Liability Data With Liability ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_credit_cards_liability_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_credit_cards_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    get_liability_details = get_liability_data_with_liability_id(liability_id, customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    logger.info("Fetch Liability Data With Liability ID Test Passed!")


@pytest.mark.parametrize("dataa", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liabilities_mortgages_liability_id(partner_cust_id,customer_id,provider_correspondence_id,post_system_manager_data,dataa,data, create_client, post_liability_data,
                                                      get_liability_data_with_liability_id):

    post_liability = post_liability_data(customer_id,partner_cust_id,provider_correspondence_id, None,'liabilities_mortgages_liability', True)
    post_liability_response = post_liability.json()
    common.check_reponse_message(post_liability_response, constants.add_liability_success_message)
    logger.info("Liability Details Added Successfully")

    liability_id = post_liability_response['data']['liability_id']
    get_liability_details = get_liability_data_with_liability_id(liability_id, customer_id)
    get_liability_response = get_liability_details.json()
    common.check_reponse_message(get_liability_response, constants.get_liability_success_message)
    assert get_liability_response["isError"] is False
    logger.info("Liability Details Fetched Successfully")

    logger.info("Fetch Liability Data With Liability ID Test Passed!")


@pytest.mark.parametrize("data", ["./jsons/create_client.json"])
def test_fetch_liability_data_with_invalid_liability_id(customer_id,data, create_client, get_liability_data_with_liability_id):

    get_liabiliy_data = get_liability_data_with_liability_id('ffd0c1d4-2cf4-40e7-bf87-79dc9bf608e0', customer_id)
    get_liability_response = get_liabiliy_data.json()
    logger.info(get_liability_response)
    common.check_reponse_message(get_liability_response, constants.invalid_liability_message)
    assert get_liability_response["isError"] is False
    logger.info("Fetch Liability Data With Invalid Liability ID Test Passed!")