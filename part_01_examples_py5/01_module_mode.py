# module mode example

import py5

def fxrand():
    py5.random_seed(123)

def setup():
    py5.size(400, 400)
    fxrand()
    py5.no_loop()

def draw():
    py5.stroke_weight(3)
    # some different ways to specify a red fill
    py5.fill(255, 0, 0)    # rgb value for red
    py5.fill('#FF0000')    # hex value for red
    py5.fill('#F00')       # shorthand hex value for red
    py5.color_mode(py5.HSB, 360, 100, 100)
    py5.fill(0, 100, 100)  # hsb value for red
    # face
    py5.circle(py5.width/2, py5.height/2, 300)
    #eyes
    py5.circle(160, 150, py5.random(50, 150))
    py5.circle(py5.width-160, 150, py5.random(50, 150))

py5.run_sketch()
