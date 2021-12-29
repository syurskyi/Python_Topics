from datetime import date, datetime, time, timedelta

TODAY = date.today()


___ gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    notification = start_date
    for _ in range(10):
        notification = notification + timedelta(days=num_days)
        for _ in range(num_bites):
            yield notification
    

# if __name__ == "__main__":
#     gen = gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY)
#     for _ in range(10):
#         print(next(gen))
    