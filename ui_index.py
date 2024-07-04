# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1233, 876)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(2, 3, 1231, 873))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.widget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget {\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_main_icon = QHBoxLayout()
        self.horizontalLayout_main_icon.setObjectName(u"horizontalLayout_main_icon")
        self.horizontalSpacer_top_icon_left = QSpacerItem(38, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_main_icon.addItem(self.horizontalSpacer_top_icon_left)

        self.icon_left_frame = QLabel(self.icon_only_widget)
        self.icon_left_frame.setObjectName(u"icon_left_frame")
        self.icon_left_frame.setMaximumSize(QSize(40, 40))
        self.icon_left_frame.setPixmap(QPixmap(u":/newPrefix/icons/logo.png"))
        self.icon_left_frame.setScaledContents(True)

        self.horizontalLayout_main_icon.addWidget(self.icon_left_frame)

        self.horizontalSpacer_top_icon_rigth = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_main_icon.addItem(self.horizontalSpacer_top_icon_rigth)


        self.verticalLayout_11.addLayout(self.horizontalLayout_main_icon)

        self.verticalLayout_icon = QVBoxLayout()
        self.verticalLayout_icon.setSpacing(20)
        self.verticalLayout_icon.setObjectName(u"verticalLayout_icon")
        self.verticalLayout_icon.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        self.dashboard_1.setMinimumSize(QSize(0, 30))
        self.dashboard_1.setMaximumSize(QSize(16777215, 30))
        self.dashboard_1.setStyleSheet(u"border: 0px;")
        icon = QIcon()
        icon.addFile(u":/newPrefix/icons/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/newPrefix/icons/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_icon.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        self.institution_1.setMinimumSize(QSize(0, 30))
        self.institution_1.setMaximumSize(QSize(16777215, 30))
        self.institution_1.setStyleSheet(u"border: 0px;")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icons/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/newPrefix/icons/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_icon.addWidget(self.institution_1)

        self.students_1 = QPushButton(self.icon_only_widget)
        self.students_1.setObjectName(u"students_1")
        self.students_1.setMinimumSize(QSize(0, 30))
        self.students_1.setMaximumSize(QSize(16777215, 30))
        self.students_1.setStyleSheet(u"border: 0px;")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icons/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/newPrefix/icons/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students_1.setIcon(icon2)
        self.students_1.setIconSize(QSize(100, 20))
        self.students_1.setCheckable(True)
        self.students_1.setAutoExclusive(True)

        self.verticalLayout_icon.addWidget(self.students_1)

        self.teacher_1 = QPushButton(self.icon_only_widget)
        self.teacher_1.setObjectName(u"teacher_1")
        self.teacher_1.setMinimumSize(QSize(0, 30))
        self.teacher_1.setMaximumSize(QSize(16777215, 30))
        self.teacher_1.setStyleSheet(u"border: 0px;")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icons/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/newPrefix/icons/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teacher_1.setIcon(icon3)
        self.teacher_1.setIconSize(QSize(100, 20))
        self.teacher_1.setCheckable(True)
        self.teacher_1.setAutoExclusive(True)

        self.verticalLayout_icon.addWidget(self.teacher_1)

        self.finance_1 = QPushButton(self.icon_only_widget)
        self.finance_1.setObjectName(u"finance_1")
        self.finance_1.setMinimumSize(QSize(0, 30))
        self.finance_1.setMaximumSize(QSize(16777215, 30))
        self.finance_1.setStyleSheet(u"border: 0px;")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icons/financessmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/newPrefix/icons/financessmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_1.setIcon(icon4)
        self.finance_1.setIconSize(QSize(100, 20))
        self.finance_1.setCheckable(True)
        self.finance_1.setAutoExclusive(True)

        self.verticalLayout_icon.addWidget(self.finance_1)


        self.verticalLayout_11.addLayout(self.verticalLayout_icon)

        self.verticalSpacer_icon = QSpacerItem(20, 415, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_icon)

        self.vLayout_settings_signout = QVBoxLayout()
        self.vLayout_settings_signout.setSpacing(20)
        self.vLayout_settings_signout.setObjectName(u"vLayout_settings_signout")
        self.vLayout_settings_signout.setContentsMargins(-1, -1, -1, 7)
        self.settings_1 = QPushButton(self.icon_only_widget)
        self.settings_1.setObjectName(u"settings_1")
        self.settings_1.setMinimumSize(QSize(0, 30))
        self.settings_1.setMaximumSize(QSize(16777215, 30))
        self.settings_1.setStyleSheet(u"border: 0px;")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icons/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/newPrefix/icons/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_1.setIcon(icon5)
        self.settings_1.setIconSize(QSize(100, 20))
        self.settings_1.setCheckable(True)
        self.settings_1.setAutoExclusive(True)

        self.vLayout_settings_signout.addWidget(self.settings_1)

        self.signout_1 = QPushButton(self.icon_only_widget)
        self.signout_1.setObjectName(u"signout_1")
        self.signout_1.setMinimumSize(QSize(0, 30))
        self.signout_1.setMaximumSize(QSize(16777215, 30))
        self.signout_1.setStyleSheet(u"border: 0px;")
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icons/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.signout_1.setIcon(icon6)
        self.signout_1.setIconSize(QSize(100, 16))
        self.signout_1.setCheckable(True)
        self.signout_1.setAutoExclusive(True)

        self.vLayout_settings_signout.addWidget(self.signout_1)


        self.verticalLayout_11.addLayout(self.vLayout_settings_signout)


        self.horizontalLayout.addWidget(self.icon_only_widget)

        self.icon_text_widget = QWidget(self.widget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: None;\n"
"}\n"
"QPushButton {\n"
"	height: 30px;\n"
"	border: None;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_top_icon_text = QHBoxLayout()
        self.horizontalLayout_top_icon_text.setSpacing(20)
        self.horizontalLayout_top_icon_text.setObjectName(u"horizontalLayout_top_icon_text")
        self.horizontalLayout_top_icon_text.setContentsMargins(20, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icons/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_top_icon_text.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)

        self.horizontalLayout_top_icon_text.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_top_icon_text)

        self.icon_text_layout = QVBoxLayout()
        self.icon_text_layout.setSpacing(20)
        self.icon_text_layout.setObjectName(u"icon_text_layout")
        self.icon_text_layout.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_text_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setMinimumSize(QSize(0, 30))
        self.dashboard_2.setMaximumSize(QSize(16777215, 30))
        self.dashboard_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icons/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/newPrefix/icons/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon7)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(False)

        self.icon_text_layout.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_text_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setMinimumSize(QSize(0, 30))
        self.institution_2.setMaximumSize(QSize(16777215, 30))
        self.institution_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -65px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icons/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/newPrefix/icons/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon8)
        self.institution_2.setIconSize(QSize(95, 45))
        self.institution_2.setCheckable(True)
        self.institution_2.setAutoExclusive(False)

        self.icon_text_layout.addWidget(self.institution_2)

        self.students = QFrame(self.icon_text_widget)
        self.students.setObjectName(u"students")
        self.students.setStyleSheet(u"")
        self.students.setFrameShape(QFrame.Shape.StyledPanel)
        self.students.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.students)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.students_2 = QPushButton(self.students)
        self.students_2.setObjectName(u"students_2")
        self.students_2.setMaximumSize(QSize(16777215, 30))
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icons/students3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/newPrefix/icons/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.students_2.setIcon(icon9)
        self.students_2.setIconSize(QSize(200, 60))
        self.students_2.setCheckable(True)
        self.students_2.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.students_2)

        self.students_dropdown = QFrame(self.students)
        self.students_dropdown.setObjectName(u"students_dropdown")
        self.students_dropdown.setStyleSheet(u"")
        self.students_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.students_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.students_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.students_info = QPushButton(self.students_dropdown)
        self.students_info.setObjectName(u"students_info")
        self.students_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.students_info.setCheckable(True)
        self.students_info.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.students_info)

        self.students_payment = QPushButton(self.students_dropdown)
        self.students_payment.setObjectName(u"students_payment")
        self.students_payment.setStyleSheet(u"QPushButton {\n"
"	padding-left: 11px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.students_payment.setCheckable(True)
        self.students_payment.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.students_payment)

        self.students_transactions = QPushButton(self.students_dropdown)
        self.students_transactions.setObjectName(u"students_transactions")
        self.students_transactions.setStyleSheet(u"QPushButton {\n"
"	padding-left: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.students_transactions.setCheckable(True)
        self.students_transactions.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.students_transactions)


        self.verticalLayout_4.addWidget(self.students_dropdown)


        self.icon_text_layout.addWidget(self.students)

        self.teachers = QFrame(self.icon_text_widget)
        self.teachers.setObjectName(u"teachers")
        self.teachers.setStyleSheet(u"")
        self.teachers.setFrameShape(QFrame.Shape.StyledPanel)
        self.teachers.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.teachers)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.teacher_2 = QPushButton(self.teachers)
        self.teacher_2.setObjectName(u"teacher_2")
        self.teacher_2.setMaximumSize(QSize(16777215, 30))
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icons/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/newPrefix/icons/teachers4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.teacher_2.setIcon(icon10)
        self.teacher_2.setIconSize(QSize(200, 60))
        self.teacher_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.teacher_2)

        self.teachers_dropdown = QFrame(self.teachers)
        self.teachers_dropdown.setObjectName(u"teachers_dropdown")
        self.teachers_dropdown.setStyleSheet(u"")
        self.teachers_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.teachers_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.teachers_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.teachers_info = QPushButton(self.teachers_dropdown)
        self.teachers_info.setObjectName(u"teachers_info")
        self.teachers_info.setStyleSheet(u"QPushButton {\n"
"	padding-left: 20px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teachers_info.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teachers_info)

        self.teachers_salaries = QPushButton(self.teachers_dropdown)
        self.teachers_salaries.setObjectName(u"teachers_salaries")
        self.teachers_salaries.setStyleSheet(u"QPushButton {\n"
"	padding-left: 3px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teachers_salaries.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teachers_salaries)

        self.teachers_transactions = QPushButton(self.teachers_dropdown)
        self.teachers_transactions.setObjectName(u"teachers_transactions")
        self.teachers_transactions.setStyleSheet(u"QPushButton {\n"
"	padding-left: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.teachers_transactions.setCheckable(True)

        self.verticalLayout_2.addWidget(self.teachers_transactions)


        self.verticalLayout_5.addWidget(self.teachers_dropdown)


        self.icon_text_layout.addWidget(self.teachers)

        self.finances = QFrame(self.icon_text_widget)
        self.finances.setObjectName(u"finances")
        self.finances.setStyleSheet(u"")
        self.finances.setFrameShape(QFrame.Shape.StyledPanel)
        self.finances.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.finances)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.finance_2 = QPushButton(self.finances)
        self.finance_2.setObjectName(u"finance_2")
        self.finance_2.setMaximumSize(QSize(16777215, 30))
        icon11 = QIcon()
        icon11.addFile(u":/newPrefix/icons/finances3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/newPrefix/icons/finances4.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.finance_2.setIcon(icon11)
        self.finance_2.setIconSize(QSize(200, 100))
        self.finance_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.finance_2)

        self.finances_dropdown = QFrame(self.finances)
        self.finances_dropdown.setObjectName(u"finances_dropdown")
        self.finances_dropdown.setStyleSheet(u"")
        self.finances_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.finances_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.finances_dropdown)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.budgets = QPushButton(self.finances_dropdown)
        self.budgets.setObjectName(u"budgets")
        self.budgets.setStyleSheet(u"QPushButton {\n"
"	padding-left: -40px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.budgets.setCheckable(True)

        self.verticalLayout_3.addWidget(self.budgets)

        self.expenses = QPushButton(self.finances_dropdown)
        self.expenses.setObjectName(u"expenses")
        self.expenses.setStyleSheet(u"QPushButton {\n"
"	padding-left: -32px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.expenses.setCheckable(True)

        self.verticalLayout_3.addWidget(self.expenses)

        self.business_overview = QPushButton(self.finances_dropdown)
        self.business_overview.setObjectName(u"business_overview")
        self.business_overview.setStyleSheet(u"QPushButton {\n"
"	padding-left: 13px;\n"
"}\n"
"QPushButton:hover {\n"
"	color:#12B298\n"
"}")
        self.business_overview.setCheckable(True)

        self.verticalLayout_3.addWidget(self.business_overview)


        self.verticalLayout_6.addWidget(self.finances_dropdown)


        self.icon_text_layout.addWidget(self.finances)


        self.verticalLayout_7.addLayout(self.icon_text_layout)

        self.verticalSpacer = QSpacerItem(20, 64, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, -1, 7)
        self.settings_2 = QPushButton(self.icon_text_widget)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setMinimumSize(QSize(0, 30))
        self.settings_2.setMaximumSize(QSize(16777215, 30))
        self.settings_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -65px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/newPrefix/icons/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon12.addFile(u":/newPrefix/icons/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.settings_2.setIcon(icon12)
        self.settings_2.setIconSize(QSize(100, 60))
        self.settings_2.setCheckable(True)
        self.settings_2.setAutoExclusive(False)

        self.verticalLayout_8.addWidget(self.settings_2)

        self.signout_2 = QPushButton(self.icon_text_widget)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setMinimumSize(QSize(0, 30))
        self.signout_2.setMaximumSize(QSize(16777215, 30))
        self.signout_2.setStyleSheet(u"QPushButton {\n"
"	padding-left: -60px;\n"
"}\n"
"QPushButton:checked {\n"
"	background-color:white;\n"
"	border-radius:3px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/newPrefix/icons/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.signout_2.setIcon(icon13)
        self.signout_2.setIconSize(QSize(100, 60))
        self.signout_2.setCheckable(True)

        self.verticalLayout_8.addWidget(self.signout_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.horizontalLayout.addWidget(self.icon_text_widget)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.header_widget_top = QWidget(self.widget)
        self.header_widget_top.setObjectName(u"header_widget_top")
        self.header_widget_top.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget_top)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_hello = QHBoxLayout()
        self.horizontalLayout_hello.setObjectName(u"horizontalLayout_hello")
        self.pushButton = QPushButton(self.header_widget_top)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon14 = QIcon()
        icon14.addFile(u":/newPrefix/icons/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_hello.addWidget(self.pushButton)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget_top)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_10.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget_top)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(72, 72, 72);")

        self.verticalLayout_10.addWidget(self.label_5)


        self.horizontalLayout_hello.addLayout(self.verticalLayout_10)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_hello)

        self.horizontalSpacer_3 = QSpacerItem(353, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget_top)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget_top)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setPixmap(QPixmap(u":/newPrefix/icons/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_9.addWidget(self.header_widget_top)

        self.main_screen_widget = QWidget(self.widget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(920, 741))
        self.main_screen_widget.setMaximumSize(QSize(841, 741))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 921, 741))
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(350, 330, 201, 101))
        font3 = QFont()
        font3.setPointSize(25)
        self.label_7.setFont(font3)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 300, 201, 101))
        self.label_8.setFont(font3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 301, 51))
        font4 = QFont()
        font4.setPointSize(20)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 40, 231, 31))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_19.setFont(font5)
        self.student_info_table = QTableWidget(self.page_3)
        if (self.student_info_table.columnCount() < 10):
            self.student_info_table.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.student_info_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.student_info_table.setObjectName(u"student_info_table")
        self.student_info_table.setGeometry(QRect(20, 200, 930, 531))
        self.student_info_table.setMinimumSize(QSize(891, 0))
        self.student_info_table.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color:black;\n"
