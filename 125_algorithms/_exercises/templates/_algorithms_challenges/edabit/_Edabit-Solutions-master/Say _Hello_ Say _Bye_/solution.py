___ say_hello_bye(name, num):
    __ num == 1:
        return "Hello " + name.capitalize()
    else:
        return "Bye " + name.capitalize()


___ test():
    print("test has started")
    __ say_hello_bye("ram", 2) != "Bye Ram":
        print("error1")
    __ say_hello_bye("jodu", 1) != "Hello Jodu":
        print("error2")
