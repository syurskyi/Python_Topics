
try:
    f = open('conversion.py')
    print("file open")
    bad = aaa
except FileNotFoundError:
    print("file not exist")
except Exception __ e:
    print(e)
____:
    print(f.read())
finally:
    print("closing")