"	color:white;\n"
"}\n"
"QTableWidget{\n"
"	alternate-background-color:#BEDFB;\n"
"	background-color:#F4F9FA\n"
"}")
        self.student_info_table.setAlternatingRowColors(True)
        self.widget1 = QWidget(self.page_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 90, 421, 43))
        self.buttons_h_layout = QHBoxLayout(self.widget1)
        self.buttons_h_layout.setObjectName(u"buttons_h_layout")
        self.buttons_h_layout.setContentsMargins(0, 0, 0, 0)
        self.add_student_btn = QPushButton(self.widget1)
        self.add_student_btn.setObjectName(u"add_student_btn")
        self.add_student_btn.setMinimumSize(QSize(0, 41))
        self.add_student_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 12px;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/newPrefix/icons/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_student_btn.setIcon(icon15)

        self.buttons_h_layout.addWidget(self.add_student_btn)

        self.excel_export_btn = QPushButton(self.widget1)
        self.excel_export_btn.setObjectName(u"excel_export_btn")
        self.excel_export_btn.setMinimumSize(QSize(0, 41))
        self.excel_export_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 12\n"
"px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/newPrefix/icons/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.excel_export_btn.setIcon(icon16)

        self.buttons_h_layout.addWidget(self.excel_export_btn)

        self.pdf_export_btn = QPushButton(self.widget1)
        self.pdf_export_btn.setObjectName(u"pdf_export_btn")
        self.pdf_export_btn.setMinimumSize(QSize(0, 41))
        self.pdf_export_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255,78,78);\n"
