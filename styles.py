OK_STATE_STYLE = """color: #86ff79;
font: bold 12pt "Calibri";"""

ERROR_STATE_STYLE = """color: #ff7e7e;
font: bold 12pt "Calibri";"""

styleLineEditOk = ("QLineEdit {\n"
                   "    border: 2px solid rgb(45, 45, 45);\n"
                   "    border-radius: 15px;\n"
                   "    padding: 15px;\n"
                   "    background-color: rgb(30, 30, 30);    \n"
                   "    color: rgb(100, 100, 100);\n"
                   "}\n"
                   "QLineEdit:hover {\n"
                   "    border: 2px solid rgb(55, 55, 55);\n"
                   "}\n"
                   "QLineEdit:focus {\n"
                   "    border: 2px solid rgb(255, 207, 0);    \n"
                   "    color: rgb(200, 200, 200);\n"
                   "}")

styleLineEditError = ("QLineEdit {\n"
                      "    border: 2px solid rgb(255, 85, 127);\n"
                      "    border-radius: 15px;\n"
                      "    padding: 15px;\n"
                      "    background-color: rgb(30, 30, 30);    \n"
                      "    color: rgb(100, 100, 100);\n"
                      "}\n"
                      "QLineEdit:hover {\n"
                      "    border: 2px solid rgb(55, 55, 55);\n"
                      "}\n"
                      "QLineEdit:focus {\n"
                      "    border: 2px solid rgb(255, 207, 0);    \n"
                      "    color: rgb(200, 200, 200);\n"
                      "}")

stylePopupError = ("background-color: rgb(255, 85, 127); border-radius: 5px;")
stylePopupOk = ("background-color: rgb(0, 255, 123); border-radius: 5px;")
