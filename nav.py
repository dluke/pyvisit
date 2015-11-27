from visit import *
# Navigation commands
# Want a few good directions already specified here

# View
# Want to interact with the graphics window to add a time slider

def add_slider():
    slider = CreateAnnotationObject("TimeSlider")
    slider.height = 0.07


def orient():
    add_slider()
    # This is just a rotation
    # Begin spontaneous state
    View3DAtts = View3DAttributes()
    View3DAtts.viewNormal = (-0.538069, -0.490617, 0.685403)
    View3DAtts.focus = (0, 0, 0)
    View3DAtts.viewUp = (0.069032, 0.784767, 0.615935)
    View3DAtts.viewAngle = 30
    View3DAtts.parallelScale = 25.4558
    View3DAtts.nearPlane = -50.9117
    View3DAtts.farPlane = 50.9117
    View3DAtts.imagePan = (0, 0)
    View3DAtts.imageZoom = 1
    View3DAtts.perspective = 1
    View3DAtts.eyeAngle = 2
    View3DAtts.centerOfRotationSet = 0
    View3DAtts.centerOfRotation = (0, 0, 0)
    View3DAtts.axis3DScaleFlag = 0
    View3DAtts.axis3DScales = (1, 1, 1)
    View3DAtts.shear = (0, 0, 1)
    View3DAtts.windowValid = 1
    SetView3D(View3DAtts)
    # End spontaneous state

def normal(normal):
    VView3DAtts = View3DAttributes()
    View3DAtts.viewNormal = normal
    SetView3D(View3DAtts)
