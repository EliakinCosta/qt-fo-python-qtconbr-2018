import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtGui import QColor, QPalette

def function():
 print("function has been called!")

app = QApplication(sys.argv)
button = QPushButton("Call function")
button.setMaximumSize(500, 200)

pal = button.palette()
pal.setColor(QPalette.Button, QColor(Qt.blue))
button.setAutoFillBackground(True)
button.setPalette(pal)

button.clicked.connect(function)
button.show()
sys.exit(app.exec_())
