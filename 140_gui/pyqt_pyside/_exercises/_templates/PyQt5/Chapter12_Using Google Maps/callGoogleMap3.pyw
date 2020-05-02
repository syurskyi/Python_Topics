_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ googlemaps.client _____ Client
____ googlemaps.distance_matrix _____ distance_matrix

____ demoGoogleMap3 _____ _

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ ?
        ui.sU..
        ui.pushButtonFindDistance.c___.c..(displayDistance)
        s..
   
    ___ displayDistance 
        api_key _ 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        gmaps _ Client(api_key)
        data _ distance_matrix(gmaps, ui.lineEditFirstLocation.t..(), ui.lineEditSecondLocation.t..())
        distance _ data['rows'][0]['elements'][0]['distance']['text']
        ui.labelDistance.sT..("Distance between "+ui.lineEditFirstLocation.t..()+" and "+ui.lineEditSecondLocation.t..()+" is "+st.(distance))
          
__ _ ____ __ _____
    app _ ?A..
    w _ ?
    w.s..
    ___.e..(app.e


