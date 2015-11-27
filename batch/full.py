# Try and open a database, plot something, draw and display

# Use this session to store all the expressions
# As well as anything else that is separate from data
RestoreSession("~/sessions/visit_setup.session", 0)

OpenDatabase('*.cfd database')

# Visit sets the attributes for the active plots
# have to set active plot every time we change attributes
# A two way dictionary might be ideal, I'll think I'll stick with a dict() for now
plots = {}


def set_fluxtube(plot, x, y):
    SetActivePlots(plot)
    StreamlineAtts = GetPlotOptions()

    # Set attributes
    # Specifying a circle here
    StreamlineAtts.sourceType = StreamlineAtts.SpecifiedCircle  
    # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
    StreamlineAtts.pointSource = (0, 0, 0)
    StreamlineAtts.lineStart = (0, 0, 0)
    StreamlineAtts.lineEnd = (1, 0, 0)
    # These 4 attrs describe the circle
    StreamlineAtts.planeOrigin = (x, y, -24)
    StreamlineAtts.planeNormal = (0, 0, 1)
    StreamlineAtts.planeUpAxis = (0, 1, 0)
    StreamlineAtts.radius = 0.7
    # 3 attrs not important
    StreamlineAtts.sphereOrigin = (0, 0, 0)
    StreamlineAtts.boxExtents = (0, 1, 0, 1, 0, 1)
    StreamlineAtts.useWholeBox = 1
    # Not sure about this one
    StreamlineAtts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
    # Sample density, ie. number of sample around circle boundary is 8
    StreamlineAtts.sampleDensity0 = 8
    StreamlineAtts.sampleDensity1 = 8
    StreamlineAtts.sampleDensity2 = 2
    # Coloring method should be useful - i.e color by magBxy is possible?
    #Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, ColorByCorrelationDistance
    StreamlineAtts.coloringMethod = StreamlineAtts.ColorByLength
    StreamlineAtts.colorTableName = "Default"
    StreamlineAtts.singleColor = (0, 0, 0, 255)

    # I set this from 1 to 0
    StreamlineAtts.showSeeds = 0
    SetPlotOptions(StreamlineAtts)

# four streamline plots 
AddPlot("Streamline", "B", 1, 0)
AddPlot("Streamline", "B", 1, 0)
AddPlot("Streamline", "B", 1, 0)
AddPlot("Streamline", "B", 1, 0)

pinch = 0.7
fixed_points = [(1,1), (-1,-1), (-pinch, pinch), (pinch ,-pinch)]
for i, fp in enumerate(fixed_points):
    x,y = fp
    set_fluxtube(i, x, y)

# draw
DrawPlots()

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


