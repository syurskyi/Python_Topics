_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ geolocation.main _____ GoogleMaps

____ demoGoogleMap1 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonSearch.clicked.c..(displayDetails)
        s..
   
    ___ displayDetails 
        address = st.(ui.lineEditLocation.text())
        google_maps = GoogleMaps(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 
        location = google_maps.search(location=address) # sends search to Google Maps.
        my_location = location.first() 
        ui.labelCity.sT..("City: "+st.(my_location.city))
        ui.labelPostalCode.sT..("Postal Code: " +st.(my_location.postal_code))
        ui.labelLongitude.sT..("Longitude: "+st.(my_location.lng))
        ui.labelLatitude.sT..("Latitude: "+st.(my_location.lat))
          
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())


