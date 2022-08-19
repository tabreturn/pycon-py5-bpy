# svg example

size(400, 400)
random_seed(123)

begin_record(SVG, 'fxape.svg')
stroke_weight(3)
# face
no_fill()
circle(width/2, height/2, 300)
#eyes
circle(160, 150, random(50, 150))
circle(width-160, 150, random(50, 150))
end_record()

'''
import vpype_cli
vpype_cli.execute('read fxape.svg write --pen-up penup.svg')
vpype_cli.execute('read fxape.svg linesort write --pen-up penup+linesort.svg')
import os
os.system(
    'vpype read penup+linesort.svg occult -i write penup+linesort+occult.svg')
'''
