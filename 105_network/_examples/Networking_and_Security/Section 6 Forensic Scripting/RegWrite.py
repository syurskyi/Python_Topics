import _winreg

valName = "myKey"
key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER, "Software\\" + valName)
_winreg.SetValueEx(key, "myVal", 0, _winreg.REG_SZ, "This is a value")

