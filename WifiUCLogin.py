from PyQt5.QtWidgets import QApplication
import sys
from main_window import Application
# launcher
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Application()
    main.show()
    app.exec()