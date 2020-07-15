import nuke


# navernoe eto rabotaet tol'ko dlja MultiScriptEditor, no esli nody zafryzit'  v pamjat to pojavljaetsja
# vozmoznost' avtomaticheskogo pojavlenie dostypnuh knobov
n = nuke.selectedNode()
n['saturation'].getValue()
n['saturation'].setValue(3)

n['channels'].setValue('rgba')

f = nuke.toNode('Read1')
f['file'].getValue()
f['file'].evaluate()

n = nuke.toNode("ColorCorrect2")
n['gamma'].setValue([1,2,3,1])