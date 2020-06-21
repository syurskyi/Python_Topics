____ ?.?G.. _______ _
____ ?.?C.. _______ _
____ ?.?W.. _______ _

___
    ____ ?.?C.. _______ QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = st.

____ _______ _______ _______

c_ RenamePage(QWidget):

    ___  -
        s__(RenamePage,self). - ()

        prompt=?L..(tr('new name:'))
        name_edit=?LE..

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
        vbox.aW..(name_edit)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        sL..(vbox)

    ___ commit
        print('ok')
        
        mongo=_______()
        name=st.(name_edit.t...toUtf8(),'utf-8','ignore')
        
        __ node_type__'coll':
            dbname=st.(
                    node.parent().parent().text(0).toUtf8(),
                    'utf-8','ignore')
            collname=st.(node.text(0).toUtf8(),
                    'utf-8','ignore')

            coll=mongo[dbname][collname]
            coll.rename(name)
            node.sT..(0,name)
        mongo.c..


    ___ cancel
        print('cancel')
        name_edit.sT..(QString())
