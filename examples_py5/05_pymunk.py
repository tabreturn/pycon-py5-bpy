# pymunk example

import pymunk

# create a new space for your simulation
space = pymunk.Space()
space.gravity = (0, 900)

# create a valley-like floor
segment1 = pymunk.Segment(space.static_body, (0, 100), (250, 450), 5)
segment1.elasticity = 1
segment2 = pymunk.Segment(space.static_body, (500, 100), (250, 450), 5)
segment2.elasticity = 1
space.add(segment1, segment2)

# create a ball
body = pymunk.Body(mass=1, moment=10)
body.position = 90, 0
ball = pymunk.Circle(body, radius=10)
ball.elasticity = 0.85
space.add(body, ball)

def setup():
    size(500, 500)

def draw():
    background(150)

    # render all of the bodies
    stroke(255)
    stroke_weight(segment1.radius*2)
    line(segment1.a.x, segment1.a.y, segment1.b.x, segment1.b.y)
    line(segment2.a.x, segment2.a.y, segment2.b.x, segment2.b.y)
    no_stroke()
    circle(ball.body.position.x, ball.body.position.y, ball.radius*2)

    # advance the simulation one step
    space.step(1/get_frame_rate())

