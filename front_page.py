from PySide6.QtWidgets import QMainWindow, QMenu
from PySide6.QtGui import QAction
# from matplotlib.pylab import f
from ui_index import Ui_MainWindow

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

        






