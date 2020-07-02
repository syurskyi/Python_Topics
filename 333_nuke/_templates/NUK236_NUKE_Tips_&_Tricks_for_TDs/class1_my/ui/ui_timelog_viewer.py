# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_timelog_viewer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

____ ?.QtCore ______ (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
____ ?.QtGui ______ (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
____ ?.?W.. ______ *

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
        gridLayout_2 = QGridLayout(TimelogViewer)
        gridLayout_2.setObjectName(u"gridLayout_2")
        gridLayout = QGridLayout()
        gridLayout.setObjectName(u"gridLayout")
        horizontalLayout = QHBoxLayout()
        horizontalLayout.setObjectName(u"horizontalLayout")
        date_label = ?L..(TimelogViewer)
        date_label.setObjectName(u"date_label")

        horizontalLayout.aW..(date_label)

        date_combo_box = QComboBox(TimelogViewer)
        date_combo_box.setObjectName(u"date_combo_box")

        horizontalLayout.aW..(date_combo_box)

        delete_push_button = ?PB..(TimelogViewer)
        delete_push_button.setObjectName(u"delete_push_button")

        horizontalLayout.aW..(delete_push_button)


        gridLayout.addLayout(horizontalLayout, 0, 0, 1, 2)

        log_knob = QTextBrowser(TimelogViewer)
        log_knob.setObjectName(u"log_knob")

        gridLayout.aW..(log_knob, 1, 0, 1, 2)

        ok_push_button = ?PB..(TimelogViewer)
        ok_push_button.setObjectName(u"ok_push_button")

        gridLayout.aW..(ok_push_button, 2, 0, 1, 1)

        cancel_push_button = ?PB..(TimelogViewer)
        cancel_push_button.setObjectName(u"cancel_push_button")

        gridLayout.aW..(cancel_push_button, 2, 1, 1, 1)


        gridLayout_2.addLayout(gridLayout, 0, 0, 1, 1)


        retranslateUi(TimelogViewer)

        QMetaObject.connectSlotsByName(TimelogViewer)
    # setupUi

    ___ retranslateUi(self, TimelogViewer):
        TimelogViewer.sQT..(QCoreApplication.translate("TimelogViewer", u"Timelog Viewer", N..))
        date_label.setText(QCoreApplication.translate("TimelogViewer", u"Date:", N..))
        delete_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Delete", N..))
        ok_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Ok", N..))
        cancel_push_button.setText(QCoreApplication.translate("TimelogViewer", u"Cancel", N..))
    # retranslateUi

