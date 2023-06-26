import sys
import pytz
from datetime import datetime
from PySide6.QtCore import Qt, QTimer, QDateTime
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QComboBox

class WorldTimeViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Time Viewer")

        self.app_timezone = ""
        self.preselected_timezone_list = {
            "JST": "Asia/Tokyo",
            "GMT": "Europe/London",
            "EST": "America/New_York",
            "CST": "America/Chicago",
            "MST": "America/Denver",
            "PST": "America/Los_Angeles",
            "IST": "Asia/Kolkata",
            "CET": "Europe/Paris"
        }

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create and set the title label
        self.title_label = QLabel("", self)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create and set the time label
        self.time_label = QLabel("", self)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create and set the menu
        self.menu_combo = QComboBox()
        self.menu_combo.addItem("JST")
        self.menu_combo.addItem("GMT")
        self.menu_combo.addItem("PST")
        self.menu_combo.setCurrentIndex(0)
        self.menu_combo.currentIndexChanged.connect(self.handle_menu_combo_change)


        # Create the colse button
        self.button = QPushButton("Close", self)
        self.button.clicked.connect(self.close)

        # Add the labels and button to the layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.menu_combo)
        layout.addWidget(self.time_label)
        layout.addWidget(self.button)

        # initial scecence
        self.set_timezone(self.get_system_timezone())
        self.set_title_label()
        self.update_time()

        # Start a timer to update the time every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def handle_menu_combo_change(self, index):
        self.set_timezone(self.menu_combo.currentText())

    def get_system_timezone(self):
        current_datetime = QDateTime.currentDateTime()
        system_timezone = current_datetime.timeZoneAbbreviation()
        return system_timezone

    def set_timezone(self, timezone):
        self.app_timezone = timezone
        print(self.app_timezone)
        self.menu_combo.setCurrentText(timezone)
        self.set_title_label()
        self.update_time()

    def set_title_label(self):
        self.title_label.setText(f'The present time in {self.app_timezone}')

    def update_time(self):
        now = datetime.now(pytz.timezone('Asia/Tokyo'))
        current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time_label.setText(current_time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorldTimeViewerApp()
    window.show()
    sys.exit(app.exec())
