____ ?.?G.. ______ *
____ ?.?W.. ______ *
____ ?.?C.. ______ *
____ ?.QtMultimedia ______ *
____ ?.QtMultimediaWidgets ______ *

____ MainWindow ______ Ui_MainWindow

____ sqlalchemy ______ Column, ForeignKey, Integer, String
____ sqlalchemy.ext.declarative ______ declarative_base
____ sqlalchemy.orm ______ sessionmaker
____ sqlalchemy ______ create_engine

Base _ declarative_base()

c_ Note(Base):
    __tablename__ _ 'note'
    id _ Column(Integer, primary_key_True)
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

_ACTIVE_NOTES _ {}

___ create_new_note
    MainWindow()

c_ MainWindow(QMainWindow, Ui_MainWindow):
    ___ __init__  *args, obj_None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags() | __.FramelessWindowHint | __.WindowStaysOnTopHint)
        self.s..

        # Load/save note data, store this notes db reference.
        __ obj:
            self.obj _ obj
            self.load()
        ____
            self.obj _ Note()
            self.save()

        self.closeButton.pressed.c..(self.delete_window)
        self.moreButton.pressed.c..(create_new_note)
        self.textEdit.textChanged.c..(self.save)

        # Flags to store dragged-dropped
        self._drag_active _ False

    ___ load(self):
        self.move(self.obj.x, self.obj.y)
        self.textEdit.setHtml(self.obj.t__)
        _ACTIVE_NOTES[self.obj.id] _ self

    ___ save(self):
        self.obj.x _ self.x()
        self.obj.y _ self.y()
        self.obj.t__ _ self.textEdit.toHtml()
        session.add(self.obj)
        session.commit()
        _ACTIVE_NOTES[self.obj.id] _ self

    ___ mousePressEvent  e):
        self.previous_pos _ e.globalPos()

    ___ mouseMoveEvent  e):
        delta _ e.globalPos() - self.previous_pos
        self.move(self.x() + delta.x(), self.y()+delta.y())
        self.previous_pos _ e.globalPos()

        self._drag_active _ True

    ___ mouseReleaseEvent  e):
        __ self._drag_active:
            self.save()
            self._drag_active _ False

    ___ delete_window(self):
        result _ ?MB...q..  "Confirm delete", "Are you sure you want to delete this note?")
        __ result == ?MB...Yes:
            session.delete(self.obj)
            session.commit()
            self.close()


__ __name__ == '__main__':
    app _ ?
    app.sAN..("Brown Note")
    app.setStyle("Fusion")

    # Custom brown palette.
    palette _ ?P..()
    palette.sC..(?P...Window, ?C..(188,170,164))
    palette.sC..(?P...WindowText, ?C..(121,85,72))
    palette.sC..(?P...ButtonText, ?C..(121,85,72))
    palette.sC..(?P...Text, ?C..(121,85,72))
    palette.sC..(?P...Base, ?C..(188,170,164))
    palette.sC..(?P...AlternateBase, ?C..(188,170,164))
    app.sP..(palette)

    existing_notes _ session.query(Note).all()
    __ len(existing_notes) == 0:
        MainWindow()
    ____
        for note in existing_notes:
            MainWindow(obj_note)





    app.e..
