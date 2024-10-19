import pytest
import logging
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_expense_category.csv"))
def test_add_data_to_expense_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'expense_category', False)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info(post_expense_category_response)
    logger.info("Expense Category Details Added Successfully")

    logger.info("Add Data To Expense Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_income_category.csv"))
def test_add_data_to_income_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'income_category', False)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Income Category Details Added Successfully")

    logger.info("Add Data To Income Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_attitude_category.csv"))
def test_add_data_to_attituderisk_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'attitude_to_risk_category', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Attitude Category Details Added Successfully")

    logger.info("Add Data To Attitude Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_attitude_rating_category.csv"))
def test_add_data_to_attituderisk_rating_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'attitude_to_risk_rating', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Attitude Risk Rating Category Details Added Successfully")

    logger.info("Add Data To Attitude Risk Rating Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_objective_detail_category.csv"))
def test_add_data_to_objective_detail_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'objectives_detail', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Objectives Detail Category Details Added Successfully")

    logger.info("Add Data To Objectives Detail Category Test Passed!")

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_objective_category.csv"))
def test_add_data_to_objective_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'objectives_category', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Objectives  Category Details Added Successfully")

    logger.info("Add Data To Objectives  Category Test Passed!")

# #

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_providers.csv"))
def test_add_data_to_provider_detail_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'provider', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Provider Detail Category Details Added Successfully")

    logger.info("Add Data To Provider Detail Category Test Passed!")

#
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_case_actions.csv"))
def test_add_data_to_case_action_detail_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'tracking_case_actions', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Case actions Detail Category Details Added Successfully")

    logger.info("Add Data To Case actions Detail Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_client_actions.csv"))
def test_add_data_to_client_action_detail_category(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_expense_category = post_system_manager_data(data, 'tracking_client_actions', False)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, expected_message)
    logger.info("Client actions Detail Category Details Added Successfully")

    logger.info("Add Data To Client actions Detail Category Test Passed!")


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_user_defined.csv"))
def test_add_data_to_user_defined(field_values, post_system_manager_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
              for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_user = post_system_manager_data(data, 'user_defined_field', False)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, expected_message)
    logger.info("User defined Details Added Successfully")

    logger.info("Add Data To User defined field Test Passed!")