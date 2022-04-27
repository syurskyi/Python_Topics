___ say_hello_bye(name, num
    __ num __ 1:
        r.. "Hello " + ?.c..
    ____
        r.. "Bye " + ?.c..


___ test
    print("test has started")
    __ say_hello_bye("ram", 2) ! "Bye Ram":
        print("error1")
    __ say_hello_bye("jodu", 1) ! "Hello Jodu":
        print("error2")
