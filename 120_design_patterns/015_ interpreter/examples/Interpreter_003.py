#=======================================================================================================================
from abc import ABCMeta, abstractmethod
# Introduce ABCMeta and abstractmethod to define abstract classes and abstract methods

class Expression(metaclass=ABCMeta):
    """Abstract expression"""

    @abstractmethod
    def interpreter(self, var):
        pass


class VarExpression(Expression):
    """Variable parser"""

    def __init__(self, key):
        self.__key = key

    def interpreter(self, var):
        return var.get(self.__key)


class SymbolExpression(Expression):
    """Operator parser, abstract class for operators"""

    def __init__(self, left, right):
        self._left = left
        self._right = right


class AddExpression(SymbolExpression):
    """Addition parser"""

    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) + self._right.interpreter(var)


class SubExpression(SymbolExpression):
    """Subtraction parser"""

    def __init__(self, left, right):
        super().__init__(left, right)

    def interpreter(self, var):
        return self._left.interpreter(var) - self._right.interpreter(var)



class Stack:
    """Encapsulating a stack class"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Calculator:
    """Calculator"""

    def __init__(self, text):
        self.__expression = self.parserText(text)

    def parserText(self, expText):
        # Define a stack, processing sequence
        stack = Stack()
        left = right = None # Left and right expression
        idx = 0
        while(idx < len(expText)):
            if (expText[idx] == '+'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(AddExpression(left, right))
            elif(expText[idx] == '-'):
                left = stack.pop()
                idx += 1
                right = VarExpression(expText[idx])
                stack.push(SubExpression(left, right))
            else:
                stack.push(VarExpression(expText[idx]))
            idx += 1
        return stack.pop()

    def run(self, var):
        return self.__expression.interpreter(var)





# Version 2.0
#=======================================================================================================================
# Code framework
#==============================


# Framework-based implementation
#==============================


# Test
#=======================================================================================================================

def Stack():
    s = Stack()
    print(s.isEmpty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    s.push(True)
    print(s.size())
    print(s.isEmpty())
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size())



def Calculator():
    # Get expression
    expStr = input("Please enter an expression ");
    # Get the key-value pairs of each parameter
    newExp, expressionMap = getMapValue(expStr)
    calculator = Calculator(newExp)
    result = calculator.run(expressionMap)
    print("The operation result is: " + expStr + " = " + str(result))

def getMapValue(expStr):
    preIdx = 0
    expressionMap = {}
    newExp = []
    for i in range(0, len(expStr)):
        if (expStr[i] == '+' or expStr[i] == '-'):
            key = expStr[preIdx:i]
            key = key.strip()  # Remove leading and trailing blank characters
            newExp.append(key)
            newExp.append(expStr[i])
            var = input("Please enter parameters" + key + "The value of ");
            var = var.strip()
            expressionMap[key] = float(var)
            preIdx = i + 1

    # Processing the last parameter
    key = expStr[preIdx:len(expStr)]
    key = key.strip()  # Remove leading and trailing blank characters
    newExp.append(key)
    var = input("Please enter parameters" + key + "The value of: ");
    var = var.strip()
    expressionMap[key] = float(var)

    return newExp, expressionMap


# testStack()
Calculator()