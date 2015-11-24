# Add vector plot
AddPlot("Vector", "Bxy", 1, 0)
# Add threshold operator
AddOperator("Threshold", 0)
#
SetActivePlots(0)

# Set threshold attributes
ThresholdAtts = ThresholdAttributes()
ThresholdAtts.outputMeshType = 0
# MagxyB is our variable
ThresholdAtts.listedVarNames = ("magxyB")
ThresholdAtts.zonePortions = (1)
# lower bound of 0.3, 1e+37 represents max
ThresholdAtts.lowerBounds = (0.3)
ThresholdAtts.upperBounds = (1e+37)
ThresholdAtts.defaultVarName = "Bxy"
ThresholdAtts.defaultVarIsScalar = 0
SetOperatorOptions(ThresholdAtts, 0)

# Set the vector plot attributes
# I only changed nVectors = 1000, so the rest are defaults.
VectorAtts = VectorAttributes()
VectorAtts.glyphLocation = VectorAtts.AdaptsToMeshResolution  # AdaptsToMeshResolution, UniformInSpace
VectorAtts.useStride = 0
VectorAtts.stride = 1
VectorAtts.nVectors = 1000
VectorAtts.lineStyle = VectorAtts.SOLID  # SOLID, DASH, DOT, DOTDASH
VectorAtts.lineWidth = 0
VectorAtts.scale = 0.25
VectorAtts.scaleByMagnitude = 1
VectorAtts.autoScale = 1
VectorAtts.headSize = 0.25
VectorAtts.headOn = 1
VectorAtts.colorByMag = 1
VectorAtts.useLegend = 1
VectorAtts.vectorColor = (0, 0, 0, 255)
VectorAtts.colorTableName = "Default"
VectorAtts.invertColorTable = 0
VectorAtts.vectorOrigin = VectorAtts.Tail  # Head, Middle, Tail
VectorAtts.minFlag = 0
VectorAtts.maxFlag = 0
VectorAtts.limitsMode = VectorAtts.OriginalData  # OriginalData, CurrentPlot
VectorAtts.min = 0
VectorAtts.max = 1
VectorAtts.lineStem = VectorAtts.Line  # Cylinder, Line
VectorAtts.geometryQuality = VectorAtts.Fast  # Fast, High
VectorAtts.stemWidth = 0.08
VectorAtts.origOnly = 1
VectorAtts.glyphType = VectorAtts.Arrow  # Arrow, Ellipsoid
SetPlotOptions(VectorAtts)
# Draw Button
DrawPlots()

# This is a mouse drag on the 3D plot in the active window
# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.24451, -0.832759, 0.496716)
View3DAtts.focus = (0, 0, 0)
View3DAtts.viewUp = (-0.0863167, 0.528924, 0.844268)
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

