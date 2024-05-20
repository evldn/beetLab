# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'svekla.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QWidget)

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide6.QtWidgets import*
from matplotlib.figure import Figure

class MplWidget(QWidget):

        def __init__(self, parent=None):
                QWidget.__init__(self, parent)

                self.canvas = FigureCanvas(Figure())

                vertical_layout = QVBoxLayout()
                vertical_layout.addWidget(self.canvas)

                self.canvas.axes = self.canvas.figure.add_subplot(111)
                self.setLayout(vertical_layout)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(x1:0.5, y1:1, x2:0.5, y2:0, stop:0 #2F9296, stop:1 #46B7B9);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 600))
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.label_2 = QLabel(self.welcomePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 160, 780, 61))
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;")
        self.label = QLabel(self.welcomePage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 780, 111))
        font = QFont()
        font.setFamilies([u"Open Sans Condensed"])
        font.setPointSize(11)
        font.setBold(True)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-family:'Open Sans Condensed';")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.testStartButton = QPushButton(self.welcomePage)
        self.testStartButton.setObjectName(u"testStartButton")
        self.testStartButton.setGeometry(QRect(10, 350, 780, 151))
        self.testStartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.testStartButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(135, 223, 214, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.programStartButton = QPushButton(self.welcomePage)
        self.programStartButton.setObjectName(u"programStartButton")
        self.programStartButton.setGeometry(QRect(10, 240, 780, 91))
        font1 = QFont()
        font1.setFamilies([u"Open Sans Condensed"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.programStartButton.setFont(font1)
        self.programStartButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.programStartButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(135, 223, 214, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"cursor: pointer;\n"
"}")
        self.stackedWidget.addWidget(self.welcomePage)
        self.programPage = QWidget()
        self.programPage.setObjectName(u"programPage")
        self.label_3 = QLabel(self.programPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 20, 781, 51))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"font-family: Open Sans Condensed;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameMatrix = QFrame(self.programPage)
        self.frameMatrix.setObjectName(u"frameMatrix")
        self.frameMatrix.setGeometry(QRect(10, 210, 781, 341))
        self.frameMatrix.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';")
        self.frameMatrix.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameMatrix.setFrameShadow(QFrame.Shadow.Raised)
        self.label_4 = QLabel(self.frameMatrix)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 781, 31))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 0px solid rbga(255, 255, 255, 40);\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family: Open Sans Condensed;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tableWidget = QTableWidget(self.frameMatrix)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 40, 761, 281))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"QTableView { \n"
