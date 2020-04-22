______ th..
______ ra..
______ ti..

c_ Publisher(threading.Thread):

  ___ __init__(self, integers, condition):
    self.condition = condition
    self.integers = integers
    threading.Thread.__init__(self)

  ___ run(self):
    while True:
      integer = random.randint(0,1000)
      self.condition.a..
      print("Condition Acquired by Publisher: {}".format(self.name))
      self.integers.append(integer)
      print("Publisher {} appending to array: {}".format(self.name, integer))
      self.condition.notify()
      print("Condition Released by Publisher: {}".format(self.name))
      self.condition.release()
      time.sleep(1)

c_ Subscriber(threading.Thread):

  ___ __init__(self, integers, condition):
    self.integers = integers
    self.condition = condition
    threading.Thread.__init__(self)

  ___ run(self):
    while True:
      self.condition.a..
      print("Condition Acquired by Consumer: {}".format(self.name))
      while True:
        if self.integers:
          integer = self.integers.pop()
          print("{} Popped from list by Consumer: {}".format(integer, self.name))
          break
        print("Condition Wait by {}".format(self.name))
        self.condition.wait()
      print("Consumer {} Releasing Condition".format(self.name))
      self.condition.release()

___ main():
  integers = []
  condition = threading.Condition()
  
  # Our Publisher
  pub1 = Publisher(integers, condition)
  pub1.start()

  # Our Subscribers
  sub1 = Subscriber(integers, condition)
  sub2 = Subscriber(integers, condition)
  sub1.start()
  sub2.start()

  ## Joining our Threads
  pub1.join()
  consumer1.join()
  consumer2.join()

if __name__ == '__main__':
  main()
