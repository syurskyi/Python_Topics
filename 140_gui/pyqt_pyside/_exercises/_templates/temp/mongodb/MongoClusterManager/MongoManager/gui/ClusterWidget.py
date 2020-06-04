______ l__.c..

____ ?.QtWidgets ______ QWidget, QVBoxLayout, QGroupBox, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView


____ app.ConfigurationManager ______ ConfigurationManager

APP_CONF _ 'conf/app.conf'
CLUSTER_CONF _ 'conf/cluster.conf'
HEADERS _ ['hostname', 'port', 'role', 'status', 'installed']


c_ ClusterWidget(QWidget):
    ___  -   cluster, parent_None):
        QWidget. -   parent)

        # Set base vars
        cluster _ cluster
        conf_manager _ ConfigurationManager()

        configuration _    # dict
        members _   # list

        # Set UI
        _init_ui()

    ___ _load_from_conf
        conf _ conf_manager.get(CLUSTER_CONF)

        ___ element in conf:
            __ element['name'] __ cluster:
                configuration _ element['configuration']
                members _ element['members']
                r_ True
        r_ False

    ___ _init_ui
        # ensure conf is loaded
        __ not _load_from_conf():
            r_ False

        layout _ QVBoxLayout(self)

        # Network members
        members_group_box _ QGroupBox('Members', self)

        members_layout _ QVBoxLayout(self)

        members_table _ QTableWidget(self)

        members_table.setRowCount(1)
        members_table.setColumnCount(len(HEADERS))
        members_table.verticalHeader().hide()
        members_table.setHorizontalHeaderLabels(HEADERS)
        members_table.hH.. .setSectionResizeMode(QHeaderView.Stretch)
        members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row _ 0
        ___ member in members:
            column _ 0
            ___ key in HEADERS:
                __ key in member:
                    members_table.setItem(row, column, QTableWidgetItem(member[key]))
                ____
                    members_table.setCellWidget(row, column, QPushButton('test'))
                column +_ 1
            row +_ 1
        #
        # self.members_table.setItem(0, 0, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 1, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 2, QTableWidgetItem('test'))
        # self.members_table.setCellWidget(0, 3, QPushButton('test'))
        # self.members_table.setCellWidget(0, 4, QPushButton('test'))

        members_layout.addWidget(members_table)
        members_group_box.setLayout(members_layout)
        layout.addWidget(members_group_box)

