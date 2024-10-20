import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

def checked():
    print("hey")

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("PyGraphicsGen.ui", None)
window.Generate.clicked.connect(checked)



window.show()
app.exec()




