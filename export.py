from visit import *
# Python for exporting plot databases
# Need to store all this analysis under a folder

import os

# Going to open visit in the Data directory for the time being
plot_dir = '../plots/'

def makedir(dname):
    if not os.path.exists(dname):
        os.makedirs(dname)
makedir(plot_dir)

def make_plotdir(dname):
    dname = os.path.join(plot_dir, dname)
    makedir(dname)

# Name the plots based on type

import glob
import re

# VTK looks like an all round good format
def uniquify(record):
    name = record
    dirs = glob.glob(os.path.join(plot_dir,'*'))
    exts =[]

    for d in dirs:
        # findall gives an empty list if it finds nothing
        # bad code - may fail for record names with numbers
        # todo
        named = re.findall(name+'_\d+', d)
        if named:  
            named = named[-1]
            extnum = re.findall('\d+', named)
            if extnum:
                extnum = extnum[-1]
                exts.append(int(extnum))
    if exts:
        new = max(exts) + 1
        record = record + '_' + str(new)
    else:
        record += '_0'
    return record



class Exporter(object):
    def __init__(self, record, ext='vtk'):
        # record is the name of the directory under ../plots/
        self.name = record
        # make record unique
        self.record = uniquify(record)
        self.savedir = os.path.join(plot_dir, self.record)
        self.savedir = os.path.abspath(self.savedir)
        print 'lets save to ', self.savedir
        makedir(self.savedir)

        # Fails to save anything and fails silently in CLI mode
        # "metadata server is not running". doesn't recognise 'VTK'
        # work around
        # I want to avoid using this database completely
        # Be careful about side effects of having this open
        OpenDatabase('~/visit/initial.vtk')

    def save(self, i): 
        #Export the database
        dbAtts = ExportDBAttributes()
        ext =  '_%04d' % i
        fname =  self.name + ext
        print 'save directory'
        print self.savedir
        dbAtts.dirname = self.savedir
        print 'filename'
        print fname
        dbAtts.filename = fname
        dbAtts.allTimes = 0
        dbAtts.db_type = "VTK"
        dbAtts.db_type_fullname = "VTK_1.0"
        # Tuple of variables to export. 
        # "default" means the plotted variable.
        dbAtts.variables = ("default")
        dbAtts.opts.types = (0, 0)
        dbAtts.opts.help = ""
        print 'export to ', dbAtts.filename
        ExportDatabase(dbAtts)

