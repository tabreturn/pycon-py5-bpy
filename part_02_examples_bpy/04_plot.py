import bpy  # install "fake-bpy-module" for external editor
from math import sin, tau

# clear meshes in the scene
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        bpy.data.objects.remove(obj)

# animation variables
total_frames = 150
theta = 0.0

# define a one hundred frame timeline
bpy.context.scene.frame_end = total_frames
bpy.context.scene.frame_start = 0

for x in range(15):
    # generate a grid of cones
    for y in range(15):
        cone = bpy.ops.mesh.primitive_monkey_add()
        cone = bpy.context.object
        cone.name = 'Cone-{}-{}'.format(x, y)
        cone.location[0] = x * 2
        cone.location[1] = y * 2
        # add keyframes to each cone
        for frame in range(0, total_frames):
            bpy.context.scene.frame_set(frame)
            cone.location.z = sin(theta + x) * 2 - 1
            cone.keyframe_insert(data_path='location')
            scale = sin(theta + y)
            cone.scale = (scale, scale, scale)
            cone.keyframe_insert(data_path='scale')
            theta += tau / total_frames


import pathlib
output = pathlib.Path().resolve() / 'render.png'
bpy.context.scene.render.filepath = str(output)
bpy.ops.render.render(write_still=True)

# run: blender --background --python 03_external_editor.py
# for sequence, run: bpy.ops.render.render(animation=True, write_still=True)
# note that blender uses it's own python env (which does include pip)

# STEP 1: SETUP THE BLENDER FILE ==============================================

# 1. open blender and save the project as ~/<proj>/setup.blend
# 2. install freestyle (edit > preferences > add-ons > freestyle svg exporter)
# 3. properties panel > render properties > enable "freestyle svg export"
# 4. properties panel > render properties > enable "freestyle"
# 5. properties panel > output properties > output path of ~/<proj>/render.svg
# 6. test the render (render > render image)
# 7. delete the cube and save
# more freestyle options: properties panel > layer properties > freestyle ...)

# run: blender scene.blend --background --python 04_plot.py

# STEP 2: CLEANING UP WITH VPYPE ==============================================

# from here, one might clean up the plot with vpype filter & linemerge
# e.g. vpype read render.svg filter -m 50 linemerge -t 50 write out.svg
