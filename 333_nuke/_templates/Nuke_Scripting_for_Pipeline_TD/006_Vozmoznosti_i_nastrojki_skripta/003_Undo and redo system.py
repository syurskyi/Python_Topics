?.Undo.begin('My Script')
___ i __ ra..(15):
    ?.cN..('Blur', inpanel=False)
?.Undo.end()

?.Undo.begin('My Script1')
___ i __ ra..(15):
    ?.nodes.Blur()
?.Undo.end()

undo = ?.Undo()
undo.begin('My Action')
___ i __ ra..(15):
    ?.nodes.Blur()
undo.end()
undo.undo()
#nuke.undo()
undo.redo()

with ?.Undo
    ___ i __ ra..(15):
        ?.nodes.Blur()