_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ googlemaps.client _____ Client
____ googlemaps.distance_matrix _____ distance_matrix

____ demoGoogleMap3 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.setupUi
        ui.pushButtonFindDistance.clicked.c..(displayDistance)
        s..
   
    ___ displayDistance 
        api_key _ 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        gmaps _ Client(api_key)
        data _ distance_matrix(gmaps, ui.lineEditFirstLocation.text(), ui.lineEditSecondLocation.text())
        distance _ data['rows'][0]['elements'][0]['distance']['text']
        ui.labelDistance.sT..("Distance between "+ui.lineEditFirstLocation.text()+" and "+ui.lineEditSecondLocation.text()+" is "+st.(distance))
          
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.exec_())


