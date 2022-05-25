# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(840, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget #centralwidget {\n"
"    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 212, 255), stop:1 rgba(113, 93, 255, 255));\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 30))
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 50))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(20, 5, 20, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_bar)
        self.frame_error.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 85, 127);\n"
"border-radius: 10px;")
        self.frame_error.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setStyleSheet("font: 11pt \"Calibri\";")
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.show_details = QtWidgets.QToolButton(self.frame_error)
        self.show_details.setStyleSheet("QToolButton{\n"
"color: rgb(0, 0, 0);\n"
"font: bold 8pt \"Segoe UI\";\n"
"}\n"
"QToolButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.show_details.setObjectName("show_details")
        self.horizontalLayout_3.addWidget(self.show_details)
        self.close_popup = QtWidgets.QPushButton(self.frame_error)
        self.close_popup.setMaximumSize(QtCore.QSize(20, 20))
        self.close_popup.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;    \n"
"    background-image: url(:/Close_Image/graphics/cil-x.png);\n"
"    background-position: center;    \n"
"    background-color: rgb(60, 60, 60, 150);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);    \n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(35, 35, 35);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.close_popup.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Graphics/graphics/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_popup.setIcon(icon)
        self.close_popup.setObjectName("close_popup")
        self.horizontalLayout_3.addWidget(self.close_popup)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.gridLayout_5.addWidget(self.top_bar, 0, 0, 1, 1)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cardview = QtWidgets.QWidget(self.widget_4)
        self.cardview.setMinimumSize(QtCore.QSize(250, 0))
        self.cardview.setMaximumSize(QtCore.QSize(400, 400))
        self.cardview.setStyleSheet("QWidget #cardview{\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(43, 110, 255);\n"
"    border-radius: 5px;\n"
"    font: 14pt \"Calibri\";\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 5px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: rgb(1, 51, 188);\n"
"}\n"
"QPushButton::pressed{\n"
"    background-color: rgb(1, 43, 120);\n"
"}")
        self.cardview.setObjectName("cardview")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.cardview)
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(120, 335, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 2)
        self.login_button = QtWidgets.QPushButton(self.cardview)
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.gridLayout_3.addWidget(self.login_button, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.cardview)
        self.label.setMinimumSize(QtCore.QSize(210, 0))
        self.label.setMaximumSize(QtCore.QSize(210, 100))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/graphics/captiveportal-logo..png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.widget_2 = QtWidgets.QWidget(self.cardview)
        self.widget_2.setStyleSheet("QLabel{\n"
"    font: bold 10pt \"Calibri\";\n"
"    color: rgb(47, 47, 47);\n"
"}\n"
"QLineEdit{\n"
"    font: 14pt \"Calibri\";\n"
"    color: rgb(47, 47, 47);\n"
"    border-bottom: 1px solid rgb(227, 227, 227);\n"
"}\n"
"QLineEdit::focus{\n"
"    border-bottom: 2px solid  rgb(43, 110, 255);\n"
"    background-color: rgb(225, 225, 225);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.user_line_edit = QtWidgets.QLineEdit(self.widget)
        self.user_line_edit.setMaxLength(20)
        self.user_line_edit.setFrame(False)
        self.user_line_edit.setClearButtonEnabled(True)
        self.user_line_edit.setObjectName("user_line_edit")
        self.gridLayout.addWidget(self.user_line_edit, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.passw_line_edit = QtWidgets.QLineEdit(self.widget_3)
        self.passw_line_edit.setMaxLength(20)
        self.passw_line_edit.setFrame(False)
        self.passw_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passw_line_edit.setPlaceholderText("")
        self.passw_line_edit.setClearButtonEnabled(True)
        self.passw_line_edit.setObjectName("passw_line_edit")
        self.gridLayout_2.addWidget(self.passw_line_edit, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.widget_3, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_2, 2, 0, 1, 2)
        self.state_label = QtWidgets.QLabel(self.cardview)
        self.state_label.setStyleSheet("color: rgb(121, 121, 121);\n"
"font: bold 12pt \"Calibri\";")
        self.state_label.setText("")
        self.state_label.setAlignment(QtCore.Qt.AlignCenter)
        self.state_label.setObjectName("state_label")
        self.gridLayout_3.addWidget(self.state_label, 3, 0, 1, 2)
        self.gridLayout_6.addWidget(self.cardview, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 68, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(203, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 65, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(203, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem6, 1, 2, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.jalexcode = QtWidgets.QLabel(self.widget_5)
        self.jalexcode.setMinimumSize(QtCore.QSize(0, 60))
        self.jalexcode.setMaximumSize(QtCore.QSize(260, 60))
        self.jalexcode.setText("")
        self.jalexcode.setScaledContents(True)
        self.jalexcode.setAlignment(QtCore.Qt.AlignCenter)
        self.jalexcode.setObjectName("jalexcode")
        self.gridLayout_7.addWidget(self.jalexcode, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_6.addWidget(self.widget_5, 3, 0, 1, 3)
        self.gridLayout_5.addWidget(self.widget_4, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 21))
        self.menubar.setObjectName("menubar")
        self.menuLogin_UC = QtWidgets.QMenu(self.menubar)
        self.menuLogin_UC.setObjectName("menuLogin_UC")
        self.info_action = QtWidgets.QMenu(self.menubar)
        self.info_action.setObjectName("info_action")
        self.menuEnlaces = QtWidgets.QMenu(self.info_action)
        self.menuEnlaces.setObjectName("menuEnlaces")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.actionGitLab = QtWidgets.QAction(MainWindow)
        self.actionGitLab.setObjectName("actionGitLab")
        self.actionTelegram = QtWidgets.QAction(MainWindow)
        self.actionTelegram.setObjectName("actionTelegram")
        self.github_action = QtWidgets.QAction(MainWindow)
        self.github_action.setObjectName("github_action")
        self.gitlab_action = QtWidgets.QAction(MainWindow)
        self.gitlab_action.setObjectName("gitlab_action")
        self.telegram_action = QtWidgets.QAction(MainWindow)
        self.telegram_action.setObjectName("telegram_action")
        self.facebook_action = QtWidgets.QAction(MainWindow)
        self.facebook_action.setObjectName("facebook_action")
        self.menuLogin_UC.addAction(self.actionSalir)
        self.menuEnlaces.addAction(self.github_action)
        self.menuEnlaces.addAction(self.gitlab_action)
        self.menuEnlaces.addAction(self.telegram_action)
        self.menuEnlaces.addAction(self.facebook_action)
        self.info_action.addAction(self.about_action)
        self.info_action.addAction(self.menuEnlaces.menuAction())
        self.menubar.addAction(self.menuLogin_UC.menuAction())
        self.menubar.addAction(self.info_action.menuAction())
        self.label_2.setBuddy(self.user_line_edit)
        self.label_3.setBuddy(self.passw_line_edit)

        self.retranslateUi(MainWindow)
        self.actionSalir.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.user_line_edit, self.passw_line_edit)
        MainWindow.setTabOrder(self.passw_line_edit, self.login_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login UC"))
        self.label_error.setText(_translate("MainWindow", "Error"))
        self.show_details.setText(_translate("MainWindow", "Ver detalles"))
        self.login_button.setText(_translate("MainWindow", "LOGIN"))
        self.label_2.setText(_translate("MainWindow", "Usuario"))
        self.user_line_edit.setPlaceholderText(_translate("MainWindow", "nombre.apellidos"))
        self.label_3.setText(_translate("MainWindow", "Constraseña"))
        self.menuLogin_UC.setTitle(_translate("MainWindow", "Login UC"))
        self.info_action.setTitle(_translate("MainWindow", "Info"))
        self.menuEnlaces.setTitle(_translate("MainWindow", "Enlaces"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.about_action.setText(_translate("MainWindow", "Acerca de"))
        self.actionGitLab.setText(_translate("MainWindow", "GitLab"))
        self.actionTelegram.setText(_translate("MainWindow", "Telegram"))
        self.github_action.setText(_translate("MainWindow", "GitHub"))
        self.gitlab_action.setText(_translate("MainWindow", "GitLab"))
        self.telegram_action.setText(_translate("MainWindow", "Telegram"))
        self.facebook_action.setText(_translate("MainWindow", "Facebook"))
import app_resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