"	gridline-color: transparent;\n"
"	gridline-width: none;\n"
"	outline: none;\n"
"align: AlignVCenter ;\n"
"}\n"
"QHeaderView {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section {\n"
"    background: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"	border: 1px solid white;\n"
"	border-radius: 5px;\n"
"	text-alignment: AlignHCenter;\n"
"}\n"
"\n"
"QTableWidget::item::selected {\n"
"	border: none;\n"
"}")
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setProperty("showDropIndicator", True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.chooseStrategy = QComboBox(self.programPage)
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.addItem("")
        self.chooseStrategy.setObjectName(u"chooseStrategy")
        self.chooseStrategy.setGeometry(QRect(10, 160, 410, 41))
        self.chooseStrategy.setCursor(QCursor(Qt.ArrowCursor))
        self.chooseStrategy.setStyleSheet(u"QComboBox {\n"
"	background-color: rgba(255,255,255,30);\n"
"	border: 1px solid white;\n"
"	border-radius: 10px;\n"
"	font-size: 16pt;\n"
"	font-family:'Open Sans Condensed';\n"
"	color:white;\n"
"}\n"
"\n"
"QComboBox:on {\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    font-size: 16px;\n"
"	border: 1px solid rgba(0,0,0,10%);\n"
"	padding: 5px;\n"
"	background-color: #46B7B9;\n"
"	outline: 0px;\n"
"	color: white;\n"
"}\n"
"")
        self.runProcessProgramModule = QPushButton(self.programPage)
        self.runProcessProgramModule.setObjectName(u"runProcessProgramModule")
        self.runProcessProgramModule.setGeometry(QRect(430, 160, 361, 41))
        self.runProcessProgramModule.setCursor(QCursor(Qt.PointingHandCursor))
        self.runProcessProgramModule.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(135, 223, 214, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.frame = QFrame(self.programPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 80, 781, 71))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-family: Consolas")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 381, 51))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';")
        self.readMatrixFileButton = QPushButton(self.frame)
        self.readMatrixFileButton.setObjectName(u"readMatrixFileButton")
        self.readMatrixFileButton.setGeometry(QRect(420, 10, 351, 51))
        self.readMatrixFileButton.setFont(font1)
        self.readMatrixFileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.readMatrixFileButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(135, 223, 214, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.backToWelcomeButton = QPushButton(self.programPage)
        self.backToWelcomeButton.setObjectName(u"backToWelcomeButton")
        self.backToWelcomeButton.setGeometry(QRect(10, 560, 91, 31))
        self.backToWelcomeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.backToWelcomeButton.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(135, 223, 214, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.stackedWidget.addWidget(self.programPage)
        self.testPage = QWidget()
        self.testPage.setObjectName(u"testPage")
        self.frame_2 = QFrame(self.testPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 80, 771, 221))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-size: 14pt;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 10, 761, 31))
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 0px solid rbga(255, 255, 255, 40);\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 40, 151, 31))
        self.label_8.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.n = QLineEdit(self.frame_2)
        self.n.setObjectName(u"n")
        self.n.setGeometry(QRect(160, 40, 71, 31))
        self.n.setMaximumSize(QSize(160, 40))
        self.n.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.n.setMaxLength(5)
        self.n.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.a_min = QLineEdit(self.frame_2)
        self.a_min.setObjectName(u"a_min")
        self.a_min.setGeometry(QRect(210, 80, 41, 31))
        self.a_min.setMaximumSize(QSize(160, 40))
        self.a_min.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.a_min.setMaxLength(2)
        self.a_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(250, 80, 51, 31))
        self.label_10.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"font-family:'Open Sans Condensed';")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.a_max = QLineEdit(self.frame_2)
        self.a_max.setObjectName(u"a_max")
        self.a_max.setGeometry(QRect(300, 80, 41, 31))
        self.a_max.setMaximumSize(QSize(160, 40))
        self.a_max.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.a_max.setMaxLength(2)
        self.a_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 120, 190, 31))
        self.label_11.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 120, 51, 31))
        self.label_12.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-weight: bold;\n"
"font-family:'Open Sans Condensed';")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_max = QLineEdit(self.frame_2)
        self.b_max.setObjectName(u"b_max")
        self.b_max.setGeometry(QRect(300, 120, 41, 31))
        self.b_max.setMaximumSize(QSize(160, 40))
        self.b_max.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.b_max.setMaxLength(4)
        self.b_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_min = QLineEdit(self.frame_2)
        self.b_min.setObjectName(u"b_min")
        self.b_min.setGeometry(QRect(210, 120, 41, 31))
        self.b_min.setMaximumSize(QSize(160, 40))
        self.b_min.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.b_min.setMaxLength(4)
        self.b_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ripeningCheck = QCheckBox(self.frame_2)
        self.ripeningCheck.setObjectName(u"ripeningCheck")
        self.ripeningCheck.setGeometry(QRect(400, 40, 141, 31))
        self.ripeningCheck.setStyleSheet(u"QCheckBox{\n"
"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(400, 80, 240, 31))
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.nu = QLineEdit(self.frame_2)
        self.nu.setObjectName(u"nu")
        self.nu.setGeometry(QRect(650, 80, 71, 31))
        self.nu.setMaximumSize(QSize(160, 40))
        self.nu.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.nu.setMaxLength(5)
        self.nu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(400, 120, 191, 31))
        self.label_14.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.b_min_2 = QLineEdit(self.frame_2)
        self.b_min_2.setObjectName(u"b_min_2")
        self.b_min_2.setGeometry(QRect(590, 120, 41, 31))
        self.b_min_2.setMaximumSize(QSize(160, 40))
        self.b_min_2.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.b_min_2.setMaxLength(4)
        self.b_min_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.b_max_2 = QLineEdit(self.frame_2)
        self.b_max_2.setObjectName(u"b_max_2")
        self.b_max_2.setGeometry(QRect(680, 120, 41, 31))
        self.b_max_2.setMaximumSize(QSize(160, 40))
        self.b_max_2.setStyleSheet(u"QLineEdit{ \n"
"border: 1px solid white;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"font-family:'Open Sans Condensed';\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit:focus{\n"
"border: 2px solid white;\n"
"}")
        self.b_max_2.setMaxLength(4)
        self.b_max_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(630, 120, 51, 31))
        self.label_15.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.runProcessTest = QPushButton(self.frame_2)
        self.runProcessTest.setObjectName(u"runProcessTest")
        self.runProcessTest.setGeometry(QRect(10, 170, 751, 41))
        self.runProcessTest.setCursor(QCursor(Qt.PointingHandCursor))
        self.runProcessTest.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 80, 190, 31))
        self.label_9.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: none;\n"
