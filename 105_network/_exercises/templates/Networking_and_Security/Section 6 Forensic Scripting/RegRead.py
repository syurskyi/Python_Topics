______ _winreg

valName _ "myKey"
___
    w__ _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\" + valName, 0, _winreg.KEY_READ) __ key:
        __ key:
            data _ _winreg.QueryValueEx(key, "myVal")
            print(data)
______ E.. __ e:
    print(e)