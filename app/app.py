import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from main import PyGraphicsGen
import numpy as np

def checked():
    pyGraphics = PyGraphicsGen()
    norms = np.random.normal(size=(20,20))
    pyGraphics.array2dLand(norms)


loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("PyGraphicsGen.ui", None)
window.Generate.clicked.connect(checked)



window.show()
app.exec()




