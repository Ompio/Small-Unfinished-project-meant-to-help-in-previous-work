# -*- coding: utf-8 -*-
"""
Module containing UserWidgetAliasesRTSteps class
"""
# TODO poprawić docstring
from engine.verification.verify import verify_condition
from shared.base_classes.base_steps import BaseSteps
# TODO poprawnie ponazywać importy
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.scripts.config import (
    UserWidgetAliasesRTConfig,
)
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.test_data.expected_values import (
    BaseValues,
    ValuesForStep,
    MotorInstances,
)

# TODO zmienić nazwę na odpowiednią
class UserWidgetAliasesRTSteps(BaseSteps):
    """
    Test steps for TestBasicControlsExtendedRT
    """
    # TODO zmienić docstring
    config: UserWidgetAliasesRTConfig
    # TODO zmienić configa razem z importem
    # TODO automatyczne tworzenie stepów
    def step_1_check_values_of_all_controls(self) -> None:
        """Check that all controls values are good in the runtime"""
        # TODO zmienić docstring
        verify_condition(
            self.config.motorwidget1_acceleration.get_value,
            BaseValues.MOTOR_WIDGET_1.ACCELERATION,
            f"Verify that MotorWidget1 acceleration value is equal to {BaseValues.MOTOR_WIDGET_1.ACCELERATION}",
        )
        verify_condition(
            self.config.motorwidget1_speed.get_value,
            BaseValues.MOTOR_WIDGET_1.SPEED,
            f"Verify that MotorWidget1 speed value is equal to {BaseValues.MOTOR_WIDGET_1.SPEED}",
        )
        verify_condition(
            self.config.motorwidget2_acceleration.get_value,
            BaseValues.MOTOR_WIDGET_2.ACCELERATION,
            f"Verify that MotorWidget2 acceleration value is equal to {BaseValues.MOTOR_WIDGET_2.ACCELERATION}",
        )
        verify_condition(
            self.config.motorwidget2_speed.get_value,
            BaseValues.MOTOR_WIDGET_2.SPEED,
            f"Verify that MotorWidget2 speed value is equal to {BaseValues.MOTOR_WIDGET_2.SPEED}",
        )
        verify_condition(
            self.config.motorwidget3_acceleration.get_value,
            BaseValues.MOTOR_WIDGET_3.ACCELERATION,
            f"Verify that MotorWidget3 acceleration value is equal to {BaseValues.MOTOR_WIDGET_3.ACCELERATION}",
        )
        verify_condition(
            self.config.motorwidget3_speed.get_value,
            BaseValues.MOTOR_WIDGET_3.SPEED,
            f"Verify that MotorWidget3 speed value is equal to {BaseValues.MOTOR_WIDGET_3.SPEED}",
        )
        verify_condition(
            self.config.motorwidget4_acceleration.get_value,
            BaseValues.MOTOR_WIDGET_4.ACCELERATION,
            f"Verify that MotorWidget4 acceleration value is equal to {BaseValues.MOTOR_WIDGET_4.ACCELERATION}",
        )
        verify_condition(
            self.config.motorwidget4_speed.get_value,
            BaseValues.MOTOR_WIDGET_4.SPEED,
            f"Verify that MotorWidget4 speed value is equal to {BaseValues.MOTOR_WIDGET_4.SPEED}",
        )
        verify_condition(
            self.config.motorwidget4_combobox.get_value,
            MotorInstances.Motor_1,
            f"Verify that MotorWidget4 combobox value is equal to {MotorInstances.Motor_1}",
        )

