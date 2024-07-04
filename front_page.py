from PySide6.QtWidgets import (QMainWindow, QMenu, QTableWidgetItem, QWidget, QHBoxLayout, 
                               QVBoxLayout, QPushButton)
from PySide6.QtGui import QAction, QIcon
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

import mysql.connector

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Side Bar Menu")

        # Hide Widget Menu
        self.icon_only_widget.setHidden(True)

        # Hide Dropdowns
        self.students_dropdown.setHidden(True)
        self.finances_dropdown.setHidden(True)
        self.teachers_dropdown.setHidden(True)

        # Start dropdowns checked
        self.students_2.setChecked(True)
        self.finance_2.setChecked(True)
        self.teacher_2.setChecked(True)

        # Connect buttons to switch to differents pages
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)

        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)

        self.students_info.clicked.connect(self.switch_to_students_info_page)
        self.students_payment.clicked.connect(self.switch_to_studentes_payments_page)
        self.students_transactions.clicked.connect(self.switch_to_students_transactions_page)

        self.teachers_info.clicked.connect(self.switch_to_teachers_info_page)
        self.teachers_salaries.clicked.connect(self.switch_to_teachers_salaries_page)
        self.teachers_transactions.clicked.connect(self.switch_to_teachers_transactions_page)

        self.teachers_info.clicked.connect(self.switch_to_teachers_info_page)
        self.teachers_salaries.clicked.connect(self.switch_to_teachers_salaries_page)
        self.teachers_transactions.clicked.connect(self.switch_to_teachers_transactions_page)

        self.budgets.clicked.connect(self.switch_to_budgets_page)
        self.expenses.clicked.connect(self.switch_to_expenses_page)
        self.business_overview.clicked.connect(self.switch_to_business_overview_page)

        self.settings_1.clicked.connect(self.switch_to_settings_page)
        self.settings_2.clicked.connect(self.switch_to_settings_page)

        # Connect buttons to respective context menus
        self.students_1.clicked.connect(self.students_context_menu)
        self.teacher_1.clicked.connect(self.teachers_context_menu)
        self.finance_1.clicked.connect(self.finances_context_menu)

        # Connect to mysql server and create database if it doesnt exist
        self.create_connection()

        # Create students table
        self.create_students_table()

        # Open add students dialog
        self.add_student_btn.clicked.connect(self.open_addStudent_dialog)

        # load student information to QTable
        self.load_students_info()
        self.select_class.currentIndexChanged.connect(self.load_students_info())
        self.select_gender.currentIndexChanged.connect(self.load_students_info())        

        # Control column widhts
        self.student_info_table.setColumnWidth(0, 120)
        self.student_info_table.setColumnWidth(1, 80)
        self.student_info_table.setColumnWidth(2, 60)
        self.student_info_table.setColumnWidth(3, 70)
        self.student_info_table.setColumnWidth(4, 70)
        self.student_info_table.setColumnWidth(5, 70)
        self.student_info_table.setColumnWidth(6, 70)
        self.student_info_table.setColumnWidth(7, 80)
        self.student_info_table.setColumnWidth(8, 120)
        self.student_info_table.setColumnWidth(9, 150)


    # Methods to switch to different pages
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_students_info_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_studentes_payments_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_students_transactions_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_teachers_info_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_teachers_salaries_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def switch_to_teachers_transactions_page(self):
        self.stackedWidget.setCurrentIndex(7)

    def switch_to_budgets_page(self):
        self.stackedWidget.setCurrentIndex(8)

    def switch_to_expenses_page(self):
        self.stackedWidget.setCurrentIndex(9)

    def switch_to_business_overview_page(self):
        self.stackedWidget.setCurrentIndex(10)

    def switch_to_settings_page(self):
        self.stackedWidget.setCurrentIndex(11)

    # Methods to show context menu
    def students_context_menu(self):
        self.show_custom_context_menu(self.students_1, ["Student Information", "Student Payments", "Student Transactions"])
    
    def teachers_context_menu(self):
        self.show_custom_context_menu(self.teacher_1, ["Teachers Information", "Teachers Salaries", "Teachers Transactions"])

    def finances_context_menu(self):
        self.show_custom_context_menu(self.finance_1, ["Budgets", "Expenses", "Business Overview"])
    
    def show_custom_context_menu(self, button, menu_items):
        menu = QMenu(self)
    
        menu.setStyleSheet("""
                            QMenu{
                            background-color: black;
                            color:white;
                            }
                            QMenu:selected{
                            background-color:white;
                            color: #12B298;               
                            }
                        """)

        # Add actions to the menu
        for item_text in menu_items:
            action = QAction(item_text, self)
            action.triggered.connect(self.handle_menu_item_click)
            menu.addAction(action)

        # show the menu
        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_item_click(self):
        # Recevie text menu 
        text = self.sender().text()

        if text == "Student Information":
            self.switch_to_students_info_page()
        elif text == "Student Payments":
            self.switch_to_studentes_payments_page()
        elif text == "Student Transactions":
            self.switch_to_students_transactions_page()
        elif text == "Teachers Information":
            self.switch_to_teachers_info_page()
        elif text == "Teachers Salaries":
            self.switch_to_teachers_salaries_page()
        elif text == "Teachers Transactions":
            self.switch_to_teachers_transactions_page()
        elif text == "Budgets":
            self.switch_to_budgets_page()
        elif text == "Expenses":
            self.switch_to_expenses_page()
        elif text == "Business Overview":
            self.switch_to_business_overview_page()

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
    
    # CREATE STUDENTS TABLE
    def create_students_table(self):
        # Create a cursor for executing SQL queries
        cursor = self.create_connection().cursor()

        # The query
        create_students_table_query = f"""
            CREATE TABLE IF NOT EXISTS students_table(
                names TEXT,
                student_id VARCHAR(15) PRIMARY KEY,
                gender TEXT,
                class TEXT,
                birthday TEXT,
                age INT,
                address TEXT,
                phone_number VARCHAR(15),
                email VARCHAR(15)
            )"""
        
        cursor.execute(create_students_table_query)

        # Commit changes and close the connection
        self.mydb.commit()
        self.mydb.close()

    def open_addStudent_dialog(self):
        from studentDialog import Ui_StudentsDialog
        
        # instatiate and show the dialog
        addStudent_dialog = Ui_StudentsDialog(self)
        result = addStudent_dialog.exec() # This will block until the dialog is closed

        if result == Ui_StudentsDialog.accepted:
            # if the dialog was accepted (user clicked add student button)
            pass

    def load_students_info(self):
        # Clear existing data in the table
        self.student_info_table.setRowCount(0)

        # Fetch data based on the selected class and gender in the combo boxes
        selected_class = self.select_class.currentText()
        selected_gender = self.select_gender.currentText()
        data = self.get_data_from_table(selected_class, selected_gender)

        # Populate the table with the filtered data
        for row_index, row_data in enumerate(data):
            self.student_info_table.insertRow(row_index)
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.student_info_table.setItem(row_index, col_index, item)

                # Create a custom widget with two buttons lined up horizontally for the actions columns
                double_button_widget = DoubleButtonWidgetStudents(row_index, row_data)

                # Set this custom widget with two buttons as the cell widget for the actions column
                self.student_info_table.setCellWidget(row_index, 9, double_button_widget)
                self.student_info_table.setRowHeight(row_index, 50)

    def get_data_from_table(self, class_filter, gender_filter):
        cursor = self.create_connection().cursor()

        # Construct the sql query based on the selected filters
        query = f"""SELECT * FROM `students_table` WHERE 
        ('{class_filter}' = 'SELECT CLASS' OR class = '{class_filter}') AND
        ('{gender_filter}' = 'SELECT GENDER' OR gender = '{gender_filter}')"""

        cursor.execute(query)
        data = cursor.fetchall()
        return data
    
    # DOUBLE BUTTON CLASS
class DoubleButtonWidgetStudents(QWidget):
    def __init__(self, row_index, row_data):
        super().__init__()

        # Store the row index and row data as an instance in variables
        self.row_index = row_index
        self.row_data = row_data

        # Get Student variables from the tuple
        self.studante_name = self.row_data[0]
        self.student_id = self.row_data[1]

        layout = QHBoxLayout(self)

        # Create the blue edit button
        self.edit_button = QPushButton("",self)
        self.edit_button.setStyleSheet("background-color:blue;")
        self.edit_button.setFixedSize(61, 31)

        # Create the red edit button   
        self.delete_button = QPushButton("",self)
        self.delete_button.setStyleSheet("background-color:red;")
        self.delete_button.setFixedSize(61, 31)

        # Set icon for the edit button
        icon_edit = QIcon()
        icon_edit.addFile(u":/newPrefix/icons/edit.png")
        self.edit_button.setIcon(icon_edit)
        
        # Set icon for delete the button
        icon_delete = QIcon()
        icon_delete.addFile(u":/newPrefix/icons/delete.png")
        self.delete_button.setIcon(icon_delete)

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)




