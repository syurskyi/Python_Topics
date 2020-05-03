"""Minimal Python 2 & 3 shim around all Qt bindings

DOCUMENTATION
    Qt.py was born in the film and visual effects industry to address
    the growing need for the development of software capable of running
    with more than one flavour of the Qt bindings for Python - PySide,
    PySide2, PyQt4 and PyQt5.

    1. Build for one, run with all
    2. Explicit is better than implicit
    3. Support co-existence

    Default resolution order:
        - PySide2
        - PyQt5
        - PySide
        - PyQt4

    Usage:
        >> import sys
        >> from Qt import QtWidgets
        >> app = QtWidgets.QApplication(sys.argv)
        >> button = QtWidgets.QPushButton("Hello World")
        >> button.show()
        >> app.exec_()

    All members of PySide2 are mapped from other bindings, should they exist.
    If no equivalent member exist, it is excluded from Qt.py and inaccessible.
    The idea is to highlight members that exist across all supported binding,
    and guarantee that code that runs on one binding runs on all others.

    For more details, visit https://github.com/mottosso/Qt.py

LICENSE

    See end of file for license (MIT, BSD) information.

"""

_____ os
_____ ___
_____ types
_____ shutil


__version__ _ "1.1.0.b5"

# Enable support for `from Qt import *`
__all__ _ []

# Flags from environment variables
QT_VERBOSE _ bool(os.getenv("QT_VERBOSE"))
QT_PREFERRED_BINDING _ os.getenv("QT_PREFERRED_BINDING", "")
QT_SIP_API_HINT _ os.getenv("QT_SIP_API_HINT")

# Reference to Qt.py
Qt _ ___.modules[__name__]
Qt.QtCompat _ types.ModuleType("QtCompat")

___
    long
_____ NameError:
    # Python 3 compatibility
    long _ int

"""Common members of all bindings

This is where each member of Qt.py is explicitly defined.
It is based on a "lowest common denominator" of all bindings;
including members found in each of the 4 bindings.

Find or add excluded members in build_membership.py

"""

