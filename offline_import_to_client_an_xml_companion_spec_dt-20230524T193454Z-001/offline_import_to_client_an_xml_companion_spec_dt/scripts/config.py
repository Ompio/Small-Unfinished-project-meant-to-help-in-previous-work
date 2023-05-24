# -*- coding: utf-8 -*-
"""
Module containing UserWidgetAliasesRTConfig class
"""
from shared.base_classes.base_config import BaseConfig
from shared.basic_controls.spin_box import SpinboxFactory
from shared.composite_controls.project_list_view.models.project_view_model import (
    ProjectViewModel,
)
from shared.data_controls.combo_box import ComboboxFactory

# TODO zmienić nazwę
class UserWidgetAliasesRTConfig(BaseConfig):
    """
    Class containing configuration for UserWidgetAliasesRT
    """
    # TODO zmienić docstring
    def __init__(self) -> None:
        super().__init__()
        project_view_model = ProjectViewModel()
        main_window = project_view_model.PROJECT_NAME.UI.MAIN_WINDOW
        # TODO stepy praktycznie wyżej są zawsze
