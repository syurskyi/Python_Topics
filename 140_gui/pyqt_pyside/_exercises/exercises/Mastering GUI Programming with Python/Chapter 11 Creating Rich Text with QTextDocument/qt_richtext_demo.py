______ ___
____ ? ______ ?W.. __ qtw
____ ? ______ ?G.. __ qtg
____ ? ______ ?C.. __ qtc


c_ MainWindow(qtw.?MW..):

    ___  -
        """MainWindow constructor."""
        s_. - ()
        # Main UI code goes here
        main _ qtw.QTextBrowser(minimumWidth_800, minimumHeight_600)
        sCW..(main)

        # Must come before the HTML is inserted
        main.document().setDefaultStyleSheet(
            'body {color: #333; font-size: 14px;} '
            'h2 {background: #CCF; color: #443;} '
            'h1 {background: #001133; color: white;} '
        )

        # TextBrowser background is a widget style, not a document style
        main.sSS..('background-color: #EEF;')
        w__ o..('fight_fighter2.html', 'r') __ fh:
            main.insertHtml(fh.r..

        main.setOpenExternalLinks( st.

        # End main UI code
        s..


__ ______ __ ______
    app _ qtw.?A..(___.a..
    mw _ MainWindow()
    ___.e.. ?.e..