_common_members _ {
    "QtCore": [
        "QAbstractAnimation",
        "QAbstractEventDispatcher",
        "QAbstractItemModel",
        "QAbstractListModel",
        "QAbstractState",
        "QAbstractTableModel",
        "QAbstractTransition",
        "QAnimationGroup",
        "QBasicTimer",
        "QBitArray",
        "QBuffer",
        "QByteArray",
        "QByteArrayMatcher",
        "QChildEvent",
        "QCoreApplication",
        "QCryptographicHash",
        "QDataStream",
        "QDate",
        "QDateTime",
        "QDir",
        "QDirIterator",
        "QDynamicPropertyChangeEvent",
        "QEasingCurve",
        "QElapsedTimer",
        "QEvent",
        "QEventLoop",
        "QEventTransition",
        "QFile",
        "QFileInfo",
        "QFileSystemWatcher",
        "QFinalState",
        "QGenericArgument",
        "QGenericReturnArgument",
        "QHistoryState",
        "QIODevice",
        "QLibraryInfo",
        "QLine",
        "QLineF",
        "QLocale",
        "QMargins",
        "QMetaClassInfo",
        "QMetaEnum",
        "QMetaMethod",
        "QMetaObject",
        "QMetaProperty",
        "QMimeData",
        "QModelIndex",
        "QMutex",
        "QMutexLocker",
        "QObject",
        "QParallelAnimationGroup",
        "QPauseAnimation",
        "QPersistentModelIndex",
        "QPluginLoader",
        "QPoint",
        "QPointF",
        "QProcess",
        "QProcessEnvironment",
        "QPropertyAnimation",
        "QReadLocker",
        "QReadWriteLock",
        "QRect",
        "QRectF",
        "QRegExp",
        "QResource",
        "QRunnable",
        "QSemaphore",
        "QSequentialAnimationGroup",
        "QSettings",
        "QSignalMapper",
        "QSignalTransition",
        "QSize",
        "QSizeF",
        "QSocketNotifier",
        "QState",
        "QStateMachine",
        "QSysInfo",
        "QSystemSemaphore",
        "QT_TRANSLATE_NOOP",
        "QT_TR_NOOP",
        "QT_TR_NOOP_UTF8",
        "QTemporaryFile",
        "QTextBoundaryFinder",
        "QTextCodec",
        "QTextDecoder",
        "QTextEncoder",
        "QTextStream",
        "QTextStreamManipulator",
        "QThread",
        "QThreadPool",
        "QTime",
        "QTimeLine",
        "QTimer",
        "QTimerEvent",
        "QTranslator",
        "QUrl",
        "QVariantAnimation",
        "QWaitCondition",
        "QWriteLocker",
        "QXmlStreamAttribute",
        "QXmlStreamAttributes",
        "QXmlStreamEntityDeclaration",
        "QXmlStreamEntityResolver",
        "QXmlStreamNamespaceDeclaration",
        "QXmlStreamNotationDeclaration",
        "QXmlStreamReader",
        "QXmlStreamWriter",
        "Qt",
        "QtCriticalMsg",
        "QtDebugMsg",
        "QtFatalMsg",
        "QtMsgType",
        "QtSystemMsg",
        "QtWarningMsg",
        "qAbs",
        "qAddPostRoutine",
        "qChecksum",
        "qCritical",
        "qDebug",
        "qFatal",
        "qFuzzyCompare",
        "qIsFinite",
        "qIsInf",
        "qIsNaN",
        "qIsNull",
        "qRegisterResourceData",
        "qUnregisterResourceData",
        "qVersion",
        "qWarning",
        "qrand",
        "qsrand"
    ],
    "QtGui": [
        "QAbstractTextDocumentLayout",
        "QActionEvent",
        "QBitmap",
        "QBrush",
        "QClipboard",
        "QCloseEvent",
        "QColor",
        "QConicalGradient",
        "QContextMenuEvent",
        "QCursor",
        "QDoubleValidator",
        "QDrag",
        "QDragEnterEvent",
        "QDragLeaveEvent",
        "QDragMoveEvent",
        "QDropEvent",
        "QFileOpenEvent",
        "QFocusEvent",
        "QFont",
        "QFontDatabase",
        "QFontInfo",
        "QFontMetrics",
        "QFontMetricsF",
        "QGradient",
        "QHelpEvent",
        "QHideEvent",
        "QHoverEvent",
        "QIcon",
        "QIconDragEvent",
        "QIconEngine",
        "QImage",
        "QImageIOHandler",
        "QImageReader",
        "QImageWriter",
        "QInputEvent",
        "QInputMethodEvent",
        "QIntValidator",
        "QKeyEvent",
        "QKeySequence",
        "QLinearGradient",
        "QMatrix2x2",
        "QMatrix2x3",
        "QMatrix2x4",
        "QMatrix3x2",
        "QMatrix3x3",
        "QMatrix3x4",
        "QMatrix4x2",
        "QMatrix4x3",
        "QMatrix4x4",
        "QMouseEvent",
        "QMoveEvent",
        "QMovie",
        "QPaintDevice",
        "QPaintEngine",
        "QPaintEngineState",
        "QPaintEvent",
        "QPainter",
        "QPainterPath",
        "QPainterPathStroker",
        "QPalette",
        "QPen",
        "QPicture",
        "QPictureIO",
        "QPixmap",
        "QPixmapCache",
        "QPolygon",
        "QPolygonF",
        "QQuaternion",
        "QRadialGradient",
        "QRegExpValidator",
        "QRegion",
        "QResizeEvent",
        "QSessionManager",
        "QShortcutEvent",
        "QShowEvent",
        "QStandardItem",
        "QStandardItemModel",
        "QStatusTipEvent",
        "QSyntaxHighlighter",
        "QTabletEvent",
        "QTextBlock",
        "QTextBlockFormat",
        "QTextBlockGroup",
        "QTextBlockUserData",
        "QTextCharFormat",
        "QTextCursor",
        "QTextDocument",
        "QTextDocumentFragment",
        "QTextFormat",
        "QTextFragment",
        "QTextFrame",
        "QTextFrameFormat",
        "QTextImageFormat",
        "QTextInlineObject",
        "QTextItem",
        "QTextLayout",
        "QTextLength",
        "QTextLine",
        "QTextList",
        "QTextListFormat",
        "QTextObject",
        "QTextObjectInterface",
        "QTextOption",
        "QTextTable",
        "QTextTableCell",
        "QTextTableCellFormat",
        "QTextTableFormat",
        "QTouchEvent",
        "QTransform",
        "QValidator",
        "QVector2D",
        "QVector3D",
        "QVector4D",
        "QWhatsThisClickedEvent",
        "QWheelEvent",
        "QWindowStateChangeEvent",
        "qAlpha",
        "qBlue",
        "qGray",
        "qGreen",
        "qIsGray",
        "qRed",
        "qRgb",
        "qRgba"
    ],
    "QtHelp": [
        "QHelpContentItem",
        "QHelpContentModel",
        "QHelpContentWidget",
        "QHelpEngine",
        "QHelpEngineCore",
        "QHelpIndexModel",
        "QHelpIndexWidget",
        "QHelpSearchEngine",
        "QHelpSearchQuery",
        "QHelpSearchQueryWidget",
        "QHelpSearchResultWidget"
    ],
    "QtNetwork": [
        "QAbstractNetworkCache",
        "QAbstractSocket",
        "QAuthenticator",
        "QHostAddress",
        "QHostInfo",
        "QLocalServer",
        "QLocalSocket",
        "QNetworkAccessManager",
        "QNetworkAddressEntry",
        "QNetworkCacheMetaData",
        "QNetworkConfiguration",
        "QNetworkConfigurationManager",
        "QNetworkCookie",
        "QNetworkCookieJar",
        "QNetworkDiskCache",
        "QNetworkInterface",
        "QNetworkProxy",
        "QNetworkProxyFactory",
        "QNetworkProxyQuery",
        "QNetworkReply",
        "QNetworkRequest",
        "QNetworkSession",
        "QSsl",
        "QTcpServer",
        "QTcpSocket",
        "QUdpSocket"
    ],
    "QtSql": [
        "QSql",
        "QSqlDatabase",
        "QSqlDriver",
        "QSqlDriverCreatorBase",
        "QSqlError",
        "QSqlField",
        "QSqlIndex",
        "QSqlQuery",
        "QSqlQueryModel",
        "QSqlRecord",
        "QSqlRelation",
        "QSqlRelationalDelegate",
        "QSqlRelationalTableModel",
        "QSqlResult",
        "QSqlTableModel"
    ],
    "QtSvg": [
        "QGraphicsSvgItem",
        "QSvgGenerator",
        "QSvgRenderer",
        "QSvgWidget"
    ],
    "QtTest": [
        "QTest"
    ],
    "QtWidgets": [
        "QAbstractButton",
        "QAbstractGraphicsShapeItem",
        "QAbstractItemDelegate",
        "QAbstractItemView",
        "QAbstractScrollArea",
        "QAbstractSlider",
        "QAbstractSpinBox",
        "QAction",
        "QActionGroup",
        "QApplication",
        "QBoxLayout",
        "QButtonGroup",
        "QCalendarWidget",
        "QCheckBox",
        "QColorDialog",
        "QColumnView",
        "QComboBox",
        "QCommandLinkButton",
        "QCommonStyle",
        "QCompleter",
        "QDataWidgetMapper",
        "QDateEdit",
        "QDateTimeEdit",
        "QDesktopWidget",
        "QDial",
        "QDialog",
        "QDialogButtonBox",
        "QDirModel",
        "QDockWidget",
        "QDoubleSpinBox",
        "QErrorMessage",
        "QFileDialog",
        "QFileIconProvider",
        "QFileSystemModel",
        "QFocusFrame",
        "QFontComboBox",
        "QFontDialog",
        "QFormLayout",
        "QFrame",
        "QGesture",
        "QGestureEvent",
        "QGestureRecognizer",
        "QGraphicsAnchor",
        "QGraphicsAnchorLayout",
        "QGraphicsBlurEffect",
        "QGraphicsColorizeEffect",
        "QGraphicsDropShadowEffect",
        "QGraphicsEffect",
        "QGraphicsEllipseItem",
        "QGraphicsGridLayout",
        "QGraphicsItem",
        "QGraphicsItemGroup",
        "QGraphicsLayout",
        "QGraphicsLayoutItem",
        "QGraphicsLineItem",
        "QGraphicsLinearLayout",
        "QGraphicsObject",
        "QGraphicsOpacityEffect",
        "QGraphicsPathItem",
        "QGraphicsPixmapItem",
        "QGraphicsPolygonItem",
        "QGraphicsProxyWidget",
        "QGraphicsRectItem",
        "QGraphicsRotation",
        "QGraphicsScale",
        "QGraphicsScene",
        "QGraphicsSceneContextMenuEvent",
        "QGraphicsSceneDragDropEvent",
        "QGraphicsSceneEvent",
        "QGraphicsSceneHelpEvent",
        "QGraphicsSceneHoverEvent",
        "QGraphicsSceneMouseEvent",
        "QGraphicsSceneMoveEvent",
        "QGraphicsSceneResizeEvent",
        "QGraphicsSceneWheelEvent",
        "QGraphicsSimpleTextItem",
        "QGraphicsTextItem",
        "QGraphicsTransform",
        "QGraphicsView",
        "QGraphicsWidget",
        "QGridLayout",
        "QGroupBox",
        "QHBoxLayout",
        "QHeaderView",
        "QInputDialog",
        "QItemDelegate",
        "QItemEditorCreatorBase",
        "QItemEditorFactory",
        "QKeyEventTransition",
        "QLCDNumber",
        "QLabel",
        "QLayout",
        "QLayoutItem",
        "QLineEdit",
        "QListView",
        "QListWidget",
        "QListWidgetItem",
        "QMainWindow",
        "QMdiArea",
        "QMdiSubWindow",
        "QMenu",
        "QMenuBar",
        "QMessageBox",
        "QMouseEventTransition",
        "QPanGesture",
        "QPinchGesture",
        "QPlainTextDocumentLayout",
        "QPlainTextEdit",
        "QProgressBar",
        "QProgressDialog",
        "QPushButton",
        "QRadioButton",
        "QRubberBand",
        "QScrollArea",
        "QScrollBar",
        "QShortcut",
        "QSizeGrip",
        "QSizePolicy",
        "QSlider",
        "QSpacerItem",
        "QSpinBox",
        "QSplashScreen",
        "QSplitter",
        "QSplitterHandle",
        "QStackedLayout",
        "QStackedWidget",
        "QStatusBar",
        "QStyle",
        "QStyleFactory",
        "QStyleHintReturn",
        "QStyleHintReturnMask",
        "QStyleHintReturnVariant",
        "QStyleOption",
        "QStyleOptionButton",
        "QStyleOptionComboBox",
        "QStyleOptionComplex",
        "QStyleOptionDockWidget",
        "QStyleOptionFocusRect",
        "QStyleOptionFrame",
        "QStyleOptionGraphicsItem",
        "QStyleOptionGroupBox",
        "QStyleOptionHeader",
        "QStyleOptionMenuItem",
        "QStyleOptionProgressBar",
        "QStyleOptionRubberBand",
        "QStyleOptionSizeGrip",
        "QStyleOptionSlider",
        "QStyleOptionSpinBox",
        "QStyleOptionTab",
        "QStyleOptionTabBarBase",
        "QStyleOptionTabWidgetFrame",
        "QStyleOptionTitleBar",
        "QStyleOptionToolBar",
        "QStyleOptionToolBox",
        "QStyleOptionToolButton",
        "QStyleOptionViewItem",
        "QStylePainter",
        "QStyledItemDelegate",
        "QSwipeGesture",
        "QSystemTrayIcon",
        "QTabBar",
        "QTabWidget",
        "QTableView",
        "QTableWidget",
        "QTableWidgetItem",
        "QTableWidgetSelectionRange",
        "QTapAndHoldGesture",
        "QTapGesture",
        "QTextBrowser",
        "QTextEdit",
        "QTimeEdit",
        "QToolBar",
        "QToolBox",
        "QToolButton",
        "QToolTip",
        "QTreeView",
        "QTreeWidget",
        "QTreeWidgetItem",
        "QTreeWidgetItemIterator",
        "QUndoCommand",
        "QUndoGroup",
        "QUndoStack",
        "QUndoView",
        "QVBoxLayout",
        "QWhatsThis",
        "QWidget",
        "QWidgetAction",
        "QWidgetItem",
        "QWizard",
        "QWizardPage"
    ],
    "QtXml": [
        "QDomAttr",
        "QDomCDATASection",
        "QDomCharacterData",
        "QDomComment",
        "QDomDocument",
        "QDomDocumentFragment",
        "QDomDocumentType",
        "QDomElement",
        "QDomEntity",
        "QDomEntityReference",
        "QDomImplementation",
        "QDomNamedNodeMap",
        "QDomNode",
        "QDomNodeList",
        "QDomNotation",
        "QDomProcessingInstruction",
        "QDomText",
        "QXmlAttributes",
        "QXmlContentHandler",
        "QXmlDTDHandler",
        "QXmlDeclHandler",
        "QXmlDefaultHandler",
        "QXmlEntityResolver",
        "QXmlErrorHandler",
        "QXmlInputSource",
        "QXmlLexicalHandler",
        "QXmlLocator",
        "QXmlNamespaceSupport",
        "QXmlParseException",
        "QXmlReader",
        "QXmlSimpleReader"
    ],
    "QtXmlPatterns": [
        "QAbstractMessageHandler",
        "QAbstractUriResolver",
        "QAbstractXmlNodeModel",
        "QAbstractXmlReceiver",
        "QSourceLocation",
        "QXmlFormatter",
        "QXmlItem",
        "QXmlName",
        "QXmlNamePool",
        "QXmlNodeModelIndex",
        "QXmlQuery",
        "QXmlResultItems",
        "QXmlSchema",
        "QXmlSchemaValidator",
        "QXmlSerializer"
    ]
}


