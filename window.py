from PyQt6 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(994, 563)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 331, 211))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
#导出按钮1
        self.exportbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.exportbutton1.setObjectName("exportbutton1")
        self.gridLayout_3.addWidget(self.exportbutton1, 7, 0, 1, 1)
#导出按钮2
        self.exportbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.exportbutton2.setObjectName("exportbutton2")
        self.gridLayout_3.addWidget(self.exportbutton2, 8, 0, 1, 1)
#导入按钮1
        self.importbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.importbutton1.setObjectName("importbutton1")
        self.gridLayout_3.addWidget(self.importbutton1, 0, 0, 1, 1)
#导入按钮2
        self.importbutton2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.importbutton2.setObjectName("importbutton2")
        self.gridLayout_3.addWidget(self.importbutton2, 1, 0, 1, 1)
#导入文本1
        self.importbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.importbrowser1.setObjectName("importbrowser1")
        self.gridLayout_3.addWidget(self.importbrowser1, 0, 1, 1, 1)
#导入文本2
        self.importbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.importbrowser2.setObjectName("importbrowser2")
        self.gridLayout_3.addWidget(self.importbrowser2, 1, 1, 1, 1)
#导出文本1
        self.exportbrowser1 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.exportbrowser1.setObjectName("exportbrowser1")
        self.gridLayout_3.addWidget(self.exportbrowser1, 7, 1, 1, 1)
#导出文本2
        self.exportbrowser2 = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.exportbrowser2.setObjectName("exportbrowser2")
        self.gridLayout_3.addWidget(self.exportbrowser2, 8, 1, 1, 1)
#开始按钮
        self.startbutton1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.startbutton1.setObjectName("startbutton1")
        self.gridLayout_3.addWidget(self.startbutton1, 2, 0, 1, 2)
#导入QTabWidget控件窗口
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(358, 10, 1011, 541))
        self.tabWidget.setObjectName("tabWidget")
#创建标签页1
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
#往标签页1添加表格1
        self.tableWidget1 = QtWidgets.QTableWidget(self.tab1)
        self.tableWidget1.setGeometry(QtCore.QRect(10, 10, 550, 551))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.tabWidget.addTab(self.tab1, "Unite1")
#创建标签页2
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
#创建表格2添加到标签页2
        self.tableWidget2 = QtWidgets.QTableWidget(self.tab2)
        self.tableWidget2.setGeometry(QtCore.QRect(10, 10, 550, 551))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
#放置控件窗口
        self.tabWidget.addTab(self.tab2, "Unite2")
# #创建标签页3
#         self.tab3 = QtWidgets.QWidget()
#         self.tab3.setObjectName("picture3")
# #创建图形视图控件并添加到第三个标签页
#         self.graphicsView_pca = QtWidgets.QGraphicsView(self.tab3)
#         self.graphicsView_pca.setGeometry(QtCore.QRect(10, 10, 550, 551))
#         self.graphicsView_pca.setObjectName("graphicsView_pca")
# #放置控件窗口
#         self.tabWidget.addTab(self.tab3, "Unite3")
#         self.retranslateUi(Form)
#         self.tabWidget.setCurrentIndex(2)
#         QtCore.QMetaObject.connectSlotsByName(Form)

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
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), _translate("Form", "Picture"))