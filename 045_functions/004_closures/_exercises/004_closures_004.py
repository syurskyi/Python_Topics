# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis


if __name__ == '__main__':
    myFunction = outerFunction('Hey!')
    myFunction()