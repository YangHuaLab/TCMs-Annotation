import sys
import pandas as pd

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import QtCore
from PyQt6.QtWidgets import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import seaborn as sns
from statannotations.Annotator import Annotator
from qt_material import apply_stylesheet


class helloui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1151, 517)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 434, 1071, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 1071, 421))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Processing of MS Data"))
        self.pushButton_2.setText(_translate("Form", "Processing of Images Data"))
        self.pushButton_3.setText(_translate("Form", "Screening of Active Compound"))
        self.pushButton_4.setText(_translate("Form", "Processing of Molecular graph"))
class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(994, 563)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 331, 211))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.exportbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.exportbutton1.setObjectName("exportbutton1")
        self.gridLayout_3.addWidget(self.exportbutton1, 2, 0, 1, 1)
        self.importbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.importbutton1.setObjectName("importbutton1")
        self.gridLayout_3.addWidget(self.importbutton1, 0, 0, 1, 1)
        self.importbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.importbrowser1.setObjectName("importbrowser1")
        self.gridLayout_3.addWidget(self.importbrowser1, 0, 1, 1, 1)
        self.exportbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.exportbrowser1.setObjectName("exportbrowser1")
        self.gridLayout_3.addWidget(self.exportbrowser1, 2, 1, 1, 1)
        self.startbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.startbutton1.setObjectName("startbutton1")
        self.gridLayout_3.addWidget(self.startbutton1, 1, 0, 1, 2)
        self.tableWidget1 = QtWidgets.QTableWidget(Form)
        self.tableWidget1.setGeometry(QtCore.QRect(350, 10, 641, 551))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exportbutton1.setText(_translate("Form", "Export file"))
        self.importbutton1.setText(_translate("Form", "Import file"))
        self.startbutton1.setText(_translate("Form", "Start"))


# window2.py代码
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1345, 563)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 311, 126))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.importButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.importButton.setObjectName("importButton")
        self.gridLayout_2.addWidget(self.importButton, 0, 0, 1, 1)
        self.importBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.importBrowser.setObjectName("importBrowser")
        self.gridLayout_2.addWidget(self.importBrowser, 0, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setGeometry(QtCore.QRect(100, 150, 141, 23))
        self.startButton.setObjectName("startButton")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(330, 10, 1011, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView_pca = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_pca.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.graphicsView_pca.setObjectName("graphicsView_pca")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphicsView_plsda = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_plsda.setGeometry(QtCore.QRect(5, 1, 991, 511))
        self.graphicsView_plsda.setObjectName("graphicsView_plsda")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.graphicsView_bar = QtWidgets.QGraphicsView(self.tab_5)
        self.graphicsView_bar.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.graphicsView_bar.setObjectName("graphicsView_bar")
        self.tabWidget.addTab(self.tab_5, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 330, 211, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exportVipButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportVipButton.setObjectName("exportVipButton")
        self.verticalLayout.addWidget(self.exportVipButton)
        self.exportTtestButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportTtestButton.setObjectName("exportTtestButton")
        self.verticalLayout.addWidget(self.exportTtestButton)
        self.exportPcaButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportPcaButton.setObjectName("exportPcaButton")
        self.verticalLayout.addWidget(self.exportPcaButton)
        self.exportPlsdaButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportPlsdaButton.setObjectName("exportPlsdaButton")
        self.verticalLayout.addWidget(self.exportPlsdaButton)
        self.exportBarplotsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportBarplotsButton.setObjectName("exportBarplotsButton")
        self.verticalLayout.addWidget(self.exportBarplotsButton)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.importButton.setText(_translate("Form", "Import file"))
        self.startButton.setText(_translate("Form", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "页"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "页"))
        self.exportVipButton.setText(_translate("Form", "Export VIP Table"))
        self.exportTtestButton.setText(_translate("Form", "Export T-test Table"))
        self.exportPcaButton.setText(_translate("Form", "Export PCA Plot"))
        self.exportPlsdaButton.setText(_translate("Form", "Export PLS-DA Plot"))
        self.exportBarplotsButton.setText(_translate("Form", "Export Bar Plots"))


# window3.py 代码
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window3.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1344, 563)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 311, 126))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.importhcsbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.importhcsbutton2.setObjectName("importhcsbutton2")
        self.gridLayout_2.addWidget(self.importhcsbutton2, 1, 0, 1, 1)
        self.importmsbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.importmsbutton2.setObjectName("importmsbutton2")
        self.gridLayout_2.addWidget(self.importmsbutton2, 0, 0, 1, 1)
        self.msbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.msbrowser2.setObjectName("msbrowser2")
        self.gridLayout_2.addWidget(self.msbrowser2, 0, 1, 1, 1)
        self.hcsbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_2)
        self.hcsbrowser2.setObjectName("hcsbrowser2")
        self.gridLayout_2.addWidget(self.hcsbrowser2, 1, 1, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 210, 301, 130))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.qthreshold2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.qthreshold2.setObjectName("qthreshold2")
        self.verticalLayout_2.addWidget(self.qthreshold2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.clusterthreshold2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.clusterthreshold2.setObjectName("clusterthreshold2")
        self.verticalLayout_2.addWidget(self.clusterthreshold2)
        self.startbutton2 = QtWidgets.QPushButton(Form)
        self.startbutton2.setGeometry(QtCore.QRect(100, 150, 141, 23))
        self.startbutton2.setObjectName("startbutton2")
        self.tabWidget2 = QtWidgets.QTabWidget(Form)
        self.tabWidget2.setGeometry(QtCore.QRect(330, 10, 1011, 541))
        self.tabWidget2.setObjectName("tabWidget2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget2 = QtWidgets.QTableWidget(self.tab)
        self.tableWidget2.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        self.tabWidget2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView2_hist = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView2_hist.setGeometry(QtCore.QRect(0, 0, 1001, 511))
        self.graphicsView2_hist.setObjectName("graphicsView2_hist")
        self.tabWidget2.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.graphicsView2_scatter = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView2_scatter.setGeometry(QtCore.QRect(-5, 1, 1001, 511))
        self.graphicsView2_scatter.setObjectName("graphicsView2_scatter")
        self.tabWidget2.addTab(self.tab_3, "")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 400, 211, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exporttablebutton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exporttablebutton2.setObjectName("exporttablebutton2")
        self.verticalLayout.addWidget(self.exporttablebutton2)
        self.exporthistagrambutton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exporthistagrambutton2.setObjectName("exporthistagrambutton2")
        self.verticalLayout.addWidget(self.exporthistagrambutton2)
        self.exportscatterbutton2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.exportscatterbutton2.setObjectName("exportscatterbutton2")
        self.verticalLayout.addWidget(self.exportscatterbutton2)

        self.retranslateUi(Form)
        self.tabWidget2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.importhcsbutton2.setText(_translate("Form", "Import HCS file"))
        self.importmsbutton2.setText(_translate("Form", "Import MS file"))
        self.label.setText(_translate("Form", "Z-score Quantile Threshold (0-1):"))
        self.label_2.setText(_translate("Form", "Cluster Score Threshold (0-1):"))
        self.startbutton2.setText(_translate("Form", "Start"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.tabWidget2.setTabText(self.tabWidget2.indexOf(self.tab_3), _translate("Form", "页"))
        self.exporttablebutton2.setText(_translate("Form", "Export Table"))
        self.exporthistagrambutton2.setText(_translate("Form", "Export Histagram"))
        self.exportscatterbutton2.setText(_translate("Form", "Export Scatter Plot"))
#window4窗口
class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(994, 563)
        self.gridLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 331, 211))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
#导出按钮1
        self.exportbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.exportbutton1.setObjectName("exportbutton1")
        self.gridLayout_4.addWidget(self.exportbutton1, 3, 0, 1, 1)
#导出按钮2
        self.exportbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.exportbutton2.setObjectName("exportbutton2")
        self.gridLayout_4.addWidget(self.exportbutton2, 4, 0, 1, 1)
#导入按钮1
        self.importbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.importbutton1.setObjectName("importbutton1")
        self.gridLayout_4.addWidget(self.importbutton1, 0, 0, 1, 1)
#导入按钮2
        self.importbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.importbutton2.setObjectName("importbutton2")
        self.gridLayout_4.addWidget(self.importbutton2, 1, 0, 1, 1)
#导入文本1
        self.importbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.importbrowser1.setObjectName("importbrowser1")
        self.gridLayout_4.addWidget(self.importbrowser1, 0, 1, 1, 1)
#导入文本2
        self.importbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.importbrowser2.setObjectName("importbrowser2")
        self.gridLayout_4.addWidget(self.importbrowser2, 1, 1, 1, 1)
#导出文本1
        self.exportbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.exportbrowser1.setObjectName("exportbrowser1")
        self.gridLayout_4.addWidget(self.exportbrowser1, 3, 1, 1, 1)
#导出文本2
        self.exportbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_4)
        self.exportbrowser2.setObjectName("exportbrowser2")
        self.gridLayout_4.addWidget(self.exportbrowser2, 4, 1, 1, 1)
#开始按钮
        self.startbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.startbutton1.setObjectName("startbutton1")
        self.gridLayout_4.addWidget(self.startbutton1, 2, 0, 1, 2)
#导入QTabWidget控件窗口
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(358, 10, 1011, 541))
        self.tabWidget.setObjectName("tabWidget")
