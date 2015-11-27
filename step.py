from visit import *

import time
import export

# Turn saving on or off globally
save = True

# 'Basic save options'
# SaveWindow and SaveWindowAttributes save the image as presented on the screen
#swatts = SaveWindowAttributes()

# Plot data can also be exported to a new database
#http://www.visitusers.org/index.php?title=Exporting_databases

# Might want to save a whole bunch of plot databases for one *.cfd database


#def step(st=1):
    #TimeSliderNextState()

#def setn(n):
    #TimeSliderSetState(n)

#def stepall(stepvar='time', record=None):
    ## good, now save the states so I can play them back 
    ## Want to be able to easily recreate a movie from any angle
    #exp = export.Exporter(record) if record else None
    #for i in range(TimeSliderGetNStates()):
        #step()
        #if exp and save:
            #exp.save()


class Step(object):
    def __init__(self, stepvar='time', record=None, start=0):
        # visit stores the names of time sliders as strings (path to database)
        # Should ideally take control of this string as soon as database is opened
        self.Ts = GetActiveTimeSlider()
        self.stepvar = stepvar
        self.start =start
        # current state variable
        self.i = start
        self.st = 1
        # Give the Step object an Exporter object called exp for saving
        self.record = record
        self.exp = None
        self.tosave = False
        if record:
            self.exp = export.Exporter(record) 
            self.tosave = True

    def setup_save(self, record):
        self.record = record
        self.exp = export.Exporter(record)
        self.tosave = True

    def save(self):
        self.exp.save(self.i)

    def reset(self):
        self.i = self.start
        TimeSliderSetState(self.i)

    def step(self):
        # Step forward by the value in st
        self.i += self.st
        TimeSliderSetState(self.i)
        if self.tosave:
            self.save()

    def setat(self,n):
        self.i = n
        TimeSliderSetState(n)
        if self.tosave:
            self.save()


    def loopon(self, rrange, rate=0):
        # set rate to a value in seconds to pause for that long between steps
        for i in rrange:
            self.setat(i)
            if rate:
               time.sleep(rate) 

    def loopall(self, rate=0):
        for i in range(TimeSliderGetNStates()):
            self.step
        
    def help(self):
        print "tt.step() #step forward by tt.st variable"
        print "tt.loopon(range) #step through a list of states"

