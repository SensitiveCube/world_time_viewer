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
        self.menu = QComboBox()
        self.menu.addItem("JST")
        self.menu.addItem("GMT")
        self.menu.addItem("PST")
        self.menu.setCurrentIndex(0)

        # Create the colse button
        self.button = QPushButton("Close", self)
        self.button.clicked.connect(self.close)

        # Add the labels and button to the layout
        layout.addWidget(self.title_label)
        layout.addWidget(self.menu)
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

    def get_system_timezone(self):
        current_datetime = QDateTime.currentDateTime()
        system_timezone = current_datetime.timeZoneAbbreviation()
        return system_timezone

    def set_timezone(self, timezone):
        self.app_timezone = timezone
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
