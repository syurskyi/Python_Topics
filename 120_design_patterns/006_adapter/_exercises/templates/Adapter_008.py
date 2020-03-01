#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class IHightPerson(metaclass=ABCMeta):
    """Interface class, which provides empty implementation methods, implemented by subclasses"""

    @abstractmethod
    def getName(self):
        """Get name"""
        pass

    @abstractmethod
    def getHeight(self):
        """Get height"""
        pass

    @abstractmethod
    def appearance(self, person):
        """appearance"""
        pass


class HighPerson(IHightPerson):
    """Tall man"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getHeight(self):
        return 170

    def appearance(self):
        print(self.getName() + "height" + str(self.getHeight()) + "，Perfect as you, born beauty!")


class ShortPerson:
    """Short man"""

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getRealHeight(self):
        return 160

    def getShoesHeight(self):
        return 6


class DecoratePerson(ShortPerson, IHightPerson):
    """People with high heels"""

    def __init__(self, name):
        super().__init__(name)

    def getName(self):
        return super().getName()

    def getHeight(self):
        return super().getRealHeight() + super().getShoesHeight()

    def appearance(self):
        print(self.getName() + "height" + str(self.getHeight()) + ", With the adaptation of high heels, your height is not less than Gao Yuanyuan, and your temperament is not less than Fan Bingbing!")


class HeightMatch:
    """Height matching"""

    def __init__(self, person):
        self.__person = person

    def matching(self, person1):
        """Assuming standard height difference within 10 cm"""
        distance = abs(self.__person.getHeight() - person1.getHeight())
        isMatch = distance <= 10
        print(self.__person.getName() + "with" + person1.getName() + "Whether it is the standard height difference of the couple："
              + ("Yes" if isMatch else "否") + ", Difference:" + str(distance))


class Hotel:
    """(Superior) Hotel"""

    def recruit(self, person):
        """
        :param person: Object of IHightPerson
        """
        suitable = self.receptionistSuitable(person)
        print(person.getName() + "Is it suitable to be a receptionist:", "meets the" if suitable else "incompatible")

    def receptionistSuitable(self, person):
        """
        s it possible to become a (premium hotel) receptionist
         : param person: Object of IHightPerson
         : return: whether it meets the requirements to be a receptionist
        """
        return person.getHeight() >= 165;

# Version 1.0
# =======================================================================================================================
from abc import ABCMeta, abstractmethod
#Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class SocketEntity:
    """Interface type definition"""

    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin


class ISocket(metaclass=ABCMeta):
    """Socket Type"""

    def getName(self):
        """Socket name"""
        pass

    def getSocket(self):
        """Get interface"""
        pass


class ChineseSocket(ISocket):
    """GB socket"""

    def getName(self):
        return  "GB socket"

    def getSocket(self):
        return SocketEntity(3, "Flat character")


class BritishSocket:
    """British Standard Socket"""

    def name(self):
        return  "British Standard Socket"

    def socketInterface(self):
        return SocketEntity(3, "T-square")

class AdapterSocket(ISocket):
    """Socket converter"""

    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return  self.__britishSocket.name() + "converter"

    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("Flat character")
        return socket



# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Target(metaclass=ABCMeta):
    """Target class"""

    @abstractmethod
    def function(self):
        pass


class Adaptee:
    """Source object class"""

    def speciaficFunction(self):
        print("Special functions of the adapted object")

class Adapter(Target):
    """adapter"""

    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def function(self):
        print("Perform function conversion")
        self.__adaptee.speciaficFunction()



#Framework-based implementation
#==============================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods
import os
# Import os library for file and path related analysis

class Page:
    """Content of an e-book page"""
    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getContent(self):
        return "First " + str(self.__pageNum) + "Content of the page ..."


class Catalogue:
    """Directory Structure"""

    def __init__(self, title):
        self.__title = title
        self.__chapters = []

    def addChapter(self, title):
        self.__chapters.append(title)

    def showInfo(self):
        print("Title:" + self.__title)
        print("table of Contents:")
        for chapter in self.__chapters:
            print("    " + chapter)


class IBook(metaclass=ABCMeta):
    """Interface class for e-book documents"""

    @abstractmethod
    def parseFile(self, filePath):
        """Parse the document"""
        pass

    @abstractmethod
    def getCatalogue(self):
        """Get the directory"""
        pass

    @abstractmethod
    def getPageCount(self):
        """Get the number of pages"""
        pass

    @abstractmethod
    def getPage(self, pageNum):
        """Get the content of pageNum"""
        pass


class TxtBook(IBook):
    """TXT parsing class"""

    def parseFile(self, filePath):
        # Parsing of simulated documents
        print(filePath + " File parsed successfully")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 500
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("Chapter 1 Title")
        catalogue.addChapter("hapter 2 Title")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class EpubBook(IBook):
    """Epub parsing class"""

    def parseFile(self, filePath):
        # Parsing of simulated documents
        print(filePath + " File parsed successfully")
        self.__title = os.path.splitext(filePath)[0]
        self.__pageCount = 800
        return True

    def getCatalogue(self):
        catalogue = Catalogue(self.__title)
        catalogue.addChapter("Chapter 1 Title")
        catalogue.addChapter("Chapter 2 Title")
        return catalogue

    def getPageCount(self):
        return self.__pageCount

    def getPage(self, pageNum):
        return Page(pageNum)


class Outline:
    """Catalog classes for third-party PDF parsing libraries"""
    def __init__(self):
        self.__outlines = []

    def addOutline(self, title):
        self.__outlines.append(title)

    def getOutlines(self):
        return self.__outlines


class PdfPage:
    "PDF pages"

    def __init__(self, pageNum):
        self.__pageNum = pageNum

    def getPageNum(self):
        return self.__pageNum


class ThirdPdf:
    """Third-party PDF parsing library"""

    def __init__(self):
        self.__pageSize = 0
        self.__title = ""

    def open(self, filePath):
        print("Parsing PDF files by third-party libraries：" + filePath)
        self.__title = os.path.splitext(filePath)[0]
        self.__pageSize = 1000
        return True

    def getTitle(self):
        return self.__title

    def getOutline(self):
        outline = Outline()
        outline.addOutline("Chapter 1 PDF eBook Title")
        outline.addOutline("Chapter 2 PDF eBook Title")
        return outline

    def pageSize(self):
        return self.__pageSize

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    """Repackage third-party PDF parsing libraries"""

    def __init__(self, thirdPdf):
        self.__thirdPdf = thirdPdf

    def parseFile(self, filePath):
        # Parsing of simulated documents
        rtn = self.__thirdPdf.open(filePath)
        if(rtn):
            print(filePath + "File parsed successfully")
        return rtn

    def getCatalogue(self):
        outline = self.getOutline()
        print("Transform the outline structure to the catalogue structure")
        catalogue = Catalogue(self.__thirdPdf.getTitle())
        for title in outline.getOutlines():
            catalogue.addChapter(title)
        return catalogue

    def getPageCount(self):
        return self.__thirdPdf.pageSize()

    def getPage(self, pageNum):
        page = self.page(pageNum)
        print("Convert a PdfPage's face object into a Page object")
        return Page(page.getPageNum())


class Reader:
    "Reader"

    def __init__(self, name):
        self.__name = name
        self.__filePath = ""
        self.__curBook = None
        self.__curPageNum = -1

    def __initBook(self, filePath):
        self.__filePath = filePath
        extName = os.path.splitext(filePath)[1]
        if(extName.lower() == ".epub"):
            self.__curBook = EpubBook()
        elif(extName.lower() == ".txt"):
            self.__curBook = TxtBook()
        elif(extName.lower() == ".pdf"):
            self.__curBook = PdfAdapterBook(ThirdPdf())
        else:
            self.__curBook = None

    def openFile(self, filePath):
        self.__initBook(filePath)
        if(self.__curBook is not None):
            rtn = self.__curBook.parseFile(filePath)
            if(rtn):
                self.__curPageNum = 1
            return rtn
        return False

    def closeFile(self):
        print("shut down " + self.__filePath + " file")
        return True

    def showCatalogue(self):
        catalogue = self.__curBook.getCatalogue()
        catalogue.showInfo()

    def prePage(self):
        print("Page forward:", end="")
        return self.gotoPage(self.__curPageNum - 1)

    def nextPage(self):
        print("Next page:", end="")
        return self.gotoPage(self.__curPageNum + 1)

    def gotoPage(self, pageNum):
        if(pageNum > 1 and pageNum < self.__curBook.getPageCount() -1):
            self.__curPageNum = pageNum

        print("Show" + str(self.__curPageNum) + "page")
        page = self.__curBook.getPage(self.__curPageNum)
        page.getContent()
        return page


# Test
#=======================================================================================================================

def testPerson():
    lira = HighPerson("Lira")
    lira.appearance()
    demi = DecoratePerson("Demi");
    demi.appearance()

    haigerMatching = HeightMatch(HighPerson("Haiger"))
    haigerMatching.matching(lira)
    haigerMatching.matching(demi)
    # hotel = Hotel()
    # hotel.recruit(lira)
    # hotel.recruit(demi)

def testAdapter():
    adpater = Adapter(Adaptee())
    adpater.function()

def testReader():
    reader = Reader("Reader")
    if(not reader.openFile("Ordinary world.txt")):
        return
    reader.showCatalogue()
    reader.prePage()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()
    print()

    if (not reader.openFile("a kite chaser.epub")):
        return
    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.prePage()
    reader.closeFile()
    print()

    if (not reader.openFile("How to understand design patterns from life.pdf")):
        return
    reader.showCatalogue()
    reader.nextPage()
    reader.nextPage()
    reader.closeFile()


def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "Flat character":
        isStandard = "meets the"
        canCharge = "can"
    else:
        isStandard = "incompatible"
        canCharge = "Can't"

    print("[%s]：\nNumber of pins: %d, pin type: %s; %s Chinese standard, %s charges mainland electronics!"
          % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))

def testSocket():
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())

    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(), britishSocket.socketInterface())

    adapterSocket = AdapterSocket(britishSocket)
    canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())


# testPerson()
# testAdapter()
testReader()
# testSocket()