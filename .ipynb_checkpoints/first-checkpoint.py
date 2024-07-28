import cadquery as cq

height = 54
width = 84
thickness = 0.8

result = cq.Workplane("XY").box(height, width, thickness)

cq.show_object(result)

