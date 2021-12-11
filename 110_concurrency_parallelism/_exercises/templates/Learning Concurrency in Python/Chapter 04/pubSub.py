______ th..
______ ra..
______ ti..

c_ Publisher(_.T..):

  ___  -   integers, condition):
    condition = condition
    integers = integers
    _.T... -

  ___ run
    w... T..
      integer = r___.r..(0,1000)
      condition.a..
      print("Condition Acquired by Publisher: {}".f..(name))
      integers.a..(integer)
      print("Publisher {} appending to array: {}".f..(name, integer))
      condition.n..
      print("Condition Released by Publisher: {}".f..(name))
      condition.r..
      t___.s..(1)

c_ Subscriber(_.T..):

  ___  -   integers, condition):
    integers = integers
    condition = condition
    _.T... -

  ___ run
    w... T..
      condition.a..
      print("Condition Acquired by Consumer: {}".f..(name))
      w... T..
        __ integers:
          integer = integers.pop()
          print("{} Popped from list by Consumer: {}".f..(integer, name))
          _____
        print("Condition Wait by {}".f..(name))
        condition.w..
      print("Consumer {} Releasing Condition".f..(name))
      condition.r..

___ main
  integers   # list
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
