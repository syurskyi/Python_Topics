########################################################################################################################
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Context(metaclass=ABCMeta):
    """Context Class for State Mode"""

    def __init__(self):
        self.__states = []
        self.__curState = None
        # Attributes that depend on state changes. When this variable is jointly determined by multiple variables, it can be defined separately as a class.
        self.__stateInfo = 0

    def addState(self, state):
        if (state not in self.__states):
            self.__states.append(state)

    def changeState(self, state):
        if (state is None):
            return False
        if (self.__curState is None):
            print("Initialized to", state.getName())
        else:
            print("by", self.__curState.getName(), "Becomes", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if( state.isMatch(stateInfo) ):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo


class State:
    """Base class for states"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        "Whether the state property stateInfo is within the current state range"
        return False

    @abstractmethod
    def behavior(self, context):
        pass



# Demo achieve

class Water(Context):
    """water(H2O)"""

    def __init__(self):
        super().__init__()
        self.addState(SolidState("Solid"))
        self.addState(LiquidState("Liquid"))
        self.addState(GaseousState("Gaseous"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)


# Singleton decorator
def singleton(cls, *args, **kwargs):
    "Construct a singleton decorator"
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """Solid"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("I have a cold personality and my current temperature", context._getStateInfo(),
              "*C, I am as strong as steel, as a cold-blooded animal, please hit me with people, hehe ...")


@singleton
class LiquidState(State):
    """Liquid"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)

    def behavior(self, context):
        print("I have a gentle personality and my current temperature", context._getStateInfo(),
              "℃, I can moisturize all things, drinking I can make you more energetic ...")

@singleton
class GaseousState(State):
    """Gaseous"""

    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("I have a warm personality and my current temperature", context._getStateInfo(),
              "℃, flying to the sky is my lifelong dream, here you will not see my existence, I will reach the realm of selflessness ...")


# Test
########################################################################################################################
def testState():
    # water = Water(LiquidState("液态"))
    water = Water()
    water.behavior()
    water.setTemperature(-4)
    water.behavior()
    water.riseTemperature(18)
    water.behavior()
    water.riseTemperature(110)
    water.behavior()


testState()


# t1 = State("State1")
# t2 = State("State2")
# t3 = SolidState("State3")
# t4 = SolidState("State4")
# print(t1.getName(), t2.getName(), t3.getName(), t4.getName())
# print(id(t1), id(t2), id(t3), id(t4))
# print(t1 == t2)
# print(t3 == t4)


