set UIFILE_%1
set UIDIR_%~dp1
set FILENAME_%~n1
set PQTNAME_%UIDIR%%FILENAME%_ui.py
set PSDNAME_%UIDIR%%FILENAME%_uis.py
CALL C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat %UIFILE% -o %PQTNAME%
CALL C:\Python27\Scripts\pyside-uic.exe %UIFILE% -o %PSDNAME%
