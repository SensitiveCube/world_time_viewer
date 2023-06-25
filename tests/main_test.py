import pytest
from pytest_bdd import given, when, then, scenario
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
import sys
sys.path.append(".")
from src.main import WorldTimeViewerApp
from main_steps import *

@scenario('world_time_viewer.feature', 'Lunch the app and display time in system timezone')
def test_Lunch_and_display_system_timezone(preselected_timezone):
    pass

@scenario('world_time_viewer.feature', 'Update Time when Selecting Timezone')
def test_update_selecting_timezone():
    pass

@scenario('world_time_viewer.feature', 'Continuously Update Time')
def test_continuously_update_time():
    pass

@scenario('world_time_viewer.feature', 'Close the App')
def test_close_app():
    pass
