______ th..
______ ra..
______ ti..

c_ Publisher(_.T..):

  ___ __init__(self, integers, condition):
    self.condition = condition
    self.integers = integers
    _.T...__init__(self)

  ___ run(self):
    w... T..
      integer = random.randint(0,1000)
      self.condition.a..
      print("Condition Acquired by Publisher: {}".format(self.name))
      self.integers.a..(integer)
      print("Publisher {} appending to array: {}".format(self.name, integer))
      self.condition.notify()
      print("Condition Released by Publisher: {}".format(self.name))
      self.condition.r..
      t___.s..(1)

c_ Subscriber(_.T..):

  ___ __init__(self, integers, condition):
    self.integers = integers
    self.condition = condition
    _.T...__init__(self)

  ___ run(self):
    w... T..
      self.condition.a..
      print("Condition Acquired by Consumer: {}".format(self.name))
      w... T..
        __ self.integers:
          integer = self.integers.pop()
          print("{} Popped from list by Consumer: {}".format(integer, self.name))
          _____
        print("Condition Wait by {}".format(self.name))
        self.condition.wait()
      print("Consumer {} Releasing Condition".format(self.name))
      self.condition.r..

___ main
  integers = []
  condition = _.Condition()
  
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
