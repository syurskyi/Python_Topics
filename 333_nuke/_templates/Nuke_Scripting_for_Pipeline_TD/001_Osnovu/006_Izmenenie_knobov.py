_____ ?


# navernoe eto rabotaet tol'ko dlja MultiScriptEditor, no esli nody zafryzit'  v pamjat to pojavljaetsja
# vozmoznost' avtomaticheskogo pojavlenie dostypnuh knobov
n = ?.selectedNode()
n['saturation'].gV..()
n['saturation'].sV..(3)

n['channels'].sV..('rgba')

f = ?.toNode('Read1')
f['file'].gV..()
f['file'].evaluate()

n = ?.toNode("ColorCorrect2")
n['gamma'].sV..([1,2,3,1])