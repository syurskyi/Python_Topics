____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.?M.. ______ *
____ ?.?MW.. ______ *

____ MainWindow ______ Ui_MainWindow

____ sqlalchemy ______ Column, ForeignKey, Integer, String
____ sqlalchemy.ext.declarative ______ declarative_base
____ sqlalchemy.orm ______ sessionmaker
____ sqlalchemy ______ create_engine

Base _ declarative_base()

c_ Note(Base):
    __tablename__ _ 'note'
    id _ Column(Integer, primary_key_ st.
    t__ _ Column(String(1000), nullable_False)
    x _ Column(Integer, nullable_False, default_0)
    y _ Column(Integer, nullable_False, default_0)

engine _ create_engine('sqlite:///notes.db')
# Initalize the database if it is not already.
#if not engine.dialect.has_table(engine, "note"):
Base.metadata.create_all(engine)

# Create a session to handle updates.
Session _ sessionmaker(bind_engine)
session _ Session()

_ACTIVE_NOTES _   # dict

___ create_new_note
    MainWindow()

c_ MainWindow(?MW.., Ui_MainWindow):
    ___  -   $ obj_None, $$):
        s__(MainWindow, self). - ($ $$)
        setupUi
        setWindowFlags(windowFlags() | __.FramelessWindowHint | __.WindowStaysOnTopHint)
        s..

        # Load/save note data, store this notes db reference.
        __ obj:
            obj _ obj
            load()
        ____
            obj _ Note()
            save()

        closeButton.pressed.c..(delete_window)
        moreButton.pressed.c..(create_new_note)
        textEdit.tC...c..(save)

        # Flags to store dragged-dropped
        _drag_active _ F..

    ___ load
        move(obj.x, obj.y)
        textEdit.setHtml(obj.t__)
        _ACTIVE_NOTES[obj.id] _ self

    ___ save
        obj.x _ x()
        obj.y _ y()
        obj.t__ _ textEdit.toHtml()
        session.add(obj)
        session.c__
        _ACTIVE_NOTES[obj.id] _ self

    ___ mousePressEvent  e):
        previous_pos _ e.globalPos()

    ___ mouseMoveEvent  e):
        delta _ e.globalPos() - previous_pos
        move(x() + delta.x(), y()+delta.y())
        previous_pos _ e.globalPos()

        _drag_active _ T..

    ___ mouseReleaseEvent  e):
        __ _drag_active:
            save()
            _drag_active _ F..

    ___ delete_window
        result _ ?MB...q..  "Confirm delete", "Are you sure you want to delete this note?")
        __ result __ ?MB...Yes:
            session.delete(obj)
            session.c__
            c..


__ ______ __ ______
    app _ ?
    app.sAN..("Brown Note")
    app.sS..("Fusion")

    # Custom brown palette.
    palette _ ?P..()
    palette.sC..(?P...Window, ?C..(188,170,164))
    palette.sC..(?P...WindowText, ?C..(121,85,72))
    palette.sC..(?P...ButtonText, ?C..(121,85,72))
    palette.sC..(?P...Text, ?C..(121,85,72))
    palette.sC..(?P...Base, ?C..(188,170,164))
    palette.sC..(?P...AlternateBase, ?C..(188,170,164))
    app.sP..(palette)

    existing_notes _ session.query(Note).al.()
    __ le.(existing_notes) __ 0:
        MainWindow()
    ____
        ___ note __ existing_notes:
            MainWindow(obj_note)





    app.e..
