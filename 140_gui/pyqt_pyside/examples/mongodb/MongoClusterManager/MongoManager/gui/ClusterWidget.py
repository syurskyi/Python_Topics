import logging.config

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView


from app.ConfigurationManager import ConfigurationManager

APP_CONF = 'conf/app.conf'
CLUSTER_CONF = 'conf/cluster.conf'
HEADERS = ['hostname', 'port', 'role', 'status', 'installed']


class ClusterWidget(QWidget):
    def __init__(self, cluster, parent=None):
        QWidget.__init__(self, parent)

        # Set base vars
        self.cluster = cluster
        self.conf_manager = ConfigurationManager()

        self.configuration = {}
        self.members = []

        # Set UI
        self._init_ui()

    def _load_from_conf(self):
        conf = self.conf_manager.get(CLUSTER_CONF)

        for element in conf:
            if element['name'] == self.cluster:
                self.configuration = element['configuration']
                self.members = element['members']
                return True
        return False

    def _init_ui(self):
        # ensure conf is loaded
        if not self._load_from_conf():
            return False

        self.layout = QVBoxLayout(self)

        # Network members
        self.members_group_box = QGroupBox('Members', self)

        self.members_layout = QVBoxLayout(self)

        self.members_table = QTableWidget(self)

        self.members_table.setRowCount(1)
        self.members_table.setColumnCount(len(HEADERS))
        self.members_table.verticalHeader().hide()
        self.members_table.setHorizontalHeaderLabels(HEADERS)
        self.members_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.members_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        row = 0
        for member in self.members:
            column = 0
            for key in HEADERS:
                if key in member:
                    self.members_table.setItem(row, column, QTableWidgetItem(member[key]))
                else:
                    self.members_table.setCellWidget(row, column, QPushButton('test'))
                column += 1
            row += 1
        #
        # self.members_table.setItem(0, 0, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 1, QTableWidgetItem('test'))
        # self.members_table.setItem(0, 2, QTableWidgetItem('test'))
        # self.members_table.setCellWidget(0, 3, QPushButton('test'))
        # self.members_table.setCellWidget(0, 4, QPushButton('test'))

        self.members_layout.addWidget(self.members_table)
        self.members_group_box.setLayout(self.members_layout)
        self.layout.addWidget(self.members_group_box)

