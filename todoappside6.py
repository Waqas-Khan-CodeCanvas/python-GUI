import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget,
    QLineEdit, QMessageBox, QLabel, QCheckBox
)
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import Qt

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📝 Modern To-Do App (PySide6)")
        self.setWindowIcon(QIcon())  # Optional: Add an icon
        self.resize(500, 600)
        self.tasks = []
        self.theme = "light"
        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(15)

        # Title
        self.title = QLabel("To-Do List")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Segoe UI", 20, QFont.Bold))
        layout.addWidget(self.title)

        # Input field and add button
        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter your task...")
        input_layout.addWidget(self.task_input)

        self.add_btn = QPushButton("Add")
        self.add_btn.clicked.connect(self.add_task)
        input_layout.addWidget(self.add_btn)

        layout.addLayout(input_layout)

        # List widget for tasks
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        # Buttons: Update, Delete, Clear
        crud_layout = QHBoxLayout()

        self.update_btn = QPushButton("Update")
        self.update_btn.clicked.connect(self.update_task)
        crud_layout.addWidget(self.update_btn)

        self.delete_btn = QPushButton("Delete")
        self.delete_btn.clicked.connect(self.delete_task)
        crud_layout.addWidget(self.delete_btn)

        self.clear_btn = QPushButton("Clear All")
        self.clear_btn.clicked.connect(self.clear_tasks)
        crud_layout.addWidget(self.clear_btn)

        layout.addLayout(crud_layout)

        # Theme toggle
        self.theme_toggle = QCheckBox("🌙 Dark Mode")
        self.theme_toggle.stateChanged.connect(self.toggle_theme)
        layout.addWidget(self.theme_toggle)

        self.setLayout(layout)

    def apply_theme(self):
        if self.theme == "dark":
            self.setStyleSheet("""
                QWidget {
                    background-color: #121212;
                    color: #f0f0f0;
                    font-family: 'Segoe UI';
                }
                QLineEdit {
                    background-color: #1e1e1e;
                    color: #f0f0f0;
                    border: 1px solid #333;
                    padding: 5px;
                }
                QListWidget {
                    background-color: #1e1e1e;
                    color: #f0f0f0;
                }
                QPushButton {
                    background-color: #333;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
            """)
        else:
            self.setStyleSheet("""
                QWidget {
                    background-color: #f4f4f4;
                    color: #333;
                    font-family: 'Segoe UI';
                }
                QLineEdit {
                    background-color: white;
                    color: #333;
                    border: 1px solid #ccc;
                    padding: 5px;
                }
                QListWidget {
                    background-color: white;
                    color: #333;
                }
                QPushButton {
                    background-color: #0078d7;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                }
                QPushButton:hover {
                    background-color: #005fa3;
                }
            """)

    def toggle_theme(self):
        self.theme = "dark" if self.theme_toggle.isChecked() else "light"
        self.apply_theme()

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.tasks.append(task)
            self.update_list()
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty.")

    def update_task(self):
        selected = self.task_list.currentRow()
        new_task = self.task_input.text().strip()
        if selected >= 0 and new_task:
            self.tasks[selected] = new_task
            self.update_list()
            self.task_input.clear()
        else:
            QMessageBox.information(self, "Info", "Select a task and enter updated text.")

    def delete_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            del self.tasks[selected]
            self.update_list()
        else:
            QMessageBox.information(self, "Info", "Select a task to delete.")

    def clear_tasks(self):
        if QMessageBox.question(self, "Confirm", "Are you sure you want to clear all tasks?") == QMessageBox.Yes:
            self.tasks.clear()
            self.update_list()

    def update_list(self):
        self.task_list.clear()
        self.task_list.addItems(self.tasks)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec())