"	color:white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight:bold;\n"
"	font-size: 12px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/newPrefix/icons/pdf.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pdf_export_btn.setIcon(icon17)

        self.buttons_h_layout.addWidget(self.pdf_export_btn)

        self.widget2 = QWidget(self.page_3)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 150, 641, 43))
        self.combobox_h_layout = QHBoxLayout(self.widget2)
        self.combobox_h_layout.setObjectName(u"combobox_h_layout")
        self.combobox_h_layout.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.widget2)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.combobox_h_layout.addWidget(self.select_gender)

        self.select_class = QComboBox(self.widget2)
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 0))
        self.select_class.setStyleSheet(u"QComboBox{\n"
"	border:2px solid white;\n"
"	border-radius: 8px;\n"
"	padding:1px 18px 1px 3px;\n"
"	background-color:black;\n"
"	color:white;\n"
"	height: 35px;\n"
"	padding-left: 15px;\n"
"	font-weight:bold;\n"
"	selection-background-color:#2980B9;\n"
"}")

        self.combobox_h_layout.addWidget(self.select_class)

        self.student_search_line_edit = QLineEdit(self.widget2)
        self.student_search_line_edit.setObjectName(u"student_search_line_edit")
        self.student_search_line_edit.setMinimumSize(QSize(0, 38))
        self.student_search_line_edit.setMaximumSize(QSize(16777215, 38))
        self.student_search_line_edit.setStyleSheet(u"QLineEdit {\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}")

        self.combobox_h_layout.addWidget(self.student_search_line_edit)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(260, 200, 341, 101))
        self.label_10.setFont(font3)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(270, 220, 341, 101))
        self.label_11.setFont(font3)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(240, 250, 341, 101))
        self.label_12.setFont(font3)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 250, 341, 101))
        self.label_13.setFont(font3)
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.label_14 = QLabel(self.page_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(230, 270, 341, 101))
        self.label_14.setFont(font3)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.label_15 = QLabel(self.page_9)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(290, 290, 341, 101))
        self.label_15.setFont(font3)
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_16 = QLabel(self.page_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 290, 341, 101))
        self.label_16.setFont(font3)
        self.stackedWidget.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.label_17 = QLabel(self.page_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(260, 230, 341, 101))
        self.label_17.setFont(font3)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.label_18 = QLabel(self.page_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(350, 270, 341, 101))
        self.label_18.setFont(font3)
        self.stackedWidget.addWidget(self.page_12)

        self.verticalLayout_9.addWidget(self.main_screen_widget)


        self.horizontalLayout.addLayout(self.verticalLayout_9)

        MainWindow.setCentralWidget(self.centralwidget)
        self.main_screen_widget.raise_()
        self.icon_only_widget.raise_()
        self.icon_text_widget.raise_()
        self.header_widget_top.raise_()

        self.retranslateUi(MainWindow)
        self.students_2.toggled.connect(self.students_dropdown.setHidden)
        self.teacher_2.toggled.connect(self.teachers_dropdown.setHidden)
        self.finance_2.toggled.connect(self.finances_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.students_2.toggled.connect(self.students_1.setChecked)
        self.teacher_2.toggled.connect(self.teacher_1.setChecked)
        self.finance_2.toggled.connect(self.finance_1.setChecked)
        self.settings_2.toggled.connect(self.settings_1.setChecked)
        self.signout_2.toggled.connect(self.signout_1.setChecked)
        self.signout_1.toggled.connect(MainWindow.close)
        self.signout_2.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.icon_left_frame.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.students_1.setText("")
        self.teacher_1.setText("")
        self.finance_1.setText("")
        self.settings_1.setText("")
        self.signout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"School", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.students_2.setText("")
        self.students_info.setText(QCoreApplication.translate("MainWindow", u"Student Information", None))
        self.students_payment.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.students_transactions.setText(QCoreApplication.translate("MainWindow", u"Students Transactions", None))
        self.teacher_2.setText("")
        self.teachers_info.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.teachers_salaries.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.teachers_transactions.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.finance_2.setText("")
        self.budgets.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.business_overview.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.settings_2.setText("")
        self.signout_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello, Aderbal", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome to your page", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search here ...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Institution", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Student Info", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Welcome to the students information page</span></p></body></html>", None))
        ___qtablewidgetitem = self.student_info_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.student_info_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Student Id", None));
        ___qtablewidgetitem2 = self.student_info_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.student_info_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem4 = self.student_info_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem5 = self.student_info_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem6 = self.student_info_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem7 = self.student_info_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem8 = self.student_info_table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem9 = self.student_info_table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.add_student_btn.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.excel_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export to Excel", None))
        self.pdf_export_btn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Famale", None))

        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT CLASS", None))
        self.select_class.setItemText(1, QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.select_class.setItemText(2, QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.select_class.setItemText(3, QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.select_class.setItemText(4, QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.select_class.setItemText(5, QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.select_class.setItemText(6, QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.select_class.setItemText(7, QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.select_class.setItemText(8, QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.select_class.setItemText(9, QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.select_class.setItemText(10, QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.select_class.setItemText(11, QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.select_class.setItemText(12, QCoreApplication.translate("MainWindow", u"Grade 12", None))

        self.student_search_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Student ...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Student Payments", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Student Transactions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Teacher Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Teacher Salaries", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Teacher Transactions", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Budgets", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Business Overview", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

