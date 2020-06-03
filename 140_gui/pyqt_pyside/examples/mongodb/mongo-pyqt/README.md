# mongo-pyqt 

## dep:
	*  PyQt5
	*  python-qt

## MAC OS Build
	dep: py2app

you should linux clang compile if not exits
* mkdir -p /Developer/Applications/
* ln -s ${QT_HOME}/5.2.1/clang_64/ /Developer/Applications/Qt
* ant


## Linux Build
dep:pyinstaller-dev https://github.com/pyinstaller/pyinstaller/zipball/develop
(pyinstaller2.1 is not avaible has some bug with Qt5 but dev is fixed)

ant linux