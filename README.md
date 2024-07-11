# Software Development Intern At Prodify Infotech 
## Task 3 : Implement a Simple Contact Management System
Develop a program that allows users to store and manage contact information. The program should provide options to add a new contact by entering their name, phone number, and email address. It should also allow users to view their contact list, edit existing contacts, and delete contacts if needed. The program should store the contacts in memory or in a file for persistent storage.

# Dependencies :
1. Python 3.12
2. PySide6
3. JSON

# Project Overview :
## Objectives:
1. Create a contact management system with functionalities to add, update, delete, and view contacts.
2. Use PySide6 for the GUI.
3. Store the contact data in a JSON file for persistence.

# Implementation
## Step-by-Step Guide:
### Setup the GUI:

1. Create the main window and set its properties.
2. Add input fields for the contact details (name, phone, email).
3. Add buttons for adding, updating, and deleting contacts.
4. Add a table widget to display the contacts.

### Load and Save Contacts:

1. Load contacts from a JSON file at the start.
2. Save contacts to the JSON file whenever changes are made.

### Handling User Actions:

1. Add Contact: Validate inputs and add the contact to the list.
2. Update Contact: Update the selected contact's details.
3. Delete Contact: Remove the selected contact from the list.
4. Select Contact: Populate the input fields with the selected contact's details.

