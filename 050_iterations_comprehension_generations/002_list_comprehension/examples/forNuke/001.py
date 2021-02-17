nSet = nuke.allNodes('Read')

[(i['first'].setExpression('test'), i['last'].setExpression('test')) for i in nSet]