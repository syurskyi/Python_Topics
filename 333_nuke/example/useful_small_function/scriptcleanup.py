###########################################################################################################
#
#  scriptCleanup
#
#  @author simon jokuschies
#  @version 1.1
#  @contact info@leafpictures.de
#  @website www.leafpictures.de
#  @pluginurl: www.leafpictures.de/code/script-cleanup
#
#  description:
#  collect all nodes that are not connected to any node and/ or which output is not used at all in the current script.
#  Hold Shift and press C. This opens the scriptCleanup window in which you can choose to select:
#
#  dependent nodes: Node's output is not used; Nodes that are connected to the node's output
#                   (all nodes that read information from this node)
#
#  dependency nodes: Node's input is not used; Nodes that are connected to the node's input
#                   (all nodes referred to by this node)
#
#  if nothing is select: check for all nodes that don't have any inputs connected
#
#  in both methods (dependent/dependencies) these node connection options are included:
#  connection via expressions
#  connection via visible input pipes
#  connection via hidden input pipes
#
#
#  after clicking the "collect" button the window shows unused nodes depending on the selected mode: nodes that are
#  not connected to any node and/ or which output is not used at all.
#
#  The nodes table shows a row for each unused node:
#      # a button with the name of the unused node. By clicking it the dag gets navigated to the node
#      # a checkbox for batch processing disable/enable (se below)
#      # a button to remove the node
#
#  At the bottom of the window you have three buttons:
#  # toggle check/uncheck nodes: check or uncheck all unused nodes in the table
#  # disable all checked nodes: click this button to disable all checked nodes. If a checkbox is unchecked then
#    the unused node will be enabled
#  # remove all checked nodes: click this button to remove all checked nodes
#
#  instalation
#
#  put the whole scriptCleanup folder in your nuke home directory
#  in init.py in your nuke home directory add this line (without "#"):
#
#  nuke.pluginAddPath("scriptCleanup")
#
#
#  Version info
#
#  v1.1
#  - Make ready for Nuke 11
#
#  v1.0
#  - Initial release
#
##########################################################################################################

# ignore_list
# ignore all nodes that are from one of these node classes
ignore_list = ["BackdropNode"]

# no need to change anything from here. Edit only if you exactly know what you're doing

import nuke

try:
    from PySide.QtGui import *
    from PySide.QtCore import *
except ImportError:
    from PySide2.QtGui import *
    from PySide2.QtCore import *
    from PySide2.QtWidgets import *


def collect_nodes(mode):
    """
    get all nodes of the search of selected dependent/ dependencies
    @param mode: list mode of dependents/ dependencies searching mode
    :return: list nodes to cleanup
    """

    cleanup_list = []
    dependent_ = mode[0]
    dependencies_ = mode[1]

    for node in nuke.allNodes():

        if node.Class() in ignore_list:
            continue

        if dependent_ and dependencies_:
            if len(node.dependent()) == 0 and len(node.dependencies()) == 0 and node.minInputs() > 0 and node.maxOutputs() > 0:
                cleanup_list.append(node)

        elif dependent_ and not dependencies_ and node.maxOutputs() > 0:
            if len(node.dependent()) == 0:
                cleanup_list.append(node)

        elif not dependent_ and dependencies_ and node.minInputs() > 0 and node.maxOutputs() > 0:
            if len(node.dependencies()) == 0:
                cleanup_list.append(node)

        else:
            if node.minInputs() > 0 and node.inputs() == 0:
                cleanup_list.append(node)

    return cleanup_list


def cleanup():
    """
    show cleanup window
    :return: None
    """

    global c
    c = CleanModeDialog()
    c.raise_()
    c.show()


