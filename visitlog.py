# Visit 2.9.2 log file
ScriptVersion = "2.9.2"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
