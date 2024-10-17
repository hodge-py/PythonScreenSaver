import numpy as np
from mayavi.mlab import *
from mayavi import mlab

norm = np.random.normal(size=(20,20))
surf(norm,colormap='gist_earth')

mlab.show()