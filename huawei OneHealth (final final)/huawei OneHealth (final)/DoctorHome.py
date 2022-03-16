# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DoctorHome.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from ConsultationInput import Ui_MainWindow as consultationAdd
from ConsultationDisplay import Ui_MainWindow as consultationDisplay
from PatientDisplay import Ui_MainWindow as patientDisplay
import cgitb

cgitb.enable(format='text')


my_db = mysql.connector.connect(host="116.205.136.149",
                                port="3306",
                                user="root",
                                passwd="marron123!",
                                database="onehealth",
                                autocommit=True)
my_cursor = my_db.cursor()

class Ui_MainWindow(object):
    def __init__(self, MainWindow,loginWindow,docDetails):
        self.loginWindow = loginWindow
        self.MainWindow = MainWindow
        self.docDetails = docDetails
        self.setupUi(self.MainWindow)
        self.load_consultations(self.docDetails)
        self.MainWindow.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 646)
        MainWindow.setStyleSheet("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(390, 230, 58, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1061, 641))
        font = QtGui.QFont()
        font.setFamily("Raleway SemiBold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(25, 25))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabHome = QtWidgets.QWidget()
        self.tabHome.setObjectName("tabHome")
        self.home_heroImage = QtWidgets.QLabel(self.tabHome)
        self.home_heroImage.setGeometry(QtCore.QRect(280, 40, 500, 101))
        self.home_heroImage.setMinimumSize(QtCore.QSize(500, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.home_heroImage.setFont(font)
        self.home_heroImage.setStyleSheet("")
        self.home_heroImage.setObjectName("home_heroImage")
        self.home_calenderBtn = QtWidgets.QPushButton(self.tabHome)
        self.home_calenderBtn.setGeometry(QtCore.QRect(90, 180, 361, 150))
        self.home_calenderBtn.setMinimumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.home_calenderBtn.setFont(font)
        self.home_calenderBtn.setStyleSheet("")
        self.home_calenderBtn.setObjectName("home_calenderBtn")
        self.home_calenderBtn_2 = QtWidgets.QPushButton(self.tabHome)
        self.home_calenderBtn_2.setGeometry(QtCore.QRect(550, 180, 361, 150))
        self.home_calenderBtn_2.setMinimumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.home_calenderBtn_2.setFont(font)
        self.home_calenderBtn_2.setStyleSheet("")
        self.home_calenderBtn_2.setObjectName("home_calenderBtn_2")
        self.home_calenderBtn_3 = QtWidgets.QPushButton(self.tabHome)
        self.home_calenderBtn_3.setGeometry(QtCore.QRect(330, 370, 361, 150))
        self.home_calenderBtn_3.setMinimumSize(QtCore.QSize(300, 150))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.home_calenderBtn_3.setFont(font)
        self.home_calenderBtn_3.setStyleSheet("")
        self.home_calenderBtn_3.setObjectName("home_calenderBtn_3")
        self.tabWidget.addTab(self.tabHome, "")
        self.tab_UpcomingConsultation = QtWidgets.QWidget()
        self.tab_UpcomingConsultation.setObjectName("tab_UpcomingConsultation")
        self.borrow_heroImage_2 = QtWidgets.QLabel(self.tab_UpcomingConsultation)
        self.borrow_heroImage_2.setGeometry(QtCore.QRect(-20, 0, 1061, 631))
        self.borrow_heroImage_2.setStyleSheet("background-image: url(:/Assets/assets/Borrow.jpg);")
        self.borrow_heroImage_2.setText("")
        self.borrow_heroImage_2.setObjectName("borrow_heroImage_2")
        self.line_3 = QtWidgets.QFrame(self.tab_UpcomingConsultation)
        self.line_3.setGeometry(QtCore.QRect(330, 240, 391, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.borrow_heroImage = QtWidgets.QLabel(self.tab_UpcomingConsultation)
        self.borrow_heroImage.setGeometry(QtCore.QRect(0, 10, 1051, 121))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.borrow_heroImage.setFont(font)
        self.borrow_heroImage.setStyleSheet("")
        self.borrow_heroImage.setObjectName("borrow_heroImage")
        self.borrowTable = QtWidgets.QTableWidget(self.tab_UpcomingConsultation)
        self.borrowTable.setGeometry(QtCore.QRect(20, 180, 1011, 391))
        self.borrowTable.setStyleSheet("")
        self.borrowTable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.borrowTable.setMidLineWidth(0)
        self.borrowTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.borrowTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.borrowTable.setTabKeyNavigation(True)
        self.borrowTable.setProperty("showDropIndicator", False)
        self.borrowTable.setDragDropOverwriteMode(False)
        self.borrowTable.setAlternatingRowColors(False)
        self.borrowTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowTable.setShowGrid(True)
        self.borrowTable.setGridStyle(QtCore.Qt.SolidLine)
        self.borrowTable.setObjectName("borrowTable")
        self.borrowTable.setColumnCount(3)
        self.borrowTable.setRowCount(0)
        header = self.borrowTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable.setHorizontalHeaderItem(2, item)
        self.borrowTable.horizontalHeader().setCascadingSectionResizes(False)
        self.borrowTable.horizontalHeader().setHighlightSections(True)
        self.return_book = QtWidgets.QPushButton(self.tab_UpcomingConsultation)
        self.return_book.setGeometry(QtCore.QRect(400, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.return_book.setFont(font)
        self.return_book.setStyleSheet("border: 2px solid #ff445c;\n"
"border-radius: 10px;\n"
"background-color: #ff445c;\n"
"color: white;\n"
"font-weight: bold;\n"
"padding-bottom: 2px;\n"
"")
        self.return_book.setObjectName("return_book")
        self.return_book_2 = QtWidgets.QPushButton(self.tab_UpcomingConsultation)
        self.return_book_2.setGeometry(QtCore.QRect(790, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.return_book_2.setFont(font)
        self.return_book_2.setStyleSheet("border: 2px solid #35e673;\n"
"border-radius: 10px;\n"
"background-color: #35e673;\n"
"color: white;\n"
"font-weight: bold;\n"
"padding-bottom: 2px;\n"
"")
        self.return_book_2.setObjectName("return_book_2")
        self.tabWidget.addTab(self.tab_UpcomingConsultation, "")
        self.tab_PreviousConstulations = QtWidgets.QWidget()
        self.tab_PreviousConstulations.setObjectName("tab_PreviousConstulations")
        self.payment_heroImage = QtWidgets.QLabel(self.tab_PreviousConstulations)
        self.payment_heroImage.setGeometry(QtCore.QRect(0, 0, 1061, 631))
        self.payment_heroImage.setStyleSheet("background-image: url(:/Assets/assets/Payment.jpg);\n"
"")
        self.payment_heroImage.setText("")
        self.payment_heroImage.setObjectName("payment_heroImage")
        self.borrow_heroImage_3 = QtWidgets.QLabel(self.tab_PreviousConstulations)
        self.borrow_heroImage_3.setGeometry(QtCore.QRect(0, 10, 1051, 121))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.borrow_heroImage_3.setFont(font)
        self.borrow_heroImage_3.setStyleSheet("")
        self.borrow_heroImage_3.setObjectName("borrow_heroImage_3")
        self.borrowTable_2 = QtWidgets.QTableWidget(self.tab_PreviousConstulations)
        self.borrowTable_2.setGeometry(QtCore.QRect(20, 140, 1011, 401))
        self.borrowTable_2.setStyleSheet("")
        self.borrowTable_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.borrowTable_2.setMidLineWidth(0)
        self.borrowTable_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.borrowTable_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.borrowTable_2.setTabKeyNavigation(True)
        self.borrowTable_2.setProperty("showDropIndicator", False)
        self.borrowTable_2.setDragDropOverwriteMode(False)
        self.borrowTable_2.setAlternatingRowColors(False)
        self.borrowTable_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowTable_2.setShowGrid(True)
        self.borrowTable_2.setGridStyle(QtCore.Qt.SolidLine)
        self.borrowTable_2.setObjectName("borrowTable_2")
        self.borrowTable_2.setColumnCount(4)
        self.borrowTable_2.setRowCount(0)
        header = self.borrowTable_2.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_2.setHorizontalHeaderItem(3, item)
        self.borrowTable_2.horizontalHeader().setCascadingSectionResizes(False)
        self.borrowTable_2.horizontalHeader().setHighlightSections(True)
        self.tabWidget.addTab(self.tab_PreviousConstulations, "")
        self.tab_Search = QtWidgets.QWidget()
        self.tab_Search.setObjectName("tab_Search")
        self.search_searchBtn = QtWidgets.QPushButton(self.tab_Search)
        self.search_searchBtn.setGeometry(QtCore.QRect(770, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.search_searchBtn.setFont(font)
        self.search_searchBtn.setStyleSheet("border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color:  #536DFE;\n"
"box-shadow: 5px 10px #888888;\n"
"\n"
"")
        self.search_searchBtn.setObjectName("search_searchBtn")
        self.label_9 = QtWidgets.QLabel(self.tab_Search)
        self.label_9.setGeometry(QtCore.QRect(470, 200, 58, 16))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.search_title = QtWidgets.QLineEdit(self.tab_Search)
        self.search_title.setGeometry(QtCore.QRect(40, 80, 711, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.search_title.setFont(font)
        self.search_title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.search_title.setAutoFillBackground(False)
        self.search_title.setStyleSheet("background-color: white;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 6px;\n"
"box-shadow: 5px 10px #000;")
        self.search_title.setMaxLength(32770)
        self.search_title.setFrame(True)
        self.search_title.setAlignment(QtCore.Qt.AlignCenter)
        self.search_title.setObjectName("search_title")
        self.label_20 = QtWidgets.QLabel(self.tab_Search)
        self.label_20.setGeometry(QtCore.QRect(370, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("")
        self.label_20.setObjectName("label_20")
        self.borrowTable_4 = QtWidgets.QTableWidget(self.tab_Search)
        self.borrowTable_4.setGeometry(QtCore.QRect(40, 160, 931, 331))
        self.borrowTable_4.setStyleSheet("")
        self.borrowTable_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.borrowTable_4.setMidLineWidth(0)
        self.borrowTable_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.borrowTable_4.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.borrowTable_4.setTabKeyNavigation(True)
        self.borrowTable_4.setProperty("showDropIndicator", False)
        self.borrowTable_4.setDragDropOverwriteMode(False)
        self.borrowTable_4.setAlternatingRowColors(False)
        self.borrowTable_4.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowTable_4.setShowGrid(True)
        self.borrowTable_4.setGridStyle(QtCore.Qt.SolidLine)
        self.borrowTable_4.setObjectName("borrowTable_4")
        self.borrowTable_4.setColumnCount(2)
        self.borrowTable_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.borrowTable_4.setHorizontalHeaderItem(1, item)
        self.borrowTable_4.horizontalHeader().setCascadingSectionResizes(False)
        self.borrowTable_4.horizontalHeader().setHighlightSections(True)
        header = self.borrowTable_4.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tabWidget.addTab(self.tab_Search, "")
        self.logoutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.logoutBtn.setGeometry(QtCore.QRect(880, 10, 183, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutBtn.sizePolicy().hasHeightForWidth())
        self.logoutBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Raleway")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.logoutBtn.setFont(font)
        self.logoutBtn.setStyleSheet("background-color: rgb(40, 170, 112);\n"
"background-color:#536DFE;\n"
"color: rgb(255, 255, 255);")
        self.logoutBtn.setIconSize(QtCore.QSize(16, 16))
        self.logoutBtn.setObjectName("logoutBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #bring to upcoming consultation calender
        self.home_calenderBtn.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))

        #bring to search page
        self.home_calenderBtn_2.clicked.connect(lambda: self.tabWidget.setCurrentIndex(3))

        #bring to past consultation page
        self.home_calenderBtn_3.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))

        #search button
        self.search_searchBtn.clicked.connect(lambda: self.load_patient_details(self.search_title.text()))

        # Logout button
        self.logoutBtn.clicked.connect(lambda: self.loggingout())

        #add consultation button
        self.return_book.clicked.connect(lambda: self.addConsultation())

        # refresh button
        self.return_book_2.clicked.connect(lambda: self.load_consultations(self.docDetails,True))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.home_heroImage.setText(_translate("MainWindow", "Welcome to OneHealth "))
        self.home_calenderBtn.setText(_translate("MainWindow", "Upcoming Consultations Calender"))
        self.home_calenderBtn_2.setText(_translate("MainWindow", "Search Patient"))
        self.home_calenderBtn_3.setText(_translate("MainWindow", "Past Consultations"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHome), _translate("MainWindow", "Home"))
        self.borrow_heroImage.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Consultation Calender</span></p></body></html>"))
        self.borrowTable.setSortingEnabled(False)
        item = self.borrowTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ConsultationID"))
        item = self.borrowTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Patient ID"))
        item = self.borrowTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PatientName"))
        self.return_book.setText(_translate("MainWindow", "Add consultation"))
        self.return_book_2.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_UpcomingConsultation), _translate("MainWindow", "Upcoming Consultations"))
        self.borrow_heroImage_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">Previous Consultations</span></p></body></html>"))
        self.borrowTable_2.setSortingEnabled(False)
        item = self.borrowTable_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ConsultationID"))
        item = self.borrowTable_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PatientID"))
        item = self.borrowTable_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PatientName"))
        item = self.borrowTable_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Remarks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_PreviousConstulations), _translate("MainWindow", "Previous Consultations"))
        self.search_searchBtn.setText(_translate("MainWindow", "Search"))
        self.search_title.setPlaceholderText(_translate("MainWindow", "   Search a Patient Name (e.g. George)"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Search Patient</span></p></body></html>"))
        self.borrowTable_4.setSortingEnabled(False)
        item = self.borrowTable_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PatientID"))
        item = self.borrowTable_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PatientName"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Search), _translate("MainWindow", "Search"))
        self.logoutBtn.setText(_translate("MainWindow", "Logout"))

        # Cells clicked
        self.borrowTable_2.cellDoubleClicked.connect(lambda: self.cell_clicked_consult1())
        self.borrowTable.cellDoubleClicked.connect(lambda: self.cell_clicked_consult2())
        self.borrowTable_4.cellDoubleClicked.connect(lambda: self.cell_clicked_search())

    def addConsultation(self):
        self.window = QtWidgets.QMainWindow()
        consultationAdd(self.window, self.MainWindow,self.docDetails)
        self.MainWindow.close()

    # Button Functions
    def loggingout(self):
        self.loginWindow.show()
        self.MainWindow.close()


    def load_consultations(self,docId,refresh=False):
        if refresh:
            self.borrowTable.setRowCount(0)
            my_cursor.execute("SELECT consultationId, patient.patientId, patient.name "
                              "FROM consultation "
                              "INNER JOIN patient ON consultation.patientId = patient.patientId "
                              "WHERE (doctorId = %s AND datetime >= NOW())", (docId,))
            rows = my_cursor.fetchall()
            for row_number, row_data in enumerate(rows):
                self.borrowTable.insertRow(row_number)
                self.borrowTable.setRowHeight(row_number, 10)
                for col_num, data in enumerate(row_data):
                    self.borrowTable.setItem(
                        row_number, col_num, QtWidgets.QTableWidgetItem(str(data))
                    )
        else:
            my_cursor.execute("SELECT consultationId, patient.patientId, patient.name, consultation.remarks "
                              "FROM consultation "
                              "INNER JOIN patient ON consultation.patientId = patient.patientId "
                              "WHERE (doctorId = %s AND datetime < NOW())",(docId,))
            rows = my_cursor.fetchall()
            for row_number, row_data in enumerate(rows):
                self.borrowTable_2.insertRow(row_number)
                self.borrowTable_2.setRowHeight(row_number,10)
                for col_num, data in enumerate(row_data):
                    self.borrowTable_2.setItem(
                        row_number, col_num, QtWidgets.QTableWidgetItem(str(data))
                    )

            my_cursor.execute("SELECT consultationId, patient.patientId, patient.name "
                              "FROM consultation "
                              "INNER JOIN patient ON consultation.patientId = patient.patientId "
                              "WHERE (doctorId = %s AND datetime > NOW())",(docId,))
            rows = my_cursor.fetchall()
            for row_number, row_data in enumerate(rows):
                self.borrowTable.insertRow(row_number)
                self.borrowTable.setRowHeight(row_number,10)
                for col_num, data in enumerate(row_data):
                    self.borrowTable.setItem(
                        row_number, col_num, QtWidgets.QTableWidgetItem(str(data))
                    )

# start
    def load_patient_details(self, name):
        # Load current insurance
        my_cursor.execute("SELECT * FROM oneHealth.patient WHERE name like %s", ('%' + name + '%',))
        rows = my_cursor.fetchall()
        print(rows)
        for row_number, row_data in enumerate(rows):
            self.borrowTable_4.insertRow(row_number)
            self.borrowTable_4.setRowHeight(row_number,10)
            for col_num, data in enumerate(row_data):
                self.borrowTable_4.setItem(
                    row_number, col_num, QtWidgets.QTableWidgetItem(str(data)))


       
# end

    # Tables Clicked
    def cell_clicked_consult1(self):
        indexes = self.borrowTable_2.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            rowtext = []
            for column in range(self.borrowTable_2.columnCount()):
                if column == 1:
                    continue
                else:
                    rowtext.append(self.borrowTable_2.item(row, column).text())
            self.window = QtWidgets.QMainWindow()
            consultationDisplay(self.window, self.MainWindow, rowtext[0])
            self.MainWindow.hide()

    def cell_clicked_consult2(self):
        indexes = self.borrowTable.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            rowtext = []
            for column in range(self.borrowTable.columnCount()):
                if column == 1:
                    continue
                else:
                    rowtext.append(self.borrowTable.item(row, column).text())
            self.window = QtWidgets.QMainWindow()
            consultationDisplay(self.window,self.MainWindow,rowtext[0])
            self.MainWindow.hide()

    def cell_clicked_search(self):
        indexes = self.borrowTable_4.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = index.row()
            rowtext = []
            for column in range(self.borrowTable_4.columnCount()):
                if column == 1:
                    continue
                else:
                    rowtext.append(self.borrowTable_4.item(row, column).text())
            self.window = QtWidgets.QMainWindow()
            patientDisplay(self.window,self.MainWindow,rowtext[0])
            self.MainWindow.hide()
import background_image



