# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_timelog_viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore ______ (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui ______ (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets ______ *

c_ Ui_TimelogViewer(object):
    ___ setupUi(self, TimelogViewer):
        __ TimelogViewer.objectName():
            TimelogViewer.setObjectName(u"TimelogViewer")
        TimelogViewer.resize(491, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TimelogViewer.sizePolicy().hasHeightForWidth())
        TimelogViewer.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(TimelogViewer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_label = QLabel(TimelogViewer)
        self.date_label.setObjectName(u"date_label")

        self.horizontalLayout.addWidget(self.date_label)

        self.date_combo_box = QComboBox(TimelogViewer)
        self.date_combo_box.setObjectName(u"date_combo_box")

        self.horizontalLayout.addWidget(self.date_combo_box)

        self.delete_push_button = QPushButton(TimelogViewer)
        self.delete_push_button.setObjectName(u"delete_push_button")

        self.horizontalLayout.addWidget(self.delete_push_button)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.log_knob = QTextBrowser(TimelogViewer)
        self.log_knob.setObjectName(u"log_knob")

        self.gridLayout.addWidget(self.log_knob, 1, 0, 1, 2)

        self.ok_push_button = QPushButton(TimelogViewer)
        self.ok_push_button.setObjectName(u"ok_push_button")

        self.gridLayout.addWidget(self.ok_push_button, 2, 0, 1, 1)

        self.cancel_push_button = QPushButton(TimelogViewer)
        self.cancel_push_button.setObjectName(u"cancel_push_button")

        self.gridLayout.addWidget(self.cancel_push_button, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(TimelogViewer)

        QMetaObject.connectSlotsByName(TimelogViewer)
    # setupUi

    ___ retranslateUi(self, TimelogViewer):
        TimelogViewer.setWindowTitle(QCoreApplication.translate("TimelogViewer", u"Timelog Viewer", None))
        self.date_label.setText(QCoreApplication.translate("TimelogViewer", u"Date:", None))
        self.delete_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Delete", None))
        self.ok_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Ok", None))
        self.cancel_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Cancel", None))
    # retranslateUi

