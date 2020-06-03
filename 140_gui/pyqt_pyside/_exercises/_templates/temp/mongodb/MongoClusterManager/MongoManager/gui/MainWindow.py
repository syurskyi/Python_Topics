from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QWidget, QAction, QSplitter, QListView, QTabWidget
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem


from app.ConfigurationManager import ConfigurationManager
from gui.ClusterWidget import ClusterWidget

WINDOW_TITLE = 'MongoManager'

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, flags=Qt.Window)

        # Set menu bar
        menu_bar = self.menuBar()

        file = menu_bar.addMenu("&File")

        new_action = QAction('&New Cluster', self, shortcut='Ctrl+N', triggered=self.new_cluster)
        exit_action = QAction('&Exit', self, shortcut='Alt+F4', triggered=self.close)

        file.addAction(new_action)
        file.addSeparator()
        file.addAction(exit_action)

        # Set core widgets
        self.conf_widget = QListView(self)
        self.conf_widget.setMinimumWidth(150)
        self.conf_widget.clicked.connect(self.load_cluster)

        self.context_widget = QTabWidget(self)
        self.context_widget.setMinimumWidth(100)

        central_widget = QSplitter(Qt.Horizontal, self)
        central_widget.addWidget(self.conf_widget)
        central_widget.addWidget(self.context_widget)
        central_widget.setCollapsible(0, False)
        central_widget.setCollapsible(1, False)
        central_widget.setSizes([150, 999])

        self.setCentralWidget(central_widget)

        # Set UI
        self.setWindowIcon(QIcon(':/icons/fire_damage.ico'))
        self.setWindowTitle(WINDOW_TITLE)
        self.setMinimumSize(600, 400)

        # Set vars
        self.config_manager = ConfigurationManager()

        self.load_configuration()
        self.loaded_clusters = []

    def new_cluster(self):
        pass

    def load_configuration(self):
        cluster_conf = self.config_manager.get(CLUSTER_CONF)

        model = QStandardItemModel()
        for element in cluster_conf:
            item = QStandardItem(element['name'])
            item.setEditable(False)
            model.appendRow(item)
        self.conf_widget.setModel(model)

    def load_cluster(self, index_item):
        cluster = index_item.data()

        if cluster not in self.loaded_clusters:
            cluster_widget = ClusterWidget(cluster, self.context_widget)
            self.context_widget.addTab(cluster_widget, cluster)
            self.loaded_clusters.append(cluster)