#创建标签页1
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
#往标签页1添加表格1
        self.tableWidget = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 550, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab1, "")
#创建标签页2
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
#创建表格2添加到标签页2
        self.tableWidget = QtWidgets.QTableWidget(self.tab2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 550, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
#放置控件窗口
        self.tabWidget.addTab(self.tab2, "")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exportbutton1.setText(_translate("Form", "Export file1"))
        self.exportbutton2.setText(_translate("Form", "Export file2"))
        # self.exportbutton3.setText(_translate("Form", "Export picture3"))
        self.importbutton1.setText(_translate("Form", "Import file1"))
        self.importbutton2.setText(_translate("Form", "Import file2"))
        self.startbutton1.setText(_translate("Form", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("Form", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("Form", "Tab 2"))
# 界面1窗口
class Window1(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_ui()

    def init_ui(self):
        # self.ui = uic.loadUi("window1.ui")   # 加载ui文件
        self.setWindowTitle('Processing of MS Data')  # 界面1标题
        # self.setWindowIcon(QIcon('logo.ico'))   # 软件logo

        # 界面各控件设置
        # 界面1的控件
        # self.importbutton1 = self.ui.importbutton1   # 导入按钮
        # self.startbutton1 = self.ui.startbutton1   # 开始按钮
        # self.exportbutton1 = self.ui.exportbutton1   # 导出按钮
        # self.importbrowser1 = self.ui.importbrowser1   # 导入文件信息展示
        # self.exportbrowser1 = self.ui.exportbrowser1   # 导出文件信息展示
        # self.tableWidget1 = self.ui.tableWidget1   # 表格信息展示

        # 各按钮与相应功能相连接
        # 界面1的各按钮与相应功能相连接
        self.startbutton1.clicked.connect(self.start_process1)  # 将开始按钮与开始处理的功能连接
        self.importbutton1.clicked.connect(self.import_file1)  # 将导入按钮与导入文件的功能连接
        self.exportbutton1.clicked.connect(self.export_file1)  # 将导出按钮与导出文件的功能连接

    # 界面1的各个功能
    # 开始处理的功能（界面1）
    def start_process1(self):
        # self.textBrowser1.setText("Processing. Please wait. This process may take a few hours...")
        # self.textBrowser1.repaint()

        self.result1 = get_mzrt(self.file_path1)

        self.tableWidget1.setRowCount(self.result1.shape[0])
        self.tableWidget1.setColumnCount(self.result1.shape[1])
        self.tableWidget1.setHorizontalHeaderLabels(self.result1.columns)

        for row in range(self.result1.shape[0]):
            for column in range(self.result1.shape[1]):
                item = QTableWidgetItem(str(self.result1.iloc[row, column]))
                self.tableWidget1.setItem(row, column, item)

        # self.textBrowser1.setText("Process done! Now you can export the result table.")
        # self.textBrowser1.repaint()

    # 导入文件的功能（界面1）
    def import_file1(self):
        file_dialog = QFileDialog()
        # 获得导入文件路径，用于后续操作
        self.file_path1, _ = file_dialog.getOpenFileName(None, "Import File", "", "(*.xls *.xlsx)")
        if self.file_path1 == '':
            pass
        else:
            self.importbrowser1.setText(f"{self.file_path1.split('/')[-1]} imported.")
            self.importbrowser1.repaint()

    # 导出文件的功能（界面1）
    def export_file1(self):
        self.export_path1, type = QFileDialog.getSaveFileName(self, 'Export Table', '/', 'xlsx(*.xlsx)')
        if self.export_path1 == '':
            pass
        else:
            self.result1.to_excel(self.export_path1, index=False)

            self.exportbrowser1.setText(f"Exported to {self.export_path1}")
            self.exportbrowser1.repaint()


# 界面2窗口
class Window2(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_ui()

    def init_ui(self):
        # self.ui = uic.loadUi("window2.ui")   # 加载ui文件
        self.setWindowTitle('Processing of Images Data')  # 软件标题
        # self.setWindowIcon(QIcon('logo.ico'))   # 软件logo

        # 界面各控件设置
        # 按钮
        # self.importButton = self.ui.importButton
        # self.startButton = self.ui.startButton
        # self.exportVipButton = self.ui.exportVipButton
        # self.exportTtestButton = self.ui.exportTtestButton
        # self.exportPcaButton = self.ui.exportPcaButton
        # self.exportPlsdaButton = self.ui.exportPlsdaButton
        # self.exportBarplotsButton = self.ui.exportBarplotsButton
        # # 显示
        # self.importBrowser = self.ui.importBrowser
        # 各Tab
        # self.tabWidget = self.ui.tabWidget
        self.tabWidget.setTabText(0, "VIP>1")
        self.tabWidget.setTabText(1, "Table")
        self.tabWidget.setTabText(2, "PCA")
        self.tabWidget.setTabText(3, "PLS-DA")
        self.tabWidget.setTabText(4, "Bar Plots")
        # self.tableWidget = self.ui.tableWidget
        # self.tableWidget_2 = self.ui.tableWidget_2
        # self.graphicsView_pca = self.ui.graphicsView_pca
        # self.graphicsView_plsda = self.ui.graphicsView_plsda
        # self.graphicsView_bar = self.ui.graphicsView_bar
        # 各按钮与相应功能相连接
        self.importButton.clicked.connect(self.import_file)
        self.startButton.clicked.connect(self.start_process)
        self.startButton.clicked.connect(self.draw_bar_plots)
        self.exportVipButton.clicked.connect(self.export_vip_table)
        self.exportTtestButton.clicked.connect(self.export_ttest_table)
        self.exportPcaButton.clicked.connect(self.export_pca)
        self.exportPlsdaButton.clicked.connect(self.export_plsda)
        self.exportBarplotsButton.clicked.connect(self.export_barplots)

    # 界面各个功能
    # 导入文件的功能
    def import_file(self):
        file_dialog = QFileDialog()
        # 获得导入文件路径，用于后续操作
        self.file_path, _ = file_dialog.getOpenFileName(None, "Import File", "", "(*.xls *.xlsx)")
        if self.file_path == '':
            pass
        else:
            self.importBrowser.setText(f"{self.file_path.split('/')[-1]} imported.")
            self.importBrowser.repaint()

    # 开始处理的功能：显示表格/pca图/plsda图
    def start_process(self):
        self.X_pca, self.X_plsda, self.cat, self.vip_gt_1, list_vip = get_results(self.file_path)
        self.df2 = ttest_table(self.file_path, list_vip)

        # 显示vip大于1的参数表格
        self.tableWidget.setRowCount(len(self.vip_gt_1))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(['Parameters (VIP>1)', ])
        for row in range(len(self.vip_gt_1)):
            item = QTableWidgetItem(self.vip_gt_1[row])
            self.tableWidget.setItem(row, 0, item)

        # 显示ttest表格
        self.tableWidget_2.setRowCount(self.df2.shape[0])
        self.tableWidget_2.setColumnCount(self.df2.shape[1])
        self.tableWidget_2.setHorizontalHeaderLabels(self.df2.columns)
        self.tableWidget_2.verticalHeader().setVisible(False)  # 不显示行号
        for row in range(self.df2.shape[0]):
            for col in range(self.df2.shape[1]):
                item = QTableWidgetItem(str(self.df2.iloc[row, col]))
                self.tableWidget_2.setItem(row, col, item)

        # 显示pca散点图
        self.F1 = MyFigure(width=6, height=4, dpi=100)
        self.F1.axes1 = self.F1.fig.add_subplot(111)
        sns.scatterplot(x=self.X_pca[:, 0], y=self.X_pca[:, 1], hue=self.cat, ax=self.F1.axes1)
        self.F1.axes1.set_xlabel('PCA 1', fontsize=14)
        self.F1.axes1.set_ylabel('PCA 2', fontsize=14)
        self.F1.axes1.set_title('PCA', fontsize=14)
        # 图像展示
        self.scene1 = QGraphicsScene()  # 创建一个场景
        self.scene1.addWidget(self.F1)  # 将图形元素添加到场景中
        self.graphicsView_pca.setScene(self.scene1)

        # 显示plsda散点图
        self.F2 = MyFigure(width=6, height=4, dpi=100)
        self.F2.axes1 = self.F2.fig.add_subplot(111)
        sns.scatterplot(x=self.X_plsda[:, 0], y=self.X_plsda[:, 1], hue=self.cat, ax=self.F2.axes1)
        self.F2.axes1.set_xlabel('PLS-DA 1', fontsize=14)
        self.F2.axes1.set_ylabel('PLS-DA 2', fontsize=14)
        self.F2.axes1.set_title('PLS-DA', fontsize=14)
        # 图像展示
        self.scene2 = QGraphicsScene()  # 创建一个场景
        self.scene2.addWidget(self.F2)  # 将图形元素添加到场景中
        self.graphicsView_plsda.setScene(self.scene2)

    def draw_bar_plots(self):
        df_bar = pd.read_excel(self.file_path, index_col=0)
        mask = [i for i in df_bar.index if "".join(list(filter(str.isalpha, i))).upper() in ('C', 'M')]
        df_bar = df_bar.loc[mask]
        self.params = df_bar.columns.tolist()
        num = len(df_bar.columns)
        table_col = 4
        if num % table_col == 0:
            table_row = num / table_col
        else:
            table_row = int(num / table_col) + 1

        cat = ["Control" if i[0].upper() == 'C' else "Model" for i in mask]
        df_bar['group'] = cat

        # 创建图像
        self.F3 = MyFigure(width=2.5 * table_col, height=3 * table_row, dpi=100)
        self.axes = []
        palette = sns.color_palette(["#00E5EE", "#EE6363"])  # 指定柱形颜色
        for i in range(num):
            ax = self.F3.fig.add_subplot(table_row, table_col, i + 1)
            ax = sns.barplot(x='group', y=df_bar.columns[i], data=df_bar, palette=palette, estimator=np.mean, ci="sd",
                             capsize=.1, errwidth=2, ax=ax)
            ax = sns.stripplot(x='group', y=df_bar.columns[i], data=df_bar, palette=palette, ax=ax)
            ax.set_xlabel('')
            ax.set_ylabel('')
            ax.set_title(df_bar.columns[i], fontsize=10)
            for spine in ["top", "right"]:
                ax.spines[spine].set_visible(False)
            # 显著性标识
            annotator = Annotator(ax, pairs=[('Control', 'Model'), ], data=df_bar, x='group', y=df_bar.columns[0],
                                  order=['Control', 'Model'])
            annotator.configure(test='t-test_ind', text_format='star', line_height=0.03, line_width=1)
            annotator.apply_and_annotate()
            self.axes.append(ax)
        self.F3.fig.tight_layout()

        # 图像展示
        self.scene3 = QGraphicsScene()  # 创建一个场景
        self.scene3.addWidget(self.F3)  # 将图形元素添加到场景中
        self.graphicsView_bar.setScene(self.scene3)

    # 导出vip表格的功能
    def export_vip_table(self):
        self.export_vip_path, type = QFileDialog.getSaveFileName(self, 'Export VIP Table', '/', 'xlsx(*.xlsx)')
        if self.export_vip_path == '':
            pass
        else:
            df = pd.DataFrame(self.vip_gt_1, columns=['Parameters (VIP>1)', ])
            df.to_excel(self.export_vip_path, index=False)

    # 导出ttest表格的功能
    def export_ttest_table(self):
        self.export_ttest_path, type = QFileDialog.getSaveFileName(self, 'Export T-test Table', '/', 'xlsx(*.xlsx)')
        if self.export_ttest_path == '':
            pass
        else:
            self.df2.to_excel(self.export_ttest_path, index=False)

    # 导出pca图的功能
    def export_pca(self):
        self.export_pca_path, type = QFileDialog.getSaveFileName(self, 'Export PCA Image', '/', 'png(*.png)')
        if self.export_pca_path == '':
            pass
        else:
            self.F1.savefig(self.export_pca_path)

    # 导出plsda图的功能
    def export_plsda(self):
        self.export_plsda_path, type = QFileDialog.getSaveFileName(self, 'Export PLS-DA Image', '/', 'png(*.png)')
        if self.export_plsda_path == '':
            pass
        else:
            self.F2.savefig(self.export_plsda_path)

    def export_barplots(self):
        self.export_barplots_path = QFileDialog.getExistingDirectory(self, 'Export Path', '/')
        if self.export_barplots_path == '':
            pass
        else:
            for i, param in enumerate(self.params):
                save_subfig(self.F3.fig, self.axes[i], self.export_barplots_path, param)


# 界面3窗口
class Window3(QWidget, Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_ui()

    def init_ui(self):
        # self.ui = uic.loadUi("window3.ui")   # 加载ui文件
        self.setWindowTitle('Screening of Active Compound')  # 软件标题
        # self.setWindowIcon(QIcon('logo.ico'))   # 软件logo

        # 界面各控件设置
        # 界面2的控件
        # 按钮
        # self.importmsbutton2 = self.ui.importmsbutton2
        # self.importhcsbutton2 = self.ui.importhcsbutton2
        # self.startbutton2 = self.ui.startbutton2
        # self.exporttablebutton2 = self.ui.exporttablebutton2
        # self.exporthistagrambutton2 = self.ui.exporthistagrambutton2
        # self.exportscatterbutton2 = self.ui.exportscatterbutton2
        # 输入阈值
        # self.qthreshold2 = self.ui.qthreshold2
        # self.clusterthreshold2 = self.ui.clusterthreshold2
        # 信息显示
        # self.msbrowser2 = self.ui.msbrowser2
        # self.hcsbrowser2 = self.ui.hcsbrowser2
        # 各Tab
        # self.tabWidget2 = self.ui.tabWidget2
        self.tabWidget2.setTabText(0, "Table")
        self.tabWidget2.setTabText(1, "Histagram")
        self.tabWidget2.setTabText(2, "Scatter Plot")
        # self.tableWidget2 = self.ui.tableWidget2
        # self.graphicsView2_hist = self.ui.graphicsView2_hist
        # self.graphicsView2_scatter = self.ui.graphicsView2_scatter

        # 各按钮与相应功能相连接
        # 界面2的各按钮与相应功能相连接
        self.startbutton2.clicked.connect(self.start_process2)  # 将开始按钮与数据处理的功能连接
        self.startbutton2.clicked.connect(self.draw_figure2)  # 将开始按钮与图像展示的功能连接
        self.importmsbutton2.clicked.connect(self.import_ms2)  # 将导入ms按钮与导入ms文件的功能连接
        self.importhcsbutton2.clicked.connect(self.import_hcs2)  # 将导入hcs按钮与导入hcs文件的功能连接
        self.exporttablebutton2.clicked.connect(self.export_table2)
        self.exporthistagrambutton2.clicked.connect(self.export_histagram2)
        self.exportscatterbutton2.clicked.connect(self.export_scatter2)

    # 界面3的各个功能
    # 开始处理的功能（界面2）
    def start_process2(self):
        # 将展示表清空
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.clearContents()

        # 获取输入阈值
        self.zscore_qtreshold = self.qthreshold2.text()
        if self.zscore_qtreshold == "":
            self.zscore_qtreshold = 0
        else:
            self.zscore_qtreshold = float(self.zscore_qtreshold)

        self.cluster_threshold = self.clusterthreshold2.text()
        if self.cluster_threshold == "":
            self.cluster_threshold = 0
        else:
            self.cluster_threshold = float(self.cluster_threshold)

        # 数据处理
        data_mzrt = process_ms_data(self.ms_path2)
        normalize_datac, normalize_datapa, normalize_datahq = process_hcs_data(self.hcs_path2)
        features = get_features(normalize_datahq)
        score_mzrt = calculate_mzrt_score(normalize_datahq, data_mzrt, features)
        score_control, score_model = calculate_control_and_model_score(normalize_datac, normalize_datapa, features)
        zscore_control, self.zscore_model, self.zscore_mzrt = calculate_zscore(score_control, score_model, score_mzrt,
                                                                               features)
        self.feature = features[0]
        cluster_score_mzrt = calculate_cluster_score(data_mzrt, normalize_datahq)

        self.final_data = make_final_data(self.zscore_mzrt, cluster_score_mzrt, data_mzrt, features,
                                          zscore_qthreshold=self.zscore_qtreshold,
                                          cluster_threshold=self.cluster_threshold)

        # 表格展示
        self.tableWidget2.setRowCount(self.final_data.shape[0])
        self.tableWidget2.setColumnCount(self.final_data.shape[1])
        self.tableWidget2.setHorizontalHeaderLabels(self.final_data.columns)

        for row in range(self.final_data.shape[0]):
            for column in range(self.final_data.shape[1]):
                item = QTableWidgetItem(str(self.final_data.iloc[row, column]))
                self.tableWidget2.setItem(row, column, item)

    def draw_figure2(self):
        # 1. Histagram累积分布图
        self.F1 = MyFigure(width=6, height=4, dpi=100)
        self.F1.axes1 = self.F1.fig.add_subplot(111)
        # 原绘图函数参数
        datas = [self.zscore_mzrt[self.feature], self.zscore_model[self.feature]]
        labels = ['treatment', 'model']
        title = title = f'${self.feature}\\ z\\ scores$'
        label_loc = 'upper right'
        q = self.zscore_qtreshold
        # 原绘图函数
        colors1 = ['#4682B4', '#FFA500', 'forestgreen']
        colors2 = ['b', 'y', 'g']
        threshold = datas[1].quantile(q=1 - q)
        maximum = 0
        span = datas[1].max() - datas[1].min()
        for i, data_label in enumerate(zip(datas, labels)):
            data = data_label[0]
            label = data_label[1]
            n, bins, patches = self.F1.axes1.hist(data, density=True, label=label,
                                                  alpha=0.8, bins=20, color=colors1[i])
            y = norm.pdf(bins, data.mean(), data.std())
            if n.max() > maximum:
                maximum = n.max()
            self.F1.axes1.plot(bins, y, colors2[i] + '--')
        median_mz = datas[0].median()
        # plt.plot([median_mz,median_mz],[0,maximum],'k--',linewidth=2)
        # plt.arrow(threshold-span*0.05,maximum/1.5,-span*0.1,0,width=maximum*0.04,head_length=span*0.05,fc='steelblue',ec='steelblue')
        self.F1.axes1.set_xlabel(r'$z\ scores$', fontsize=14)
        self.F1.axes1.set_ylabel('$frequncy$', fontsize=14)
        self.F1.axes1.set_title(title, fontsize=14)
        self.F1.axes1.legend(loc=label_loc, fontsize=14)
        # F1.axes1.tick_params(labelsize=10)
        # 图像展示
        self.scene1 = QGraphicsScene()  # 创建一个场景
        self.scene1.addWidget(self.F1)  # 将图形元素添加到场景中
        self.graphicsView2_hist.setScene(self.scene1)

        # 2. Scatter Plot散点图
        self.F2 = MyFigure(width=10, height=4, dpi=100)
        # 原绘图函数参数
        datas = [self.zscore_mzrt[self.feature], self.zscore_model[self.feature]]
        threshold = self.zscore_qtreshold
        title = f'{self.feature} score'
        # 原绘图函数
        data = datas[0]
        cutoff = data.quantile(q=threshold)  # 蓝色横线的值cutoff
        grid = plt.GridSpec(1, 3, wspace=0.5, hspace=0.5)
        self.F2.axes1 = self.F2.fig.add_subplot(grid[0, 0:2])
        self.F2.axes1.set_title(title, fontsize=18)
        self.F2.axes1.plot(np.arange(len(data)), data, 'k.', markersize=2, alpha=0.8)  # 画散点
        self.F2.axes1.plot([0, len(data)], [cutoff, cutoff], color='steelblue', linewidth=3)  # 画蓝色的线
        self.F2.axes1.axis([0, 1.1 * len(data), data.min() - 3 * data.std(), data.max() + 3 * data.std()])
        for i in ['top', 'right']:
            self.F2.axes1.spines[i].set_visible(False)
        # plt.text(len(data)/2,data.max()-1*data.std(),'Hits',fontsize=20,
        #         verticalalignment='center',horizontalalignment='center',color='darkorange')
        self.F2.axes1.arrow(1.05 * len(data), cutoff + 0.5, 0, 2 * data.std(), width=15, head_length=data.std(),
                            fc='steelblue', ec='steelblue')
        self.F2.axes1.arrow(1.05 * len(data), cutoff, 0, -2 * data.std(), width=15, head_length=data.std(),
                            fc='darkorange', ec='darkorange')
        self.F2.axes1.set_xlabel('Compounds', fontsize=14)
        self.F2.axes1.set_ylabel('Robust Z-scores', fontsize=14)

        self.F2.axes2 = self.F2.fig.add_subplot(grid[0, 2])
        sort_data = np.sort(data)
        mu1, sigma1 = curve_fit(norm.cdf, sort_data, np.arange(len(data)) / len(data), p0=[0, 1])[0]
        t = np.linspace(sort_data[0], sort_data[-1], len(data))
        y = norm.cdf(t, mu1, sigma1)
        self.F2.axes2.plot(sort_data, y * len(data), color='steelblue')  # 拟合曲线（蓝色）
        self.F2.axes2.yaxis.set_label_position("right")
        self.F2.axes2.yaxis.tick_right()
        for i in ['top', 'left']:
            self.F2.axes2.spines[i].set_visible(False)
        self.F2.axes2.set_xlabel('Robust Z-score', fontsize=14)
        self.F2.axes2.set_ylabel('Values', fontsize=14)
        self.F2.axes2.step(sort_data, np.arange(len(data)) + 1, 'k-', linewidth=3.5, alpha=0.8)  #
        self.F2.axes2.axis([data.min(), data.max(), 0, len(data)])
        # 图像展示
        self.scene2 = QGraphicsScene()  # 创建一个场景
        self.scene2.addWidget(self.F2)  # 将图形元素添加到场景中
        self.graphicsView2_scatter.setScene(self.scene2)

    # 导入ms文件的功能（界面2）
    def import_ms2(self):
        file_dialog = QFileDialog()
        # 获得导入文件路径，用于后续操作
        self.ms_path2, _ = file_dialog.getOpenFileName(None, "Import MS File", "", "(*.xls *.xlsx)")
        if self.ms_path2 == '':
            pass
        else:
            self.msbrowser2.setText(f"{self.ms_path2.split('/')[-1]} imported.")
            self.msbrowser2.repaint()

    # 导入hcs文件的功能（界面2）
    def import_hcs2(self):
        file_dialog = QFileDialog()
        # 获得导入文件路径，用于后续操作
        self.hcs_path2, _ = file_dialog.getOpenFileName(None, "Import HCS File", "", "(*.xls *.xlsx)")
        if self.hcs_path2 == '':
            pass
        else:
            self.hcsbrowser2.setText(f"{self.hcs_path2.split('/')[-1]} imported.")
            self.hcsbrowser2.repaint()

    # 导出表格的功能（界面2）
    def export_table2(self):
        self.export_path2_1, type = QFileDialog.getSaveFileName(self, 'Export Table', '/', 'xlsx(*.xlsx)')
        if self.export_path2_1 == '':
            pass
        else:
            self.final_data.to_excel(self.export_path2_1, index=False)

            # 导出累积分布图的功能（界面2）

    def export_histagram2(self):
        self.export_path2_2, type = QFileDialog.getSaveFileName(self, 'Export Histogram', '/', 'png(*.png)')
        if self.export_path2_2 == '':
            pass
        else:
            # plot_hist([self.zscore_mzrt[self.feature],self.zscore_model[self.feature]],['treatment','model'],f'${self.feature}\ z\ scores$')
            self.F1.savefig(self.export_path2_2, dpi=300)

    # 导出散点图的功能（界面2）
    def export_scatter2(self):
        self.export_path2_3, type = QFileDialog.getSaveFileName(self, 'Export Scatter Plot', '/', 'png(*.png)')
        if self.export_path2_3 == '':
            pass
        else:
            # plot_scatter_curve([self.zscore_mzrt[self.feature],self.zscore_model[self.feature]],self.zscore_qtreshold,f'{self.feature} score')
            self.F2.savefig(self.export_path2_3, dpi=300)
#界面4窗口
class Window4(QWidget, Ui_Form4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle('Processing of Network')
        self.file_path1 = ""
        self.file_path2 = ""
        self.startbutton1.clicked.connect(self.start_process1)
        self.startbutton1.clicked.connect(self.start_process2)
        self.importbutton1.clicked.connect(self.import_file1)
        self.importbutton2.clicked.connect(self.import_file2)
        self.exportbutton1.clicked.connect(self.export_file1)
        self.exportbutton2.clicked.connect(self.export_file2)


    def import_file1(self):
        file_dialog = QFileDialog()
    # 获得导入文件路径，用于后续操作
        self.file_path1, _ = file_dialog.getOpenFileName(parent=None, caption="Import File1", directory="")
        if self.file_path1 == '':
            pass
        else:
            self.importbrowser1.setText(f"{self.file_path1.split('/')[-1]} imported.")
            self.importbrowser1.repaint()

    def import_file2(self):
        file_dialog = QFileDialog()
        # 获得导入文件路径，用于后续操作
        self.file_path2, _ = file_dialog.getOpenFileName(parent=None, caption="Import File2", directory="")
        if self.file_path2 == '':
            pass
        else:
            self.importbrowser2.setText(f"{self.file_path2.split('/')[-1]} imported.")
            self.importbrowser2.repaint()

    def start_process1(self):
        self.result1 = unite_mzrt1(self.file_path1)

        self.tableWidget1.setRowCount(self.result1.shape[0])
        self.tableWidget1.setColumnCount(self.result1.shape[1])
        self.tableWidget1.setHorizontalHeaderLabels(self.result1.columns)


        for row in range(self.result1.shape[0]):
            for column in range(self.result1.shape[1]):
                item = QTableWidgetItem(str(self.result1.iloc[row, column]))
                self.tableWidget1.setItem(row, column, item)
#
        self.result2 = unite_mzrt_Component(self.file_path1, self.file_path2)

        self.tableWidget2.setRowCount(self.result2.shape[0])
        self.tableWidget2.setColumnCount(self.result2.shape[1])
        self.tableWidget2.setHorizontalHeaderLabels(self.result2.columns)
        for row in range(self.result2.shape[0]):
            for column in range(self.result2.shape[1]):
                item = QTableWidgetItem(str(self.result2.iloc[row, column]))
                self.tableWidget2.setItem(row, column, item)

    def start_process2(self):
        try:
            connect_to_gephi(self.file_path1, self.file_path2)
        except Exception as e:
            self.exportbrowser2.setText(f"Error: {str(e)}")
            self.exportbrowser2.repaint()

    def export_file1(self):
        self.export_path1, types = QFileDialog.getSaveFileName(self, caption='Export file1', directory='/',
                                                               filter='*.xlsx')
        if self.export_path1 == '':
            pass
        else:
            self.result1.to_excel(self.export_path1, index=False)
            self.exportbrowser1.setText(f"Exported to {self.export_path1}")
            self.exportbrowser1.repaint()

    def export_file2(self):
        self.export_path2, types = QFileDialog.getSaveFileName(self, caption='Export file2', directory='/',
                                                               filter='*.xlsx')
        if self.export_path2 == '':
            pass
        else:
            self.result2.to_excel(self.export_path2, index=False)

            self.exportbrowser2.setText(f"Exported to {self.export_path2}")
            self.exportbrowser2.repaint()

# 主界面
class HelloWindow(QWidget, helloui):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.init_ui()

    def init_ui(self):
        # self.ui = uic.loadUi("hello_ui.ui")   # 加载ui文件
        self.setWindowTitle(
            'Activity annotation software for Complex chemical system and High-content images of TCMs V1.0')  # 主界面标题
        # self.setWindowIcon(QIcon('logo.ico'))   # 软件logo
        # self.ui.setWindowTitle('TCMs-CFA V1.0')
        # self.ui.setWindowIcon(QIcon('logo.ico'))   # 软件logo

        # self.window1Button = self.ui.pushButton
        # self.window1Button.clicked.connect(self.goWindow1)
        self.pushButton.clicked.connect(self.goWindow1)

        # self.window1Button = self.ui.pushButton_2
        # self.window1Button.clicked.connect(self.goWindow2)
        self.pushButton_2.clicked.connect(self.goWindow2)

        # self.window3Button = self.ui.pushButton_3
        # self.window3Button.clicked.connect(self.goWindow3)
        self.pushButton_3.clicked.connect(self.goWindow3)
        # self.window4Button = self.ui.pushButton_4
        # self.window4Button.clicked.connect(self.goWindow4)
        self.pushButton_4.clicked.connect(self.goWindow4)
        image_path = "E:\\project\\pythonProject2\\pyqt\\icon\\软件封面.jpg"
        pix = QPixmap(image_path)  # 封面图片
        # self.ui.label.setPixmap(pix)
        # self.ui.label.setScaledContents(True)
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)

    def goWindow1(self):
        self.switch_window1.emit()

    def goWindow2(self):
        self.switch_window2.emit()

    def goWindow3(self):
        self.switch_window3.emit()

    def goWindow4(self):
        self.switch_window4.emit()


# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass

    # 跳转到 hello 窗口
    def show_hello(self):
        self.hello = HelloWindow()
        self.hello.switch_window1.connect(self.show_window1)
        self.hello.switch_window2.connect(self.show_window2)
        self.hello.switch_window3.connect(self.show_window3)
        self.hello.switch_window4.connect(self.show_window4)
        self.hello.show()

    # 跳转到 window1 窗口, 不关闭原页面
    def show_window1(self):
        self.window1 = Window1()
        self.window1.show()

    # 跳转到 window2 窗口, 不关闭原页面
    def show_window2(self):
        self.window2 = Window2()
        self.window2.show()

    # 跳转到 window3 窗口, 不关闭原页面
    def show_window3(self):
        self.window3 = Window3()
        self.window3.show()

    # 跳转到 window4 窗口, 不关闭原页面
    def show_window4(self):
        self.window4 = Window4()
        self.window4.show()


class MyFigure(FigureCanvasQTAgg):
    def __init__(self, width=5, height=4, dpi=100):
        # 1、创建一个绘制窗口Figure对象
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 2、在父类中激活Figure窗口,同时继承父类属性
        super(MyFigure, self).__init__(self.fig)

    # 这里就是绘制图像、示例
    def plotSin(self, x, y):
        self.axes0 = self.fig.add_subplot(111)
        self.axes0.plot(x, y)

    def savefig(self, savepath, dpi=300):
        self.fig.savefig(savepath, dpi=dpi)

    # def savefig(self, savepath):
    #     self.fig.savefig(savepath, dpi=300)


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    controller = Controller()  # 控制器实例
    controller.show_hello()  # 默认展示的是 hello 页面
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# func.py代码
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.stats import ttest_ind
from scipy.optimize import curve_fit
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import PLSRegression

'''
section 2
'''


# 1：处理质谱数据
def process_ms_data(msdata_path):
    excel = pd.ExcelFile(msdata_path)

    data_pos = excel.parse(sheet_name=excel.sheet_names[0])
    data_neg = excel.parse(sheet_name=excel.sheet_names[1])

    data_pos['m/z, rt'] = data_pos['m/z'].apply(lambda x: str(x)) + ', ' + data_pos['RT'].apply(lambda x: str(x))
    data_neg['m/z, rt'] = data_neg['m/z'].apply(lambda x: str(x)) + ', ' + data_neg['RT'].apply(lambda x: str(x))

    data_mzrt = pd.concat([data_pos, data_neg])
    # 删除只有一个组分的m/z, rt
    mzrt_set = pd.Series(list(set(data_mzrt['m/z, rt'])))
    only_one_mz_mask = [len(data_mzrt.loc[data_mzrt['m/z, rt'] == mzrt]['fraction']) == 1 for mzrt in mzrt_set]
    data_mzrt.index = data_mzrt['m/z, rt']
    data_mzrt = data_mzrt.drop(mzrt_set.loc[only_one_mz_mask])
    data_mzrt.index = range(0, len(data_mzrt))

    # data_mzrt包括4列：RT m/z fraction m/z, rt
    return data_mzrt


# 2：处理高内涵数据，生成归一化后的数据（同时同一HQ数据合并）
def process_hcs_data(hcsdata_path):
    excel = pd.ExcelFile(hcsdata_path)
    ind = excel.parse(sheet_name=excel.sheet_names[0], index_col=0).index.tolist()

    # 获取drug_name（如HQ/BYD）
    for para in ind:
        alpha_para = "".join(list(filter(str.isalpha, para)))
        if alpha_para not in ('C', 'M', 'c', 'm'):
            drug_name = alpha_para
            break

    # 比较各参数的control组和model组的值大小，以此确定上调参数和下调参数
    datacs = []
    for s_n in excel.sheet_names:
        data = excel.parse(sheet_name=s_n, index_col=0)
        mask = [i for i in data.index if "".join(list(filter(str.isalpha, i))).upper() == 'C']
        datacs.append(data.loc[mask])
    datac = pd.concat(datacs)

    datapas = []
    for s_n in excel.sheet_names:
        data = excel.parse(sheet_name=s_n, index_col=0)
        mask = [i for i in data.index if "".join(list(filter(str.isalpha, i))).upper() == 'M']
        datapas.append(data.loc[mask])
    datapa = pd.concat(datapas)

    df1 = pd.DataFrame(datac.mean())
    df1.columns = ['c']
    df2 = pd.DataFrame(datapa.mean())
    df2.columns = ['pa']
    df = pd.merge(df1, df2, left_index=True, right_index=True)

    # 生成上调参数、下调参数和所有参数列表
    up_paras = df.loc[df['pa'] < df['c']].index.tolist()
    down_paras = df.loc[df['pa'] > df['c']].index.tolist()
    # all_paras = df.index.tolist()

    # 归一化操作
    normalize_datas = []
    for s_n in excel.sheet_names:
        data = excel.parse(sheet_name=s_n, index_col=0)
        data[up_paras] = (data[up_paras] - data[up_paras].min()) / (data[up_paras].max() - data[up_paras].min())
        data[down_paras] = (data[down_paras] - data[down_paras].max()) / (
                    data[down_paras].max() - data[down_paras].min())
        normalize_datas.append(data)
    normalize_data = pd.concat(normalize_datas)

    mask_c = [i for i in normalize_data.index if "".join(list(filter(str.isalpha, i))).upper() == 'C']
    normalize_datac = normalize_data.loc[mask_c]  # 所有control组归一化数据
    mask_pa = [i for i in normalize_data.index if "".join(list(filter(str.isalpha, i))).upper() == 'M']
    normalize_datapa = normalize_data.loc[mask_pa]  # 所有model组归一化数据
    mask_hq = [i for i in normalize_data.index if "".join(list(filter(str.isalpha, i))) == drug_name]
    normalize_datahq = normalize_data.loc[mask_hq]  # 所有HQ组归一化数据

    # 聚合同一组分的数据
    hq_list = [i.split('-')[0] for i in normalize_datahq.index]
    normalize_datahq[drug_name] = hq_list
    normalize_datahq = normalize_datahq.groupby(drug_name).mean()  # drug_name为normalize_datahq的index

    # 每列为一个参数（如ER1,ER2,ER3...），每行为一个hq/c/pa
    return normalize_datac, normalize_datapa, normalize_datahq


def get_features(normalize_datahq):
    # 根据列名提取参数，如：['LY', 'M', 'ER']
    features = []
    for para in normalize_datahq.columns:
        alpha_para = "".join(list(filter(str.isalpha, para)))
        features.append(alpha_para)
    features = list(set(features))

    while "Unnamed" in features:
        features.remove("Unnamed")

    return features


def calculate_mzrt_score(normalize_datahq, data_mzrt, features):
    score_mzrt = cal_score_by_mz(data_mzrt, normalize_datahq, features)
    # score_mzrt：每行为一个mzrt，每列为一种参数类别（如ER/M/LY）
    return score_mzrt


def calculate_control_and_model_score(normalize_datac, normalize_datapa, features):
    score_model = pd.DataFrame(
        np.array([normalize_datapa.loc[:, list(map(lambda x: feature in x, normalize_datapa.columns))].abs().sum(axis=1)
                  for feature in features]).T, index=normalize_datapa.index, columns=features)
    score_control = pd.DataFrame(
        np.array([normalize_datac.loc[:, list(map(lambda x: feature in x, normalize_datac.columns))].abs().sum(axis=1)
                  for feature in features]).T, index=normalize_datac.index, columns=features)

    # score_control：每行为一个C组数据，每列为一种参数类别（如ER/M/LY）
    # score_model：每行为一个M组数据，每列为一种参数类别（如ER/M/LY）
    return score_control, score_model


def calculate_zscore(score_control, score_model, score_mzrt, features):
    zscores_mzrt = []
    for feature in features:
        zscores_mzrt.append((score_mzrt[feature] - score_control[feature].mean()) / score_control[feature].std())
    zscore_mzrt = pd.concat(zscores_mzrt, axis=1, ignore_index=False)

    zscores_model = []
    for feature in features:
        zscores_model.append((score_model[feature] - score_control[feature].mean()) / score_control[feature].std())
    zscore_model = pd.concat(zscores_model, axis=1, ignore_index=False)

    zscores_control = []
    for feature in features:
        zscores_control.append((score_control[feature] - score_control[feature].mean()) / score_control[feature].std())
    zscore_control = pd.concat(zscores_control, axis=1, ignore_index=False)

    # zscore_mzrt：每行为一个mzrt，每列为一种参数类别（如ER/M/LY）
    # zscore_control：每行为一个C组数据，每列为一种参数类别（如ER/M/LY）
    # zscore_model：每行为一个M组数据，每列为一种参数类别（如ER/M/LY）
    return zscore_control, zscore_model, zscore_mzrt


def calculate_cluster_score(data_mzrt, normalize_datahq):
    drug_name = normalize_datahq.index.name
    mzrt_set = list(set(data_mzrt['m/z, rt']))
    number_matrix_by_mzrt = [
        map(lambda x: drug_name + str(x), list(data_mzrt.loc[data_mzrt['m/z, rt'] == mzrt]['fraction']))
        for mzrt in mzrt_set]
    cluster_score_list = []
    for number_list in number_matrix_by_mzrt:
        corr_matrix = normalize_datahq.loc[number_list].T.corr()
        j = len(corr_matrix)
        if j != 1:
            cluster_score = (corr_matrix.apply(lambda x: x ** 3).sum().sum() - j) / (j ** 2 - j)
        else:
            cluster_score = 1
        cluster_score_list.append(cluster_score)
    cluster_score_mzrt = pd.DataFrame(cluster_score_list, index=mzrt_set, columns=['cluster_score'])
    # cluster_score_mzrt：每行为一个mzrt，只有一列cluster_score
    return cluster_score_mzrt


def make_final_data(zscore_mzrt, cluster_score_mzrt, data_mzrt, features, zscore_qthreshold=0.5, cluster_threshold=0.7):
    final_data = pd.concat([zscore_mzrt, cluster_score_mzrt], axis=1, ignore_index=False)
    col_zufen = [",".join(map(lambda x: str(x), sorted(list(data_mzrt.loc[data_mzrt['m/z, rt'] == mzrt]['fraction']))))
                 for mzrt in final_data.index]
    final_data['fraction'] = col_zufen
    final_data.reset_index(inplace=True)
    final_data.rename(columns={"index": "m/z, rt"}, inplace=True)

    # for feature in features:
    #     final_data.rename(columns={feature: "zscore_"+feature}, inplace=True)

    # 根据阈值进行筛选：
    # 确定各参数zscore具体阈值
    zscore_thresholds = []
    for feature in features:
        zscore_threshold = zscore_mzrt[feature].quantile(q=zscore_qthreshold)
        zscore_thresholds.append(zscore_threshold)

    # 根据各参数zscore阈值与簇值阈值生成条件查询语句
    query_sentences = []
    for i in range(len(features)):
        query_sentences.append(f"{features[i]}>={zscore_thresholds[i]}")
    query_sentences.append(f"cluster_score>={cluster_threshold}")
    query = "&".join(query_sentences)

    # 根据条件进行筛选
    final_data = final_data.query(query)

    # final_data包含列：m/z, rt，若干个feature，cluster_score，fraction
    return final_data


# 函数中的函数
# 计算各mz的得分的函数
def cal_score_by_mz(data_mzrt, data_high_number, features):
    drug_name = data_high_number.index.name
    mzrt_set = list(set(data_mzrt['m/z, rt']))
    score_by_mz = []
    for i in mzrt_set:
        number_by_mz = list(map(lambda x: str(x), list(data_mzrt.loc[data_mzrt['m/z, rt'] == i]['fraction'])))
        HQ_number_by_mz = [drug_name + str(x) for x in number_by_mz]
        data_per_mz = data_high_number.loc[HQ_number_by_mz].abs().sum() / len(number_by_mz)
        # 合并同一mz的组分的数据（方式：求绝对值平均）
        score_per_mz = [data_per_mz.loc[list(map(lambda x: feature in x, data_high_number.columns))].sum()
                        for feature in features]  # 合并列参数数据（方式：求和）
        score_by_mz.append(score_per_mz)
    return pd.DataFrame(score_by_mz, index=mzrt_set, columns=features)


'''
section 1
处理m/z rt的函数
'''


def get_mzrt(file_path):
    excel = pd.ExcelFile(file_path)
    result = pd.DataFrame(columns=['RT', 'm/z', 'fraction'])

    for sheet_name in excel.sheet_names:
        df = excel.parse(sheet_name=sheet_name)
        row_num = df.shape[0]
        for r in range(row_num):
            rt = df.loc[r, 'RT']
            mz = df.loc[r, 'm/z']
            # 组分：提取sheet_name中的数字部分
            zufen = "".join(list(filter(str.isdigit, sheet_name)))
            zufen = int(zufen)

            # 第一行直接添加
            if result.shape[0] == 0:
                result.loc[0] = [rt, mz, zufen]

            # 先判断是否与现有rtmz相符合
            else:
                new_flag = 1
                for i in range(result.shape[0]):
                    compare_rt = result.loc[i, 'RT']
                    compare_mz = result.loc[i, 'm/z']
                    # 若与现有mzrt相似，则添加现有的mzrt
                    if rt <= compare_rt + 0.5 and rt >= compare_rt - 0.5 and mz <= compare_mz + 2 and mz >= compare_mz - 2:
                        new_flag = 0
                        result.loc[result.shape[0]] = [compare_rt, compare_mz, zufen]
                        break

                # 若不与现有mzrt相似，则添加新的mzrt
                if new_flag == 1:
                    result.loc[result.shape[0]] = [rt, mz, zufen]

    result2 = result.drop_duplicates()
    return result2


'''
section 2
'''


def get_results(filepath):
    df = pd.read_excel(filepath, index_col=0)
    mask = [i for i in df.index if "".join(list(filter(str.isalpha, i))).upper() in ('C', 'M')]
    df = df.loc[mask]
    params = df.columns.tolist()

    X = df.values
    X = StandardScaler().fit_transform(X)
    cat = ["Control" if i[0].upper() == 'C' else "Model" for i in mask]
    cat_01 = [0 if i[0].upper() == 'C' else 1 for i in mask]

    # 获取pca矩阵
    pca = PCA()  # 返回满足主成分方差累计贡献率达到98%的主成分
    X_pca = pca.fit_transform(X)

    # 获取plsda矩阵
    plsda = PLSRegression()
    plsda.fit(X, cat_01)
    X_plsda = np.array(plsda.x_scores_)

    # 获取vip值大于1对应的参数
    list_vip = Cal_VIP(plsda)
    vip_gt_1 = []
    for i, vip in enumerate(list_vip):
        if vip > 1:
            vip_gt_1.append(params[i])

    return X_pca, X_plsda, cat, vip_gt_1, list_vip


def ttest_table(filepath, list_vip):
    df = pd.read_excel(filepath, index_col=0)
    mask = [i for i in df.index if "".join(list(filter(str.isalpha, i))).upper() in ('C', 'M')]
    df = df.loc[mask]
    params = df.columns.tolist()

    cat = ["Control" if i[0].upper() == 'C' else "Model" for i in mask]
    df['group'] = cat

    p_vals = []
    for i in range(len(df.columns) - 1):
        sample_control = df[df['group'] == 'Control'][df.columns[i]].tolist()
        sample_model = df[df['group'] == 'Model'][df.columns[i]].tolist()
        tstat, pval = ttest_ind(a=sample_control, b=sample_model, alternative="two-sided")
        p_vals.append(pval)

    df = df.groupby('group').agg(['mean', 'std'])
    df = df.T
    mean_mask = [i for i in range(0, df.shape[0] - 1, 2)]
    std_mask = [i for i in range(1, df.shape[0] + 1, 2)]
    mean_matrix = df.values[[mean_mask], :]
    std_matrix = df.values[[std_mask], :]
    matrix = np.concatenate((mean_matrix[0], std_matrix[0]), axis=1)
    df2 = pd.DataFrame(matrix, columns=['Control_mean', 'Model_mean', 'Control_std', 'Model_std'])
    df2['P-Value(T-test)'] = p_vals
    df2.insert(loc=0, column='Parameter', value=params)
    df2['VIP'] = list_vip
    # df2包括7列：Parameter/Control_mean/Model_mean/Control_std/Model_std/P-Value(T-test)/VIP
    return df2


def Cal_VIP(model):
    t = model.x_scores_
    w = model.x_weights_
    q = model.y_loadings_
    p, h = w.shape
    vips = np.zeros((p,))
    s = np.diag(np.matmul(np.matmul(np.matmul(t.T, t), q.T), q)).reshape(h, -1)
    # s = np.diag(t.T @ t @ q.T @ q).reshape(h, -1)  # @表示矩阵相乘
    total_s = np.sum(s)
    for i in range(p):
        weight = np.array([(w[i, j] / np.linalg.norm(w[:, j])) ** 2 for j in range(h)])
        vips[i] = np.sqrt(p * (np.matmul(s.T, weight)) / total_s)
    return vips


# 用于单独保存子图的函数
def save_subfig(fig, ax, save_path, fig_name):
    bbox = ax.get_tightbbox(fig.canvas.get_renderer()).expanded(1.02, 1.02)
    extent = bbox.transformed(fig.dpi_scale_trans.inverted())
    fig.savefig(save_path + '/' + fig_name, bbox_inches=extent, dpi=300)

'''
section 4
'''
from gephistreamer import graph
from gephistreamer import streamer
def unite_mzrt1(file_path1):
    excel = pd.ExcelFile(file_path1)
    result_data1 = []

    for sheet_name in excel.sheet_names:
        df = excel.parse(sheet_name=0)
        row_num = df.shape[0]
        for r in range(row_num):
            rt = df.loc[r, 'RT']
            mz = df.loc[r, 'm/z']
            rt_mz = f"{rt},{mz}"
            # 组分：提取sheet_name中的数字部分
            fraction = df.loc[r, "fraction"]
            try:
                fraction = int(fraction)
            except ValueError:
                # 如果转换失败，可以设置为 None 或者其他默认值
                fraction = None
            # 添加
            result_data1.append({'RT,m/z': rt_mz, 'fraction': fraction})
    result = pd.DataFrame(result_data1, columns=['RT,m/z', 'fraction'])
    result2 = result.drop_duplicates()
    return result2

def unite_mzrt_Component(file_path1, file_path2):
    excel_1 = pd.ExcelFile(file_path1)
    excel_2 = pd.ExcelFile(file_path2)
    result_data = []

    for sheet_name in excel_1.sheet_names:
        if sheet_name in excel_2.sheet_names:
            df = excel_1.parse(sheet_name=sheet_name)
            de = excel_2.parse(sheet_name=sheet_name)
            # print(df)
            # print(de)
            row_num1 = df.shape[0]
            row_num2 = de.shape[0]
            for r in range(row_num1):
                rt = df.loc[r, 'RT']
                mz = df.loc[r, 'm/z']
                rt_mz = f"{rt},{mz}"
                fraction = df.loc[r, "fraction"]
                try:
                    fraction = int(fraction)
                except ValueError:
                    fraction = None
                found = False  # 标记是否找到匹配项
                for j in range(row_num2):
                    component = de.loc[j, "Component"]
                    compare_rt = de.loc[j, "RT"]
                    compare_mz = de.loc[j, "m/z"]
                    if rt == compare_rt and mz == compare_mz:
                        result_data.append({'RT,m/z': rt_mz, 'fraction': fraction, "Component": component})
                        found = True  # 找到匹配项
                        break  # 跳出内部循环

                if not found:  # 如果没有找到匹配项
                    result_data.append({'RT,m/z': rt_mz, 'fraction': fraction, "Component": ""})

    if result_data:
        result = pd.DataFrame(result_data, columns=['RT,m/z', 'fraction', 'Component'])
        result2 = result.drop_duplicates()
        result2.fillna('', inplace=True)
        return result2
    else:
        return pd.DataFrame(columns=['RT,m/z', 'fraction', 'Component'])

def connect_to_gephi(file_path1, file_path2):
    result = unite_mzrt_Component(file_path1, file_path2)
    df = result
    row1 = df.shape[0]
    stream = streamer.Streamer(streamer.GephiREST(hostname="localhost", port=8080, workspace="workspace0"))
    for i in range(row1):
        rt_mz = str(df.loc[i, "RT,m/z"])
        fraction = str(df.loc[i, "fraction"])
        component = str(df.loc[i, "Component"])
        if component != "":
            node_A = graph.Node(fraction)
            node_B = graph.Node(component)
            node_C = graph.Node(rt_mz)
            stream.add_node(node_A, node_B, node_C)
            edge_AC = graph.Edge(node_A, node_C)
            edge_BC = graph.Edge(node_B, node_C)
            stream.add_edge(edge_AC, edge_BC)
        else:
            node_A = graph.Node(fraction)
            node_C = graph.Node(rt_mz)
            stream.add_node(node_A, node_C)
            edge_AC = graph.Edge(node_A, node_C)
            stream.add_edge(edge_AC)
    stream = streamer.Streamer(streamer.GephiREST(), auto_commit=False)
    stream.commit()
# hello_ui.py代码
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets





# window1.py代码
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


