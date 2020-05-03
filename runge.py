import numpy as np
from bpy import context, data, ops

def runge1(x):
    return 1 / (1 + 10*x**2)

x = np.linspace(-1,1,20)	

ops.curve.primitive_bezier_curve_add(enter_editmode=True)
ops.curve.subdivide(number_cuts=18)

curve = context.active_object

bz_pts = curve.data.splines[0].bezier_points

len(bz_pts)
#20

for i in range(0,20):
	bz_pts[i].co = Vector((x[i], runge1(x[i]), 0.0))
	bz_pts[i].handle_left = Vector((x[i], runge1(x[i]), 0.0))
	bz_pts[i].handle_right = Vector((x[i], runge1(x[i]), 0.0))

ops.object.mode_set(mode='OBJECT')
obj_data = context.active_object.data
obj_data.fill_mode = 'FULL'
obj_data.extrude = 0.125
obj_data.bevel_depth = 0.02