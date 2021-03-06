# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsultationDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
my_db = mysql.connector.connect(host="116.205.136.149",
                                port="3306",
                                user="root",
                                passwd="marron123!",
                                database="onehealth",
                                autocommit=True)
my_cursor = my_db.cursor()

class Ui_MainWindow(object):
    def __init__(self, MainWindow,doctorWindow,consultDetails):
        self.doctorWindow = doctorWindow
        self.consultDetails = consultDetails
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.load_details()
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(30, 20, 881, 591))
        font = QtGui.QFont()
        font.setFamily("Raleway SemiBold")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_41 = QtWidgets.QLabel(self.groupBox_11)
        self.label_41.setGeometry(QtCore.QRect(480, 120, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_40 = QtWidgets.QLabel(self.groupBox_11)
        self.label_40.setGeometry(QtCore.QRect(480, 240, 111, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.search_yeadateInputer_3 = QtWidgets.QLineEdit(self.groupBox_11)
        self.search_yeadateInputer_3.setGeometry(QtCore.QRect(160, 120, 241, 21))
        self.search_yeadateInputer_3.setReadOnly(True)
        self.search_yeadateInputer_3.setObjectName("search_yeadateInputer_3")
        self.label_37 = QtWidgets.QLabel(self.groupBox_11)
        self.label_37.setGeometry(QtCore.QRect(20, 120, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_36 = QtWidgets.QLabel(self.groupBox_11)
        self.label_36.setGeometry(QtCore.QRect(20, 160, 131, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.idInout = QtWidgets.QLineEdit(self.groupBox_11)
        self.idInout.setGeometry(QtCore.QRect(160, 80, 241, 21))
        self.idInout.setReadOnly(True)
        self.idInout.setObjectName("idInout")
        self.label_38 = QtWidgets.QLabel(self.groupBox_11)
        self.label_38.setGeometry(QtCore.QRect(20, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Raleway Light")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.nameInput = QtWidgets.QLineEdit(self.groupBox_11)
        self.nameInput.setGeometry(QtCore.QRect(160, 40, 241, 21))
        self.nameInput.setReadOnly(True)
        self.nameInput.setObjectName("nameInput")
        self.label_39 = QtWidgets.QLabel(self.groupBox_11)
        self.label_39.setGeometry(QtCore.QRect(20, 40, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.backBtn = QtWidgets.QPushButton(self.groupBox_11)
        self.backBtn.setGeometry(QtCore.QRect(20, 540, 75, 23))
        self.backBtn.setObjectName("backBtn")
        self.diagnosisInput = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.diagnosisInput.setGeometry(QtCore.QRect(160, 160, 241, 81))
        self.diagnosisInput.setReadOnly(True)
        self.diagnosisInput.setObjectName("diagnosisInput")
        self.remarkInput = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.remarkInput.setGeometry(QtCore.QRect(620, 240, 241, 81))
        self.remarkInput.setReadOnly(True)
        self.remarkInput.setObjectName("remarkInput")
        self.followUpInput = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.followUpInput.setGeometry(QtCore.QRect(620, 120, 241, 81))
        self.followUpInput.setReadOnly(True)
        self.followUpInput.setObjectName("followUpInput")
        self.facilityNameInput = QtWidgets.QLineEdit(self.groupBox_11)
        self.facilityNameInput.setGeometry(QtCore.QRect(620, 40, 241, 21))
        self.facilityNameInput.setReadOnly(True)
        self.facilityNameInput.setObjectName("facilityNameInput")
        self.label_42 = QtWidgets.QLabel(self.groupBox_11)
        self.label_42.setGeometry(QtCore.QRect(480, 40, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_11)
        self.label_43.setGeometry(QtCore.QRect(480, 80, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.doctorNameInput = QtWidgets.QLineEdit(self.groupBox_11)
        self.doctorNameInput.setGeometry(QtCore.QRect(620, 80, 241, 21))
        self.doctorNameInput.setReadOnly(True)
        self.doctorNameInput.setObjectName("doctorNameInput")
        self.label_44 = QtWidgets.QLabel(self.groupBox_11)
        self.label_44.setGeometry(QtCore.QRect(20, 270, 121, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_11)
        self.tableWidget.setGeometry(QtCore.QRect(160, 270, 251, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 957, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.backBtn.clicked.connect(lambda: self.show_DoctorHome())
    
    def show_DoctorHome(self):
        self.doctorWindow.show()
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Consultation Details"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p>Follow-up Action</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p>Remarks</p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p>Date</p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p>Diagnosis</p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p>Patient ID</p><p><br/></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p>Patient Name</p></body></html>"))
        self.backBtn.setText(_translate("MainWindow", "Back"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p>Facility Name</p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p>Doctor Name</p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p>Services</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "service name"))

    def load_details(self):
        my_cursor.execute("SELECT * FROM consultation WHERE consultationId = %s",(self.consultDetails,))
        rows = my_cursor.fetchall()
        self.idInout.setText(str(rows[0][4]))
        self.search_yeadateInputer_3.setText(str(rows[0][1]))
        self.diagnosisInput.appendPlainText(str(rows[0][7]))
        self.remarkInput.appendPlainText(str(rows[0][2]))
        self.followUpInput.appendPlainText(str(rows[0][3]))
        tempPatient = str(rows[0][4])
        tempDoc = str(rows[0][5])
        tempFacil = str(rows[0][6])
        my_cursor.execute("SELECT name FROM patient WHERE patientId = %s", (tempPatient,))
        rows = my_cursor.fetchall()
        self.nameInput.setText(rows[0][0])
        my_cursor.execute("SELECT name FROM doctor WHERE doctorId = %s", (tempDoc,))
        rows = my_cursor.fetchall()
        self.doctorNameInput.setText(rows[0][0])
        my_cursor.execute("SELECT name FROM healthcarefacility WHERE facilityId = %s", (tempFacil,))
        rows = my_cursor.fetchall()
        self.facilityNameInput.setText(rows[0][0])
        my_cursor.execute("SELECT * FROM consultationservice WHERE consultationId = %s", (self.consultDetails,))
        rows = my_cursor.fetchall()
        list_of_serviceIds = []
        for i in rows:
            list_of_serviceIds.append(i[1])
        if list_of_serviceIds:
            sql = 'SELECT name FROM service WHERE serviceId IN (%s)'
            in_p = ', '.join(list(map(lambda x: '%s', list_of_serviceIds)))
            sql = sql % in_p
            my_cursor.execute(sql, list_of_serviceIds)
            rows = my_cursor.fetchall()
            for row_number, row_data in enumerate(rows):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setRowHeight(row_number,10)
                for col_num, data in enumerate(row_data):
                    self.tableWidget.setItem(
                        row_number, col_num, QtWidgets.QTableWidgetItem(str(data))
                    )



