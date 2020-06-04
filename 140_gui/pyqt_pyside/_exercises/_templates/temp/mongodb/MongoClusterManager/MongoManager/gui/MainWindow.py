____ ?.?C.. ______ __
____ ?.QtWidgets ______ ?MW.., QWidget, ?A.., QSplitter, QListView, QTabWidget
____ ?.QtGui ______ QIcon, QStandardItemModel, QStandardItem


____ app.ConfigurationManager ______ ConfigurationManager
____ gui.ClusterWidget ______ ClusterWidget

WINDOW_TITLE = 'MongoManager'

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'


c_ MainWindow(?MW..):
    ___  - 
        ?MW... - (self, flags=__.Window)

        # Set menu bar
        menu_bar = menuBar()

        file = menu_bar.addMenu("&File")

        new_action = ?A..('&New Cluster', self, shortcut='Ctrl+N', t___=new_cluster)
        exit_action = ?A..('&Exit', self, shortcut='Alt+F4', t___=close)

        file.aA..(new_action)
        file.addSeparator()
        file.aA..(exit_action)

        # Set core widgets
        conf_widget = QListView(self)
        conf_widget.setMinimumWidth(150)
        conf_widget.c__.c__(load_cluster)

        context_widget = QTabWidget(self)
        context_widget.setMinimumWidth(100)

        central_widget = QSplitter(__.Horizontal, self)
        central_widget.addWidget(conf_widget)
        central_widget.addWidget(context_widget)
        central_widget.setCollapsible(0, False)
        central_widget.setCollapsible(1, False)
        central_widget.setSizes([150, 999])

        setCentralWidget(central_widget)

        # Set UI
        setWindowIcon(QIcon(':/icons/fire_damage.ico'))
        setWindowTitle(WINDOW_TITLE)
        setMinimumSize(600, 400)

        # Set vars
        config_manager = ConfigurationManager()

        load_configuration()
        loaded_clusters = []

    ___ new_cluster
        p..

    ___ load_configuration
        cluster_conf = config_manager.get(CLUSTER_CONF)

        model = QStandardItemModel()
        for element in cluster_conf:
            item = QStandardItem(element['name'])
            item.setEditable(False)
            model.appendRow(item)
        conf_widget.sM..(model)

    ___ load_cluster(self, index_item):
        cluster = index_item.data()

        if cluster not in loaded_clusters:
            cluster_widget = ClusterWidget(cluster, context_widget)
            context_widget.addTab(cluster_widget, cluster)
            loaded_clusters.append(cluster)
