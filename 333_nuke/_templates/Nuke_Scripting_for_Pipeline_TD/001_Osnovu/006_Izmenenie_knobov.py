_____ ?


# navernoe eto rabotaet tol'ko dlja MultiScriptEditor, no esli nody zafryzit'  v pamjat to pojavljaetsja
# vozmoznost' avtomaticheskogo pojavlenie dostypnuh knobov
n = ?.selectedNode()
n['saturation'].getValue()
n['saturation'].setValue(3)

n['channels'].setValue('rgba')

f = ?.toNode('Read1')
f['file'].getValue()
f['file'].evaluate()

n = ?.toNode("ColorCorrect2")
n['gamma'].setValue([1,2,3,1])