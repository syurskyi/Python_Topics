____ ?.?C.. _______ Qt
____ ?.?W.. _______ ?MW.., QWidget, QAction, QSplitter, QListView, QTabWidget
____ ?.?G.. _______ QIcon, QStandardItemModel, QStandardItem


____ app.ConfigurationManager _______ ConfigurationManager
____ gui.ClusterWidget _______ ClusterWidget

WINDOW_TITLE = 'MongoManager'

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'


c_ MainWindow(?MW..):
    ___  -
        ?MW... - (self, flags=Qt.Window)

        # Set menu bar
        menu_bar = menuBar()

        file = menu_bar.addMenu("&File")

        new_action = QAction('&New Cluster', self, shortcut='Ctrl+N', triggered=new_cluster)
        exit_action = QAction('&Exit', self, shortcut='Alt+F4', triggered=close)

        file.addAction(new_action)
        file.addSeparator()
        file.addAction(exit_action)

        # Set core widgets
        conf_widget = QListView(self)
        conf_widget.setMinimumWidth(150)
        conf_widget.c__.c..(load_cluster)

        context_widget = QTabWidget(self)
        context_widget.setMinimumWidth(100)

        central_widget = QSplitter(Qt.Horizontal, self)
        central_widget.aW..(conf_widget)
        central_widget.aW..(context_widget)
        central_widget.setCollapsible(0, False)
        central_widget.setCollapsible(1, False)
        central_widget.setSizes([150, 999])

        sCW..(central_widget)

        # Set UI
        setWindowIcon(QIcon(':/icons/fire_damage.ico'))
        sWT..(WINDOW_TITLE)
        setMinimumSize(600, 400)

        # Set vars
        config_manager = ConfigurationManager()

        load_configuration()
        loaded_clusters = []

    ___ new_cluster
        pass

    ___ load_configuration
        cluster_conf = config_manager.get(CLUSTER_CONF)

        model = QStandardItemModel()
        ___ element __ cluster_conf:
            item = QStandardItem(element['name'])
            item.setEditable(False)
            model.appendRow(item)
        conf_widget.setModel(model)

    ___ load_cluster(self, index_item):
        cluster = index_item.data()

        __ cluster not __ loaded_clusters:
            cluster_widget = ClusterWidget(cluster, context_widget)
            context_widget.addTab(cluster_widget, cluster)
            loaded_clusters.append(cluster)
