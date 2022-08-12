# inspired by @yuruyurau

size(420*4, 297*4, SVG, '06_multicolor_plot.svg')
#os_noise_seed(12345 * 42)
#random_seed(54321 * 42)

time = random(123456789)
diameter = height * 0.9
resolution = 300
xy_range = np.linspace(-1, 1, resolution)

background(0)
no_fill()
translate(width/2, height/2)
rotate(random(PI))

# you could employ xml.etree to separate colors (pens) onto different layers
# https://github.com/tabreturn/cc-fest-plotter/blob/main/tasks/02-py5_svg.py
bands = [
  '#B85', '#B85', '#B85', '#B85', '#B85',  # bronze
  '#CC0', '#CC0', '#CC0',  # gold
  '#FFF', '#FFF',  # white
  '#999', '#999',  # silver
  '#A00',  # red
  '#000', '#000'  # black (none)
]

select = 0
jitter = 0

for y in xy_range:
    
    if random() > 0.8: select = int(random(len(bands)))
    if select == '#000':
        no_stroke()
    else:
        stroke(bands[select])

    jitter += 0.25
    if random() > 0.8: jitter = 0
    
    begin_shape()
    
    for x in xy_range:     
        n = os_noise(time+x, x+y, time+y*3)
        n = remap(n, -1, 1, 0, 1)
        n = 3*n if n >.5 else 1.4
        d = x*x + y*y + n
        xco, yco = x/d*diameter, diameter*y/d
        j = random(jitter)
        vertex(xco, yco+j)

    end_shape()

exit_sketch()