"color: white;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.backToWelcomeButton_2 = QPushButton(self.testPage)
        self.backToWelcomeButton_2.setObjectName(u"backToWelcomeButton_2")
        self.backToWelcomeButton_2.setGeometry(QRect(10, 560, 91, 31))
        self.backToWelcomeButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.backToWelcomeButton_2.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.label_6 = QLabel(self.testPage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 20, 771, 51))
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255);\n"
"border: 1px solid white;\n"
"border-radius: 10px;\n"
"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"font-family:'Open Sans Condensed';")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.MplHist = MplWidget(self.testPage)
        self.MplHist.setObjectName(u"MplHist")
        self.MplHist.setGeometry(QRect(10, 310, 370, 210))
        self.MplLine = MplWidget(self.testPage)
        self.MplLine.setObjectName(u"MplLine")
        self.MplLine.setGeometry(QRect(410, 310, 370, 210))
        self.plusButtonHist = QPushButton(self.testPage)
        self.plusButtonHist.setObjectName(u"plusButtonHist")
        self.plusButtonHist.setGeometry(QRect(140, 530, 91, 24))
        self.plusButtonHist.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.plusButtonLine = QPushButton(self.testPage)
        self.plusButtonLine.setObjectName(u"plusButtonLine")
        self.plusButtonLine.setGeometry(QRect(560, 530, 101, 24))
        self.plusButtonLine.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 10px;\n"
"font-size: 16pt;\n"
"font-family:'Open Sans Condensed';\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}")
        self.stackedWidget.addWidget(self.testPage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.ripeningCheck.toggled.connect(self.label_13.setVisible)
        self.ripeningCheck.toggled.connect(self.nu.setVisible)
        self.ripeningCheck.toggled.connect(self.label_14.setVisible)
        self.ripeningCheck.toggled.connect(self.b_min_2.setVisible)
        self.ripeningCheck.toggled.connect(self.label_15.setVisible)
        self.ripeningCheck.toggled.connect(self.b_max_2.setVisible)

        self.stackedWidget.setCurrentIndex(0)
        self.chooseStrategy.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Open Sans Condensed'; font-size:22pt;\">\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u043c\u043e\u0434\u0443\u043b\u044c \u0434\u043b\u044f \u0437\u0430\u043f\u0443\u0441\u043a\u0430:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\"font-family:'Open Sans Condensed'; font-size:24pt; font-weight:400;\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430</span></p><p align=\"center\"><span style=\" font-family:'Open Sans Condensed'; font-size:24pt;\">&quot;\u041f\u0435\u0440\u0435\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043f\u0430\u0440\u0442\u0438\u0439 \u0441\u0430\u0445\u0430\u0440\u043d\u043e\u0439 \u0441\u0432\u0435\u043a\u043b\u044b&quot;</span></p></body></html>", None))
        self.testStartButton.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.\n"
"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u0432\u0432\u0435\u0441\u0442\u0438 \u0432\u0445\u043e\u0434\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043b\u044f \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u0438\u043d\u0438\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438 \u043c\u0430\u0442\u0440\u0438\u0446, \u0430 \u0437\u0430\u0442\u0435\u043c\n"
"\u0437\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0441\u0435\u0445 \u0438\u043c\u0435\u044e\u0449\u0438\u0445\u0441\u044f \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0439. \u041f\u043e \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u0438 \u0442\u0435\u0441\u0442\u0438\u0440"
                        "\u043e\u0432\u0430\u043d\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e \u0432\u044b\u0432\u043e\u0434\u0438\u0442\u0441\u044f\n"
"\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0441\u0430\u043c\u043e\u0439 \u043b\u0443\u0447\u0448\u0435\u0439 \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u0438, \u0430 \u0442\u0430\u043a\u0436\u0435 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0432\u044b\u0432\u0435\u0441\u0442\u0438 \u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0438\n"
"\u0441\u0432\u043e\u0434\u043d\u0443\u044e \u0442\u0430\u0431\u043b\u0438\u0446\u0443.", None))
        self.programStartButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043c\u043e\u0434\u0443\u043b\u044c.\n"
