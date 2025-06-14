import sys
import pytz
import tzlocal
import json
from datetime import datetime
from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox

class WorldTimeViewerApp(QMainWindow):
    """"
    A GUI application to view and display the current time in different timezones.

    Attributes:
        selected_timezone (str): The currently selected timezone.
        preselected_timezone_list (dict): A dictionary containing preselected timezones
            and their corresponding timezone names.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Time Viewer")

        self.selected_timezone = ""
        self.selected_location = ""
        self.preselected_timezone_list = ""

        # Load preselected timezone from a JSON file
        with open('src/preselected_timezones.json', 'r') as f:
            self.preselected_timezone_list = json.load(f)

        # initial sequence
        self.create_widgets()
        self.set_timezone(self.get_system_timezone())
        self.set_preselected_list()
        self.set_menu_combo_to_system_timezone()
        self.set_title_label()
        self.update_time()

        # Start a timer to update the time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def create_widgets(self):
        # Create a central widget and set the layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        # Create and set the title label
        self.title_label = QLabel("", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create and set the time label
        self.time_label = QLabel("", self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create the menu
        self.menu_combo = QComboBox()

        # Create the colse button
        self.button = QPushButton("Close", self)
        self.button.clicked.connect(self.close)

        # Add the labels and button to the layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.menu_combo)
        layout.addWidget(self.time_label)
        layout.addWidget(self.button)

    def handle_menu_combo_change(self, index):
        self.set_timezone(self.menu_combo.currentText())

    def set_preselected_list(self):
        # Add preselected timezones to the menu
        for timezone in self.preselected_timezone_list.keys():
            self.menu_combo.addItem(timezone)

    def set_menu_combo_to_system_timezone(self):
        # Set the menu to the current system timezone
        current_datetime = QDateTime.currentDateTime()
        system_timezone_key = current_datetime.timeZoneAbbreviation()
        self.menu_combo.setCurrentText(system_timezone_key)
        self.menu_combo.currentIndexChanged.connect(self.handle_menu_combo_change)

    def get_system_timezone(self):
        # Get the system timezone as key and name
        current_datetime = QDateTime.currentDateTime()
        system_timezone_key = current_datetime.timeZoneAbbreviation()
        system_timezone_name = tzlocal.get_localzone_name()
        print(f'key: {system_timezone_key}, name: {system_timezone_name}')

        # Add the system timezone to the preselected list if not already present
        self.preselected_timezone_list.setdefault(system_timezone_key,system_timezone_name)
        return system_timezone_key

    def set_timezone(self, timezone):
        # Set the app timezone and update UI
        self.selected_timezone = timezone
        self.selected_location = self.preselected_timezone_list.get(self.selected_timezone)
        print(self.selected_timezone)
        self.menu_combo.setCurrentText(timezone)
        self.set_title_label()
        self.update_time()

    def set_title_label(self):
        # Update the title label with the app timezone
        self.title_label.setText(f'The present time in {self.selected_location}')

    def update_time(self):
        # Update the time label with the current time in the app timezone
        current_timezone = pytz.timezone(self.preselected_timezone_list[self.selected_timezone])
        now_timezone = datetime.now(current_timezone)
        current_time_str = now_timezone.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(current_time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorldTimeViewerApp()
    window.show()
    sys.exit(app.exec())
