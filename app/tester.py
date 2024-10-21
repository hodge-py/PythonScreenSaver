from main import PyGraphicsGen
import numpy as np

host2 = PyGraphicsGen()

data = np.random.normal(size=(20,20))

#data = np.random.random((20,20))
host2.setMoveCamera(10,0,0)
host2.setPitchCamera(10)
host2.setRollCamera(10)

host2.array2dLand(data,mode='rgb')

#host2.surf2dArray(data)