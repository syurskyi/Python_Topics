_____ ?
_____ revealInFinder

node_classes = ["Read", "Write", "Camera", "Camera2", "ReadGeo", "ReadGeo2", "WriteGeo"]

___ node __ node_classes:
    ?.addOnUserCreate(revealInFinder.add_reveal_button, nodeClass=node)
    ?.addKnobChanged(revealInFinder.reveal_in_finder, nodeClass=node)
