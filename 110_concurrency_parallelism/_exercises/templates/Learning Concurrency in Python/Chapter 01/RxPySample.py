______ rx
____ rx ______ Observable, Observer

# Here we define our custom observer which
# contains an on_next method, an on_error method
# and an on_completed method
c_ temperatureObserver(Observer):

  # Every t__ we receive a temperature reading
  # this method is called
  ___ on_next  x):
    print("Temperature is: %s degrees centigrade" % x)
    __ (x > 6):
      print("Warning: Temperate Is Exceeding Recommended Limit")
    __ (x == 9):
      print("DataCenter is shutting down. Temperature is too high")

  # if we were to receive an error message
  # we would handle it here
  ___ on_error  e):
    print("Error: %s" % e)
  
  # This is called when the stream is finished
  ___ on_completed
    print("All Temps Read")

# Publish some fake temperature readings 
xs = Observable.from_iterable(r...(10))
# subscribe to these temperature readings
d = xs.subscribe(temperatureObserver())