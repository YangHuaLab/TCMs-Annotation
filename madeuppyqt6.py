from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
# from window4 import Ui_Form as windowui
import pandas as pd
from gephistreamer import graph
from gephistreamer import streamer
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
class Window4(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.file_path1 = ""
        self.file_path2 = ""
        self.startbutton1.clicked.connect(self.start_process1)
        self.startbutton1.clicked.connect(self.start_process2)
        self.importbutton1.clicked.connect(self.import_file1)
        self.importbutton2.clicked.connect(self.import_file2)
        self.exportbutton1.clicked.connect(self.export_file1)
        self.exportbutton2.clicked.connect(self.export_file2)
        self.init_ui()
    def init_ui(self):
#界面4标题
#_self.ui = uic.loadUi("window.ui")##tuix#
        self.setWindowTitle('Processing of Network')
#软件Logo
# self.setWindowIcon(QIcon('logo.ico'))
#导入按钮
#

# self.setWindowIcon(QIcon('logo.ico'))  # 软件Logo

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
        connect_to_gephi(self.file_path1, self.file_path2)

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window4()
    window.show()
    sys.exit(app.exec())