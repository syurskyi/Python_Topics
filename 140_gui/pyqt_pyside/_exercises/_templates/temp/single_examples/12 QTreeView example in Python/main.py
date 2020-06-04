____ os.path ______ expanduser
____ ?.QtWidgets ______ *

home_directory = expanduser('~')

app = ?A..([])
model = QDirModel()
view = QTreeView()
view.sM..(model)
view.setRootIndex(model.index(home_directory))
view.s..
app.exec_()