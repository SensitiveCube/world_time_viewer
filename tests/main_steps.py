import pytest
from pytest_bdd import given, when, then, scenario
from PySide6.QtCore import Qt, QDateTime
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication
import pytz
from datetime import datetime
import sys
sys.path.append(".")
from src.main import WorldTimeViewerApp

app = None  # Placeholder for the app instance


@pytest.fixture(scope="session")
def window():
    global app

    # Create a QApplication instance
    app = QApplication([])

    # Create the window
    window = WorldTimeViewerApp()

    # Yield the window to the test case
    yield window

    # Cleanup
    window.close()
    app.quit()

@pytest.fixture()
# Provide a list of system timezones
def system_timezone():
    current_datetime = QDateTime.currentDateTime()
    timezone_abbreviation = current_datetime.timeZoneAbbreviation()
    print(timezone_abbreviation)
    return timezone_abbreviation

@pytest.fixture(params=["JST", "GMT", "PST"])
# Provide a list of system timezones
def preselected_timezone(request):
    return request.param

@pytest.fixture()
def initial_time():
    return QDateTime.currentDateTime()


@given("the App is launched")
def app_is_launched(window):
    # The app instance is already created in the fixture
    assert window is not None

@when("user run the app")
def user_runs_app(window):
    # The app instance is already created in the fixture
    assert window is not None

@then("the app timezone set to the system timezone <timezone>")
def app_timezone_set_to_system_timezone(window, system_timezone):
    # Code to check if the app timezone is set to the system timezone
    assert window.app_timezone == system_timezone

@then('And the timezone menu should be visible and display"<timezone>"')
def timezone_menu_visible_and_display(window, preselected_timezone):
    # Code to check if the timezone menu is visible and displays the expected timezone
    assert window.menu.text() == preselected_timezone

@then('the title label should be visible and display "The present time in <timezone>"')
def title_label_visible_and_display(window, preselected_timezone):
    # Code to check if the title label is visible and displays the expected text
    assert window.title_label.text() == f'The present time in {preselected_timezone}'

@then('the time label should be visible and display the current time in <timezone>')
def time_label_visible_and_display():
    # Code to check if the time label is visible and displays the current time in the expected timezone
    current_detetime = QDateTime.currentDateTime()
    current_time = current_detetime.toString("yyyy-MM-dd HH:mm:ss")
    assert window.time_label.text() == current_time

@when("user selects a timezone from the timezone menu")
def user_selects_timezone(window, preselected_timezone):
    # Code to simulate selecting a timezone from the timezone menu
    # Ensure that the timezone menu is visible
    QTest.qWaitForWindowExposed(window)

    # Click on the timezone menu to open it
    timezone_menu = window.timezone_menu
    QTest.mouseClick(timezone_menu, Qt.LeftButton)

    # Find the menu item corresponding to the desired timezone and click on it
    menu_items = timezone_menu.findChildren(QtWidgets.QAction)
    for menu_item in menu_items:
        if menu_item.text() == preselected_timezone:
            QTest.mouseClick(menu_item, Qt.LeftButton)
            break

@then('the app timezone set to the user-selected timezone <timezone>')
def app_timezone_set_to_user_selected_timezone(window, preselected_timezone):
    # Code to check if the app timezone is set to the user-selected timezone
    assert window.app_timezone == preselected_timezone

@when("the time passes")
def time_passes(initial_time):
    # Code to simulate the passage of time (e.g., wait for a few seconds)
    QTest.qWait(3000)  # Wait for 3 seconds

@then('the time label should be updated to reflect the current time in the app timezone')
def time_label_updated_to_current_time(initial_time):
    # Code to check if the time label is updated to reflect the current time in the app timezone
    current_time = QDateTime.currentDateTime()
    elapsed_time = initial_time.msecsTo(current_time) / 1000 # Convert milliseconds to seconds

    # Compare the elapsed time with the expected duration
    assert elapsed_time >= 3.0

@when("user click the close button")
def user_clicks_close_button(window, qtbot):
    # Code to simulate clicking the close button
    button_text = window.button.text()
    qtbot.mouseClick(window.button, Qt.LeftButton)
    assert button_text == "Close"

@then("the app should be closed")
def app_should_be_closed(window):
    # Code to check if the app is closed
    assert window.isVisible() is False
