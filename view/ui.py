# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 603)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.assetView = QTableView(self.centralwidget)
        self.assetView.setObjectName(u"assetView")
        self.assetView.setGeometry(QRect(130, 90, 631, 391))
        self.uploadButton = QPushButton(self.centralwidget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(31, 139, 80, 81))
        self.createButton = QPushButton(self.centralwidget)
        self.createButton.setObjectName(u"createButton")
        self.createButton.setGeometry(QRect(680, 490, 80, 51))
        self.deleteButton = QPushButton(self.centralwidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(30, 260, 80, 81))
        self.projectEdit = QLineEdit(self.centralwidget)
        self.projectEdit.setObjectName(u"projectEdit")
        self.projectEdit.setGeometry(QRect(30, 37, 731, 41))
        self.updateButton = QPushButton(self.centralwidget)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setGeometry(QRect(30, 380, 80, 81))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(140, 500, 511, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.projectNameEdit = QLineEdit(self.widget)
        self.projectNameEdit.setObjectName(u"projectNameEdit")

        self.horizontalLayout.addWidget(self.projectNameEdit)

        self.newAssetTypeEdit = QLineEdit(self.widget)
        self.newAssetTypeEdit.setObjectName(u"newAssetTypeEdit")

        self.horizontalLayout.addWidget(self.newAssetTypeEdit)

        self.newAssetNameEdit = QLineEdit(self.widget)
        self.newAssetNameEdit.setObjectName(u"newAssetNameEdit")

        self.horizontalLayout.addWidget(self.newAssetNameEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 835, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Asset Manager", None))
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"upload", None))
        self.createButton.setText(QCoreApplication.translate("MainWindow", u"create", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"delete", None))
        self.updateButton.setText(QCoreApplication.translate("MainWindow", u"update", None))
    # retranslateUi

