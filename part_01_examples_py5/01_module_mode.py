# module mode example

import py5

def setup():
    py5.size(300, 200)

def draw():
    py5.fill('#F00')
    py5.circle(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()

