import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader
from main import PyGraphicsGen
import numpy as np

pyGraphics = PyGraphicsGen()

def arr2D(x1,y1):
    norms = np.random.normal(size=(x1, y1))
    pyGraphics.array2dLand(norms)

def arrSurf(x1,y1):
    norms = np.random.normal(size=(x1, y1))
    pyGraphics.surf2dArray(norms)

def camera(forward,right,up,pitch,roll):
    pyGraphics.setMoveCamera(forward,right,up)
    pyGraphics.setPitchCamera(pitch)
    pyGraphics.setRollCamera(roll)

def checked():
    x1 = window.xspin.value()
    y1 = window.yspin.value()
    forward = window.forward.value()
    right = window.right.value()
    up = window.up.value()
    pitch = window.pitch.value()
    roll = window.roll.value()
    camera(forward,right,up,pitch,roll)
    text = str(window.graphictype.currentText())
    if text == "2D Land":
        arr2D(x1,y1)
    elif text == "2D Surf":
        arrSurf(x1,y1)

app = 0

loader = QUiLoader()
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)
else:
    app = QtWidgets.QApplication.instance()
window = loader.load("PyGraphicsGen.ui", None)
window.Generate.clicked.connect(checked)



window.show()
app.exec()




