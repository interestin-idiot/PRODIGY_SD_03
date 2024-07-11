from PySide6.QtWidgets import QApplication
import sys
from contactManagement import ContactManager



app = QApplication(sys.argv)
window = ContactManager(app)


window.show()
app.exec()