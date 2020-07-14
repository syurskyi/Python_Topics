import nuke

nuke.scriptSaveAs('c:/script.nk')
nuke.scriptClear()
nuke.scriptOpen('c:/script.nk')
nuke.scriptReadFile('c:/script.nk') # same nuke.scriptSource
nuke.scriptReadText('text')
nuke.load('c:/script.nk')

nuke.script_directory()

nuke.scriptSaveAndClear()