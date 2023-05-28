from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import resources  # generated after adding graphics to your UI in Pyqt Designer
from db_manager import DBManager
import sys
from add_student import AddUserUI
from search_sid import UISearchSID
from search_name import UINameSearch

# Main Screen of Program
class MainUI(QMainWindow):
    def __init__(self):
        # This is needed here to inherit methods and data from QMainWindow
        super().__init__()
        self.setup_ui(self)  # This method was provided by PyQt Designer. Note the snake_case update
        self.retranslate_ui(self)  # This method was provided by PyQt Designer. Note the snake_case update
        self.db_manager = DBManager('..')

    # Opens the search-by-student-name dialog.
    def open_name_search_dialog(self):
        search_dialog = UINameSearch()
        search_dialog.show()
        search_dialog.exec_()

    # Loads initial records into the database
    def load_records(self):
        self.db_manager.open_connection()
        self.db_manager.init_tables()  # initialize your table(s): process the lists and load data into your DB
        self.db_manager.close_connection()

    # Main window UI setup
    def setup_ui(self, main_window):
        main_window.setObjectName("Student Account Management System (SAMS)")
        main_window.resize(744, 511)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.main_title = QtWidgets.QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(130, 50, 491, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.main_title.setFont(font)
        self.main_title.setObjectName("main_title")
        self.graphic_img = QtWidgets.QLabel(self.centralwidget)
        self.graphic_img.setGeometry(QtCore.QRect(-10, 90, 801, 461))
        self.graphic_img.setObjectName("graphic_img")

        self.add_student_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_student_btn.clicked.connect(self.open_add_user)            # When button clicked, open add user page
        self.add_student_btn.setGeometry(QtCore.QRect(140, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.add_student_btn.setFont(font)
        self.add_student_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n" "border-radius:8px")
        self.add_student_btn.setObjectName("add_student_btn")

        self.search_id = QtWidgets.QPushButton(self.centralwidget)
        self.search_id.setGeometry(QtCore.QRect(320, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.search_id.setFont(font)
        self.search_id.setStyleSheet("background-color: rgb(255, 255, 255);\n" "border-radius:8px;")
        self.search_id.setObjectName("search_id")
        self.search_id.clicked.connect(self.open_search_sid)                # When button clicked, open search by SID page

        self.search_name = QtWidgets.QPushButton(self.centralwidget)
        self.search_name.clicked.connect(self.open_name_search_dialog)      # When button clicked, open search by name page
        self.search_name.setGeometry(QtCore.QRect(490, 200, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.search_name.setFont(font)
        self.search_name.setStyleSheet("background-color: rgb(255, 255, 255);\n" "border-color: rgb(0, 0, 0);\n" "border-radius:8px;\n""")
        self.search_name.setObjectName("search_name")

        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(650, 420, 75, 31))
        self.quit_btn.clicked.connect(self.close)                           # Closes the program when pressed
        font = QtGui.QFont()
        font.setFamily("Segoe UI Historic")
        self.quit_btn.setFont(font)
        self.quit_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n" "border-radius:8px;")
        self.quit_btn.setObjectName("quit_btn")

        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("Student Account Management System (SAMS)", "Student Account Management System (SAMS)"))
        self.main_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:22pt;\">Student Account Management System</span></p></body></html>"))
        self.graphic_img.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/graphic_img/wave1.png\"/></p></body></html>"))
        self.add_student_btn.setText(_translate("MainWindow", "Add Student"))
        self.search_id.setText(_translate("MainWindow", "Search by ID"))
        self.search_name.setText(_translate("MainWindow", "Search by Name"))
        self.quit_btn.setText(_translate("MainWindow", "Quit"))

    # Opens add user screen when called
    def open_add_user(self):
        self.dialog = AddUserUI()
        self.dialog.show()
        self.dialog.exec_()

    # Opens search by student ID screen when called
    def open_search_sid(self):
        self.search_sid = UISearchSID()
        self.search_sid.show()
        self.search_sid.exec_()


# Creates app screen and main UI screen
def main():
    app = QApplication(sys.argv)
    ui = MainUI()  # creates an instance of the MainUI
    ui.show()
    ui.load_records()   # Initializes db table with list of students
    sys.exit(app.exec_())


main()

