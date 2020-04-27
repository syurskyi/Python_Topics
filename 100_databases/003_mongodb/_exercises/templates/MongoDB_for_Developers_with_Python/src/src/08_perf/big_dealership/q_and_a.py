____ nosql.car _____ Car
____ nosql.owner _____ Owner
____ d_t_ _____ d_t_
_____ nosql.mongo_setup __ mongo_setup


___ timed(msg, func):
    t0 _ d_t_.n..()

    func()

    dt _ d_t_.n..() - t0
    print("{} Time: {:,.3f} ms".f..(msg, dt.total_seconds() * 1000.0), flush_True)


mongo_setup.init()

print("Time to ask some questions")

timed(
    'How many owners?',
    l___ Owner.objects().filter().c..
)
timed(
    'How many cars?',
    l___ Owner.objects().filter().c..
)

timed(
    'Find the 10,000th owner by name?',
    l___ Owner.objects().order_by('name')[10000:10001][0]
)

owner _ Owner.objects().order_by('name')[10000:10001][0]


___ find_cars_by_owner(owner_id):
    the_owner _ Owner.objects(id_owner_id).first()
    cars _ Car.objects().filter(id__in_the_owner.car_ids)
    r_ list(cars)


timed(
    'How many cars are owned by the 10,000th owner?',
    l___ find_cars_by_owner(owner.id)
)


___ find_owners_by_car(car_id):
    print(car_id)
    owners _ Owner.objects(car_ids_car_id)
    r_ list(owners)


car _ Car.objects()[10000:10001][0]
timed(
    'How many owners own the 10,000th car?',
    l___ find_owners_by_car(car.id)
)

owner50k _ Owner.objects()[50000:50001][0]
timed(
    'Find owner 50,000 by name?',
    l___ Owner.objects(name_owner50k.name).first()
)

timed(
    'Cars with expensive service?',
    l___ Car.objects(service_history__price__gt_16800).c..
)

timed(
    'Cars with expensive service and spark plugs?',
    l___ Car.objects(service_history__price__gt_16800,
                        service_history__description_'Spark plugs').c..
)

timed(
    'Load cars with expensive service and spark plugs?',
    l___ list(Car.objects(service_history__price__gt_15000)[:100])
)

timed(
    'Load car name and ids with expensive service and spark plugs?',
    l___ list(Car.objects(service_history__price__gt_15000)
                 .only('make', 'model', 'id')[:100])
)

timed(
    'Highly rated, high price service events?',
    l___ Car.objects(service_history__customer_rating_5, service_history__price__gt_16800).c..
)

timed(
    'Low rated, low price service events?',
    l___ Car.objects(service_history__customer_rating_1, service_history__price__lt_50).c..
)

timed(
    'How many high mileage cars?',
    l___ Car.objects(mileage__gt_140000).c..
)
