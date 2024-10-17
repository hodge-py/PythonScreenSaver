import numpy as np
from mayavi.mlab import *
from mayavi import mlab

class PyGraphicsGen:

    def __init__(self):
        pass


    def TwoDArrIm(self,background=(.155,.25,.125)):
        mlab.figure(1,bgcolor=(background))
        norm = np.random.normal(size=(20,20))
        imshow(norm,colormap='gist_earth')

        mlab.savefig(filename='test.png')

        mlab.show()


host = PyGraphicsGen()

host.TwoDArrIm()