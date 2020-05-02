_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ geolocation.main _____ GoogleMaps

____ demoGoogleMap2 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui _ Ui_Dialog()
        ui.sU..
        ui.pushButtonSearch.c___.c..(displayLocation)
        s..
   
    ___ displayLocation 
        lng _ float(ui.lineEditLongitude.t..())
        lat _ float(ui.lineEditLatitude.t..())
        google_maps _ GoogleMaps(api_key_'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        my_location _ google_maps.search(lat_lat, lng_lng).first()
        ui.labelLocation.sT..("Location: "+st.(my_location))
        ui.labelCity.sT..("City: "+st.(my_location.city))
        ui.labelCountry.sT..("Country: "+st.(my_location.country))
        ui.labelPostalCode.sT..("Postal Code: "+st.(my_location.postal_code))
          
__ _ ____ __ _____
    app _ ?A..(___.argv)
    w _ ?
    w.s..
    ___.e..(app.e


