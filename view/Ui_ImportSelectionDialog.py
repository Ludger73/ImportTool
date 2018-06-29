# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportSelectionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImportSelectionDialog(object):
    def setupUi(self, ImportSelectionDialog):
        ImportSelectionDialog.setObjectName("ImportSelectionDialog")
        ImportSelectionDialog.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(ImportSelectionDialog)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")

        self.retranslateUi(ImportSelectionDialog)
        self.button_box.accepted.connect(ImportSelectionDialog.accept)
        self.button_box.rejected.connect(ImportSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImportSelectionDialog)

    def retranslateUi(self, ImportSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        ImportSelectionDialog.setWindowTitle(_translate("ImportSelectionDialog", "ImportSelection"))

