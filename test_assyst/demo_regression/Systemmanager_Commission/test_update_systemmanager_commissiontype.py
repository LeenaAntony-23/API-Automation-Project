import pytest
import logging

from test_assyst import constants
from test_assyst.utils import common

logger = logging.getLogger('my_logger')

@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager_commissiontype.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Systemmanager_Commission/test_data_systemmanager_commissiontype.csv"))
def test_add_data_to_commission_type(get_commission_type,data,field_values, post_systemmanager_commissiontype_data,patch_systemmanager_commissiontype_data):

    post_commission_type = post_systemmanager_commissiontype_data(data, 'commission_types', True)
    post_commission_type_response = post_commission_type.json()
    common.check_reponse_message(post_commission_type_response, constants.add_commission_type_success_message)
    logger.info(post_commission_type_response)
    logger.info("Commission Type Details Added Successfully")

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    commission_id = post_commission_type_response['data']['id']
    patch_system_data = patch_systemmanager_commissiontype_data(commission_id, data, 'commission_types', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("CommissionType Updated Successfully")
    get_provider_data = get_commission_type()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_commission_type_success_message)
    logger.info(get_provider_data_response)


@pytest.mark.parametrize("data", ["./jsons/create_new_systemmanager_commissiontype.json"])
@pytest.mark.parametrize("field_values", common.read_csv("./test_data_regression/Systemmanager_Commission/test_data_systemmanager_commissionrule.csv"))
def test_add_data_to_commission_rule(get_commission_rule,data,field_values, post_systemmanager_commissiontype_data,patch_systemmanager_commissiontype_data):

    post_commission_rule = post_systemmanager_commissiontype_data(data, 'commission_rule', True)
    post_commission_rule_response = post_commission_rule.json()
    common.check_reponse_message(post_commission_rule_response, constants.get_sys_commission_rule_success_message)
    logger.info(post_commission_rule_response)
    logger.info("Commission Rule Details Added Successfully")

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-1])
    data.popitem()
    data.popitem()
    commission_id = post_commission_rule_response['data']['id']
    logger.info(commission_id)
    patch_system_data = patch_systemmanager_commissiontype_data(commission_id, data, 'commission_rule', False)
    patch_system_data_response = patch_system_data.json()
    common.check_reponse_message(patch_system_data_response, expected_message)
    logger.info(patch_system_data_response)
    logger.info("CommissionRule Updated Successfully")
    get_provider_data = get_commission_rule()
    get_provider_data_response = get_provider_data.json()
    common.check_reponse_message(get_provider_data_response, constants.get_commission_rule_success_message)
    logger.info(get_provider_data_response)