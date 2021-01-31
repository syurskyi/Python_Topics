?.Undo.begin('My Script')
___ i __ ra..(15):
    ?.cN..('Blur', __.._F..)
?.Undo.end()

?.Undo.begin('My Script1')
___ i __ ra..(15):
    ?.n__.Blur()
?.Undo.end()

undo _ ?.Undo()
undo.begin('My Action')
___ i __ ra..(15):
    ?.n__.Blur()
undo.end()
undo.undo()
#nuke.undo()
undo.redo()

with ?.Undo
    ___ i __ ra..(15):
        ?.n__.Blur()