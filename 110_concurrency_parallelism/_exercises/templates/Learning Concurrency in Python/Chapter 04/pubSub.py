______ th..
______ ra..
______ ti..

c_ Publisher(_.T..):

  ___  -   integers, condition):
    condition = condition
    integers = integers
    _.T... - (self)

  ___ run
    w... T..
      integer = random.randint(0,1000)
      condition.a..
      print("Condition Acquired by Publisher: {}".format(name))
      integers.a..(integer)
      print("Publisher {} appending to array: {}".format(name, integer))
      condition.n..
      print("Condition Released by Publisher: {}".format(name))
      condition.r..
      t___.s..(1)

c_ Subscriber(_.T..):

  ___  -   integers, condition):
    integers = integers
    condition = condition
    _.T... - (self)

  ___ run
    w... T..
      condition.a..
      print("Condition Acquired by Consumer: {}".format(name))
      w... T..
        __ integers:
          integer = integers.pop()
          print("{} Popped from list by Consumer: {}".format(integer, name))
          _____
        print("Condition Wait by {}".format(name))
        condition.w..
      print("Consumer {} Releasing Condition".format(name))
      condition.r..

___ main
  integers = []
  condition = _.C...()
  
  # Our Publisher
  pub1 = Publisher(integers, condition)
  pub1.s..

  # Our Subscribers
  sub1 = Subscriber(integers, condition)
  sub2 = Subscriber(integers, condition)
  sub1.s..
  sub2.s..

  ## Joining our Threads
  pub1.j..()
  consumer1.j..()
  consumer2.j..()

__ _____ __ _____
  main()
