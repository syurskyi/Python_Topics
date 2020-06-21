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

c_ ServerInfoPage(QWidget):
    ___  -
        s__(ServerInfoPage,self). - ()

        server='mongodb://localhost:27017'

        lbl_info=?L..(tr('server info:'))
        txt_info=?TE..
        
        vbox=QVBoxLayout()
        vbox.aW..(lbl_info)
        vbox.aW..(txt_info,1)

        sL..(vbox)

    ___ set_server(self,server):
        server=server
        mongo=_______(server)
        output=json.dumps(mongo.server_info(),indent=4)
        txt_info.sT..(QString(output))
        mongo.c..
