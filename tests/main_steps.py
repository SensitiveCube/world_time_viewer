import pytest
from pytest_bdd import given, when, then, scenario
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
import sys
sys.path.append(".")
from src.main import WorldTimeViewerApp

app = None  # Placeholder for the app instance

@pytest.fixture(scope="session")
def app_launch():
    global app

    # Create a QApplication instance
    app = QApplication([])

    # Create the window
    window = WorldTimeViewerApp()

    # Yield the window to the test case
    yield window

    # Cleanup
    # window.close()
    app.quit()

@pytest.fixture()
def timezone():
    pass


@given("the App is launched")
def app_is_launched(app_launch):
    # The app instance is already created in the fixture
    pass

@when("user run the app")
def user_runs_app():
    # App is already launched in the fixture, nothing to do here
    pass

@then("the app timezone set to the system timezone <timezone>")
def app_timezone_set_to_system_timezone(timezone):
    # Code to check if the app timezone is set to the system timezone
    pass

@then('the timezone menu should be visible and display "<timezone>"')
def timezone_menu_visible_and_display(timezone):
    # Code to check if the timezone menu is visible and displays the expected timezone
    pass

@then('the title label should be visible and display "The present time in <timezone>"')
def title_label_visible_and_display(timezone):
    # Code to check if the title label is visible and displays the expected text
    pass

@then('the time label should be visible and display the current time in <timezone>')
def time_label_visible_and_display(timezone):
    # Code to check if the time label is visible and displays the current time in the expected timezone
    pass

@when("user selects a timezone from the timezone menu")
def user_selects_timezone(timezone):
    # Code to simulate selecting a timezone from the timezone menu
    pass

@then('the app timezone set to the user-selected timezone <timezone>')
def app_timezone_set_to_user_selected_timezone(timezone):
    # Code to check if the app timezone is set to the user-selected timezone
    pass

@then('the timezone menu should be update and display "<timezone>"')
def timezone_menu_update_and_display(timezone):
    # Code to check if the timezone menu is updated and displays the expected timezone
    pass

@then('the title label should be update and display "The present time in <timezone>"')
def title_label_update_and_display(timezone):
    # Code to check if the title label is updated and displays the expected text
    pass

@then('the time label should be update and display the current time in <timezone>')
def time_label_update_and_display(timezone):
    # Code to check if the time label is updated and displays the current time in the expected timezone
    pass

@when("the time passes")
def time_passes():
    # Code to simulate the passage of time (e.g., wait for a few seconds)
    # QTest.qWait(3000)  # Wait for 3 seconds
    pass

@then('the time label should be updated to reflect the current time in the app timezone')
def time_label_updated_to_current_time():
    # Code to check if the time label is updated to reflect the current time in the app timezone
    pass

@when("user click the close button")
def user_clicks_close_button():
    # Code to simulate clicking the close button
    pass

@then("the app should be closed")
def app_should_be_closed():
    # Code to check if the app is closed
    pass
