import numpy as np
from mayavi.mlab import *
from mayavi import mlab
from PIL import Image
import random
import PyQt5

class PyGraphicsGen:

    def __init__(self):
        pass


    def array2dLand(self,data,background=(0,0,0),screenshot=True,mode='rgba',anti=True,showfig=True):
        fig = mlab.figure(1,bgcolor=background)
        norm = data
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


    def surf2dArray(self,data,background=(0,0,0),screenshot=True,mode='rgba',anti=True,showfig=True):
        fig = mlab.figure(1, bgcolor=background)
        norm = data
        surf(norm, colormap='gist_earth')

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


        def array2dLandAnim(self):
            pass

        def surf2dLArray(self):
            pass


