# python pdb debugger example

import pdb

x = 0

def draw():
    global x
    circle(x, height/2, 10)
    x += 10
    pdb.set_trace()

