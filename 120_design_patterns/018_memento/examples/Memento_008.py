#=======================================================================================================================
class Engineer:
    """engineer"""

    def __init__(self, name):
        self.__name = name
        self.__workItems = []

    def addWorkItem(self, item):
        self.__workItems.append(item)

    def forget(self):
        self.__workItems.clear()
        print(self.__name + "I'm too busy at work, I've forgotten what to do!")

    def writeTodoList(self):
        """Record work items in TodoList"""
        todoList = TodoList()
        for item in self.__workItems:
            todoList.writeWorkItem(item)
        return todoList

    def retrospect(self, todoList):
        """Recall work items"""
        self.__workItems = todoList.getWorkItems()
        print(self.__name + "Think of what to do!")

    def showWorkItem(self):
        if(len(self.__workItems)):
            print(self.__name + "Work item:")
            for idx in range(0, len(self.__workItems)):
                print(str(idx + 1) + ". " + self.__workItems[idx] + ";")
        else:
            print(self.__name + "No work items!")


class TodoList:
    """Work item"""

    def __init__(self):
        self.__workItems = []

    def writeWorkItem(self, item):
        self.__workItems.append(item)

    def getWorkItems(self):
        return self.__workItems


class TodoListCaretaker:
    """TodoList Management Class"""

    def __init__(self):
        self.__todoList = None

    def setTodoList(self, todoList):
        self.__todoList = todoList

    def getTodoList(self):
        return self.__todoList


# Version 2.0
#=======================================================================================================================
# Code framework
#==============================
from copy import deepcopy

class Memento:
    """memorandum"""

    def setAttributes(self, dict):
        """Deep copy all attributes in dictionary dict"""
        self.__dict__ = deepcopy(dict)

    def getAttributes(self):
        """Get attribute dictionary"""
        return self.__dict__


class Caretaker:
    """Memo Management"""

    def __init__(self):
        self._mementos = {}

    def addMemento(self, name, memento):
        self._mementos[name] = memento

    def getMemento(self, name):
        return self._mementos[name]

class Originator:
    """Backup initiator"""

    def createMemento(self):
        memento = Memento()
        memento.setAttributes(self.__dict__)
        return memento

    def restoreFromMemento(self, memento):
        self.__dict__.update(memento.getAttributes())


# Framework-based implementation
#==============================

# Test
#=======================================================================================================================

def Engineer():
    tony = Engineer("Tony")
    tony.addWorkItem("Solve the problem that some users online cannot display the full name because the nickname is too long")
    tony.addWorkItem("Complete the parsing of the PDF")
    tony.addWorkItem("Display the contents of the first page of a PDF in a reader")
    tony.showWorkItem()
    caretaker = TodoListCaretaker()
    caretaker.setTodoList(tony.writeTodoList())

    print()
    tony.forget()
    tony.showWorkItem()

    print()
    tony.retrospect(caretaker.getTodoList())
    tony.showWorkItem()

# testEngineer()