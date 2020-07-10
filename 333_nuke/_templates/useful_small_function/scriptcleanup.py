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

______ nuke

___
    ____ ?.?G.. ______ *
    ____ ?.?C.. ______ *
except ImportError:
    ____ ?.?G.. ______ *
    ____ ?.?C.. ______ *
    ____ ?.?W.. ______ *


___ collect_nodes(mode):
    """
    get all nodes of the search of selected dependent/ dependencies
    @param mode: list mode of dependents/ dependencies searching mode
    :return: list nodes to cleanup
    """

    cleanup_list = []
    dependent_ = mode[0]
    dependencies_ = mode[1]

    ___ node __ nuke.allNodes():

        __ node.Class() __ ignore_list:
            continue

        __ dependent_ and dependencies_:
            __ le.(node.dependent()) __ 0 and le.(node.dependencies()) __ 0 and node.minInputs() > 0 and node.maxOutputs() > 0:
                cleanup_list.append(node)

        ____ dependent_ and no. dependencies_ and node.maxOutputs() > 0:
            __ le.(node.dependent()) __ 0:
                cleanup_list.append(node)

        ____ no. dependent_ and dependencies_ and node.minInputs() > 0 and node.maxOutputs() > 0:
            __ le.(node.dependencies()) __ 0:
                cleanup_list.append(node)

        else:
            __ node.minInputs() > 0 and node.inputs() __ 0:
                cleanup_list.append(node)

    r_ cleanup_list


___ cleanup():
    """
    show cleanup window
    :return: None
    """

    g__ c
    c = CleanModeDialog()
    c.raise_()
    c.s__


c_ CleanModeDialog(?W..):
    """
    dialog to ask for cleanup mode (dependent and dependencies)
    """

    ___ -
        s_(CleanModeDialog, self).- ()
        sQT..("Please choose the cleanup mode")
        setFixedWidth(550)

        # buildUI
        create_widgets()
        create_layouts()
        create_signals()

    ___ create_widgets
        check_dependent = QCheckBox("dependent: Node's output is not used (all nodes that read information from this node)")
        check_dependent.setChecked(T..)
        check_dependencies = QCheckBox("dependencies: Node's input is not used (all nodes referred to by this node)")
        check_dependencies.setChecked(T..)
        push_collect = ?PB..("collect")
        push_collect.setStyleSheet("QPushButton{background-color: rgba(51, 204, 255, 150);}")
        push_cancel = ?PB..("cancel")

    ___ create_layouts
        layout_master = ?VB..
        layout_master.aW..(check_dependent)
        layout_master.aW..(check_dependencies)

        layout_push = QHBoxLayout()
        layout_push.aW..(push_collect)
        layout_push.aW..(push_cancel)
        layout_master.addLayout(layout_push)

        sL..(layout_master)

    ___ create_signals
        push_cancel.c__.c..(close)
        push_collect.c__.c..(process_cleanup)

    ___ process_cleanup
        """
        process cleanup and create cleanup table
        :return: None
        """

        cleanup_list = collect_nodes([check_dependent.isChecked(), check_dependencies.isChecked()])
        populate(cleanup_list)
        sQT..("cleanup script")

    ___ populate(self, cleanup_list):
        """
        create widgets for each cleanup node
        @param: cleanup_list: list of nodes to cleanup
        :return: None
        """

        ___
            group_cleanup.setParent(N..)
            push_close.setParent(N..)
        except Exception, e:
            pass

        table_cleanup = QTableWidget()

        checkboxes = []

        # set dimensions
        table_cleanup.setRowCount(le.(cleanup_list))
        table_cleanup.setColumnCount(3)
        table_cleanup.setColumnWidth(0, 250)
        table_cleanup.horizontalHeader().setStretchLastSection(T..)

        # header
        table_cleanup.setHorizontalHeaderItem(0, QTableWidgetItem("node"))
        table_cleanup.setHorizontalHeaderItem(1, QTableWidgetItem("check"))
        table_cleanup.setHorizontalHeaderItem(2, QTableWidgetItem("delete"))

        r = 0
        ___ node __ cleanup_list:

            # node
            push_node = ?PB..(node.name())
            push_node.setProperty("node", node.name())
            table_cleanup.setCellWidget(r, 0, push_node)
            push_node.c__.c..(jump_to_node)

            # push checkbox
            widget = ?W..()
            layout_widget = QHBoxLayout()
            checkbox = QCheckBox()
            checkbox.setProperty("node", node.name())
            layout_widget.addStretch()
            layout_widget.aW..(checkbox)
            layout_widget.addStretch()
            widget.sL..(layout_widget)
            table_cleanup.setCellWidget(r, 1, widget)
            checkboxes.append(checkbox)

            # remove push
            push_remove_node = ?PB..("delete")
            push_remove_node.setProperty("node", node.name())
            push_remove_node.setStyleSheet("QPushButton{background-color: rgb(90,30,30);}")
            table_cleanup.setCellWidget(r, 2, push_remove_node)
            push_remove_node.c__.c..(lambda r=r, node=node: remove_node(r, node.name()))

            r += 1

        # resize main
        resize(QSize(width(), 200 + (r * 40)))

        group_cleanup = QGroupBox()
        layout_cleanup_master = ?VB..
        layout_cleanup_master.aW..(table_cleanup)

        push_toggle = ?PB..("toggle check/uncheck nodes")
        push_disable_checked = ?PB..("disable all checked nodes")
        push_remove_checked = ?PB..("remove all checked nodes")
        layout_cleanup_push = QHBoxLayout()
        layout_cleanup_push.aW..(push_toggle)
        layout_cleanup_push.aW..(push_disable_checked)
        layout_cleanup_push.aW..(push_remove_checked)
        layout_cleanup_master.addLayout(layout_cleanup_push)
        group_cleanup.sL..(layout_cleanup_master)

        push_toggle.c__.c..(toggle_checkboxes)
        push_disable_checked.c__.c..(disable_checked)
        push_remove_checked.c__.c..(remove_nodes)

        push_close = ?PB..("close")
        push_close.c__.c..(close)
        layout_master.aW..(group_cleanup)
        layout_master.aW..(push_close)

    ___ jump_to_node
        """
        jump to clicked node name
        :return: None
        """

        node = nuke.toNode(sender().property("node"))
        node.selectOnly()
        nuke.zoom(1, (node.xpos(), node.ypos()))

    ___ remove_node(self, row, node):
        """
        remove node
        @param row: int row to remove from table
        @param node: String name of node to remove
        :return: None
        """

        nuke.delete(nuke.toNode(node))
        process_cleanup()

    ___ remove_nodes
        """
        remove all checked nodes
        :return: None
        """

        ___ c __ checkboxes:
            __ c.isChecked():
                nuke.delete(nuke.toNode(c.property("node")))

        cleanup_list = collect_nodes([check_dependent.isChecked(), check_dependencies.isChecked()])
        process_cleanup()

    ___ disable_checked
        """
        disable checked nodes
        :return: None
        """

        ___ c __ checkboxes:
            ___
                disable = nuke.toNode(c.property("node"))["disable"].setValue(c.isChecked())
            except Exception, e:
                continue

    ___ toggle_checkboxes
        """
        toggle check/uncheck checkboxes
        :return: None
        """

        __ checkboxes[0].isChecked():
            ___ c __ checkboxes:
                c.setChecked(False)
        else:
            ___ c __ checkboxes:
                c.setChecked(T..)

    ___ keyPressEvent(self, event):
        """
        close on escape key pressed
        :return: None
        """

        __ event.key() __ __.Key_Escape:
            c__
