from abc import ABC
from fly_behavior import FlyBehavior
from quack_behavior import QuackBehavior

class Duck(FlyBehavior, QuackBehavior):
