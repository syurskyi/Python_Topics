# """Memento pattern
# """
#
#
# c_ Originator o...
#     """Originator is some object that has an internal state.
#     The Originator knows how to save and restore itself, but it's the Caretaker
#     than controls when to save and restore the Originator."""
#
#     ___ -
#         _state _ N..
#
#     ??
#     ___ state
#         r_ _?
#
#     ??.?
#     ___ state new_state
#         _s.. _ ?
#
#     ___ save
#         """Create a Memento and copy the Originator state in it."""
#         r_ M.. s..
#
#     ___ restore memento
#         """Restore the Originator to a previous state (stored in Memento)."""
#         state _ m__.s..
#
#
# c_ Memento o...
#     """Memento is an opaque object that holds the state of an Originator."""
#
#     ___ - state
#         _?  ?
#
#     ??
#     ___ state
#         r_ _?
#
#
# # Client, the Caretaker of the Memento pattern.
# # The Caretaker is going to do something to the Originator, but wants to be
# # able to undo the change.
# # The Caretaker holds the Memento but cannot change it (Memento is opaque).
# # The Caretaker knows when to save and when to restore the Originator.
#
#
# ___ main
#     originator _ O..
#     ?.st.. _ "State1"
#     memento1 _ ?.s..
#     ?.st.. _ "State2"
#     memento2 _ ?.s..
#     ?.st.. _ "State3"
#     ?.st.. _ "State4"
#
#     ?.re.. m_1
#     ass.. ?.st.. __ "State1"
#     print ?.st..
#
#     ?.restore m_2
#     ass.. ?.st.. __ "State2"
#     print ?.st..
#
#
# __ _______ __ ______
#     ?
