import nuke

s = 'c:/temp/script.nk'
nuke.scriptSaveAs(s)
nuke.scriptClear()
nuke.scriptOpen(s)
nuke.scriptReadFile(s)
nuke.scriptSource(s)
nuke.scriptReadText()

nuke.script_directory()
nuke.scriptSaveandClear(s,False)
