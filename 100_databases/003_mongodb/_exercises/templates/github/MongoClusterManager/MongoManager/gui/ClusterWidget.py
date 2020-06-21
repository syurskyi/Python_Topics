_______ logging.config

____ ?.?W.. _______ QWidget, QVBoxLayout, QGroupBox, ?PB.., QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView


____ app.ConfigurationManager _______ ConfigurationManager

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'
HEADERS = ['hostname', 'port', 'role', 'status', 'installed']


c_ ClusterWidget(QWidget):
    ___  - (self, cluster, p.._N..
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

        ___ element __ conf:
            __ element['name'] __ cluster:
                configuration = element['configuration']
                members = element['members']
                return True
        return False

    ___ _init_ui
        # ensure conf is loaded
        __ not _load_from_conf():
            return False

        layout = QVBoxLayout(self)

        # Network members
        members_group_box = QGroupBox('Members', self)

        members_layout = QVBoxLayout(self)

        members_table = QTableWidget(self)

        members_table.sRC..(1)
        members_table.sCC..(le.(HEADERS))
        members_table.verticalHeader().hide()
        members_table.sHHL..(HEADERS)
        members_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row = 0
        ___ member __ members:
            column = 0
            ___ key __ HEADERS:
                __ key __ member:
                    members_table.setItem(row, column, QTableWidgetItem(member[key]))
                ____
                    members_table.setCellWidget(row, column, ?PB..('test'))
                column += 1
            row += 1
        #
        # self.members_table.setItem(0, 0, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 1, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 2, QTableWidgetItem('test'))
        # self.members_table.setCellWidget(0, 3, QPushButton('test'))
        # self.members_table.setCellWidget(0, 4, QPushButton('test'))

        members_layout.aW..(members_table)
        members_group_box.sL..(members_layout)
        layout.aW..(members_group_box)

