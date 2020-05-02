set UIFILE_%1
set UIDIR_%~dp$PATH:1
set FILENAME_%~n1
set NNAME_%UIDIR%%FILENAME%_UI.py
set SNAME_%UIDIR%%FILENAME%_UIs.py

CALL C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat %UIFILE% -o %NNAME%
CALL C:\Python27\Scripts\pyside-uic.exe %UIFILE% -o %SNAME%
