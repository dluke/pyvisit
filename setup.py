from visit import *

import step
global tt 
def setup(db='*.cfd database'):
    print 'Restoring expressions using a visit session'
    RestoreSession("~/sessions/visit_setup.session", 0)
    print 'opening *.cfd database in current directory'
    OpenDatabase('*.cfd database')
    print "Use 'tt' variable to control time"
    tt = step.Step()
    return tt
