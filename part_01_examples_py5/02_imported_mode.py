# imported mode example

def fxrand():
    random_seed(123)

def setup():
    size(400, 400)
    fxrand()
    no_loop()

def draw():
    stroke_weight(3)
    # face
    fill('#F00')
    circle(width/2, height/2, 300)
    #eyes
    circle(160, 150, random(50, 150))
    circle(width-160, 150, random(50, 150))
