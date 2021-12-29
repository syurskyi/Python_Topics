____ visit_pycons _______ (
    _get_pycons,
    update_pycons_lat_lon,
    create_travel_plan,
    total_travel_distance,
)


___ test_update_pycons_lat_lon():
    pycons = _get_pycons()
    update_pycons_lat_lon(pycons)
    ___ pycon __ pycons:
        ... isi..(pycon.lat, float)
        ... isi..(pycon.lon, float)


___ test_create_travel_plan():
    pycons = _get_pycons()
    update_pycons_lat_lon(pycons)
    travel_plan = create_travel_plan(pycons)
    ... l..(travel_plan) __ 8
    ... travel_plan[0].origin.name __ "PyCon Odessa"
    ... travel_plan[0].destination.name __ "PyCon SK"
    ... travel_plan[-1].origin.name __ "PyCon DE & PyData Berlin"
    ... travel_plan[-1].destination.name __ "PyCon Ireland"


___ test_total_travel_distance():
    pycons = _get_pycons()
    update_pycons_lat_lon(pycons)
    travel_plan = create_travel_plan(pycons)
    ... total_travel_distance(travel_plan) __ 8444.9