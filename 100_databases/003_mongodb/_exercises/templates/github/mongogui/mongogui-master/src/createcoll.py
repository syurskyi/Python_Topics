____ ?.?G.. _______ _
____ ?.?C.. _______ _
____ ?.?W.. _______ _

___
    ____ ?.?C.. _______ QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = st.

____ _______ _______ _______
# import unicode


c_ CreateCollPage(QWidget):
    collection_created=pyqtSignal(QTreeWidgetItem)

    ___  -
        s__(CreateCollPage,self). - ()

        dbname='test'

        prompt=?L..(tr('collection name:'))
        coll_name_edit=?LE..

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
        vbox.aW..(coll_name_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        sL..(vbox)

    ___ set_db(self,dbname):
        dbname=st.(dbname.toUtf8(),'utf-8','ignore')

    ___ commit
        print('ok')
        
        mongo=_______()
        db=mongo[dbname]
        collname=st.(coll_name_edit.t...toUtf8(),
                'utf-8','ignore')
        print(collname)
        db.create_collection(collname)
        mongo.c..
        collection_created.emit(dbitem)

    ___ cancel
        print('cancel')
        coll_name_edit.sT..(QString())
