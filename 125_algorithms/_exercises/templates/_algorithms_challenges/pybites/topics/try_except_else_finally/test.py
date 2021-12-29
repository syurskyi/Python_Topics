
try:
    f = open('conversion.py')
    print("file open")
    bad = aaa
except FileNotFoundError:
    print("file not exist")
except Exception as e:
    print(e)
____:
    print(f.read())
finally:
    print("closing")