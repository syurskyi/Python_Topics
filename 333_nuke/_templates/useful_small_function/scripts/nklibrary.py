#coding:utf8
____ ?.?W.. ______ *
______ __
______ nuke

c_ NkLibrary(?W..):
	___ -
		s_(NkLibrary, self).- ()
		#variable
		libpath = __.getenv("NUKE_PATH")+"/nk/"
		appname = "Nuke Library"
		version = "v0.1"

		#widget
		nklist = QListWidget()
		addNkList()
		ok = QPushButton("OK")
		cancel = QPushButton("Cancel")

		#layout
		layout = ?VB..
		layout.aW..(nklist)
		layout.aW..(ok)
		layout.aW..(cancel)
		setWindowTitle(appname + " " + version)
		sL..(layout)
		
		#event
		ok.clicked.connect(pushOK)
		cancel.clicked.connect(close)
		nklist.itemClicked.connect(itemClick)

	___ pushOK
		nuke.nodePaste(libpath + currentItem)
		c__

	___ itemClick(self, item):
		currentItem = item.text()
	
	___ addNkList
		if not __.path.exists(libpath):
			nuke.message(libpath + "The path does not exist.")
		___ i __ __.listdir(libpath):
			base, ext = __.path.splitext(i)
			if ext != ".nk":
				continue
			nklist.addItem(QListWidgetItem(i))

___ main():
	g__ customApp
	___
		customApp.c__
	______
		pass
	
	customApp = NkLibrary()
	___
		customApp.s__
	______
		pass