"""Misplaced members

These members from the original submodule are misplaced relative PySide2

"""
_misplaced_members _ {
    "PySide2": {
        "QtGui.QStringListModel": "QtCore.QStringListModel",
        "QtCore.Property": "QtCore.Property",
        "QtCore.Signal": "QtCore.Signal",
        "QtCore.Slot": "QtCore.Slot",
        "QtCore.QAbstractProxyModel": "QtCore.QAbstractProxyModel",
        "QtCore.QSortFilterProxyModel": "QtCore.QSortFilterProxyModel",
        "QtCore.QItemSelection": "QtCore.QItemSelection",
        "QtCore.QItemSelectionModel": "QtCore.QItemSelectionModel",
    },
    "PyQt5": {
        "QtCore.pyqtProperty": "QtCore.Property",
        "QtCore.pyqtSignal": "QtCore.Signal",
        "QtCore.pyqtSlot": "QtCore.Slot",
        "QtCore.QAbstractProxyModel": "QtCore.QAbstractProxyModel",
        "QtCore.QSortFilterProxyModel": "QtCore.QSortFilterProxyModel",
        "QtCore.QStringListModel": "QtCore.QStringListModel",
        "QtCore.QItemSelection": "QtCore.QItemSelection",
        "QtCore.QItemSelectionModel": "QtCore.QItemSelectionModel",
    },
    "PySide": {
        "QtGui.QAbstractProxyModel": "QtCore.QAbstractProxyModel",
        "QtGui.QSortFilterProxyModel": "QtCore.QSortFilterProxyModel",
        "QtGui.QStringListModel": "QtCore.QStringListModel",
        "QtGui.QItemSelection": "QtCore.QItemSelection",
        "QtGui.QItemSelectionModel": "QtCore.QItemSelectionModel",
        "QtCore.Property": "QtCore.Property",
        "QtCore.Signal": "QtCore.Signal",
        "QtCore.Slot": "QtCore.Slot",

    },
    "PyQt4": {
        "QtGui.QAbstractProxyModel": "QtCore.QAbstractProxyModel",
        "QtGui.QSortFilterProxyModel": "QtCore.QSortFilterProxyModel",
        "QtGui.QItemSelection": "QtCore.QItemSelection",
        "QtGui.QStringListModel": "QtCore.QStringListModel",
        "QtGui.QItemSelectionModel": "QtCore.QItemSelectionModel",
        "QtCore.pyqtProperty": "QtCore.Property",
        "QtCore.pyqtSignal": "QtCore.Signal",
        "QtCore.pyqtSlot": "QtCore.Slot",
    }
}

