import pytest
import logging
from test_assyst.utils import common

logger = logging.getLogger('my_logger')


@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Systemmanager_Commission/test_data_systemmanager_commissiontype.csv"))
def test_add_data_to_commission_type(field_values, post_systemmanager_commissiontype_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_commission_type = post_systemmanager_commissiontype_data(data, 'commission_types', False)
    post_commission_type_response = post_commission_type.json()
    common.check_reponse_message(post_commission_type_response, expected_message)
    logger.info(post_commission_type_response)
    logger.info("Commission Type Details Added Successfully")

    logger.info("Add Data To Commission Type Test Passed!")

@pytest.mark.parametrize("field_values", common.read_csv("./test_data/Systemmanager_Commission/test_data_systemmanager_commissionrule.csv"))
def test_add_data_to_commission_rule(field_values, post_systemmanager_commissiontype_data):

    data = {field: int(field_values.get(field)) if field_values.get(field).isdigit() else field_values.get(field)
            for field in field_values.keys() if field_values.get(field) is not None and field_values.get(field) != ''}
    expected_message = data.get(list(data)[-2])
    data.popitem()
    data.popitem()
    post_commission_rule = post_systemmanager_commissiontype_data(data, 'commission_rule', False)
    post_commission_rule_response = post_commission_rule.json()
    common.check_reponse_message(post_commission_rule_response, expected_message)
    logger.info(post_commission_rule_response)
    logger.info("Commission Rule Details Added Successfully")

    logger.info("Add Data To Commission Type Test Passed!")