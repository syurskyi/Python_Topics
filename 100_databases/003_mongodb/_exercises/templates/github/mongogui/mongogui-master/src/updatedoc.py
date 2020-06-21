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

c_ UpdateDocPage(QWidget):
    ___  -
        s__(UpdateDocPage,self). - ()

        dbname='test'
        collname=''

        toolbar=QToolBar()
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        
        update_one_act=toolbar.addAction(
                QIcon('../icon/save.svg'),
                tr('update one'))
        update_one_act.triggered.c..(update_one)
        
        update_many_act=toolbar.addAction(
                QIcon('../icon/save.svg'),
                tr('update many'))
        update_many_act.triggered.c..(update_many)

        replace_act=toolbar.addAction(
                QIcon('../icon/replace.svg'),
                tr('replace one'))
        replace_act.triggered.c..(replace)
        
        hsplitter=QSplitter()
        
        filter_view=?W..
        filter_header=?L..(tr("filter:"))
        filter_edit=?TE..
        filter_vbox=QVBoxLayout()
        filter_vbox.aW..(filter_header)
        filter_vbox.aW..(filter_edit,1)
        filter_vbox.setMargin(0)
        filter_vbox.setSpacing(0)
        filter_view.sL..(filter_vbox)

        update_view=?W..
        update_header=?L..(tr("update:"))
        update_edit=?TE..
        header_vbox=QVBoxLayout()
        header_vbox.aW..(update_header)
        header_vbox.aW..(update_edit,1)
        header_vbox.setMargin(0)
        header_vbox.setSpacing(0)
        update_view.sL..(header_vbox)

        hsplitter.aW..(filter_view)
        hsplitter.aW..(update_view)

        splitter=QSplitter()
        results_view=?W..
        results_header=?L..(tr("results:"))
        results_edit=?TE..
        results_vbox=QVBoxLayout()
        results_vbox.aW..(results_header)
        results_vbox.aW..(results_edit,1)
        results_vbox.setMargin(0)
        results_vbox.setSpacing(0)
        results_view.sL..(results_vbox)

        splitter.aW..(hsplitter)
        splitter.aW..(results_view)

        splitter.setOrientation(Qt.Vertical)

        vbox=QVBoxLayout()
        vbox.aW..(toolbar)
        vbox.aW..(splitter,1)
        vbox.setMargin(0)
        vbox.setSpacing(0)
        sL..(vbox)

    ___ set_db_and_coll(self,dbname,collname):
        dbname=st.(dbname)
        collname=st.(collname)

    ___ update_one
        print('update one')
        
        mongo =_______()
        coll=mongo[dbname][collname]

        filter_text=st.(filter_edit.toPlainText().toUtf8(),
                'utf8','ignore')
        update_text=st.(update_edit.toPlainText().toUtf8(),
                'utf8','ignore')

        print(filter_text)
        print(update_text)

        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)
        
        result=coll.update_one(filter_data,update_data)
        
        results_edit.sT..(
                'matched count:%r \nmodified count:%r' % (
                    result.matched_count,
                    result.modified_count))
        mongo.c..

    ___ update_many
        print('update many')
        
        mongo=_______()
        coll = mongo[dbname][collname]

        filter_text=st.(filter_edit.toPlainText())
        update_text=st.(update_edit.toPlainText())
        
        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)
        
        result=coll.update_many(filter_data,update_data)
        results_edit.sT..(
                'matched count:%r \nmodified count:%r' % (
                    result.matched_count,
                    result.modified_count))

        mongo.c..

    ___ replace
        print('replace one')
        mongo=_______()
        coll=mongo[dbname][collname]

        filter_text=st.(filter_edit.toPlainText())
        update_text=st.(update_edit.toPlainText())

        filter_data=json.loads(filter_text)
        update_data=json.loads(update_text)

        result=coll.replace_one(filter_data,update_data)
        results_edit.sT..(
                    'matched count:%r \nmodified count:%r' %(
                        result.matched_count,
                        result.modified_count))
        
        mongo.c..
