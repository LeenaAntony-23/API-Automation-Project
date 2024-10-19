import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_expense_category.csv"))
def test_update_data_to_expense_category(get_expense_category_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'expense_category', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.add_expense_category_success_message)
    logger.info(post_expense_category_response)
    logger.info("Expense Category Details Added Successfully")
    get_expense_category_details_data = get_expense_category_details()
    get_expense_category_details_response = get_expense_category_details_data.json()
    common.check_reponse_message(get_expense_category_details_response, constants.get_expense_category_success_message)
    logger.info(get_expense_category_details_response)
    logger.info("All Expense Category Details Fetched Successfully")
    logger.info("Add Data To Expense Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'expense_category', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_expense_category_details_data = get_expense_category_details()
    get_expense_category_details_response = get_expense_category_details_data.json()
    common.check_reponse_message(get_expense_category_details_response, constants.get_expense_category_success_message)
    logger.info(get_expense_category_details_response)
    logger.info("All Expense Category Details Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_income_category.csv"))
def test_update_data_to_income_category(get_income_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'income_category', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_incomecategory_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Income Category Details Added Successfully")
    get_income_data = get_income_details()
    get_income_response = get_income_data.json()
    common.check_reponse_message(get_income_response, constants.get_income_category_success_message)
    logger.info(get_income_response)
    logger.info("All Client Details Fetched Successfully")

    logger.info("Add Data To Income Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'income_category', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_income_data = get_income_details()
    get_income_response = get_income_data.json()
    common.check_reponse_message(get_income_response, constants.get_income_category_success_message)
    logger.info(get_income_response)
    logger.info("All Client Details Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_attitude_category.csv"))
def test_update_data_to_attitude_category(get_attitude_category_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'attitude_to_risk_category', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_attitude_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Attitude risk Category Details Added Successfully")
    get_attitude_category_details_data = get_attitude_category_details()
    get_attitude_category_details_response = get_attitude_category_details_data.json()
    common.check_reponse_message(get_attitude_category_details_response,
                                 constants.get_attitude_category_success_message)
    logger.info(get_attitude_category_details_response)
    logger.info("All Attituderisk Category Details Fetched Successfully")

    logger.info("Add Data To Attitude risk Category Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'attitude_to_risk_category', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_attitude_category_details_data = get_attitude_category_details()
    get_attitude_category_details_response = get_attitude_category_details_data.json()
    common.check_reponse_message(get_attitude_category_details_response,
                                 constants.get_attitude_category_success_message)
    logger.info(get_attitude_category_details_response)
    logger.info("All Attituderisk Category Details Fetched Successfully")


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_attitude_rating_category.csv"))
def test_update_data_to_attitude_rating_category(get_attitude_rating_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'attitude_to_risk_rating', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_attitude_rating_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Attitude risk Rating Category Details Added Successfully")
    get_attitude_rating_data = get_attitude_rating_details()
    get_attitude_rating_response = get_attitude_rating_data.json()
    common.check_reponse_message(get_attitude_rating_response, constants.get_attitude_rating_success_message)
    logger.info(get_attitude_rating_response)
    logger.info("Attitude rating details listed successfully")

    logger.info("Add Data To Attitude risk Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'attitude_to_risk_rating', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_attitude_rating_data = get_attitude_rating_details()
    get_attitude_rating_response = get_attitude_rating_data.json()
    common.check_reponse_message(get_attitude_rating_response, constants.get_attitude_rating_success_message)
    logger.info(get_attitude_rating_response)
    logger.info("Attitude rating details listed successfully")


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_objective_detail_category.csv"))
def test_update_data_to_objective_detail_category(get_objective_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'objectives_detail', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_objective_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Objective Detail Category Details Added Successfully")
    get_objective_details_data = get_objective_details()
    get_objective_details_response = get_objective_details_data.json()
    common.check_reponse_message(get_objective_details_response, constants.get_objective_detail_success_message)
    logger.info(get_objective_details_response)
    logger.info("Objective details listed successfully")

    logger.info("Add Data To Objective Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'objectives_detail', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_objective_details_data = get_objective_details()
    get_objective_details_response = get_objective_details_data.json()
    common.check_reponse_message(get_objective_details_response, constants.get_objective_detail_success_message)
    logger.info(get_objective_details_response)
    logger.info("Objective details listed successfully")


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data/System_Manager/test_data_objective_category.csv"))
def test_update_data_to_objective_category(data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'objectives_category', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_objective_category_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Objective  Category Details Added Successfully")


    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'objectives_category', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")


#
@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_providers.csv"))
def test_update_data_to_provider_detail_category(get_providers_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'provider', True)
    post_expense_category_response = post_expense_category.json()
    common.check_reponse_message(post_expense_category_response, constants.get_provider_patch_sucess_message)
    logger.info(post_expense_category_response)
    logger.info("Provider Detail Category Details Added Successfully")
    get_provider_data = get_providers_details()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_providers_success_message)
    logger.info(get_provider_data_response)
    logger.info("Provider details listed successfully")

    logger.info("Add Data To Provider Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'provider', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_provider_data = get_providers_details()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_providers_success_message)
    logger.info(get_provider_data_response)
    logger.info("Provider details listed successfully")
#

@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_client_actions.csv"))
def test_update_data_to_standard_clientaction_category(get_client_action_details,data,field_values, post_system_manager_data, patch_system_data):

    post_expense_category = post_system_manager_data(data, 'tracking_client_actions', True)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, constants.get_client_actions_patch_sucess_message)
    logger.info("Client actions Detail Category Details Added Successfully")

    logger.info("Add Data To Client actions Category Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'tracking_client_actions', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_client_action_details_data = get_client_action_details()
    get_client_action_details_response = get_client_action_details_data.json()
    common.check_reponse_message(get_client_action_details_response, constants.get_clientaction_success_message)
    logger.info(get_client_action_details_response)
    logger.info("All ClientAction Category Details Fetched Successfully")

@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_case_actions.csv"))
def test_update_data_to_standard_caseaction_category(get_standard_caseaction_details,data,field_values, post_system_manager_data, patch_system_data):
    post_expense_category = post_system_manager_data(data, 'tracking_case_actions', True)
    post_expense_category_response = post_expense_category.json()
    logger.info(post_expense_category_response)
    common.check_reponse_message(post_expense_category_response, constants.get_caseactn_tracking_success_message)
    logger.info("Case actions Detail Category Details Added Successfully")

    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_expense_category_response['data']['id']
    patch_system_data = patch_system_data(category_id, data, 'tracking_case_actions', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("System manager Updated Successfully")
    get_loard_standard_clientaction_data = get_standard_caseaction_details()
    get_loard_standard_clientaction_response = get_loard_standard_clientaction_data.json()
    common.check_reponse_message(get_loard_standard_clientaction_response,
                                 constants.get__standard_client_action_success_message)
    logger.info(get_loard_standard_clientaction_response)
    logger.info("Load standard action for client listed successfully")


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/System_Manager/test_data_user_defined.csv"))
def test_update_data_to_user_defined(get_userdefined_details,data,field_values, post_system_manager_data, patch_system_data):
    post_user = post_system_manager_data(data, 'user_defined_field', True)
    post_user_response = post_user.json()
    logger.info(post_user_response)
    common.check_reponse_message(post_user_response, constants.add_user_defined_success)
    logger.info("User defined Details Added Successfully")
    get_client_action_details_data = get_userdefined_details()
    get_client_action_details_response = get_client_action_details_data.json()
    common.check_reponse_message(get_client_action_details_response, constants.get_user_defined_success_message)
    logger.info(get_client_action_details_response)
    logger.info("All User defined Field Details Fetched Successfully")

    logger.info("Add Data To user defined field Test Passed!")
    data = {field: field_values.get(field) for field in field_values.keys() if
            field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    category_id = post_user_response['data']['id']
    patch_system_data = patch_system_data(category_id,data, 'user_defined_field', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)

    logger.info("User defined field Updated Successfully")
    get_client_action_details_data = get_userdefined_details()
    get_client_action_details_response = get_client_action_details_data.json()
    common.check_reponse_message(get_client_action_details_response, constants.get_user_defined_success_message)
    logger.info(get_client_action_details_response)
    logger.info("All User defined Field Details Fetched Successfully")