"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e \u043f\u0440\u0435\u0434\u043b\u0430\u0433\u0430\u0435\u0442\u0441\u044f \u0441\u0447\u0438\u0442\u0430\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430, \u0430 \u0437\u0430\u0442\u0435\u043c \u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044e, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u043e\u043d \u0445\u043e\u0447\u0435\u0442\n"
"\u043f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c \u043a \u0434\u0430\u043d\u043d\u043e\u0439 \u043c\u0430\u0442\u0440\u0438\u0446\u0435.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u0439 \u043c\u043e\u0434\u0443\u043b\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041c\u0430\u0442\u0440\u0438\u0446\u0430</p></body></html>", None))
        self.chooseStrategy.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0412\u0435\u043d\u0433\u0435\u0440\u0441\u043a\u0438\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.chooseStrategy.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0416\u0430\u0434\u043d\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.chooseStrategy.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0435\u0436\u043b\u0438\u0432\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.chooseStrategy.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0416\u0430\u0434\u043d\u043e-\u0431\u0435\u0440\u0435\u0436\u043b\u0438\u0432\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.chooseStrategy.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0435\u0436\u043b\u0438\u0432\u043e-\u0436\u0430\u0434\u043d\u044b\u0439 \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c", None))
        self.chooseStrategy.setItemText(5, QCoreApplication.translate("MainWindow", u"CTG", None))
        self.chooseStrategy.setItemText(6, QCoreApplication.translate("MainWindow", u"T(k)G", None))
        self.chooseStrategy.setItemText(7, QCoreApplication.translate("MainWindow", u"G(k)", None))

        self.chooseStrategy.setCurrentText("")
        self.chooseStrategy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0441\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044e", None))
        self.runProcessProgramModule.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1. \u0424\u043e\u0440\u043c\u0430\u0442 \u0432\u0432\u043e\u0434\u0430 \u0434\u0430\u043d\u043d\u044b\u0445: \u043c\u0430\u0442\u0440\u0438\u0446\u0430 (NxN)\n"
"2. \u0424\u043e\u0440\u043c\u0430\u0442 \u0444\u0430\u0439\u043b\u0430: \u0442\u0435\u043a\u0441\u0442\u043e\u0432\u044b\u0439 \u0444\u043e\u0440\u043c\u0430\u0442 (.txt)", None))
        self.readMatrixFileButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0447\u0438\u0442\u0430\u0442\u044c \u043c\u0430\u0442\u0440\u0438\u0446\u0443 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.backToWelcomeButton.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043d\u0435\u0439 (n):", None))
        self.n.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.n.setPlaceholderText("")
        self.a_min.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2264 a<span style=\" vertical-align:sub;\">i</span> \u2264</p></body></html>", None))
        self.a_max.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0434\u0435\u0433\u0440\u0430\u0434\u0430\u0446\u0438\u0438:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2264 b<span style=\" vertical-align:sub;\">ij</span> \u2264</p></body></html>", None))
        self.b_max.setText(QCoreApplication.translate("MainWindow", u"0.99", None))
        self.b_min.setText(QCoreApplication.translate("MainWindow", u"0.96", None))
        self.ripeningCheck.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0437\u0430\u0440\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043d\u0435\u0439 \u0434\u043e\u0437\u0430\u0440\u0438\u0432\u0430\u043d\u0438\u044f (\u03bd):</p></body></html>", None))
        self.nu.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0434\u0435\u0433\u0440\u0430\u0434\u0430\u0446\u0438\u0438:", None))
        self.b_min_2.setText(QCoreApplication.translate("MainWindow", u"1.01", None))
        self.b_max_2.setText(QCoreApplication.translate("MainWindow", u"1.05", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2264 b<span style=\" vertical-align:sub;\">ij</span> \u2264</p></body></html>", None))
        self.runProcessTest.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u043f\u0440\u043e\u0446\u0435\u0441\u0441", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u0441\u0430\u0445\u0430\u0440\u0438\u0441\u0442\u043e\u0441\u0442\u0438:", None))
        self.backToWelcomeButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0443\u043b\u044c \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.plusButtonHist.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u044c", None))
        self.plusButtonLine.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0437\u0438\u0442\u044c", None))
    # retranslateUi

