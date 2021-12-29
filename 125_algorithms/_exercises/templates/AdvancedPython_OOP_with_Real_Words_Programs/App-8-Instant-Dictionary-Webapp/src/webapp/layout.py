_____ justpy as jp

c_ DefaultLayout(jp.QLayout):

    ___  -    view"hHh lpR fFf", **kwargs):
        super(). - (viewview, **kwargs)

        header  jp.QHeader(aself)
        toolbar  jp.QToolbar(aheader)

        drawer  jp.QDrawer(aself, show_if_aboveTrue, v_mode"left",
                            borderedTrue)
        scroller  jp.QScrollArea(adrawer, classes"fit")
        qlist  jp.QList(ascroller)
        a_classes  "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(aqlist, text"Home", href"/", classesa_classes)
        jp.Br(aqlist)
        jp.A(aqlist, text"Dictionary", href"/dictionary", classesa_classes)
        jp.Br(aqlist)
        jp.A(aqlist, text"About", href"/about", classesa_classes)
        jp.Br(aqlist)

        jp.QBtn(atoolbar, denseTrue, flatTrue, r__True, icon"menu",
                clickmove_drawer, drawerdrawer)
        jp.QToolbarTitle(atoolbar, text"Instant Dictionary")

    @staticmethod
    ___ move_drawer(widget, msg):
        __ widget.drawer.value:
            widget.drawer.value  F..
        else:
            widget.drawer.value  T..
