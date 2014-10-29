# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Oct 28 18:30:15 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mian_window(object):
    def setupUi(self, mian_window):
        mian_window.setObjectName(_fromUtf8("mian_window"))
        mian_window.resize(470, 125)
        mian_window.setMinimumSize(QtCore.QSize(465, 125))
        mian_window.setMaximumSize(QtCore.QSize(700, 125))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/alarm_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mian_window.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(mian_window)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(mian_window)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.due_time = QtGui.QTimeEdit(mian_window)
        self.due_time.setObjectName(_fromUtf8("due_time"))
        self.horizontalLayout.addWidget(self.due_time)
        self.label_2 = QtGui.QLabel(mian_window)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(mian_window)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.messgae_value = QtGui.QLineEdit(mian_window)
        self.messgae_value.setObjectName(_fromUtf8("messgae_value"))
        self.horizontalLayout_2.addWidget(self.messgae_value)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.close_after = QtGui.QCheckBox(mian_window)
        self.close_after.setEnabled(True)
        self.close_after.setCheckable(True)
        self.close_after.setChecked(False)
        self.close_after.setObjectName(_fromUtf8("close_after"))
        self.horizontalLayout_3.addWidget(self.close_after)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cancel_button = QtGui.QPushButton(mian_window)
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.horizontalLayout_3.addWidget(self.cancel_button)
        self.ok_button = QtGui.QPushButton(mian_window)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout_3.addWidget(self.ok_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(mian_window)
        QtCore.QMetaObject.connectSlotsByName(mian_window)
        mian_window.setTabOrder(self.due_time, self.messgae_value)
        mian_window.setTabOrder(self.messgae_value, self.close_after)
        mian_window.setTabOrder(self.close_after, self.ok_button)
        mian_window.setTabOrder(self.ok_button, self.cancel_button)

    def retranslateUi(self, mian_window):
        mian_window.setWindowTitle(_translate("mian_window", "IReminder", None))
        self.label.setText(_translate("mian_window", "When it is", None))
        self.label_2.setText(_translate("mian_window", "Remind me to:", None))
        self.label_3.setText(_translate("mian_window", "Message:", None))
        self.close_after.setText(_translate("mian_window", "Close the remider after 10 sec", None))
        self.cancel_button.setText(_translate("mian_window", "Cancel", None))
        self.ok_button.setText(_translate("mian_window", "Ok", None))

from icons import resource
