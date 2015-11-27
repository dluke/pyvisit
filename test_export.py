

RestoreSession("~/sessions/visit_setup.session", 0)
#OpenDatabase('~/lare/braids/ltp_transition/ltp_0.7/Data/*.cfd database')
OpenDatabase('*.cfd database')
import tubes
tubes.plot()


ExportDBAtts = ExportDBAttributes()
ExportDBAtts.allTimes = 0
ExportDBAtts.db_type = "VTK"
ExportDBAtts.db_type_fullname = "VTK_1.0"
ExportDBAtts.filename = "initial"
ExportDBAtts.dirname = "/home/daniel/visit/test/"
ExportDBAtts.variables = ("default")
ExportDBAtts.opts.types = (0, 0)
ExportDBAtts.opts.help = ""
ExportDatabase(ExportDBAtts)

