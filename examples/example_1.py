import sys
from PySide2.QtWidgets import QApplication, QLabel
#from PySide2.QtCore import Qt

# Qt Application 
app = QApplication(sys.argv)

# Qt Widget
label = QLabel("Hello World!")
#label.setAlignment(Qt.AlignCenter)
label.show()

#Executing app
sys.exit(app.exec_())
