# Version 1.0 Code framework
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Template(metaclass=ABCMeta):
    """Template class (abstract class)"""

    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethold(self):
        """Template method"""
        self.stepOne()
        self.stepTwo()
        self.stepThree()


class TemplateImplA(Template):
    """Template implementation class A"""

    def stepOne(self):
        print("step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")


class TemplateImplB(Template):
    """Template implementation class B"""

    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")


# Version 2.0 Reader view
#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class ReaderView(metaclass=ABCMeta):
    """Reader view"""

    def __init__(self):
        self.__curPageNum = 1

    def getPage(self, pageNum):
        self.__curPageNum = pageNum
        return "First" + str(pageNum) + "Content"

    def prePage(self):
        """Template method, page forward"""
        content = self.getPage(self.__curPageNum - 1)
        self._displayPage(content)

    def nextPage(self):
        """Template method, page backward"""
        content = self.getPage(self.__curPageNum + 1)
        self._displayPage(content)

    @abstractmethod
    def _displayPage(self, content):
        """Page turning effect"""
        pass


class SmoothView(ReaderView):
    """Left and right smooth view"""

    def _displayPage(self, content):
        print("Smooth left and right:" + content)


class SimulationView(ReaderView):
    """Flip page view"""

    def _displayPage(self, content):
        print("Page turning simulation:" + content)


# Test
#=======================================================================================================================
def testReader():
    smoothView = SmoothView()
    smoothView.nextPage()
    smoothView.prePage()

    simulationView = SimulationView()
    simulationView.nextPage()
    simulationView.prePage()

def testTemplate():
    templateA = TemplateImplA()
    templateA.templateMethold()
    templateB = TemplateImplB()
    templateB.templateMethold()


testReader()
# testTemplate()