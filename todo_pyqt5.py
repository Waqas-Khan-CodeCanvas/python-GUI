from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QListWidget, QMessageBox
)
from PyQt5.QtGui import QFont
import sys

class ModernTodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("📝 Modern To-Do App - PyQt5")
        self.setGeometry(100, 100, 500, 600)
        self.setStyleSheet("background-color: #f4f4f4;")
        self.tasks = []
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Task Input
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.setFont(QFont("Segoe UI", 12))
        self.task_input.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
        """)
        layout.addWidget(self.task_input)

        # Buttons
        button_layout = QHBoxLayout()
        self.add_btn = self.create_button("Add", self.add_task)
        self.update_btn = self.create_button("Update", self.update_task)
        self.delete_btn = self.create_button("Delete", self.delete_task)
        self.clear_btn = self.create_button("Clear All", self.clear_all)
        for btn in [self.add_btn, self.update_btn, self.delete_btn, self.clear_btn]:
            button_layout.addWidget(btn)
        layout.addLayout(button_layout)

        # Task List
        self.task_list = QListWidget()
        self.task_list.setFont(QFont("Segoe UI", 11))
        self.task_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                border-radius: 8px;
                padding: 10px;
                border: 1px solid #ccc;
            }
            QListWidget::item:selected {
                background-color: #a3c9f1;
            }
        """)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.setFont(QFont("Segoe UI", 10))
        button.clicked.connect(callback)
        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        return button

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty.")

    def update_task(self):
        current_item = self.task_list.currentItem()
        if current_item:
            new_task = self.task_input.text().strip()
            if new_task:
                current_item.setText(new_task)
                index = self.task_list.currentRow()
                self.tasks[index] = new_task
                self.task_input.clear()
            else:
                QMessageBox.warning(self, "Warning", "Updated task cannot be empty.")
        else:
            QMessageBox.information(self, "Info", "Please select a task to update.")

    def delete_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            self.tasks.pop(row)
            self.task_list.takeItem(row)
        else:
            QMessageBox.information(self, "Info", "Please select a task to delete.")

    def clear_all(self):
        confirm = QMessageBox.question(self, "Clear All Tasks", "Are you sure?",
                                       QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.tasks.clear()
            self.task_list.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModernTodoApp()
    window.show()
    sys.exit(app.exec_())
