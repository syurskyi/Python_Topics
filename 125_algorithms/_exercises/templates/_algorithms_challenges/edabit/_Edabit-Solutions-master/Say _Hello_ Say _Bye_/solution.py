___ say_hello_bye(name, num
    __ num __ 1:
        r_ "Hello " + name.capitalize()
    ____
        r_ "Bye " + name.capitalize()


___ test(
    print("test has started")
    __ say_hello_bye("ram", 2) != "Bye Ram":
        print("error1")
    __ say_hello_bye("jodu", 1) != "Hello Jodu":
        print("error2")
