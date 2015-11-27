# The streamline plots for initial flux 'tubes' for ltp 0.7

# Streamlines have a lot of attributes

AddPlot("Streamline", "B", 1, 0)
SetActivePlots(0)

# Set attributes
StreamlineAtts = StreamlineAttributes()
# Specifying a circle here
StreamlineAtts.sourceType = StreamlineAtts.SpecifiedCircle  # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
StreamlineAtts.pointSource = (0, 0, 0)
StreamlineAtts.lineStart = (0, 0, 0)
StreamlineAtts.lineEnd = (1, 0, 0)
# These 4 attrs describe the circle
StreamlineAtts.planeOrigin = (1, 1, -24)
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
# Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, ColorByVariable, ColorByCorrelationDistance
StreamlineAtts.coloringMethod = StreamlineAtts.ColorByTime  
# Rest are all defaults
StreamlineAtts.colorTableName = "Default"
StreamlineAtts.singleColor = (0, 0, 0, 255)
StreamlineAtts.legendFlag = 1
StreamlineAtts.lightingFlag = 1
StreamlineAtts.integrationDirection = StreamlineAtts.Forward  # Forward, Backward, Both
StreamlineAtts.maxSteps = 1000
StreamlineAtts.terminateByDistance = 0
StreamlineAtts.termDistance = 10
StreamlineAtts.terminateByTime = 0
StreamlineAtts.termTime = 10
StreamlineAtts.maxStepLength = 0.1
StreamlineAtts.limitMaximumTimestep = 0
StreamlineAtts.maxTimeStep = 0.1
StreamlineAtts.relTol = 0.0001
StreamlineAtts.absTolSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.absTolAbsolute = 1e-06
StreamlineAtts.absTolBBox = 1e-06
StreamlineAtts.fieldType = StreamlineAtts.Default  # Default, FlashField, M3DC12DField, M3DC13DField, Nek5000Field, NIMRODField
StreamlineAtts.fieldConstant = 1
StreamlineAtts.velocitySource = (0, 0, 0)
StreamlineAtts.integrationType = StreamlineAtts.DormandPrince  # Euler, Leapfrog, DormandPrince, AdamsBashforth, RK4, M3DC12DIntegrator
StreamlineAtts.parallelizationAlgorithmType = StreamlineAtts.VisItSelects  # LoadOnDemand, ParallelStaticDomains, MasterSlave, VisItSelects
StreamlineAtts.maxProcessCount = 10
StreamlineAtts.maxDomainCacheSize = 3
StreamlineAtts.workGroupSize = 32
StreamlineAtts.pathlines = 0
StreamlineAtts.pathlinesOverrideStartingTimeFlag = 0
StreamlineAtts.pathlinesOverrideStartingTime = 0
StreamlineAtts.pathlinesPeriod = 0
StreamlineAtts.pathlinesCMFE = StreamlineAtts.POS_CMFE  # CONN_CMFE, POS_CMFE
StreamlineAtts.coordinateSystem = StreamlineAtts.AsIs  # AsIs, CylindricalToCartesian, CartesianToCylindrical
StreamlineAtts.phiScalingFlag = 0
StreamlineAtts.phiScaling = 1
StreamlineAtts.coloringVariable = ""
StreamlineAtts.legendMinFlag = 0
StreamlineAtts.legendMaxFlag = 0
StreamlineAtts.legendMin = 0
StreamlineAtts.legendMax = 1
StreamlineAtts.displayBegin = 0
StreamlineAtts.displayEnd = 1
StreamlineAtts.displayBeginFlag = 0
StreamlineAtts.displayEndFlag = 0
StreamlineAtts.referenceTypeForDisplay = StreamlineAtts.Distance  # Distance, Time, Step
StreamlineAtts.displayMethod = StreamlineAtts.Lines  # Lines, Tubes, Ribbons
StreamlineAtts.tubeSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.tubeRadiusAbsolute = 0.125
StreamlineAtts.tubeRadiusBBox = 0.005
StreamlineAtts.ribbonWidthSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.ribbonWidthAbsolute = 0.125
StreamlineAtts.ribbonWidthBBox = 0.01
StreamlineAtts.lineWidth = 2
# I set this from 1 to 0
StreamlineAtts.showSeeds = 0
StreamlineAtts.seedRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.seedRadiusAbsolute = 1
StreamlineAtts.seedRadiusBBox = 0.015
StreamlineAtts.showHeads = 0
StreamlineAtts.headDisplayType = StreamlineAtts.Sphere  # Sphere, Cone
StreamlineAtts.headRadiusSizeType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.headRadiusAbsolute = 0.25
StreamlineAtts.headRadiusBBox = 0.02
StreamlineAtts.headHeightRatio = 2
StreamlineAtts.opacityType = StreamlineAtts.FullyOpaque  # FullyOpaque, Constant, Ramp, VariableRange
StreamlineAtts.opacityVariable = ""
StreamlineAtts.opacity = 1
StreamlineAtts.opacityVarMin = 0
StreamlineAtts.opacityVarMax = 1
StreamlineAtts.opacityVarMinFlag = 0
StreamlineAtts.opacityVarMaxFlag = 0
StreamlineAtts.tubeDisplayDensity = 10
StreamlineAtts.geomDisplayQuality = StreamlineAtts.Medium  # Low, Medium, High, Super
StreamlineAtts.sampleDistance0 = 10
StreamlineAtts.sampleDistance1 = 10
StreamlineAtts.sampleDistance2 = 10
StreamlineAtts.fillInterior = 0
StreamlineAtts.randomSamples = 0
StreamlineAtts.randomSeed = 0
StreamlineAtts.numberOfRandomSamples = 1
StreamlineAtts.forceNodeCenteredData = 0
StreamlineAtts.issueTerminationWarnings = 1
StreamlineAtts.issueStiffnessWarnings = 1
StreamlineAtts.issueCriticalPointsWarnings = 1
StreamlineAtts.criticalPointThreshold = 0.001
StreamlineAtts.varyTubeRadius = StreamlineAtts.None  # None, Scalar
StreamlineAtts.varyTubeRadiusFactor = 10
StreamlineAtts.varyTubeRadiusVariable = ""
StreamlineAtts.correlationDistanceAngTol = 5
StreamlineAtts.correlationDistanceMinDistAbsolute = 1
StreamlineAtts.correlationDistanceMinDistBBox = 0.005
StreamlineAtts.correlationDistanceMinDistType = StreamlineAtts.FractionOfBBox  # Absolute, FractionOfBBox
StreamlineAtts.selection = ""
SetPlotOptions(StreamlineAtts)

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


