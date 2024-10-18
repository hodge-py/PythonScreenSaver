import numpy as np
from mayavi.mlab import *
from mayavi import mlab
from PIL import Image
import random

class PyGraphicsGen:

    def __init__(self):
        pass


    def Array2dLand(self,size=(20,20),background=(0,0,0),screenshot=True,mode='rgb',anti=True,showfig=True):
        fig = mlab.figure(1,bgcolor=background)
        norm = np.random.normal(size=size)
        imshow(norm,colormap='gist_earth')

        if screenshot == True and mode == 'rgba':
            screen = mlab.screenshot(figure=fig,mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen * 255))
            screen.save(f"test{random.randint(0,10000)}.png")
        elif screenshot == True and mode == 'rgb':
            screen = mlab.screenshot(figure=fig, mode=mode,antialiased=anti)
            screen = Image.fromarray(np.uint8(screen))
            screen.save(f"test{random.randint(0, 10000)}.png")
        if showfig:
            mlab.show()


host = PyGraphicsGen()

test = host.Array2dLand()





