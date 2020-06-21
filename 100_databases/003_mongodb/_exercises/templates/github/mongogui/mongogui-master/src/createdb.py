____ ?.?G.. _______ _
____ ?.?C.. _______ _
____ ?.?W.. _______ _

___
    ____ ?.?C.. _______ QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = st.

____ _______ _______ _______

c_ CreateDbPage(QWidget):
    db_created=pyqtSignal(st.)

    ___  -
        s__(CreateDbPage,self). - ()

        prompt=?L..(tr('database name:'))
        dbname_edit=?LE..

        ok_btn=?PB..(tr('commit'))
        ok_btn.sI..(QIcon('../icon/ok.svg'))
        ok_btn.c__.c..(commit)

        cancel_btn=?PB..(tr('cancel'))
        cancel_btn.sI..(QIcon('../icon/cancel.svg'))
        cancel_btn.c__.c..(cancel)

        hbox=QHBoxLayout()
        hbox.addStretch(1)
        hbox.aW..(ok_btn)
        hbox.aW..(cancel_btn)

        vbox=QVBoxLayout()
        vbox.aW..(prompt)
        vbox.aW..(dbname_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        sL..(vbox)

    ___ commit
        print('ok')
        
        mongo=_______()
        dbname=st.(dbname_edit.t...toUtf8(),'utf-8','ignore')
        print(dbname)
        db=mongo.get_database(dbname)
        db.create_collection('temp')
        mongo.c..

        client=_______()
        db=client[dbname]
        db.drop_collection('temp')
        client.c..

        db_created.emit(dbname)

    ___ cancel
        print('cancel')
        coll_name_edit.sT..(QString())
