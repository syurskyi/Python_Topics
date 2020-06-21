____ ?.?G.. _______ _
____ ?.?C.. _______ _
____ ?.?W.. _______ _

___
    ____ ?.?C.. _______ QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = st.

____ _______ _______ _______
_______ json

c_ RemoveDocPage(QSplitter):
    ___  -
        s__(RemoveDocPage,self). - ()

        dbname='test'
        collname=''

        #self.toolbar=QToolBar()
        #self.toolbar.setIconSize(QSize(16,16))
        #self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        #self.commit_act=self.toolbar.addAction(
        #        QIcon('../icon/save.svg'),
        #        self.tr('commit'))
        #self.commit_act.triggered.connect(self.commit)
        
        #self.splitter=QSplitter()
        input_view=?W..
        input_header=?W..
        
        input_title=?L..(tr("input filter for deletes:"))
        
        remove_one_btn=QToolButton()
        remove_one_btn.sI..(QIcon('../icon/save.svg'))
        remove_one_btn.sT..(tr('delete one'))
        remove_one_btn.setIconSize(QSize(16,16))
        remove_one_btn.setToolButtonStyle(
                Qt.ToolButtonTextBesideIcon)
        remove_one_btn.c__.c..(delete_one)

        remove_many_btn=?PB..()
        remove_many_btn.sI..(QIcon('../icon/save.svg'))
        remove_many_btn.sT..(tr('delete many'))
        remove_many_btn.setIconSize(QSize(16,16))
        remove_many_btn.c__.c..(delete_many)

        hbox=QHBoxLayout()
        hbox.aW..(input_title,1)
        hbox.aW..(remove_one_btn)
        hbox.aW..(remove_many_btn)
        hbox.setMargin(0)
        hbox.setSpacing(0)
        input_header.sL..(hbox)

        docs_edit=?TE..

        vbox=QVBoxLayout()
        vbox.aW..(input_header)
        vbox.aW..(docs_edit,1)
        vbox.setMargin(0)
        vbox.setSpacing(0)
        input_view.sL..(vbox)

        results_view=?W..
        results_header=?L..(tr("results:"))
        results_edit=?TE..
        results_vbox=QVBoxLayout()
        results_vbox.aW..(results_header)
        results_vbox.aW..(results_edit,1)
        results_vbox.setMargin(0)
        results_vbox.setSpacing(0)
        results_view.sL..(results_vbox)

        aW..(input_view)
        aW..(results_view)

        setOrientation(Qt.Vertical)

        #vbox=QVBoxLayout()
        #vbox.addWidget(self.toolbar)
        #vbox.addWidget(self.splitter,1)
        #vbox.setMargin(0)
        #vbox.setSpacing(0)
        #self.setLayout(vbox)

    ___ set_db_and_coll(self,dbname,collname):
        dbname=st.(dbname)
        collname=st.(collname)

    ___ delete_one
        print('delete one')
        mongo =_______()
        text=st.(docs_edit.toPlainText().toUtf8(),
                'utf8','ignore')
        #text=self.docs_edit.toPlainText()
        print(text)
        data=json.loads(text)
        coll=mongo[dbname][collname]

        result=coll.delete_one(data)
        results_edit.sT..(st.(result.deleted_count))

    ___ delete_many
        print('delete many')

        mongo=_______()
        coll=mongo[dbname][collname]

        text=st.(docs_edit.toPlainText())
        data=json.loads(text)
        
        result=coll.delete_many(data)
        results_edit.sT..(st.(result.deleted_count))
