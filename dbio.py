#
#RestoreSession("~/sessions/visit_setup.session", 0)
#OpenDatabase('*.cfd database')



# Want to be able to open new data in new windows
# As well as reopen a plot databases in new windows

# plot_dir
from export import plot_dir
import os
def oplot(record):
    record = os.path.join(plot_dir, record)
    db = os.path.join(record, '*.vtk database')
   


