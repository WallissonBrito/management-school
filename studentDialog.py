# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StudentsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)

import mysql.connector 
from mysql.connector import errorcode
from random import randint
from datetime import datetime

class Ui_StudentsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)


        self.resize(548, 580)
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet(u"QDialog{\n"
"	background-color: white\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 35px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QDateEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left:15px;\n"
"	height: 31px;\n"
"	background-color:white;\n"
"	color:black;\n"
"}\n"
"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}\n"
"QLabel{\n"
"color: black;\n"
"}\n"
"")
        self.line_student_dialog = QFrame(self)
        self.line_student_dialog.setObjectName(u"line_student_dialog")
        self.line_student_dialog.setGeometry(QRect(0, 50, 551, 21))
        self.line_student_dialog.setFrameShape(QFrame.Shape.HLine)
        self.line_student_dialog.setFrameShadow(QFrame.Shadow.Sunken)
        self.name_page_label = QLabel(self)
        self.name_page_label.setObjectName(u"name_page_label")
        self.name_page_label.setGeometry(QRect(10, 0, 271, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.name_page_label.setFont(font1)
        self.name_page_label.setStyleSheet(u"")
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 80, 511, 411))
        self.form_v_layout = QVBoxLayout(self.widget)
        self.form_v_layout.setObjectName(u"form_v_layout")
        self.form_v_layout.setContentsMargins(0, 0, 0, 0)
        self.name_v_layout = QVBoxLayout()
        self.name_v_layout.setObjectName(u"name_v_layout")
        self.name_label = QLabel(self.widget)
        self.name_label.setObjectName(u"name_label")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.name_label.setFont(font2)

        self.name_v_layout.addWidget(self.name_label)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.name_lineEdit.setFont(font3)

        self.name_v_layout.addWidget(self.name_lineEdit)


        self.form_v_layout.addLayout(self.name_v_layout)

        self.combobox_date_h_layout = QHBoxLayout()
        self.combobox_date_h_layout.setObjectName(u"combobox_date_h_layout")
        self.gender_v_layout = QVBoxLayout()
        self.gender_v_layout.setObjectName(u"gender_v_layout")
        self.gender_label = QLabel(self.widget)
        self.gender_label.setObjectName(u"gender_label")
        self.gender_label.setFont(font2)

        self.gender_v_layout.addWidget(self.gender_label)

        self.gender_comboBox = QComboBox(self.widget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.gender_v_layout.addWidget(self.gender_comboBox)


        self.combobox_date_h_layout.addLayout(self.gender_v_layout)

        self.class_v_layout = QVBoxLayout()
        self.class_v_layout.setObjectName(u"class_v_layout")
        self.class_label = QLabel(self.widget)
        self.class_label.setObjectName(u"class_label")
        self.class_label.setFont(font2)

        self.class_v_layout.addWidget(self.class_label)

        self.class_comboBox = QComboBox(self.widget)
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.addItem("")
        self.class_comboBox.setObjectName(u"class_comboBox")

        self.class_v_layout.addWidget(self.class_comboBox)


        self.combobox_date_h_layout.addLayout(self.class_v_layout)

        self.birth_v_layout = QVBoxLayout()
        self.birth_v_layout.setObjectName(u"birth_v_layout")
        self.birth_label = QLabel(self.widget)
        self.birth_label.setObjectName(u"birth_label")
        self.birth_label.setFont(font2)

        self.birth_v_layout.addWidget(self.birth_label)

        self.birth_dateEdit = QDateEdit(self.widget)
        self.birth_dateEdit.setObjectName(u"birth_dateEdit")

        self.birth_v_layout.addWidget(self.birth_dateEdit)


        self.combobox_date_h_layout.addLayout(self.birth_v_layout)


        self.form_v_layout.addLayout(self.combobox_date_h_layout)

        self.addres_v_layout = QVBoxLayout()
        self.addres_v_layout.setObjectName(u"addres_v_layout")
        self.addres_label = QLabel(self.widget)
        self.addres_label.setObjectName(u"addres_label")
        self.addres_label.setFont(font2)

        self.addres_v_layout.addWidget(self.addres_label)

        self.addres_lineEdit = QLineEdit(self.widget)
        self.addres_lineEdit.setObjectName(u"addres_lineEdit")
        self.addres_lineEdit.setMinimumSize(QSize(0, 35))
        self.addres_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.addres_v_layout.addWidget(self.addres_lineEdit)


        self.form_v_layout.addLayout(self.addres_v_layout)

        self.phone_v_layout = QVBoxLayout()
        self.phone_v_layout.setObjectName(u"phone_v_layout")
        self.phone_label = QLabel(self.widget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setFont(font2)

        self.phone_v_layout.addWidget(self.phone_label)

        self.phonelineEdit = QLineEdit(self.widget)
        self.phonelineEdit.setObjectName(u"phonelineEdit")
        self.phonelineEdit.setMinimumSize(QSize(0, 35))
        self.phonelineEdit.setMaximumSize(QSize(16777215, 35))

        self.phone_v_layout.addWidget(self.phonelineEdit)


        self.form_v_layout.addLayout(self.phone_v_layout)

        self.email_v_layout = QVBoxLayout()
        self.email_v_layout.setObjectName(u"email_v_layout")
        self.email_label = QLabel(self.widget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setFont(font2)

        self.email_v_layout.addWidget(self.email_label)

        self.email_lineEdit = QLineEdit(self.widget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))

        self.email_v_layout.addWidget(self.email_lineEdit)


        self.form_v_layout.addLayout(self.email_v_layout)

        self.widget1 = QWidget(self)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(320, 510, 211, 43))
        self.add_cancel_button_h_Layout = QHBoxLayout(self.widget1)
        self.add_cancel_button_h_Layout.setObjectName(u"add_cancel_button_h_Layout")
        self.add_cancel_button_h_Layout.setContentsMargins(0, 0, 0, 0)
        self.saveStudent_btn = QPushButton(self.widget1)
        self.saveStudent_btn.setObjectName(u"add_student_button")
        self.saveStudent_btn.setMinimumSize(QSize(0, 41))
        self.saveStudent_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.add_cancel_button_h_Layout.addWidget(self.saveStudent_btn)

        self.cancel_button = QPushButton(self.widget1)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 41))
        self.cancel_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 15px;\n"
