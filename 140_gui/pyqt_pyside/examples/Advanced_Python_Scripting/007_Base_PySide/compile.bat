set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PQTNAME=%UIDIR%%FILENAME%_ui.py
set PSDNAME=%UIDIR%%FILENAME%_uis.py

CALL C:\Users\serge\.virtualenvs\QT5-pYEvVUVx\Lib\site-packages\PyQt5\uic\pyuic.py %UIFILE% -o %PQTNAME%
CALL C:\Users\serge\.pyenv\pyenv-win\versions\3.7.7\Scripts\pyside2-uic.exe %UIFILE% -o %PSDNAME%