class CleanModeDialog(QWidget):
    """
    dialog to ask for cleanup mode (dependent and dependencies)
    """

    def __init__(self):
        super(CleanModeDialog, self).__init__()
        self.setWindowTitle("Please choose the cleanup mode")
        self.setFixedWidth(550)

        # buildUI
        self.create_widgets()
        self.create_layouts()
        self.create_signals()

    def create_widgets(self):
        self.check_dependent = QCheckBox("dependent: Node's output is not used (all nodes that read information from this node)")
        self.check_dependent.setChecked(True)
        self.check_dependencies = QCheckBox("dependencies: Node's input is not used (all nodes referred to by this node)")
        self.check_dependencies.setChecked(True)
        self.push_collect = QPushButton("collect")
        self.push_collect.setStyleSheet("QPushButton{background-color: rgba(51, 204, 255, 150);}")
        self.push_cancel = QPushButton("cancel")

    def create_layouts(self):
        self.layout_master = QVBoxLayout()
        self.layout_master.addWidget(self.check_dependent)
        self.layout_master.addWidget(self.check_dependencies)

        self.layout_push = QHBoxLayout()
        self.layout_push.addWidget(self.push_collect)
        self.layout_push.addWidget(self.push_cancel)
        self.layout_master.addLayout(self.layout_push)

        self.setLayout(self.layout_master)

    def create_signals(self):
        self.push_cancel.clicked.connect(self.close)
        self.push_collect.clicked.connect(self.process_cleanup)

    def process_cleanup(self):
        """
        process cleanup and create cleanup table
        :return: None
        """

        cleanup_list = collect_nodes([self.check_dependent.isChecked(), self.check_dependencies.isChecked()])
        self.populate(cleanup_list)
        self.setWindowTitle("cleanup script")

    def populate(self, cleanup_list):
        """
        create widgets for each cleanup node
        @param: cleanup_list: list of nodes to cleanup
        :return: None
        """

        try:
            self.group_cleanup.setParent(None)
            self.push_close.setParent(None)
        except Exception, e:
            pass

        self.table_cleanup = QTableWidget()

        self.checkboxes = []

        # set dimensions
        self.table_cleanup.setRowCount(len(cleanup_list))
        self.table_cleanup.setColumnCount(3)
        self.table_cleanup.setColumnWidth(0, 250)
        self.table_cleanup.horizontalHeader().setStretchLastSection(True)

        # header
        self.table_cleanup.setHorizontalHeaderItem(0, QTableWidgetItem("node"))
        self.table_cleanup.setHorizontalHeaderItem(1, QTableWidgetItem("check"))
        self.table_cleanup.setHorizontalHeaderItem(2, QTableWidgetItem("delete"))

        r = 0
        for node in cleanup_list:

            # node
            self.push_node = QPushButton(node.name())
            self.push_node.setProperty("node", node.name())
            self.table_cleanup.setCellWidget(r, 0, self.push_node)
            self.push_node.clicked.connect(self.jump_to_node)

            # push checkbox
            self.widget = QWidget()
            self.layout_widget = QHBoxLayout()
            self.checkbox = QCheckBox()
            self.checkbox.setProperty("node", node.name())
            self.layout_widget.addStretch()
            self.layout_widget.addWidget(self.checkbox)
            self.layout_widget.addStretch()
            self.widget.setLayout(self.layout_widget)
            self.table_cleanup.setCellWidget(r, 1, self.widget)
            self.checkboxes.append(self.checkbox)

            # remove push
            self.push_remove_node = QPushButton("delete")
            self.push_remove_node.setProperty("node", node.name())
            self.push_remove_node.setStyleSheet("QPushButton{background-color: rgb(90,30,30);}")
            self.table_cleanup.setCellWidget(r, 2, self.push_remove_node)
            self.push_remove_node.clicked.connect(lambda r=r, node=node: self.remove_node(r, node.name()))

            r += 1

        # resize main
        self.resize(QSize(self.width(), 200 + (r * 40)))

        self.group_cleanup = QGroupBox()
        self.layout_cleanup_master = QVBoxLayout()
        self.layout_cleanup_master.addWidget(self.table_cleanup)

        self.push_toggle = QPushButton("toggle check/uncheck nodes")
        self.push_disable_checked = QPushButton("disable all checked nodes")
        self.push_remove_checked = QPushButton("remove all checked nodes")
        self.layout_cleanup_push = QHBoxLayout()
        self.layout_cleanup_push.addWidget(self.push_toggle)
        self.layout_cleanup_push.addWidget(self.push_disable_checked)
        self.layout_cleanup_push.addWidget(self.push_remove_checked)
        self.layout_cleanup_master.addLayout(self.layout_cleanup_push)
        self.group_cleanup.setLayout(self.layout_cleanup_master)

        self.push_toggle.clicked.connect(self.toggle_checkboxes)
        self.push_disable_checked.clicked.connect(self.disable_checked)
        self.push_remove_checked.clicked.connect(self.remove_nodes)

        self.push_close = QPushButton("close")
        self.push_close.clicked.connect(self.close)
        self.layout_master.addWidget(self.group_cleanup)
        self.layout_master.addWidget(self.push_close)

    def jump_to_node(self):
        """
        jump to clicked node name
        :return: None
        """

        node = nuke.toNode(self.sender().property("node"))
        node.selectOnly()
        nuke.zoom(1, (node.xpos(), node.ypos()))

    def remove_node(self, row, node):
        """
        remove node
        @param row: int row to remove from table
        @param node: String name of node to remove
        :return: None
        """

        nuke.delete(nuke.toNode(node))
        self.process_cleanup()

    def remove_nodes(self):
        """
        remove all checked nodes
        :return: None
        """

        for c in self.checkboxes:
            if c.isChecked():
                nuke.delete(nuke.toNode(c.property("node")))

        cleanup_list = collect_nodes([self.check_dependent.isChecked(), self.check_dependencies.isChecked()])
        self.process_cleanup()

    def disable_checked(self):
        """
        disable checked nodes
        :return: None
        """

        for c in self.checkboxes:
            try:
                disable = nuke.toNode(c.property("node"))["disable"].setValue(c.isChecked())
            except Exception, e:
                continue

    def toggle_checkboxes(self):
        """
        toggle check/uncheck checkboxes
        :return: None
        """

        if self.checkboxes[0].isChecked():
            for c in self.checkboxes:
                c.setChecked(False)
        else:
            for c in self.checkboxes:
                c.setChecked(True)

    def keyPressEvent(self, event):
        """
        close on escape key pressed
        :return: None
        """

        if event.key() == Qt.Key_Escape:
            self.close()