"}")

        self.add_cancel_button_h_Layout.addWidget(self.cancel_button)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, StudentsDialog):
        StudentsDialog.setWindowTitle(QCoreApplication.translate("StudentsDialog", u"Students Dialog", None))
        self.name_page_label.setText(QCoreApplication.translate("StudentsDialog", u"Add New Student", None))
        self.name_label.setText(QCoreApplication.translate("StudentsDialog", u"Full Name", None))
        self.gender_label.setText(QCoreApplication.translate("StudentsDialog", u"Select Gender", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Female", None))

        self.class_label.setText(QCoreApplication.translate("StudentsDialog", u"Select Class", None))
        self.class_comboBox.setItemText(0, QCoreApplication.translate("StudentsDialog", u"Grade 1", None))
        self.class_comboBox.setItemText(1, QCoreApplication.translate("StudentsDialog", u"Grade 2", None))
        self.class_comboBox.setItemText(2, QCoreApplication.translate("StudentsDialog", u"Grade 3", None))
        self.class_comboBox.setItemText(3, QCoreApplication.translate("StudentsDialog", u"Grade 4", None))
        self.class_comboBox.setItemText(4, QCoreApplication.translate("StudentsDialog", u"Grade 5", None))
        self.class_comboBox.setItemText(5, QCoreApplication.translate("StudentsDialog", u"Grade 6", None))
        self.class_comboBox.setItemText(6, QCoreApplication.translate("StudentsDialog", u"Grade 7", None))
        self.class_comboBox.setItemText(7, QCoreApplication.translate("StudentsDialog", u"Grade 8", None))
        self.class_comboBox.setItemText(8, QCoreApplication.translate("StudentsDialog", u"Grade 9", None))
        self.class_comboBox.setItemText(9, QCoreApplication.translate("StudentsDialog", u"Grade 10", None))
        self.class_comboBox.setItemText(10, QCoreApplication.translate("StudentsDialog", u"Grade 11", None))
        self.class_comboBox.setItemText(11, QCoreApplication.translate("StudentsDialog", u"Grade 12", None))

        self.birth_label.setText(QCoreApplication.translate("StudentsDialog", u"Date of Birth", None))
        self.addres_label.setText(QCoreApplication.translate("StudentsDialog", u"Address", None))
        self.phone_label.setText(QCoreApplication.translate("StudentsDialog", u"Phone Number", None))
        self.email_label.setText(QCoreApplication.translate("StudentsDialog", u"E-mail", None))
        self.saveStudent_btn.setText(QCoreApplication.translate("StudentsDialog", u"Add Student", None))
        self.cancel_button.setText(QCoreApplication.translate("StudentsDialog", u"Cancel", None))
    # retranslateUi

        # Add a new pupil when you press a button
        self.saveStudent_btn.clicked.connect(self.add_student)
        self.cancel_button.clicked.connect(self.close)

    # CREATE DATABASE CONECTOR
    def create_connection(self):
        # Replace these with your actual mysql server details
        host_name = "localhost"
        user_name = "root"
        my_password = ""
        database_name = "my_school"

        # Estabilish a connection to MySQL server
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = my_password,
        )

        # Create a cursor to execute SQL queries
        cursor = self.mydb.cursor()

        # Create the database if it doesn´t exist
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

        # Connect to the created database
        self.mydb = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = my_password, 
            database = database_name
        )
        return self.mydb
    
    # INSERT NEW STUDENT 
    def insert_new_student(self):
        try:
            # Create connection
            con = self.create_connection()
            if con  is None:
                return
            
            cursor = con.cursor()

            gender = self.gender_comboBox.currentText()
            student_id = self.generate_studentId(gender)

            birthday = self.handleDateChange()

            # Assuming birthday is a QDate object
            birth_date = self.birth_dateEdit.date()
            age = self.calculate_age(birth_date)

            # Create a list of students information
            self.new_student = [
                self.name_lineEdit.text(),
                student_id,
                self.gender_comboBox.currentText(),
                self.class_comboBox.currentText(),
                birthday,
                age,
                self.addres_lineEdit.text(),
                self.phonelineEdit.text(),
                self.email_lineEdit.text()
           ] 

            # To insert multiple rows in the mysql database
            insert_student_query = """
            INSERT INTO students_table (names, student_id, gender, class, birthday, age, address, phone_number, email) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_student_query, self.new_student)
            self.show_inserted_message()
            con.commit()

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo está errado com o seu nome de usuário ou senha")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe")
            else:
                print(err)

        finally:
            if cursor:
                cursor.close()
            if self.mydb:
                con.close()

    def generate_studentId(self, gender):
        cursor = self.create_connection().cursor()

        while True:
            if gender == "Male":
                id_start_value = '24' + '/U/M'
            else:
                id_start_value = '24' + '/U/F'

            random_value = self.generate_ramdonNumber()
            student_id = id_start_value + random_value

            # Check if the generated student id is already in the table
            cursor.execute(F"SELECT student_id FROM students_table WHERE student_id = '{student_id}'")
            existing_id = cursor.fetchone()

            if not existing_id:
                return student_id   

    def generate_ramdonNumber(self):
        number = randint(1, 1000)
        random_number = f"{number:04d}"
        return random_number

    def handleDateChange(self):
        # Convert QDate to a string in the format 'YYYY-MM-DD'
        selected_date = self.birth_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)
        
        return self.date_string
    
    def calculate_age(self, birth_date):
        # get the current date
        current_date = datetime.now().date()

        # Create a date object for the birthdate
        birth_datetime = datetime(birth_date.year(), birth_date.month(), birth_date.day())

        # Calculate the difference in years
        age = current_date.year - birth_datetime.year

        # Check if the birthday has occured this year
        if (current_date.month, current_date.day) < (birth_datetime.month, birth_datetime.day):
            age -= 1
            
        return age
    
    def show_inserted_message(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineEdit.text() + " inserted into the database")
        msg_box.exec()


    def add_student(self):
        self.insert_new_student()
        self.accept()