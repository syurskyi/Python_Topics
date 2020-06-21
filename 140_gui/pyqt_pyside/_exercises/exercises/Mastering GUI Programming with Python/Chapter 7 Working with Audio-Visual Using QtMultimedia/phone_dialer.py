______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?C.. __ qtc
____ ? ______ ?M.. __ qtmm

______ resources


c_ SoundButton ?.?PB..

    ___  -   wav_fil, $ $$
        s_. - $ $$
        wav_file _ wav_file
        player _ ?.?SE..
        ?.sS.. ?.?U...fLF.. w..
        c__.c.. p__.p..


c_ MainWindow ?.?MW..

    ___  -
        """MainWindow constructor.

        This widget will be our main window.
        We'll define all the UI components in here.
        """
        s_. -
        # Main UI code goes here
        dialpad _ ?.?W..
        sCW.. ?
        ?.sL.. ?.?GL..

        ___ i symbol __ en.. '123456789*0#'
            button _ ? _*:/dtmf/{symbol}.wav s..
            row _ ? // 3
            column _ ? % 3
            d__.la__ .aW.. ? ? ?

        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A.. ___.a..
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw _ ?
    ___.e.. ?.e..