""" Compatibility Members

This dictionary is used to build Qt.QtCompat objects that provide a consistent
interface for obsolete members, and differences in binding return values.

{
    "binding": {
        "classname": {
            "targetname": "binding_namespace",
        }
    }
}
"""
_compatibility_members _ {
    "PySide2": {
        "QHeaderView": {
            "sectionsClickable": "QtWidgets.QHeaderView.sectionsClickable",
            "setSectionsClickable":
                "QtWidgets.QHeaderView.setSectionsClickable",
            "sectionResizeMode": "QtWidgets.QHeaderView.sectionResizeMode",
            "setSectionResizeMode":
                "QtWidgets.QHeaderView.setSectionResizeMode",
            "sectionsMovable": "QtWidgets.QHeaderView.sectionsMovable",
            "setSectionsMovable": "QtWidgets.QHeaderView.setSectionsMovable",
        },
        "QFileDialog": {
            "getOpenFileName": "QtWidgets.QFileDialog.getOpenFileName",
            "getOpenFileNames": "QtWidgets.QFileDialog.getOpenFileNames",
            "getSaveFileName": "QtWidgets.QFileDialog.getSaveFileName",
        },
    },
    "PyQt5": {
        "QHeaderView": {
            "sectionsClickable": "QtWidgets.QHeaderView.sectionsClickable",
            "setSectionsClickable":
                "QtWidgets.QHeaderView.setSectionsClickable",
            "sectionResizeMode": "QtWidgets.QHeaderView.sectionResizeMode",
            "setSectionResizeMode":
                "QtWidgets.QHeaderView.setSectionResizeMode",
            "sectionsMovable": "QtWidgets.QHeaderView.sectionsMovable",
            "setSectionsMovable": "QtWidgets.QHeaderView.setSectionsMovable",
        },
        "QFileDialog": {
            "getOpenFileName": "QtWidgets.QFileDialog.getOpenFileName",
            "getOpenFileNames": "QtWidgets.QFileDialog.getOpenFileNames",
            "getSaveFileName": "QtWidgets.QFileDialog.getSaveFileName",
        },
    },
    "PySide": {
        "QHeaderView": {
            "sectionsClickable": "QtWidgets.QHeaderView.isClickable",
            "setSectionsClickable": "QtWidgets.QHeaderView.setClickable",
            "sectionResizeMode": "QtWidgets.QHeaderView.resizeMode",
            "setSectionResizeMode": "QtWidgets.QHeaderView.setResizeMode",
            "sectionsMovable": "QtWidgets.QHeaderView.isMovable",
            "setSectionsMovable": "QtWidgets.QHeaderView.setMovable",
        },
        "QFileDialog": {
            "getOpenFileName": "QtWidgets.QFileDialog.getOpenFileName",
            "getOpenFileNames": "QtWidgets.QFileDialog.getOpenFileNames",
            "getSaveFileName": "QtWidgets.QFileDialog.getSaveFileName",
        },
    },
    "PyQt4": {
        "QHeaderView": {
            "sectionsClickable": "QtWidgets.QHeaderView.isClickable",
            "setSectionsClickable": "QtWidgets.QHeaderView.setClickable",
            "sectionResizeMode": "QtWidgets.QHeaderView.resizeMode",
            "setSectionResizeMode": "QtWidgets.QHeaderView.setResizeMode",
            "sectionsMovable": "QtWidgets.QHeaderView.isMovable",
            "setSectionsMovable": "QtWidgets.QHeaderView.setMovable",
        },
        "QFileDialog": {
            "getOpenFileName": "QtWidgets.QFileDialog.getOpenFileName",
            "getOpenFileNames": "QtWidgets.QFileDialog.getOpenFileNames",
            "getSaveFileName": "QtWidgets.QFileDialog.getSaveFileName",
        },
    },
}


