import sys
import json


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtCore import QTimer, QTime, Qt
from datetime import datetime

class StopwatchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle('Stopwatch')
        self.setGeometry(200, 200, 300, 300)

        # Timer setup
        self.main_timer = QTimer(self)  # Main timer
        self.main_timer.timeout.connect(self.update_time)
        self.time = QTime(0, 0, 0)

        self.secondary_timer = QTimer(self)  # Secondary timer
        self.secondary_timer.timeout.connect(self.update_secondary_time)
        self.secondary_time = QTime(0, 0, 0)

        # Main Layout
        main_layout = QVBoxLayout()

        # Stopwatch display (Main Clock)
        self.time_display = QLabel(self.time.toString("hh:mm:ss"), self)
        self.time_display.setStyleSheet("font-size: 50px;")
        self.time_display.setAlignment(Qt.AlignCenter)

        # Secondary Stopwatch display (Secondary Clock)
        self.secondary_time_display = QLabel(self.secondary_time.toString("hh:mm:ss"), self)
        self.secondary_time_display.setStyleSheet("font-size: 30px; color: red;")
        self.secondary_time_display.setAlignment(Qt.AlignCenter)

        # Task name input
        self.task_name_input = QLineEdit(self)
        self.task_name_input.setPlaceholderText("Enter task name...")
        main_layout.addWidget(self.task_name_input)

        # Button Layout
        button_layout = QHBoxLayout()

        # Start/Pause button
        self.start_pause_btn = QPushButton('Start', self)
        self.start_pause_btn.clicked.connect(self.toggle_timer)
        button_layout.addWidget(self.start_pause_btn)

        # Reset button
        self.reset_btn = QPushButton('Reset', self)
        self.reset_btn.clicked.connect(self.reset_timer)
        button_layout.addWidget(self.reset_btn)

        # Save button
        self.save_btn = QPushButton('Save', self)
        self.save_btn.clicked.connect(self.save_time)  # Connect the save button to save_time method
        button_layout.addWidget(self.save_btn)

        # Add everything to the main layout
        main_layout.addWidget(self.time_display)
        main_layout.addWidget(self.secondary_time_display)  # Add secondary clock below the main clock
        main_layout.addLayout(button_layout)

        # Set the main layout
        self.setLayout(main_layout)

        # Start with timers paused
        self.running = False

    def toggle_timer(self):
        if self.running:
            self.main_timer.stop()
            self.start_pause_btn.setText('Start')

            # Start secondary timer when the main timer is paused
            self.secondary_timer.start(1000)

        else:
            self.main_timer.start(1000)
            self.start_pause_btn.setText('Pause')

            # Stop the secondary timer when the main timer is running
            self.secondary_timer.stop()

        self.running = not self.running

    def update_time(self):
        self.time = self.time.addSecs(1)
        self.time_display.setText(self.time.toString("hh:mm:ss"))

    def update_secondary_time(self):
        self.secondary_time = self.secondary_time.addSecs(1)
        self.secondary_time_display.setText(self.secondary_time.toString("hh:mm:ss"))

    def reset_timer(self):
        # Stop both timers and reset both clocks
        self.main_timer.stop()
        self.secondary_timer.stop()
        self.time = QTime(0, 0, 0)
        self.secondary_time = QTime(0, 0, 0)
        self.time_display.setText(self.time.toString("hh:mm:ss"))
        self.secondary_time_display.setText(self.secondary_time.toString("hh:mm:ss"))
        self.start_pause_btn.setText('Start')
        self.running = False
        self.task_name_input.clear()

    def save_time(self):
        # Get the current time for both the main and secondary clocks
        main_time_str = self.time.toString("hh:mm:ss")
        secondary_time_str = self.secondary_time.toString("hh:mm:ss")
        
        # Get the task name
        task_name = self.task_name_input.text()

         # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create a dictionary to store the time data
        time_data = {
            'task_name': task_name,
            'main_time': main_time_str,
            'secondary_time': secondary_time_str,
            'timestamp': current_datetime 
        }

        # Save the dictionary as a JSON file
        with open('stopwatch_times.json', 'w') as f:
            json.dump(time_data, f, indent=4)

        print(f"Time saved to stopwatch_times.json: {time_data}")


# Application setup
def main():
    app = QApplication(sys.argv)
    stopwatch = StopwatchApp()
    stopwatch.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
