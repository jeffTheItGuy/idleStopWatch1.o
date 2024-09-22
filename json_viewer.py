# json_viewer.py
import json
import os
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextEdit, QDialogButtonBox, QMessageBox

class JSONViewer(QDialog):
    def __init__(self, json_file, parent=None):
        super().__init__(parent)
        self.json_file = json_file
        self.initUI()

    def initUI(self):
        self.setWindowTitle('View Saved Data')
        self.setGeometry(300, 300, 400, 300)

        # Main layout
        layout = QVBoxLayout()

        # Text box to display JSON content
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        # Load JSON content and display it
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                try:
                    data = json.load(file)
                    json_content = json.dumps(data, indent=4)
                    self.text_edit.setText(json_content)
                except json.JSONDecodeError:
                    QMessageBox.warning(self, "Error", "Invalid JSON format.")
        else:
            self.text_edit.setText("No data found.")

        layout.addWidget(self.text_edit)

        # OK button to close the dialog
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        self.setLayout(layout)
