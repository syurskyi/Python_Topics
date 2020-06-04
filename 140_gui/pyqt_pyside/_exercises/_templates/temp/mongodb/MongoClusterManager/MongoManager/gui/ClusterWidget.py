______ l__.c..

____ ?.QtWidgets ______ QWidget, QVBoxLayout, QGroupBox, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView


____ app.ConfigurationManager ______ ConfigurationManager

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'
HEADERS = ['hostname', 'port', 'role', 'status', 'installed']


c_ ClusterWidget(QWidget):
    ___  - (self, cluster, parent=None):
        QWidget. - (self, parent)

        # Set base vars
        cluster = cluster
        conf_manager = ConfigurationManager()

        configuration = {}
        members = []

        # Set UI
        _init_ui()

    ___ _load_from_conf
        conf = conf_manager.get(CLUSTER_CONF)

        for element in conf:
            if element['name'] == cluster:
                configuration = element['configuration']
                members = element['members']
                return True
        return False

    ___ _init_ui
        # ensure conf is loaded
        if not _load_from_conf():
            return False

        layout = QVBoxLayout(self)

        # Network members
        members_group_box = QGroupBox('Members', self)

        members_layout = QVBoxLayout(self)

        members_table = QTableWidget(self)

        members_table.setRowCount(1)
        members_table.setColumnCount(len(HEADERS))
        members_table.verticalHeader().hide()
        members_table.setHorizontalHeaderLabels(HEADERS)
        members_table.hH.. .setSectionResizeMode(QHeaderView.Stretch)
        members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row = 0
        for member in members:
            column = 0
            for key in HEADERS:
                if key in member:
                    members_table.setItem(row, column, QTableWidgetItem(member[key]))
                else:
                    members_table.setCellWidget(row, column, QPushButton('test'))
                column += 1
            row += 1
        #
        # self.members_table.setItem(0, 0, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 1, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 2, QTableWidgetItem('test'))
        # self.members_table.setCellWidget(0, 3, QPushButton('test'))
        # self.members_table.setCellWidget(0, 4, QPushButton('test'))

        members_layout.addWidget(members_table)
        members_group_box.setLayout(members_layout)
        layout.addWidget(members_group_box)

