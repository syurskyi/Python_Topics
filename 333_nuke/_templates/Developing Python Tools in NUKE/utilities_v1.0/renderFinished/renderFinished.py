_____ ?
_____ PySide.QtGui
_____ __



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
sound_file = "{}/01.wav".f..(__.pa__.dirname(__file__))

################################################################################


___ notify_user
    """
    play a sound and show a notification when render is finished
    :return: None
    """

    __ play_sound:
        PySide.QtGui.QSound.play(sound_file)
    __ show_notification:
        ?.m__("Finished rendering")
