from importlib import resources
import threading
import webbrowser
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QGraphicsDropShadowEffect, QCompleter
from PyQt5.QtCore import (QEasingCurve, QEvent, QPropertyAnimation, QRect, Qt,
                          QTime, QTimer, QUrl, pyqtProperty)
from PyQt5.QtGui import QColor, QIcon, QPixmap
from PyQt5 import uic
from const import *
from login import Login
from main import Ui_MainWindow
from net import *
from threads import LoginThread
from user import User
from util import *
from styles import *
import icons_rc
import file_rc
import app_resources

class Application(Ui_MainWindow, QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        #uic.loadUi("main.ui", self)
        self.init()
        self.connections()

    def update_users_list(self):
        my_completer = QCompleter(get_usernames(self.users), self)
        my_completer.setCaseSensitivity(0)
        self.user_line_edit.setCompleter(my_completer)
        
    def autocomplete_credentials(self, text):
        for user in self.users:
            if user.is_username(text):
                self.passw_line_edit.setText(user.password)
                break
    
    def init(self):
        # users
        self.users = load_users()
        # set autocompleter
        self.update_users_list()
        # message box
        self.message = None
        #
        self.wait_message.setVisible(False)
        # setting icon by resources
        self.close_popup.setIcon(QIcon(":/Graphics/graphics/cil-x.png"))
        # setting up window title
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon(":/Icon/graphics/skypewifi.png"))
        self.jalexcode.setPixmap(QPixmap(":/images/images/jalex.png"))
        # hide error widget
        self.frame_error.hide()
        # set visual effects
        self.set_visual_effects(self.frame_error)
        self.set_visual_effects(self.cardview)
        # focus on Username
        self.user_line_edit.setFocus()
        # is password visible
        self.password_shown = False
        # toggle action
        self.visibleIcon = QIcon(":/icons/icons/eye_on_32x32.png")
        self.hiddenIcon = QIcon(":/icons/icons/eye_off_32x32.png")
        self.togglepasswordAction = self.passw_line_edit.addAction(self.visibleIcon,
                                                                   QLineEdit.ActionPosition.TrailingPosition)
        self.togglepasswordAction.triggered.connect(
            self.on_toggle_password_Action)

    def connections(self):
        self.login_button.clicked.connect(self.login)
        self.close_popup.clicked.connect(self.closeMessage)
        self.show_details.clicked.connect(self.details_message)
        # username on text change
        self.user_line_edit.textChanged.connect(self.autocomplete_credentials)
        # about
        self.about_action.triggered.connect(self.about)
        # links
        self.github_action.triggered.connect(lambda: webbrowser.open(DEVELOPER_GITHUB, new=1, autoraise=False))
        self.gitlab_action.triggered.connect(lambda: webbrowser.open(DEVELOPER_GITLAB, new=1, autoraise=False))
        self.telegram_action.triggered.connect(lambda: webbrowser.open(DEVELOPER_TELEGRAM, new=1, autoraise=False))
        self.facebook_action.triggered.connect(lambda: webbrowser.open(DEVELOPER_FACEBOOK, new=1, autoraise=False))

    def login(self):
        user = self.user_line_edit.text()
        passw = self.passw_line_edit.text()
        # 
        if user and passw:
            try:
                # try to login
                login = Login(user=user, passw=passw)
                login_thread = LoginThread(login)
                # signals
                login_thread.post_request_signal.connect(lambda: self.show_hide_wait_message(True))
                login_thread.error_signal.connect(self.post_error)
                login_thread.finish_signal.connect(self.post_success)
                # launch thread
                task = threading.Thread(target=login_thread.run)
                task.start()
            except Exception as error:
                self.error("Hilo de petición", "Ha fallado el proceso", error.args[0])
        else:
            self.error("Login", "Debe ingresar un usuario y una contraseña")

    def show_hide_wait_message(self, b:bool):
        self.wait_message.setVisible(b)
        self.cardview.setVisible(not b)
    
    def post_error(self, exception:Exception):
        if isinstance(exception, LoginError):
            self.set_state(exception.args[0], STATE_ERROR)
        elif isinstance(exception, BadServerResponseCode):
            self.set_state(exception.args[0], STATE_ERROR)
        elif isinstance(exception, requests.exceptions.ConnectionError):
            self.error("Mientras se conectaba",
                           "Ha fallado la conexión", str(exception.args[0]))
        self.show_hide_wait_message(False)
    
    def post_success(self):
        self.show_hide_wait_message(False)
        # if success, show notification
        self.set_state("Ya está conectado", STATE_OK)
        # save user
        user = self.user_line_edit.text()
        passw = self.passw_line_edit.text()
        self.users.append(User(username=user, password=passw))
        save_users(self.users)
        # update autocompleter
        self.update_users_list()
    
    # show an error notification
    def error(self, place, text="", details=""):
        self.message = QMessageBox(
            QMessageBox.Icon.Critical, "Error", f"* {place} *")
        self.message.buttonClicked.connect(self.frame_error.close)
        self.message.setBaseSize(300, 100)
        self.message.setInformativeText(f"-> {text}")
        show_details = False
        if details:
            self.message.setDetailedText(str(details))
            show_details = True
        #
        self.showMessage(text.split("\n")[0], False, show_details)
        self.frame_error.setStyleSheet(stylePopupError)

    # when Ver detalles label is pressed, it shows the QMessageBox
    def details_message(self):
        if self.message is not None:
            self.message.exec_()
            self.message = None

    # green or red
    def set_state(self, message: str, type: int):
        self.showMessage(message, True if type == STATE_OK else False)

    # toggle action for show/hide password button
    def on_toggle_password_Action(self):
        if not self.password_shown:
            self.passw_line_edit.setEchoMode(QLineEdit.Normal)
            self.password_shown = True
            self.togglepasswordAction.setIcon(self.hiddenIcon)
        else:
            self.passw_line_edit.setEchoMode(QLineEdit.Password)
            self.password_shown = False
            self.togglepasswordAction.setIcon(self.visibleIcon)

    # set shadow effect to a widget
    def set_visual_effects(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(QColor(0, 0, 0))
        shadow.setBlurRadius(20)
        shadow.setOffset(0)
        widget.setGraphicsEffect(shadow)

    # shows/hides the notification with an animation
    def animate_notification(self, show=True):
        parent = self.frame_error.parent()
        spacing = 5
        coord = parent.x()+spacing, parent.y()+spacing
        if show:
            start = *coord, 0, parent.height()-spacing
            end = *coord, parent.width()-spacing*2, parent.height()-spacing
        else:
            start = *coord, parent.width()-spacing*2, parent.height()-spacing
            end = *coord, 0, parent.height()
        self.frame_error.setGeometry(*start)
        if show:
            self.frame_error.show()
        self.animation = QPropertyAnimation(self.frame_error, b"geometry")
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)
        self.animation.setStartValue(QRect(*start))
        self.animation.setEndValue(QRect(*end))
        self.animation.start()
        self.frame_error.setGeometry(*end)
        if not show:
            self.frame_error.hide()
    
    def showMessage(self, message, status=False, show_details=False):
        self.animate_notification()
        self.label_error.setText(message)
        if status:
            self.frame_error.setStyleSheet(stylePopupOk)
        else:
            self.frame_error.setStyleSheet(stylePopupError)
        self.show_details.setVisible(show_details)

    def closeMessage(self):
        self.animate_notification(False)
        
    def about(self):
        QMessageBox.information(self, f"Acerca de {APP_NAME}", ABOUT_MESSAGE)