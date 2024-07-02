from PySide6.QtWidgets import QApplication
from front_page import MySideBar
import sys

app = QApplication(sys.argv)
windows = MySideBar()
windows.show()
app.exec()