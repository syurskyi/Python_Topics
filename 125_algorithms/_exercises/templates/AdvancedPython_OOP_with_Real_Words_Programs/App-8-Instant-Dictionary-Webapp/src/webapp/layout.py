_____ justpy as jp

c_ DefaultLayout(jp.QLayout):

    ___  -    view="hHh lpR fFf", **kwargs):
        super(). - (view=view, **kwargs)

        header = jp.QHeader(a=self)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=self, show_if_above=True, v_mode="left",
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        qlist = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        jp.Br(a=qlist)

        jp.QBtn(a=toolbar, dense=True, flat=True, r__=True, icon="menu",
                click=move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    ___ move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True
