import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
)

class ContactManager(QMainWindow):
    def __init__(self,app):

        self.app = app
        super().__init__()
        self.setWindowTitle("Contact Management System")
        self.setGeometry(100, 100, 600, 400)

        self.contacts = {}
        self.load_contacts()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter name")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter phone number")
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter email address")

        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.email_input)

        self.add_button = QPushButton("Add Contact")
        self.update_button = QPushButton("Update Contact")
        self.delete_button = QPushButton("Delete Contact")

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.update_button)
        button_layout.addWidget(self.delete_button)
        self.layout.addLayout(button_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Name", "Phone", "Email"])
        self.layout.addWidget(self.table)

        self.add_button.clicked.connect(self.add_contact)
        self.update_button.clicked.connect(self.update_contact)
        self.delete_button.clicked.connect(self.delete_contact)
        self.table.cellClicked.connect(self.select_contact)

        self.selected_contact = None
        self.loadContacts()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)

    def loadContacts(self):
        self.table.setRowCount(0)
        for name, details in self.contacts.items():
            self.addContacts(name, details["phone"], details["email"])

    def addContacts(self, name, phone, email):
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)
        self.table.setItem(row_position, 0, QTableWidgetItem(name))
        self.table.setItem(row_position, 1, QTableWidgetItem(phone))
        self.table.setItem(row_position, 2, QTableWidgetItem(email))

    def clear_inputs(self):
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        if not name or not phone or not email:
            self.show_message("Error", "All fields are required.")
            return

        if name in self.contacts:
            self.show_message("Error", "Contact already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            self.save_contacts()
            self.addContacts(name, phone, email)
            self.clear_inputs()
            self.show_message("Success", f"Contact {name} added successfully.")

    def update_contact(self):
        if self.selected_contact is None:
            self.show_message("Error", "No contact selected.")
            return

        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()

        if not name or not phone or not email:
            self.show_message("Error", "All fields are required.")
            return

        self.contacts[self.selected_contact] = {"phone": phone, "email": email}
        self.save_contacts()
        self.loadContacts()
        self.clear_inputs()
        self.show_message("Success", f"Contact {self.selected_contact} updated successfully.")

    def delete_contact(self):
        if self.selected_contact is None:
            self.show_message("Error", "No contact selected.")
            return

        del self.contacts[self.selected_contact]
        self.save_contacts()
        self.loadContacts()
        self.clear_inputs()
        self.show_message("Success", f"Contact {self.selected_contact} deleted successfully.")
        self.selected_contact = None

    def select_contact(self, row, column):
        self.selected_contact = self.table.item(row, 0).text()
        self.name_input.setText(self.selected_contact)
        self.phone_input.setText(self.contacts[self.selected_contact]["phone"])
        self.email_input.setText(self.contacts[self.selected_contact]["email"])


