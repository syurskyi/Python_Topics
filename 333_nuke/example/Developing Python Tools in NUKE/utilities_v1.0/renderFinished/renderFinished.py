import nuke
import PySide.QtGui
import os



"""
this module contains functionality of notifying the user when a render is finished.
This is done by playing a sound and showing a notification window.
"""


# renderFinished settings
################################################################################

# show_notification: if True show message 'render finished' when render is done
show_notification = True

# play_sound: if True play a sound when render is done
play_sound = True

# sound_file: path of sound file
sound_file = "{}/01.wav".format(os.path.dirname(__file__))

################################################################################


def notify_user():
    """
    play a sound and show a notification when render is finished
    :return: None
    """

    if play_sound:
        PySide.QtGui.QSound.play(sound_file)
    if show_notification:
        nuke.message("Finished rendering")
