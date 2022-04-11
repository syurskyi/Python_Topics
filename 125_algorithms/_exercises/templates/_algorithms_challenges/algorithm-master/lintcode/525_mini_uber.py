"""
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
"""
____ Trip _______ Trip, Helper


c_ MiniUber:
    driver_to_locs    # dict
    driver_to_trip    # dict
    INFINITY f__('inf')

    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information
    #               if there have matched rider or null
    ___ report  driver_id, lat, lng
        __ n.. driver_id:
            r..

        __ driver_id __ driver_to_trip:
            r.. driver_to_trip[driver_id]

        __ driver_id __ driver_to_locs:
            driver_to_locs[driver_id] 'lat'  = lat
            driver_to_locs[driver_id] 'lng'  = lng
        ____
            driver_to_locs[driver_id] _new_location(lat, lng)

    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    ___ request  rider_id, lat, lng
        __ n.. rider_id:
            r..
        trip Trip(rider_id, lat, lng)
        _distance distance INFINITY
        driver_id -1

        ___ _driver_id, _loc __ driver_to_locs.i..:
            _distance Helper.get_distance(_loc 'lat' , _loc 'lng' , lat, lng)
            __ _distance < distance:
                driver_id _driver_id
                distance _distance

        __ driver_id __ -1:
            r.. trip

        trip.driver_id driver_id
        driver_to_trip[driver_id] trip
        del driver_to_locs[driver_id]

        r.. trip

    ___ _new_location  lat, lng
        r.. {
            'lat': lat,
            'lng': lng
        }
