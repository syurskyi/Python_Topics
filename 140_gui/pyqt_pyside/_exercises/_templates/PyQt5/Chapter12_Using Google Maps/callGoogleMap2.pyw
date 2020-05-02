_____ ___

____ ?.?W.. _____ ?D.., ?A..
____ geolocation.main _____ GoogleMaps

____ demoGoogleMap2 _____ *

c_ MyForm(?D..
    ___  -  
        s__. - ()
        ui = Ui_Dialog()
        ui.setupUi
        ui.pushButtonSearch.clicked.c..(displayLocation)
        s..
   
    ___ displayLocation 
        lng = float(ui.lineEditLongitude.text())
        lat = float(ui.lineEditLatitude.text())
        google_maps = GoogleMaps(api_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx') 
        my_location = google_maps.search(lat=lat, lng=lng).first()
        ui.labelLocation.sT..("Location: "+st.(my_location))
        ui.labelCity.sT..("City: "+st.(my_location.city))
        ui.labelCountry.sT..("Country: "+st.(my_location.country))
        ui.labelPostalCode.sT..("Postal Code: "+st.(my_location.postal_code))
          
__ __name____"__main__":    
    app = ?A..(___.argv)
    w = MyForm()
    w.s..
    ___.e..(app.exec_())


