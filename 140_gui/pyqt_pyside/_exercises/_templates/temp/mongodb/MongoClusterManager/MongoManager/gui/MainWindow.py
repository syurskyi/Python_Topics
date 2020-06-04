____ ?.?C.. ______ __
____ ?.QtWidgets ______ ?MW.., QWidget, ?A.., QSplitter, QListView, QTabWidget
____ ?.?G.. ______ QIcon, QStandardItemModel, ?SI..


____ app.ConfigurationManager ______ ConfigurationManager
____ gui.ClusterWidget ______ ClusterWidget

WINDOW_TITLE _ 'MongoManager'

APP_CONF _ 'conf/app.conf'
CLUSTER_CONF _ 'conf/cluster.conf'


c_ MainWindow(?MW..):
    ___  - 
        ?MW... -   flags___.Window)

        # Set menu bar
        menu_bar _ menuBar()

        file _ menu_bar.addMenu("&File")

        new_action _ ?A..('&New Cluster', self, shortcut_'Ctrl+N', t____new_cluster)
        exit_action _ ?A..('&Exit', self, shortcut_'Alt+F4', t____close)

        file.aA..(new_action)
        file.addSeparator()
        file.aA..(exit_action)

        # Set core widgets
        conf_widget _ QListView(self)
        conf_widget.setMinimumWidth(150)
        conf_widget.c__.c__(load_cluster)

        context_widget _ QTabWidget(self)
        context_widget.setMinimumWidth(100)

        central_widget _ QSplitter(__.Horizontal, self)
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
        config_manager _ ConfigurationManager()

        load_configuration()
        loaded_clusters _   # list

    ___ new_cluster
        p..

    ___ load_configuration
        cluster_conf _ config_manager.get(CLUSTER_CONF)

        model _ QStandardItemModel()
        ___ element in cluster_conf:
            item _ ?SI..(element['name'])
            item.setEditable F..
            model.appendRow(item)
        conf_widget.sM..(model)

    ___ load_cluster  index_item):
        cluster _ index_item.data()

        __ cluster not in loaded_clusters:
            cluster_widget _ ClusterWidget(cluster, context_widget)
            context_widget.addTab(cluster_widget, cluster)
            loaded_clusters.ap..(cluster)
