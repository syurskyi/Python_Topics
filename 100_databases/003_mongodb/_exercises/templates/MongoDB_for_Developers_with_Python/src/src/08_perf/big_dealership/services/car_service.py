_____ ty..

_____ bson
_____ d_t_

____ nosql.car _____ Car
____ nosql.engine _____ Engine
____ nosql.owner _____ Owner
____ nosql.service_record _____ ServiceRecord


___ create_owner(name: st.) -> O..
    owner _ Owner(name_name)
    owner.save()

    r_ owner


___ create_car(model: st., make: st., year: int,
               horsepower: int, liters: fl..,
               mpg: fl.., mileage: int) -> Car:
    engine _ Engine(horsepower_horsepower, liters_liters, mpg_mpg)
    car _ Car(model_model, make_make, year_year, engine_engine, mileage_mileage)
    car.save()

    r_ car


___ record_visit(customer):
    Owner.objects(name_customer).u_o..(inc__number_of_visits_1)


___ find_cars_by_make(make) -> Car:
    car _ Car.objects(make_make).first()
    r_ car


___ find_owner_by_name(name) -> O..
    t0 _ d_t_.d_t_.n..()
    owner _ Owner.objects(name_name).first()
    dt _ d_t_.d_t_.n..() - t0
    print("Owner found in {} ms".f..(dt.total_seconds() * 1000))

    r_ owner


___ find_owner_by_id(owner_id) -> O..
    owner _ Owner.objects(id_owner_id).first()
    r_ owner


___ find_cars_with_bad_service(limit_10) -> ty__.List[Car]:
    cars _ Car.objects(service_history__customer_rating__lt_4)[:limit]
    r_ list(cars)


___ percent_cars_with_bad_service
    t0 _ d_t_.d_t_.n..()
    bad _ Car.objects().filter(service_history__customer_rating__lte_1).c..
    dt _ d_t_.d_t_.n..() - t0
    print("bad computed in {} ms, bad: {:,}".f..(dt.total_seconds() * 1000, bad))

    all_cars _ Car.objects().c..

    percent _ 100 * bad / max(all_cars, 1)
    r_ percent


___ find_car_by_id(car_id: bson.ObjectId) -> Car:
    car _ Car.objects(id_car_id).first()
    Car.objects().filter(id_car_id).first()
    r_ car


___ add_service_record(car_id, description, price, customer_rating):
    record _ ServiceRecord(description_description, price_price, customer_rating_customer_rating)

    res _ Car.objects(id_car_id).u_o..(push__service_history_record)
    __ res !_ 1:
        r_ E..("No car with id {}".f..(car_id))


___ add_owner(owner_id, car_id):
    res _ Owner.objects(id_owner_id).u_o..(add_to_set__car_ids_car_id)
    __ res !_ 1:
        r_ E..("No owner with id {}".f..(owner_id))
