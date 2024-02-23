from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(301, 424)
        icon = QtGui.QIcon(":/design/Icon.png")
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(105, 345, 90, 90))
        self.pushButton.setStyleSheet("border : 2px solid; background-color: rgba(0,0,0,0); border: 2px solid rgba(0,0,0,0); font: 11px; color: red")
        self.pushButton.clicked.connect(self.calculate)
        
        self.label_clicked = QtWidgets.QLabel(MainWindow)
        self.label_clicked.setGeometry(110, 350, 80, 80)
        self.label_clicked.setStyleSheet("font: 80px")
        self.label_clicked.setText("❤")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -18, 301, 421))
        self.label.setStyleSheet("border-image: url(:/design/background.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 3, 230, 35))
        self.label_2.setStyleSheet("font: 10pt \"Ravie\";")
        self.label_2.setObjectName("label_2")

        placeholder_font = QtGui.QFont()
        placeholder_font.setPointSize(10)  # Set the font size for the placeholder text

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 259, 81, 31))
        self.lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border-color: rgb(255, 255, 0); border: 2px dotted rgba(0,0,0,0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Your Name")
        self.lineEdit.setFont(placeholder_font)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 270, 81, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border-top-color: rgb(85, 255, 127); border: 2px dotted rgba(0,0,0,0)")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setPlaceholderText("Crush Name")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(placeholder_font)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(126, 170, 81, 45))
        self.textEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0); \n"
"border-color: rgba(0, 0, 0, 0); border: 2px dotted rgba(0, 0, 0, 0); font: 25px; color: red")
        self.textEdit.setEnabled(False)

        self.TextEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_1.setGeometry(QtCore.QRect(20, 50, 261, 100))
        self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 16px \"Arial\"; color: black; border: 2px dotted black")
        self.TextEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.TextEdit_1.setReadOnly(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setStyleSheet("background-color: black; color: red")
        self.menubar.setObjectName("menubar")

        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")

        MainWindow.setMenuBar(self.menubar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.triggered.connect(self.help)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.triggered.connect(self.about)

        self.menuMenu.addAction(self.actionHelp)
        self.menuMenu.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.text_clear_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Ctrl+D"), MainWindow)
        self.text_clear_shortcut.activated.connect(self.clear)

        self.pushButton.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def calculate(self):
        self.sum1 = sum([ord(char) for char in str(self.lineEdit.text()).lower()])
        self.sum2 = sum([ord(char) for char in str(self.lineEdit_2.text()).lower()])

        love_percentage = (self.sum1 + self.sum2) % 100

        if self.sum1 != 0 and self.sum2 !=0:
            if love_percentage <= 20 and love_percentage != 0:
                self.TextEdit_1.setHtml("<i><b>A modest start to the journey of love.</b> There's room for growth and discovery. Keep nurturing the connection.</i>")

            elif love_percentage <= 40 and love_percentage != 0:
                self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 17px \"Arial\"; color: beige; border: 2px dotted green")
                self.TextEdit_1.setHtml("<i><b>The spark is there,</b> and there's potential for deeper feelings. Cultivate the bond and see where it leads.</i>")

            elif love_percentage <= 70 and love_percentage != 0:
                self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 17px \"Arial\"; color: lightblue; border: 2px dotted brown")
                self.TextEdit_1.setHtml("<i><b>A substantial percentage of love is evident.</b> Your connection is solid, and there's a good foundation for a meaningful relationship.</i>")

            elif love_percentage <= 90 and love_percentage != 0:
                self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 16px \"Arial\"; color: pink; border: 2px dotted #352F44")
                self.TextEdit_1.setHtml("<i><b>Love is flourishing!</b> Your connection is strong, and there's a profound understanding between you two. Cherish the special moments.</i>")
        
            elif love_percentage <= 99 and love_percentage != 0:
                self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 17px \"Arial\"; color: yellow; border: 2px dotted #F6B17A;")
                self.TextEdit_1.setHtml("<i><b>An exceptional level of love!</b> Your bond is extraordinary, and it's a rare connection. Treasure the deep affection you share.</i>")

            elif love_percentage == 100:
                self.TextEdit_1.setStyleSheet("background-color: rgba(0,0,0,0); font: 17px \"Arial\"; color: red; border: 2px dotted red")
                self.TextEdit_1.setText("<i><b>Congratulations!</b> You've achieved a perfect score on the love scale. Your connection is unparalleled, and it's a testament to the extraordinary love you both share.</i>")
        
            else:
                self.TextEdit_1.setText("Please enter the names")

            self.textEdit.setText(f"{love_percentage}%")
        else:
            self.TextEdit_1.setText("Please fill out the required information on the form.")

    def clear(self):
        self.textEdit.clear()
        self.TextEdit_1.clear()
        self.lineEdit.clear()
        self.lineEdit_2.clear()

    def help(self):
        help_text = """To utilize this application procedurally 
        • Enter your name (surname optional).
        • Input your partner's name (surname optional) 
        • Click "submit" to determine the love compatibility between you two
        • Press (ctrl+D) to clear the previous input 
        • Feel free to input new information as desired \n\n* The inclusion of a surname will alter the calculated percentage of affection."""

        help_box = QMessageBox()
        help_box.setIcon(QMessageBox.Question)
        help_icon = QtGui.QIcon(":/design/Icon.png")
        help_box.setWindowIcon(help_icon)
        help_box.setWindowTitle("How to use this program")
        help_box.setStyleSheet("background-color: black; color: red")
        help_box.setText(help_text)
        help_box.exec_()

    def about(self):
        about_text = """
        The application has been created by John Scantlin B. Cayson. 🇵🇭

        Referred to as PEROVE, the app is an abbreviation for "Percent of Love" and serves the purpose of computing the percentage of affection between two individuals through an algorithm.
        This love calculator represents a project conceived for the February App Challenge, organized by the Applied Computing - M.A.C organization."""

        about_box = QMessageBox()
        about_box.setIcon(QMessageBox.Information)
        about_box.setWindowTitle("About this program")
        about_box.setStyleSheet("background-color: black; color: red")
        about_icon = QtGui.QIcon(":/design/Icon.png")
        about_box.setWindowIcon(about_icon)
        about_box.setText(about_text)
        about_box.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Percent of Love"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:23pt; color:#00ffff;\">PEROVE</span></p></body></html>"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionHelp.setText(_translate("MainWindor", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))

import loveCal_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