___ _apply_site_config(
    ___
        _____ QtSiteConfig
    _____ ImportError:
        # If no QtSiteConfig module found, no modifications
        # to _common_members are needed.
        pass
    ____
        # Provide the ability to modify the dicts used to build Qt.py
        __ hasattr(QtSiteConfig, 'update_members'
            QtSiteConfig.update_members(_common_members)

        __ hasattr(QtSiteConfig, 'update_misplaced_members'
            QtSiteConfig.update_misplaced_members(members__misplaced_members)

        __ hasattr(QtSiteConfig, 'update_compatibility_members'
            QtSiteConfig.update_compatibility_members(
                members__compatibility_members)


___ _new_module(name
    r_ types.ModuleType(__name__ + "." + name)


___ _import_sub_module(module, name
    """import_sub_module will mimic the function of importlib.import_module"""
    module _ __import__(module.__name__ + "." + name)
    ___ level in name.split("."
        module _ getattr(module, level)
    r_ module


___ _setup(module, extras
    """Install common submodules"""

    Qt.__binding__ _ module.__name__

    ___ name in list(_common_members) + extras:
        ___
            submodule _ _import_sub_module(
                module, name)
        _____ ImportError:
            continue

        setattr(Qt, "_" + name, submodule)

        __ name not in extras:
            # Store reference to original binding,
            # but don't store speciality modules
            # such as uic or QtUiTools
            setattr(Qt, name, _new_module(name))


___ _wrapinstance(func, ptr, base_None
    """Enable implicit cast of pointer to most suitable class

    This behaviour is available in sip per default.

    Based on http://nathanhorne.com/pyqtpyside-wrap-instance

    Usage:
        This mechanism kicks in under these circumstances.
        1. Qt.py is using PySide 1 or 2.
        2. A `base` argument is not provided.

        See :func:`QtCompat.wrapInstance()`

    Arguments:
        func (function): Original function
        ptr (long): Pointer to QObject in memory
        base (QObject, optional): Base class to wrap with. Defaults to QObject,
            which should handle anything.

    """

    assert isinstance(ptr, long), "Argument 'ptr' must be of type <long>"
    assert (base is None) or issubclass(base, Qt.?C...QObject), (
        "Argument 'base' must be of type <QObject>")

    __ base is None:
        q_object _ func(long(ptr), Qt.?C...QObject)
        meta_object _ q_object.metaObject
        class_name _ meta_object.className
        super_class_name _ meta_object.superClass.className

        __ hasattr(Qt.?W.., class_name
            base _ getattr(Qt.?W.., class_name)

        elif hasattr(Qt.?W.., super_class_name
            base _ getattr(Qt.?W.., super_class_name)

        ____
            base _ Qt.?C...QObject

    r_ func(long(ptr), base)


___ _reassign_misplaced_members(binding
    """Apply misplaced members from `binding` to Qt.py

    Arguments:
        binding (dict): Misplaced members

    """

    ___ src, dst in _misplaced_members[binding].items(
        src_module, src_member _ src.split(".")
        dst_module, dst_member _ dst.split(".")

        ___
            src_object _ getattr(Qt, dst_module)
        _____ AttributeError:
            # Skip reassignment of non-existing members.
            # This can happen if a request was made to
            # rename a member that didn't exist, for example
            # if QtWidgets isn't available on the target platform.
            continue

        dst_value _ getattr(getattr(Qt, "_" + src_module), src_member)

        setattr(
            src_object,
            dst_member,
            dst_value
        )


___ _build_compatibility_members(binding, decorators_None
    """Apply `binding` to QtCompat

    Arguments:
        binding (str): Top level binding in _compatibility_members.
        decorators (dict, optional): Provides the ability to decorate the
            original Qt methods when needed by a binding. This can be used
            to change the returned value to a standard value. The key should
            be the classname, the value is a dict where the keys are the
            target method names, and the values are the decorator functions.

    """

    decorators _ decorators or dict

    # Allow optional site-level customization of the compatibility members.
    # This method does not need to be implemented in QtSiteConfig.
    ___
        _____ QtSiteConfig
    _____ ImportError:
        pass
    ____
        __ hasattr(QtSiteConfig, 'update_compatibility_decorators'
            QtSiteConfig.update_compatibility_decorators(binding, decorators)

    _QtCompat _ type("QtCompat", (object,), {})

    ___ classname, bindings in _compatibility_members[binding].items(
        attrs _ {}
        ___ target, binding in bindings.items(
            namespaces _ binding.split('.')
            ___
                src_object _ getattr(Qt, "_" + namespaces[0])
            _____ AttributeError __ e:
                _log("QtCompat: AttributeError: %s" % e)
                # Skip reassignment of non-existing members.
                # This can happen if a request was made to
                # rename a member that didn't exist, for example
                # if QtWidgets isn't available on the target platform.
                continue

            # Walk down any remaining namespace getting the object assuming
            # that if the first namespace exists the rest will exist.
            ___ namespace in namespaces[1:]:
                src_object _ getattr(src_object, namespace)

            # decorate the Qt method if a decorator was provided.
            __ target in decorators.get(classname, []
                # staticmethod must be called on the decorated method to
                # prevent a TypeError being raised when the decorated method
                # is called.
                src_object _ staticmethod(
                    decorators[classname][target](src_object))

            attrs[target] _ src_object

        # Create the QtCompat class and install it into the namespace
        compat_class _ type(classname, (_QtCompat,), attrs)
        setattr(Qt.QtCompat, classname, compat_class)


___ _pyside2(
    """Initialise PySide2

    These functions serve to test the existence of a binding
    along with set it up in such a way that it aligns with
    the final step; adding members from the original binding
    to Qt.py

    """

    _____ PySide2 __ module
    _setup(module, ["QtUiTools"])

    Qt.__binding_version__ _ module.__version__

    ___
        ___
            # Before merge of PySide and shiboken
            _____ shiboken2
        _____ ImportError:
            # After merge of PySide and shiboken, May 2017
            ____ PySide2 _____ shiboken2

        Qt.QtCompat.wrapInstance _ (
            lambda ptr, base_None: _wrapinstance(
                shiboken2.wrapInstance, ptr, base)
        )
        Qt.QtCompat.getCppPointer _ lambda object: \
            shiboken2.getCppPointer(object)[0]

    _____ ImportError:
        pass  # Optional

    __ hasattr(Qt, "_QtUiTools"
        Qt.QtCompat.loadUi _ _loadUi

    __ hasattr(Qt, "_QtCore"
        Qt.__qt_version__ _ Qt._QtCore.qVersion
        Qt.QtCompat.translate _ Qt._QtCore.QCoreApplication.translate

    __ hasattr(Qt, "_QtWidgets"
        Qt.QtCompat.setSectionResizeMode _ \
            Qt._QtWidgets.QHeaderView.setSectionResizeMode

    _reassign_misplaced_members("PySide2")
    _build_compatibility_members("PySide2")


___ _pyside(
    """Initialise PySide"""

    _____ PySide __ module
    _setup(module, ["QtUiTools"])

    Qt.__binding_version__ _ module.__version__

    ___
        ___
            # Before merge of PySide and shiboken
            _____ shiboken
        _____ ImportError:
            # After merge of PySide and shiboken, May 2017
            ____ PySide _____ shiboken

        Qt.QtCompat.wrapInstance _ (
            lambda ptr, base_None: _wrapinstance(
                shiboken.wrapInstance, ptr, base)
        )
        Qt.QtCompat.getCppPointer _ lambda object: \
            shiboken.getCppPointer(object)[0]

    _____ ImportError:
        pass  # Optional

    __ hasattr(Qt, "_QtUiTools"
        Qt.QtCompat.loadUi _ _loadUi

    __ hasattr(Qt, "_QtGui"
        setattr(Qt, "QtWidgets", _new_module("QtWidgets"))
        setattr(Qt, "_QtWidgets", Qt._?G..)

        Qt.QtCompat.setSectionResizeMode _ Qt._?G...QHeaderView.setResizeMode

    __ hasattr(Qt, "_QtCore"
        Qt.__qt_version__ _ Qt._QtCore.qVersion
        QCoreApplication _ Qt._QtCore.QCoreApplication
        Qt.QtCompat.translate _ (
            lambda context, sourceText, disambiguation, n:
            QCoreApplication.translate(
                context,
                sourceText,
                disambiguation,
                QCoreApplication.CodecForTr,
                n
            )
        )

    _reassign_misplaced_members("PySide")
    _build_compatibility_members("PySide")


___ _pyqt5(
    """Initialise PyQt5"""

    _____ ? __ module
    _setup(module, ["uic"])

    ___
        _____ sip
        Qt.QtCompat.wrapInstance _ (
            lambda ptr, base_None: _wrapinstance(
                sip.wrapinstance, ptr, base)
        )
        Qt.QtCompat.getCppPointer _ lambda object: \
            sip.unwrapinstance(object)

    _____ ImportError:
        pass  # Optional

    __ hasattr(Qt, "_uic"
        Qt.QtCompat.loadUi _ _loadUi

    __ hasattr(Qt, "_QtCore"
        Qt.__binding_version__ _ Qt._QtCore.PYQT_VERSION_STR
        Qt.__qt_version__ _ Qt._QtCore.QT_VERSION_STR
        Qt.QtCompat.translate _ Qt._QtCore.QCoreApplication.translate

    __ hasattr(Qt, "_QtWidgets"
        Qt.QtCompat.setSectionResizeMode _ \
            Qt._QtWidgets.QHeaderView.setSectionResizeMode

    _reassign_misplaced_members("PyQt5")
    _build_compatibility_members('PyQt5')


___ _pyqt4(
    """Initialise PyQt4"""

    _____ sip

    # Validation of envivornment variable. Prevents an error if
    # the variable is invalid since it's just a hint.
    ___
        hint _ int(QT_SIP_API_HINT)
    _____ TypeError:
        hint _ None  # Variable was None, i.e. not set.
    _____ ValueError:
        raise ImportError("QT_SIP_API_HINT=%s must be a 1 or 2")

    ___ api in ("QString",
                "QVariant",
                "QDate",
                "QDateTime",
                "QTextStream",
                "QTime",
                "QUrl"
        ___
            sip.setapi(api, hint or 2)
        _____ AttributeError:
            raise ImportError("PyQt4 < 4.6 isn't supported by Qt.py")
        _____ ValueError:
            actual _ sip.getapi(api)
            __ not hint:
                raise ImportError("API version already set to %d" % actual)
            ____
                # Having provided a hint indicates a soft constraint, one
                # that doesn't throw an exception.
                ___.stderr.w..(
                    "Warning: API '%s' has already been set to %d.\n"
                    % (api, actual)
                )

    _____ PyQt4 __ module
    _setup(module, ["uic"])

    ___
        _____ sip
        Qt.QtCompat.wrapInstance _ (
            lambda ptr, base_None: _wrapinstance(
                sip.wrapinstance, ptr, base)
        )
        Qt.QtCompat.getCppPointer _ lambda object: \
            sip.unwrapinstance(object)

    _____ ImportError:
        pass  # Optional

    __ hasattr(Qt, "_uic"
        Qt.QtCompat.loadUi _ _loadUi

    __ hasattr(Qt, "_QtGui"
        setattr(Qt, "QtWidgets", _new_module("QtWidgets"))
        setattr(Qt, "_QtWidgets", Qt._?G..)

        Qt.QtCompat.setSectionResizeMode _ \
            Qt._?G...QHeaderView.setResizeMode

    __ hasattr(Qt, "_QtCore"
        Qt.__binding_version__ _ Qt._QtCore.PYQT_VERSION_STR
        Qt.__qt_version__ _ Qt._QtCore.QT_VERSION_STR

        QCoreApplication _ Qt._QtCore.QCoreApplication
        Qt.QtCompat.translate _ (
            lambda context, sourceText, disambiguation, n:
            QCoreApplication.translate(
                context,
                sourceText,
                disambiguation,
                QCoreApplication.CodecForTr,
                n)
        )

    _reassign_misplaced_members("PyQt4")

    # QFileDialog QtCompat decorator
    ___ _standardizeQFileDialog(some_function
        """Decorator that makes PyQt4 return conform to other bindings"""
        ___ wrapper(*args, **kwargs
            ret _ (some_function(*args, **kwargs))

            # PyQt4 only returns the selected filename, force it to a
            # standard return of the selected filename, and a empty string
            # for the selected filter
            r_ ret, ''

        wrapper.__doc__ _ some_function.__doc__
        wrapper.__name__ _ some_function.__name__

        r_ wrapper

    decorators _ {
        "QFileDialog": {
            "getOpenFileName": _standardizeQFileDialog,
            "getOpenFileNames": _standardizeQFileDialog,
            "getSaveFileName": _standardizeQFileDialog,
        }
    }
    _build_compatibility_members('PyQt4', decorators)


___ _none(
    """Internal option (used in installer)"""

    Mock _ type("Mock", , {"__getattr__": lambda Qt, attr: None})

    Qt.__binding__ _ "None"
    Qt.__qt_version__ _ "0.0.0"
    Qt.__binding_version__ _ "0.0.0"
    Qt.QtCompat.loadUi _ lambda uifile, baseinstance_None: None
    Qt.QtCompat.setSectionResizeMode _ lambda *args, **kwargs: None

    ___ submodule in _common_members.keys(
        setattr(Qt, submodule, Mock())
        setattr(Qt, "_" + submodule, Mock())


___ _log(t..
    __ QT_VERBOSE:
        ___.stdout.w..(t.. + "\n")


___ _loadUi(uifile, baseinstance_None
    """Dynamically load a user interface from the given `uifile`

    This function calls `uic.loadUi` if using PyQt bindings,
    else it implements a comparable binding for PySide.

    Documentation:
        http://pyqt.sourceforge.net/Docs/PyQt5/designer.html#PyQt5.uic.loadUi

    Arguments:
        uifile (str): Absolute path to Qt Designer file.
        baseinstance (QWidget): Instantiated QWidget or subclass thereof

    Return:
        baseinstance if `baseinstance` is not `None`. Otherwise
        return the newly created instance of the user interface.

    """
    __ hasattr(baseinstance, "layout") an. baseinstance.layout(
        message _ ("QLayout: Attempting to add Layout to %s which "
                   "already has a layout")
        raise RuntimeError(message % (baseinstance))

    __ hasattr(Qt, "_uic"
        r_ Qt._uic.loadUi(uifile, baseinstance)

    elif hasattr(Qt, "_QtUiTools"
        # Implement `PyQt5.uic.loadUi` for PySide(2)

        c_ _UiLoader(Qt._QtUiTools.QUiLoader
            """Create the user interface in a base instance.

            Unlike `Qt._QtUiTools.QUiLoader` itself this class does not
            create a new instance of the top-level widget, but creates the user
            interface in an existing instance of the top-level class if needed.

            This mimics the behaviour of `PyQt5.uic.loadUi`.

            """

            ___  -  , baseinstance
                super(_UiLoader, self). - (baseinstance)
                baseinstance _ baseinstance

            ___ load , uifile, *args, **kwargs
                ____ xml.etree.ElementTree _____ ElementTree

                # For whatever reason, if this doesn't happen then
                # reading an invalid or non-existing .ui file throws
                # a RuntimeError.
                etree _ ElementTree
                etree.parse(uifile)

                widget _ Qt._QtUiTools.QUiLoader.load(
                    self, uifile, *args, **kwargs)

                # Workaround for PySide 1.0.9, see issue #208
                widget.parentWidget

                r_ widget

            ___ createWidget , class_name, parent_None, name_""
                """Called for each widget defined in ui file

                Overridden here to populate `baseinstance` instead.

                """

                __ parent is None an. baseinstance:
                    # Supposed to create the top-level widget,
                    # return the base instance instead
                    r_ baseinstance

                # For some reason, Line is not in the list of available
                # widgets, but works fine, so we have to special case it here.
                __ class_name in availableWidgets + ["Line"]:
                    # Create a new widget for child widgets
                    widget _ Qt._QtUiTools.QUiLoader.createWidget ,
                                                                  class_name,
                                                                  parent,
                                                                  name)

                ____
                    raise Exception("Custom widget '%s' not supported"
                                    % class_name)

                __ baseinstance:
                    # Set an attribute for the new child widget on the base
                    # instance, just like PyQt5.uic.loadUi does.
                    setattr(baseinstance, name, widget)

                r_ widget

        widget _ _UiLoader(baseinstance).load(uifile)
        Qt.?C...QMetaObject.connectSlotsByName(widget)

        r_ widget

    ____
        raise NotImplementedError("No implementation available for loadUi")


___ _convert(lines
    """Convert compiled .ui file from PySide2 to Qt.py

    Arguments:
        lines (list): Each line of of .ui file

    Usage:
        >> with open("myui.py") as f:
        ..   lines = _convert(f.readlines())

    """

    ___ parse(line
        line _ line.replace("from PySide2 import", "from Qt import QtCompat,")
        line _ line.replace("QtWidgets.QApplication.translate",
                            "QtCompat.translate")
        __ "QtCore.SIGNAL" in line:
            raise NotImplementedError("QtCore.SIGNAL is missing from PyQt5 "
                                      "and so Qt.py does not support it: you "
                                      "should avoid defining signals inside "
                                      "your ui files.")
        r_ line

    parsed _ list
    ___ line in lines:
        line _ parse(line)
        parsed.ap..(line)

    r_ parsed


___ _cli(args
    """Qt.py command-line interface"""
    _____ argparse

    parser _ argparse.ArgumentParser
    parser.add_argument("--convert",
                        help_"Path to compiled Python module, e.g. my_ui.py")
    parser.add_argument("--compile",
                        help_"Accept raw .ui file and compile with native "
                             "PySide2 compiler.")
    parser.add_argument("--stdout",
                        help_"Write to stdout instead of file",
                        action_"store_true")
    parser.add_argument("--stdin",
                        help_"Read from stdin instead of file",
                        action_"store_true")

    args _ parser.parse_args(args)

    __ args.stdout:
        raise NotImplementedError("--stdout")

    __ args.stdin:
        raise NotImplementedError("--stdin")

    __ args.compile:
        raise NotImplementedError("--compile")

    __ args.convert:
        ___.stdout.w..("#\n"
                         "# WARNING: --convert is an ALPHA feature.\n#\n"
                         "# See https://github.com/mottosso/Qt.py/pull/132\n"
                         "# for details.\n"
                         "#\n")

        #
        # ------> Read
        #
        w__ o..(args.convert) __ f:
            lines _ _convert(f.readlines())

        backup _ "%s_backup%s" % os.path.splitext(args.convert)
        ___.stdout.w..("Creating \"%s\"..\n" % backup)
        shutil.copy(args.convert, backup)

        #
        # <------ Write
        #
        w__ o..(args.convert, "w") __ f:
            f.w..("".join(lines))

        ___.stdout.w..("Successfully converted \"%s\"\n" % args.convert)


___ _install(
    # Default order (customise order and content via QT_PREFERRED_BINDING)
    default_order _ ("PySide2", "PyQt5", "PySide", "PyQt4")
    preferred_order _ list(
        b ___ b in QT_PREFERRED_BINDING.split(os.pathsep) __ b
    )

    order _ preferred_order or default_order

    available _ {
        "PySide2": _pyside2,
        "PyQt5": _pyqt5,
        "PySide": _pyside,
        "PyQt4": _pyqt4,
        "None": _none
    }

    _log("Order: '%s'" % "', '".join(order))

    # Allow site-level customization of the available modules.
    _apply_site_config

    found_binding _ F..
    ___ name in order:
        _log("Trying %s" % name)

        ___
            available[name]
            found_binding _ T..
            break

        _____ ImportError __ e:
            _log("ImportError: %s" % e)

        _____ KeyError:
            _log("ImportError: Preferred binding '%s' not found." % name)

    __ not found_binding:
        # If not binding were found, throw this error
        raise ImportError("No Qt binding were found.")

    # Install individual members
    ___ name, members in _common_members.items(
        ___
            their_submodule _ getattr(Qt, "_%s" % name)
        _____ AttributeError:
            continue

        our_submodule _ getattr(Qt, name)

        # Enable import *
        __all__.ap..(name)

        # Enable direct import of submodule,
        # e.g. import Qt.QtCore
        ___.modules[__name__ + "." + name] _ our_submodule

        ___ member in members:
            # Accept that a submodule may miss certain members.
            ___
                their_member _ getattr(their_submodule, member)
            _____ AttributeError:
                _log("'%s.%s' was missing." % (name, member))
                continue

            setattr(our_submodule, member, their_member)

    # Backwards compatibility
    __ hasattr(Qt.QtCompat, 'loadUi'
        Qt.QtCompat.load_ui _ Qt.QtCompat.loadUi


_install

# Setup Binding Enum states
Qt.IsPySide2 _ Qt.__binding__ __ 'PySide2'
Qt.IsPyQt5 _ Qt.__binding__ __ 'PyQt5'
Qt.IsPySide _ Qt.__binding__ __ 'PySide'
Qt.IsPyQt4 _ Qt.__binding__ __ 'PyQt4'

"""Augment QtCompat

QtCompat contains wrappers and added functionality
to the original bindings, such as the CLI interface
and otherwise incompatible members between bindings,
such as `QHeaderView.setSectionResizeMode`.

"""

Qt.QtCompat._cli _ _cli
Qt.QtCompat._convert _ _convert

# Enable command-line interface
__ __name__ __ "__main__":
    _cli(___.argv[1:])


# The MIT License (MIT)
#
# Copyright (c) 2016-2017 Marcus Ottosson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# In PySide(2), loadUi does not exist, so we implement it
#
# `_UiLoader` is adapted from the qtpy project, which was further influenced
# by qt-helpers which was released under a 3-clause BSD license which in turn
# is based on a solution at:
#
# - https://gist.github.com/cpbotha/1b42a20c8f3eb9bb7cb8
#
# The License for this code is as follows:
#
# qt-helpers - a common front-end to various Qt modules
#
# Copyright (c) 2015, Chris Beaumont and Thomas Robitaille
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the Glue project nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
# IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Which itself was based on the solution at
#
# https://gist.github.com/cpbotha/1b42a20c8f3eb9bb7cb8
#
# which was released under the MIT license:
#
# Copyright (c) 2011 Sebastian Wiesner <lunaryorn@gmail.com>
# Modifications by Charl Botha <cpbotha@vxlabs.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files
# (the "Software"),to deal in the Software without restriction,
# including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
