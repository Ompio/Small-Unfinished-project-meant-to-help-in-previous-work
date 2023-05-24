# -*- coding: utf-8 -*-
"""
Test for checking behavior of dynamic links between data controls. There is used model of data to display in controls.
(in runtime environment)
"""
# TODO docstring for file
from configuration.pytest_markers.marker_enums import (
    FunctionalArea,
    RuntimeEnvironment,
    DesigntimeEnvironment,
)
from configuration.pytest_markers.pytest_markers import (
    functional_area,
    qtest_link,
    runtime_environment_supported,
    designtime_environment_supported,
)
# TODO make imports work
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.test_data.remote_projects import (
    USER_WIDGET_ALIASES_RT,
)
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.scripts.config import (
    UserWidgetAliasesRTConfig,
)
from testsuites.opc_ua.advanced.offline_import_to_client_an_xml_companion_spec_dt.scripts.steps import (
    UserWidgetAliasesRTSteps,
)

# TODO functional area @
@functional_area(FunctionalArea.ALIASING)
@functional_area(FunctionalArea.DYNAMIC_LINKS)
@qtest_link(
    # TODO qtest link
    "https://ra.qtestnet.com/p/120524/portal/project#tab=testdesign&object=1&id=73558127"
)
@runtime_environment_supported(
    (
        # TODO runtime env support
        RuntimeEnvironment.EMULATOR,
        RuntimeEnvironment.WEB_UI,
    )
)
@designtime_environment_supported((DesigntimeEnvironment.NATIVE_IDE,))
# TODO rename class
class TestUserWidgetAliasesRT:
    """
    Test class for checking behavior of dynamic links between data controls.
    There is used model of data to display in controls.
    """
    # TODO rewrite docstring
    steps: UserWidgetAliasesRTSteps
    # TODO rename steps class
    def setup_method(self) -> None:
        """Test setup method"""
        # TODO w przypadku rt dodaj initialize_runtime()
        self.steps = UserWidgetAliasesRTSteps(UserWidgetAliasesRTConfig())
        self.steps.initialize_designer()

    def test_user_widget_aliases_rt(self) -> None:
        """Test basic controls extended for runtime"""
        # TODO test steps equal to qTest ones
        self.steps.step_1_check_values_of_all_controls()

    def teardown_method(self) -> None:
        """Test teardown method"""
        # TODO w zależności czy rt czy dt usun cleanup runtime
        self.steps.cleanup_runtime()
        self.steps.cleanup_designer()
