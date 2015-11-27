# this module represents a set of streamline plots (flux tubes) directly
# Generalise this by using objects  

# Use this session to store all the expressions
# As well as anything else that is separate from data
#RestoreSession("~/sessions/visit_setup.session", 0)

# Try and open a database, plot something, draw and display
#OpenDatabase('*.cfd database')

# Visit sets the attributes for the active plots
# have to set active plot every time we change attributes

from visit import *
from nav import *

# Configure
density = 6
radius = 0.6

## The tools for plotting flux tubes
plots = {}

# four streamline plots with pinch configuration
pinch = 0.7
def update_pinch(pinch):
    global fixed_points
    # Anticlockwise from top right
    fixed_points = [(1,1), (-pinch, pinch), (-1,-1), (pinch ,-pinch)]
update_pinch(pinch)

# tube colors
# 4th number is opacity?
cyan = (75, 224, 235, 255)
green = (144, 235, 75, 255)
red = (235, 86, 75)
purple = (170, 88, 232)
full = (255, 0, 0, 255)
clist = [cyan, green, red, purple]

## Manage tube variables

def set_attr(plot, attr, value):
    # Deal with the attributes of one plot at a time
    SetActivePlots(plot)
    Atts = GetPlotOptions()
    setattr(Atts, attr, value)
    SetPlotOptions(Atts)

class FluxTube(object):

    colorstyles = ['default', 'magBxy', 'tubes']

    def __init__(self, xy, color, density=density, radius=radius, z=-24):
        # plot if the visit plot identifier
        AddPlot("Streamline", "B", 1, 0)
        self.plot = GetNumPlots() -1 

        # define proxies
        self.z = z
        self._xy = xy
        self._color = color
        self._density = density
        self._radius = radius
        # coloring mode is initialised in another call
        self._colorstyle= 'default'


        # The Atts object is very important
        # All the other instance variables are just proxies for Atts fields
        SetActivePlots(self.plot)
        # Store this as instance only for access to constants
        self.Atts = GetPlotOptions()
        Atts = self.Atts

        # Set attributes
        # Specifying a circle here
        Atts.sourceType = Atts.SpecifiedCircle  
        # SpecifiedPoint, SpecifiedPointList, SpecifiedLine, SpecifiedCircle, SpecifiedPlane, SpecifiedSphere, SpecifiedBox, Selection
        Atts.pointSource = (0, 0, 0)
        Atts.lineStart = (0, 0, 0)
        Atts.lineEnd = (1, 0, 0)
        # These 4 attrs describe the circle
        x,y, = xy
        Atts.planeOrigin = (x, y, self.z)
        Atts.planeNormal = (0, 0, 1)
        Atts.planeUpAxis = (0, 1, 0)
        Atts.radius = radius
        # Not sure about this one
        Atts.pointList = (0, 0, 0, 1, 0, 0, 0, 1, 0)
        # Sample density, ie. number of sample around circle boundary is 8
        Atts.sampleDensity0 = density
        Atts.sampleDensity1 = 2
        Atts.sampleDensity2 = 2
        # Coloring method should be useful - i.e color by magBxy is possible?
        #Solid, ColorBySpeed, ColorByVorticity, ColorByLength, ColorByTime, ColorBySeedPointID, 
        #ColorByVariable, ColorByCorrelationDistance
        Atts.coloringMethod = Atts.ColorByTime
        Atts.colorTableName = "Default"
        Atts.singleColor = color
        # I set this from 1 to 0
        Atts.showSeeds = 0

        SetPlotOptions(Atts)


    def attr(self, attr, val):
        set_attr(self.plot, attr, val)
    @property
    def density(self): return self._density
    @density.setter
    def density(self, dens):
        self._density = dens
        set_attr(self.plot, 'sampleDensity0', dens)

    @property
    def radius(self): return self._radius
    @radius.setter
    def radius(self, rad):
        self._radius = rad
        set_attr(self.plot, 'radius', rad)

    @property
    def xy(self): return self._xy
    @xy.setter
    def xy(self, v):
        self._xy = v
        x, y = v
        set_attr(self.plot, 'planeOrigin', (x,y,self.z))

    @property
    def color(self): return self_color
    @color.setter
    def color(self, c):
        self._color = c
        set_attr(self.plot, 'singleColor', c)

    @property
    def colorstyle(self):
        return self._colorstyle
    @colorstyle.setter
    def colorstyle(self, style):
        self._colorstyle= style
        if style is 'default':
            set_attr(self.plot, 'coloringMethod', self.Atts.ColorByTime)
        elif style is 'magBxy':
            set_attr(self.plot, 'coloringMethod', self.Atts.ColorByVariable)
            self.attr('colorTableName', 'Default')
            self.attr('coloringVariable', 'magBxy')
        elif style is 'tubes':
            self.attr('coloringMethod', self.Atts.Solid)


plots = []
# setup 4 plots for a list of points
def setup_tubes(fixed):
    for i, fp in enumerate(fixed):
        FT = FluxTube(fp, clist[i])
        FT.colorstyle = 'tubes'
        plots.append(FT)

# Control functions 
def plot():
    setup_tubes(fixed_points)
    # draw
    DrawPlots()
    orient()


