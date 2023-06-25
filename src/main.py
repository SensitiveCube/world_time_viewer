import sys
import pytz
from datetime import datetime
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget

class WorldTimeViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Time Viewer")

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create and set the title label
        self.titleLabel = QLabel("The present time", self)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create and set the time label
        self.timeLabel = QLabel("", self)
        self.timeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create the colse button
        self.button = QPushButton("Close", self)
        self.button.clicked.connect(self.close)

        # Add the labels and button to the layout
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.button)

        # Start a timer to update the time every second
        self.update_time()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        now = datetime.now(pytz.timezone('Asia/Tokyo'))
        current_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.timeLabel.setText(current_time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WorldTimeViewerApp()
    window.show()
    sys.exit(app.exec())
