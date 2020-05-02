_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ geolocation.main _____ GoogleMaps

____ demoGoogleMap1 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonSearch.c___.c..(displayDetails)
        s..
   
    ___ displayDetails 
        address _ st.(ui.lineEditLocation.t..())
        google_maps _ GoogleMaps(api_key_'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        location _ google_maps.search(location_address) # sends search to Google Maps.
        my_location _ location.first()
        ui.labelCity.sT..("City: "+st.(my_location.city))
        ui.labelPostalCode.sT..("Postal Code: " +st.(my_location.postal_code))
        ui.labelLongitude.sT..("Longitude: "+st.(my_location.lng))
        ui.labelLatitude.sT..("Latitude: "+st.(my_location.lat))
          
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ MyForm()
    w.s..
    ___.e..(app.e


