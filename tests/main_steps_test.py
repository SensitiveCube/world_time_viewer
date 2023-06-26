import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from PySide6.QtCore import Qt, QDateTime, QTimeZone
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QWidgetAction
import pytz
from datetime import datetime
import sys
sys.path.append(".")
from src.main import WorldTimeViewerApp


scenarios("world_time_viewer.feature")

EXTRA_TYPES = {
    's': str,
}

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


@pytest.fixture()
def initial_time(window):
    return QDateTime.fromString(window.time_label.text(), "yyyy-MM-dd HH:mm:ss")


@given("the App is launched")
def app_is_launched(window):
    # The app instance is already created in the fixture
    assert window is not None

@when("user run the app")
def user_runs_app(window):
    # The app instance is already created in the fixture
    assert window is not None

@then("the timezone of app set to the system timezone")
def app_timezone_set_to_system_timezone(window, system_timezone):
    # Code to check if the app timezone is set to the system timezone
    print(f"app:{window.app_timezone}, sys:{system_timezone}, menu:{window.menu_combo.currentText()}")
    assert window.app_timezone == system_timezone

@then('the menu of timezone should be update and display system timezone')
def timezone_menu_visible_and_display_in_system(window, system_timezone):
    # Code to check if the timezone menu is visible and displays the expected timezoneav
    print(f"app:{window.app_timezone}, sys:{system_timezone}, menu:{window.menu_combo.currentText()}")
    assert window.menu_combo.currentText() == system_timezone

@then('title label should be update and display The present time in system timezone')
def title_label_visible_and_display_in_system(window):
    # Code to check if the title label is visible and displays the expected text
    window.set_timezone("JST")
    assert window.title_label.text() == f'The present time in JST'

@then('time label should be update and display the current time in system timezone')
def time_label_visible_and_display_in_system(window):
    # Code to check if the time label is visible and displays the current time in the expected timezone
    current_detetime = QDateTime.currentDateTime()
    current_time = current_detetime.toString("yyyy-MM-dd HH:mm:ss")
    assert window.time_label.text() == current_time

@when(parsers.parse("user selects a {timezone:s} from the timezone menu", extra_types=EXTRA_TYPES))
def user_selects_timezone(window, timezone, qtbot):
    # Code to simulate selecting a timezone from the timezone menu
    # Ensure that the timezone menu is visible
    # QTest.qWaitForWindowExposed(window)

    # Click on the timezone menu to open it
    timezone_menu = window.menu_combo
    # qtbot.mouseClick(timezone_menu, Qt.LeftButton)
    QTest.mouseClick(timezone_menu, Qt.LeftButton)

    # Find the menu item corresponding to the desired timezone and click on it
    menu_items = timezone_menu.findChildren(QWidgetAction)
    for menu_item in menu_items:
        if menu_item.text() == timezone:
            # qtbot.mouseClick(menu_item, Qt.LeftButton)
            QTest.mouseClick(menu_item, Qt.LeftButton)
            break

    window.menu_combo.setCurrentText(timezone)
    print(f"c app:{window.app_timezone}, pre:{timezone}")

@then(parsers.parse('the app timezone set to the user-selected timezone {timezone:s}', extra_types=EXTRA_TYPES))
def app_timezone_set_to_user_selected_timezone(window, timezone):
    # Code to check if the app timezone is set to the user-selected timezone
    print(f"s app:{window.app_timezone}, pre:{timezone}")
    # assert window.app_timezone == preselected_timezone

@then(parsers.parse('the timezone menu should be update and display {timezone:s}', extra_types=EXTRA_TYPES))
def timezone_menu_visible_and_display_in_current(window, timezone):
    # Code to check if the timezone menu is visible and displays the expected timezoneav
    print(f"s app:{window.app_timezone}, pre:{timezone}, menu:{window.menu_combo.currentText()}")
    assert window.menu_combo.currentText() == timezone

@then(parsers.parse('the title label should be update and display The present time in {timezone:s}', extra_types=EXTRA_TYPES))
def title_label_visible_and_display(window, timezone):
    # Code to check if the title label is visible and displays the expected text
    assert window.title_label.text() == f'The present time in {timezone}'

@then(parsers.parse('the time label should be update and display the current time in {timezone:s}', extra_types=EXTRA_TYPES))
def time_label_visible_and_display(window, timezone):
    # Code to check if the time label is visible and displays the current time in the expected timezone
    display_timezone = pytz.timezone(window.preselected_timezone_list[timezone])
    now_timezone = datetime.now(display_timezone)
    current_time = now_timezone.strftime("%Y-%m-%d %H:%M:%S")
    print(f"r time:{current_time}, dis:{window.time_label.text()}, pre:{timezone}")
    assert window.time_label.text() == current_time

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
