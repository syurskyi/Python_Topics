def generate():                  # Fails prior to Python 2.2, works later
    class Spam:
        count = 1
        def method(self):        # Name Spam not visible:
            print(Spam.count)    # not local (def), global (module), built-in
    return Spam()

generate().method()

# C:\python\examples> python nester.py
# ...error text omitted...
#     Print(Spam.count)            # Not local (def), global (module), built-in
# NameError: Spam



def generate():
    global Spam                 # Force Spam to module scope
    class Spam:
        count = 1
        def method(self):
            print(Spam.count)   # Works: in global (enclosing module)
    return Spam()

generate().method()             # Prints 1



def generate():
    return Spam()

class Spam:                    # Define at top level of module
    count = 1
    def method(self):
        print(Spam.count)      # Works: in global (enclosing module)

generate().method()



def generate():
    class Spam:
        count = 1
        def method(self):
            print(self.__class__.count)      # Works: qualify to get class
    return Spam()

generate().method()
