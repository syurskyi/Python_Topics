# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.r..(549, 452)
        centralWidget = QtWidgets.?W..(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(centralWidget.sizePolicy().hasHeightForWidth())
        centralWidget.sSP..(sizePolicy)
        centralWidget.setObjectName("centralWidget")
        verticalLayout = QtWidgets.QVBoxLayout(centralWidget)
        verticalLayout.setContentsMargins(11, 11, 11, 11)
        verticalLayout.setSpacing(6)
        verticalLayout.setObjectName("verticalLayout")
        horizontalLayout = QtWidgets.QHBoxLayout()
        horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        horizontalLayout.setSpacing(6)
        horizontalLayout.setObjectName("horizontalLayout")
        verticalLayout_2 = QtWidgets.QVBoxLayout()
        verticalLayout_2.setSpacing(6)
        verticalLayout_2.setObjectName("verticalLayout_2")
        widget = QtWidgets.?W..(centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())
        widget.sSP..(sizePolicy)
        widget.setObjectName("widget")
        gridLayout = QtWidgets.QGridLayout(widget)
        gridLayout.setContentsMargins(11, 11, 11, 11)
        gridLayout.setSpacing(15)
        gridLayout.setObjectName("gridLayout")
        rectButton = QtWidgets.QPushButton(widget)
        rectButton.sMS..(QtCore.?S..(30, 30))
        rectButton.sMS..(QtCore.?S..(30, 30))
        rectButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.?P..("images/layer-shape.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        rectButton.setIcon(icon)
        rectButton.setCheckable( st.
        rectButton.setObjectName("rectButton")
        gridLayout.addWidget(rectButton, 6, 0, 1, 1)
        polylineButton = QtWidgets.QPushButton(widget)
        polylineButton.sMS..(QtCore.?S..(30, 30))
        polylineButton.sMS..(QtCore.?S..(30, 30))
        polylineButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.?P..("images/layer-shape-polyline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        polylineButton.setIcon(icon1)
        polylineButton.setCheckable( st.
        polylineButton.setObjectName("polylineButton")
        gridLayout.addWidget(polylineButton, 5, 1, 1, 1)
        selectrectButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(selectrectButton.sizePolicy().hasHeightForWidth())
        selectrectButton.sSP..(sizePolicy)
        selectrectButton.sMS..(QtCore.?S..(30, 30))
        selectrectButton.sMS..(QtCore.?S..(30, 30))
        selectrectButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.?P..("images/selection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectrectButton.setIcon(icon2)
        selectrectButton.setCheckable( st.
        selectrectButton.setObjectName("selectrectButton")
        gridLayout.addWidget(selectrectButton, 0, 1, 1, 1)
        eraserButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(eraserButton.sizePolicy().hasHeightForWidth())
        eraserButton.sSP..(sizePolicy)
        eraserButton.sMS..(QtCore.?S..(30, 30))
        eraserButton.sMS..(QtCore.?S..(30, 30))
        eraserButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.?P..("images/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        eraserButton.setIcon(icon3)
        eraserButton.setCheckable( st.
        eraserButton.setObjectName("eraserButton")
        gridLayout.addWidget(eraserButton, 1, 0, 1, 1)
        stampButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stampButton.sizePolicy().hasHeightForWidth())
        stampButton.sSP..(sizePolicy)
        stampButton.sMS..(QtCore.?S..(30, 30))
        stampButton.sMS..(QtCore.?S..(30, 30))
        stampButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.?P..("images/cake.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        stampButton.setIcon(icon4)
        stampButton.setCheckable( st.
        stampButton.setObjectName("stampButton")
        gridLayout.addWidget(stampButton, 2, 1, 1, 1)
        dropperButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dropperButton.sizePolicy().hasHeightForWidth())
        dropperButton.sSP..(sizePolicy)
        dropperButton.sMS..(QtCore.?S..(30, 30))
        dropperButton.sMS..(QtCore.?S..(30, 30))
        dropperButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.?P..("images/pipette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dropperButton.setIcon(icon5)
        dropperButton.setCheckable( st.
        dropperButton.setObjectName("dropperButton")
        gridLayout.addWidget(dropperButton, 2, 0, 1, 1)
        selectpolyButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(selectpolyButton.sizePolicy().hasHeightForWidth())
        selectpolyButton.sSP..(sizePolicy)
        selectpolyButton.sMS..(QtCore.?S..(30, 30))
        selectpolyButton.sMS..(QtCore.?S..(30, 30))
        selectpolyButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.?P..("images/selection-poly.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        selectpolyButton.setIcon(icon6)
        selectpolyButton.setCheckable( st.
        selectpolyButton.setObjectName("selectpolyButton")
        gridLayout.addWidget(selectpolyButton, 0, 0, 1, 1)
        brushButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(brushButton.sizePolicy().hasHeightForWidth())
        brushButton.sSP..(sizePolicy)
        brushButton.sMS..(QtCore.?S..(30, 30))
        brushButton.sMS..(QtCore.?S..(30, 30))
        brushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.?P..("images/paint-brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        brushButton.setIcon(icon7)
        brushButton.setCheckable( st.
        brushButton.setObjectName("brushButton")
        gridLayout.addWidget(brushButton, 3, 1, 1, 1)
        penButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(penButton.sizePolicy().hasHeightForWidth())
        penButton.sSP..(sizePolicy)
        penButton.sMS..(QtCore.?S..(30, 30))
        penButton.sMS..(QtCore.?S..(30, 30))
        penButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.?P..("images/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        penButton.setIcon(icon8)
        penButton.setCheckable( st.
        penButton.setObjectName("penButton")
        gridLayout.addWidget(penButton, 3, 0, 1, 1)
        fillButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fillButton.sizePolicy().hasHeightForWidth())
        fillButton.sSP..(sizePolicy)
        fillButton.sMS..(QtCore.?S..(30, 30))
        fillButton.sMS..(QtCore.?S..(30, 30))
        fillButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.?P..("images/paint-can.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        fillButton.setIcon(icon9)
        fillButton.setCheckable( st.
        fillButton.setObjectName("fillButton")
        gridLayout.addWidget(fillButton, 1, 1, 1, 1)
        textButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(textButton.sizePolicy().hasHeightForWidth())
        textButton.sSP..(sizePolicy)
        textButton.sMS..(QtCore.?S..(30, 30))
        textButton.sMS..(QtCore.?S..(30, 30))
        textButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.?P..("images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        textButton.setIcon(icon10)
        textButton.setCheckable( st.
        textButton.setObjectName("textButton")
        gridLayout.addWidget(textButton, 4, 1, 1, 1)
        polygonButton = QtWidgets.QPushButton(widget)
        polygonButton.sMS..(QtCore.?S..(30, 30))
        polygonButton.sMS..(QtCore.?S..(30, 30))
        polygonButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.?P..("images/layer-shape-polygon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        polygonButton.setIcon(icon11)
        polygonButton.setCheckable( st.
        polygonButton.setObjectName("polygonButton")
        gridLayout.addWidget(polygonButton, 6, 1, 1, 1)
        roundrectButton = QtWidgets.QPushButton(widget)
        roundrectButton.sMS..(QtCore.?S..(30, 30))
        roundrectButton.sMS..(QtCore.?S..(30, 30))
        roundrectButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.?P..("images/layer-shape-round.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        roundrectButton.setIcon(icon12)
        roundrectButton.setCheckable( st.
        roundrectButton.setObjectName("roundrectButton")
        gridLayout.addWidget(roundrectButton, 7, 1, 1, 1)
        ellipseButton = QtWidgets.QPushButton(widget)
        ellipseButton.sMS..(QtCore.?S..(30, 30))
        ellipseButton.sMS..(QtCore.?S..(30, 30))
        ellipseButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.?P..("images/layer-shape-ellipse.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ellipseButton.setIcon(icon13)
        ellipseButton.setCheckable( st.
        ellipseButton.setObjectName("ellipseButton")
        gridLayout.addWidget(ellipseButton, 7, 0, 1, 1)
        lineButton = QtWidgets.QPushButton(widget)
        lineButton.sMS..(QtCore.?S..(30, 30))
        lineButton.sMS..(QtCore.?S..(30, 30))
        lineButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.?P..("images/layer-shape-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lineButton.setIcon(icon14)
        lineButton.setCheckable( st.
        lineButton.setObjectName("lineButton")
        gridLayout.addWidget(lineButton, 5, 0, 1, 1)
        sprayButton = QtWidgets.QPushButton(widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sprayButton.sizePolicy().hasHeightForWidth())
        sprayButton.sSP..(sizePolicy)
        sprayButton.sMS..(QtCore.?S..(30, 30))
        sprayButton.sMS..(QtCore.?S..(30, 30))
        sprayButton.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.?P..("images/spray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sprayButton.setIcon(icon15)
        sprayButton.setCheckable( st.
        sprayButton.setFlat(F..)
        sprayButton.setObjectName("sprayButton")
        gridLayout.addWidget(sprayButton, 4, 0, 1, 1)
        verticalLayout_2.addWidget(widget)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.E..)
        verticalLayout_2.aI..(spacerItem)
        horizontalLayout.aL..(verticalLayout_2)
        canvas = QtWidgets.QLabel(centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.ME.., QtWidgets.QSizePolicy.ME..)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(canvas.sizePolicy().hasHeightForWidth())
        canvas.sSP..(sizePolicy)
        canvas.setText("")
        canvas.setObjectName("canvas")
        horizontalLayout.addWidget(canvas)
        verticalLayout.aL..(horizontalLayout)
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        horizontalLayout_2.setSpacing(6)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        widget_3 = QtWidgets.?W..(centralWidget)
        widget_3.sMS..(QtCore.?S..(78, 0))
        widget_3.sMS..(QtCore.?S..(78, 16777215))
        widget_3.setObjectName("widget_3")
        secondaryButton = QtWidgets.QPushButton(widget_3)
        secondaryButton.setGeometry(QtCore.QRect(30, 10, 40, 40))
        secondaryButton.sMS..(QtCore.?S..(40, 40))
        secondaryButton.sMS..(QtCore.?S..(40, 40))
        secondaryButton.setText("")
        secondaryButton.setObjectName("secondaryButton")
        primaryButton = QtWidgets.QPushButton(widget_3)
        primaryButton.setGeometry(QtCore.QRect(10, 0, 40, 40))
        primaryButton.sMS..(QtCore.?S..(40, 40))
        primaryButton.sMS..(QtCore.?S..(40, 40))
        primaryButton.setText("")
        primaryButton.setObjectName("primaryButton")
        horizontalLayout_2.addWidget(widget_3)
        widget_2 = QtWidgets.?W..(centralWidget)
        widget_2.setObjectName("widget_2")
        gridLayout_2 = QtWidgets.QGridLayout(widget_2)
        gridLayout_2.setContentsMargins(15, 0, 15, 15)
        gridLayout_2.setSpacing(15)
        gridLayout_2.setObjectName("gridLayout_2")
        colorButton_11 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_11.sizePolicy().hasHeightForWidth())
        colorButton_11.sSP..(sizePolicy)
        colorButton_11.sMS..(QtCore.?S..(20, 20))
        colorButton_11.sMS..(QtCore.?S..(20, 13))
        colorButton_11.setText("")
        colorButton_11.setObjectName("colorButton_11")
        gridLayout_2.addWidget(colorButton_11, 0, 10, 1, 1)
        colorButton_7 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_7.sizePolicy().hasHeightForWidth())
        colorButton_7.sSP..(sizePolicy)
        colorButton_7.sMS..(QtCore.?S..(20, 20))
        colorButton_7.sMS..(QtCore.?S..(20, 13))
        colorButton_7.setText("")
        colorButton_7.setObjectName("colorButton_7")
        gridLayout_2.addWidget(colorButton_7, 0, 6, 1, 1)
        colorButton_9 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_9.sizePolicy().hasHeightForWidth())
        colorButton_9.sSP..(sizePolicy)
        colorButton_9.sMS..(QtCore.?S..(20, 20))
        colorButton_9.sMS..(QtCore.?S..(20, 13))
        colorButton_9.setText("")
        colorButton_9.setObjectName("colorButton_9")
        gridLayout_2.addWidget(colorButton_9, 0, 8, 1, 1)
        colorButton_10 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_10.sizePolicy().hasHeightForWidth())
        colorButton_10.sSP..(sizePolicy)
        colorButton_10.sMS..(QtCore.?S..(20, 20))
        colorButton_10.sMS..(QtCore.?S..(20, 13))
        colorButton_10.setText("")
        colorButton_10.setObjectName("colorButton_10")
        gridLayout_2.addWidget(colorButton_10, 0, 9, 1, 1)
        colorButton_23 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_23.sizePolicy().hasHeightForWidth())
        colorButton_23.sSP..(sizePolicy)
        colorButton_23.sMS..(QtCore.?S..(20, 20))
        colorButton_23.sMS..(QtCore.?S..(20, 13))
        colorButton_23.setText("")
        colorButton_23.setObjectName("colorButton_23")
        gridLayout_2.addWidget(colorButton_23, 1, 8, 1, 1)
        colorButton_18 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_18.sizePolicy().hasHeightForWidth())
        colorButton_18.sSP..(sizePolicy)
        colorButton_18.sMS..(QtCore.?S..(20, 20))
        colorButton_18.sMS..(QtCore.?S..(20, 13))
        colorButton_18.setText("")
        colorButton_18.setObjectName("colorButton_18")
        gridLayout_2.addWidget(colorButton_18, 1, 3, 1, 1)
        colorButton_20 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_20.sizePolicy().hasHeightForWidth())
        colorButton_20.sSP..(sizePolicy)
        colorButton_20.sMS..(QtCore.?S..(20, 20))
        colorButton_20.sMS..(QtCore.?S..(20, 13))
        colorButton_20.setText("")
        colorButton_20.setObjectName("colorButton_20")
        gridLayout_2.addWidget(colorButton_20, 1, 5, 1, 1)
        colorButton_6 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_6.sizePolicy().hasHeightForWidth())
        colorButton_6.sSP..(sizePolicy)
        colorButton_6.sMS..(QtCore.?S..(20, 20))
        colorButton_6.sMS..(QtCore.?S..(20, 13))
        colorButton_6.setText("")
        colorButton_6.setObjectName("colorButton_6")
        gridLayout_2.addWidget(colorButton_6, 0, 5, 1, 1)
        colorButton_3 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_3.sizePolicy().hasHeightForWidth())
        colorButton_3.sSP..(sizePolicy)
        colorButton_3.sMS..(QtCore.?S..(20, 20))
        colorButton_3.sMS..(QtCore.?S..(20, 13))
        colorButton_3.setText("")
        colorButton_3.setObjectName("colorButton_3")
        gridLayout_2.addWidget(colorButton_3, 0, 2, 1, 1)
        colorButton_24 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_24.sizePolicy().hasHeightForWidth())
        colorButton_24.sSP..(sizePolicy)
        colorButton_24.sMS..(QtCore.?S..(20, 20))
        colorButton_24.sMS..(QtCore.?S..(20, 13))
        colorButton_24.setText("")
        colorButton_24.setObjectName("colorButton_24")
        gridLayout_2.addWidget(colorButton_24, 1, 9, 1, 1)
        colorButton_17 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_17.sizePolicy().hasHeightForWidth())
        colorButton_17.sSP..(sizePolicy)
        colorButton_17.sMS..(QtCore.?S..(20, 20))
        colorButton_17.sMS..(QtCore.?S..(20, 13))
        colorButton_17.setText("")
        colorButton_17.setObjectName("colorButton_17")
        gridLayout_2.addWidget(colorButton_17, 1, 2, 1, 1)
        colorButton_1 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_1.sizePolicy().hasHeightForWidth())
        colorButton_1.sSP..(sizePolicy)
        colorButton_1.sMS..(QtCore.?S..(20, 20))
        colorButton_1.sMS..(QtCore.?S..(20, 13))
        colorButton_1.sSS..("")
        colorButton_1.setText("")
        colorButton_1.setObjectName("colorButton_1")
        gridLayout_2.addWidget(colorButton_1, 0, 0, 1, 1)
        colorButton_8 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_8.sizePolicy().hasHeightForWidth())
        colorButton_8.sSP..(sizePolicy)
        colorButton_8.sMS..(QtCore.?S..(20, 20))
        colorButton_8.sMS..(QtCore.?S..(20, 13))
        colorButton_8.setText("")
        colorButton_8.setObjectName("colorButton_8")
        gridLayout_2.addWidget(colorButton_8, 0, 7, 1, 1)
        colorButton_27 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_27.sizePolicy().hasHeightForWidth())
        colorButton_27.sSP..(sizePolicy)
        colorButton_27.sMS..(QtCore.?S..(20, 20))
        colorButton_27.sMS..(QtCore.?S..(20, 13))
        colorButton_27.setText("")
        colorButton_27.setObjectName("colorButton_27")
        gridLayout_2.addWidget(colorButton_27, 1, 12, 1, 1)
        colorButton_22 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_22.sizePolicy().hasHeightForWidth())
        colorButton_22.sSP..(sizePolicy)
        colorButton_22.sMS..(QtCore.?S..(20, 20))
        colorButton_22.sMS..(QtCore.?S..(20, 13))
        colorButton_22.setText("")
        colorButton_22.setObjectName("colorButton_22")
        gridLayout_2.addWidget(colorButton_22, 1, 7, 1, 1)
        colorButton_15 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_15.sizePolicy().hasHeightForWidth())
        colorButton_15.sSP..(sizePolicy)
        colorButton_15.sMS..(QtCore.?S..(20, 20))
        colorButton_15.sMS..(QtCore.?S..(20, 13))
        colorButton_15.setText("")
        colorButton_15.setObjectName("colorButton_15")
        gridLayout_2.addWidget(colorButton_15, 1, 0, 1, 1)
        colorButton_5 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_5.sizePolicy().hasHeightForWidth())
        colorButton_5.sSP..(sizePolicy)
        colorButton_5.sMS..(QtCore.?S..(20, 20))
        colorButton_5.sMS..(QtCore.?S..(20, 13))
        colorButton_5.setText("")
        colorButton_5.setObjectName("colorButton_5")
        gridLayout_2.addWidget(colorButton_5, 0, 4, 1, 1)
        colorButton_2 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_2.sizePolicy().hasHeightForWidth())
        colorButton_2.sSP..(sizePolicy)
        colorButton_2.sMS..(QtCore.?S..(20, 20))
        colorButton_2.sMS..(QtCore.?S..(20, 13))
        colorButton_2.setText("")
        colorButton_2.setObjectName("colorButton_2")
        gridLayout_2.addWidget(colorButton_2, 0, 1, 1, 1)
        colorButton_16 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_16.sizePolicy().hasHeightForWidth())
        colorButton_16.sSP..(sizePolicy)
        colorButton_16.sMS..(QtCore.?S..(20, 20))
        colorButton_16.sMS..(QtCore.?S..(20, 13))
        colorButton_16.setText("")
        colorButton_16.setObjectName("colorButton_16")
        gridLayout_2.addWidget(colorButton_16, 1, 1, 1, 1)
        colorButton_14 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_14.sizePolicy().hasHeightForWidth())
        colorButton_14.sSP..(sizePolicy)
        colorButton_14.sMS..(QtCore.?S..(20, 20))
        colorButton_14.sMS..(QtCore.?S..(20, 13))
        colorButton_14.setText("")
        colorButton_14.setObjectName("colorButton_14")
        gridLayout_2.addWidget(colorButton_14, 0, 13, 1, 1)
        colorButton_4 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_4.sizePolicy().hasHeightForWidth())
        colorButton_4.sSP..(sizePolicy)
        colorButton_4.sMS..(QtCore.?S..(20, 20))
        colorButton_4.sMS..(QtCore.?S..(20, 13))
        colorButton_4.setText("")
        colorButton_4.setObjectName("colorButton_4")
        gridLayout_2.addWidget(colorButton_4, 0, 3, 1, 1)
        colorButton_21 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_21.sizePolicy().hasHeightForWidth())
        colorButton_21.sSP..(sizePolicy)
        colorButton_21.sMS..(QtCore.?S..(20, 20))
        colorButton_21.sMS..(QtCore.?S..(20, 13))
        colorButton_21.setText("")
        colorButton_21.setObjectName("colorButton_21")
        gridLayout_2.addWidget(colorButton_21, 1, 6, 1, 1)
        colorButton_25 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_25.sizePolicy().hasHeightForWidth())
        colorButton_25.sSP..(sizePolicy)
        colorButton_25.sMS..(QtCore.?S..(20, 20))
        colorButton_25.sMS..(QtCore.?S..(20, 13))
        colorButton_25.setText("")
        colorButton_25.setObjectName("colorButton_25")
        gridLayout_2.addWidget(colorButton_25, 1, 10, 1, 1)
        colorButton_12 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_12.sizePolicy().hasHeightForWidth())
        colorButton_12.sSP..(sizePolicy)
        colorButton_12.sMS..(QtCore.?S..(20, 20))
        colorButton_12.sMS..(QtCore.?S..(20, 13))
        colorButton_12.setText("")
        colorButton_12.setObjectName("colorButton_12")
        gridLayout_2.addWidget(colorButton_12, 0, 11, 1, 1)
        colorButton_19 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_19.sizePolicy().hasHeightForWidth())
        colorButton_19.sSP..(sizePolicy)
        colorButton_19.sMS..(QtCore.?S..(20, 20))
        colorButton_19.sMS..(QtCore.?S..(20, 13))
        colorButton_19.setText("")
        colorButton_19.setObjectName("colorButton_19")
        gridLayout_2.addWidget(colorButton_19, 1, 4, 1, 1)
        colorButton_13 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_13.sizePolicy().hasHeightForWidth())
        colorButton_13.sSP..(sizePolicy)
        colorButton_13.sMS..(QtCore.?S..(20, 20))
        colorButton_13.sMS..(QtCore.?S..(20, 13))
        colorButton_13.setText("")
        colorButton_13.setObjectName("colorButton_13")
        gridLayout_2.addWidget(colorButton_13, 0, 12, 1, 1)
        colorButton_26 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_26.sizePolicy().hasHeightForWidth())
        colorButton_26.sSP..(sizePolicy)
        colorButton_26.sMS..(QtCore.?S..(20, 20))
        colorButton_26.sMS..(QtCore.?S..(20, 13))
        colorButton_26.setText("")
        colorButton_26.setObjectName("colorButton_26")
        gridLayout_2.addWidget(colorButton_26, 1, 11, 1, 1)
        colorButton_28 = QtWidgets.QPushButton(widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(colorButton_28.sizePolicy().hasHeightForWidth())
        colorButton_28.sSP..(sizePolicy)
        colorButton_28.sMS..(QtCore.?S..(20, 20))
        colorButton_28.sMS..(QtCore.?S..(20, 13))
        colorButton_28.setText("")
        colorButton_28.setObjectName("colorButton_28")
        gridLayout_2.addWidget(colorButton_28, 1, 13, 1, 1)
        horizontalLayout_2.addWidget(widget_2)
        stampnextButton = QtWidgets.QPushButton(centralWidget)
        stampnextButton.sMS..(QtCore.?S..(78, 55))
        stampnextButton.sMS..(QtCore.?S..(78, 55))
        stampnextButton.setText("")
        stampnextButton.setIconSize(QtCore.?S..(80, 50))
        stampnextButton.setObjectName("stampnextButton")
        horizontalLayout_2.addWidget(stampnextButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.E.., QtWidgets.QSizePolicy.Minimum)
        horizontalLayout_2.aI..(spacerItem1)
        verticalLayout.aL..(horizontalLayout_2)
        MainWindow.setCentralWidget(centralWidget)
        menuBar = QtWidgets.QMenuBar(MainWindow)
        menuBar.setGeometry(QtCore.QRect(0, 0, 549, 22))
        menuBar.setObjectName("menuBar")
        menuFIle = QtWidgets.QMenu(menuBar)
        menuFIle.setObjectName("menuFIle")
        menuEdit = QtWidgets.QMenu(menuBar)
        menuEdit.setObjectName("menuEdit")
        menuImage = QtWidgets.QMenu(menuBar)
        menuImage.setObjectName("menuImage")
        menuHelp = QtWidgets.QMenu(menuBar)
        menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(menuBar)
        statusBar = QtWidgets.QStatusBar(MainWindow)
        statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(statusBar)
        fileToolbar = QtWidgets.QToolBar(MainWindow)
        fileToolbar.setIconSize(QtCore.?S..(16, 16))
        fileToolbar.setObjectName("fileToolbar")
        MainWindow.aTB..(QtCore.Qt.TopToolBarArea, fileToolbar)
        drawingToolbar = QtWidgets.QToolBar(MainWindow)
        drawingToolbar.setIconSize(QtCore.?S..(16, 16))
        drawingToolbar.setObjectName("drawingToolbar")
        MainWindow.aTB..(QtCore.Qt.TopToolBarArea, drawingToolbar)
        fontToolbar = QtWidgets.QToolBar(MainWindow)
        fontToolbar.setIconSize(QtCore.?S..(16, 16))
        fontToolbar.setObjectName("fontToolbar")
        MainWindow.aTB..(QtCore.Qt.TopToolBarArea, fontToolbar)
        actionCopy = QtWidgets.QAction(MainWindow)
        actionCopy.setObjectName("actionCopy")
        actionClearImage = QtWidgets.QAction(MainWindow)
        actionClearImage.setObjectName("actionClearImage")
        actionOpenImage = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.?P..("images/blue-folder-open-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionOpenImage.setIcon(icon16)
        actionOpenImage.setObjectName("actionOpenImage")
        actionSaveImage = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.?P..("images/disk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionSaveImage.setIcon(icon17)
        actionSaveImage.setObjectName("actionSaveImage")
        actionInvertColors = QtWidgets.QAction(MainWindow)
        actionInvertColors.setObjectName("actionInvertColors")
        actionFlipHorizontal = QtWidgets.QAction(MainWindow)
        actionFlipHorizontal.setObjectName("actionFlipHorizontal")
        actionFlipVertical = QtWidgets.QAction(MainWindow)
        actionFlipVertical.setObjectName("actionFlipVertical")
        actionNewImage = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.?P..("images/document-image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionNewImage.setIcon(icon18)
        actionNewImage.setObjectName("actionNewImage")
        actionBold = QtWidgets.QAction(MainWindow)
        actionBold.setCheckable( st.
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.?P..("images/edit-bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionBold.setIcon(icon19)
        actionBold.setObjectName("actionBold")
        actionItalic = QtWidgets.QAction(MainWindow)
        actionItalic.setCheckable( st.
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.?P..("images/edit-italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionItalic.setIcon(icon20)
        actionItalic.setObjectName("actionItalic")
        actionUnderline = QtWidgets.QAction(MainWindow)
        actionUnderline.setCheckable( st.
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.?P..("images/edit-underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionUnderline.setIcon(icon21)
        actionUnderline.setObjectName("actionUnderline")
        actionFillShapes = QtWidgets.QAction(MainWindow)
        actionFillShapes.setCheckable( st.
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.?P..("images/paint-can-color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        actionFillShapes.setIcon(icon22)
        actionFillShapes.setObjectName("actionFillShapes")
        menuFIle.addAction(actionNewImage)
        menuFIle.addAction(actionOpenImage)
        menuFIle.addAction(actionSaveImage)
        menuEdit.addAction(actionCopy)
        menuEdit.addSeparator()
        menuEdit.addAction(actionClearImage)
        menuImage.addAction(actionInvertColors)
        menuImage.addSeparator()
        menuImage.addAction(actionFlipHorizontal)
        menuImage.addAction(actionFlipVertical)
        menuBar.addAction(menuFIle.menuAction())
        menuBar.addAction(menuEdit.menuAction())
        menuBar.addAction(menuImage.menuAction())
        menuBar.addAction(menuHelp.menuAction())
        fileToolbar.addAction(actionNewImage)
        fileToolbar.addAction(actionOpenImage)
        fileToolbar.addAction(actionSaveImage)

        retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore. ?CA...translate
        MainWindow.sWT..(_translate("MainWindow", "Piecasso"))
        menuFIle.setTitle(_translate("MainWindow", "FIle"))
        menuEdit.setTitle(_translate("MainWindow", "Edit"))
        menuImage.setTitle(_translate("MainWindow", "Image"))
        menuHelp.setTitle(_translate("MainWindow", "Help"))
        fileToolbar.sWT..(_translate("MainWindow", "toolBar"))
        drawingToolbar.sWT..(_translate("MainWindow", "toolBar"))
        fontToolbar.sWT..(_translate("MainWindow", "toolBar"))
        actionCopy.setText(_translate("MainWindow", "Copy"))
        actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        actionClearImage.setText(_translate("MainWindow", "Clear Image"))
        actionOpenImage.setText(_translate("MainWindow", "Open Image..."))
        actionSaveImage.setText(_translate("MainWindow", "Save Image As..."))
        actionInvertColors.setText(_translate("MainWindow", "Invert Colors"))
        actionFlipHorizontal.setText(_translate("MainWindow", "Flip Horizontal"))
        actionFlipVertical.setText(_translate("MainWindow", "Flip Vertical"))
        actionNewImage.setText(_translate("MainWindow", "New Image"))
        actionBold.setText(_translate("MainWindow", "Bold"))
        actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        actionItalic.setText(_translate("MainWindow", "Italic"))
        actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        actionUnderline.setText(_translate("MainWindow", "Underline"))
        actionFillShapes.setText(_translate("MainWindow", "Fill Shapes?"))

