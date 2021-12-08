from mouse import Mouse
from cat import Cat
import time

Mouse() # Instance of Mouse as a thread object.
Cat()   # Instance of Cat as a thread object.

while True:
    time.sleep(1)
