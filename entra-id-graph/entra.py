from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import matplotlib.pylab as plt
import pandas as pd
import sys
import csv

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 293)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setGeometry(QtCore.QRect(20, 10, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.top_frame.setFont(font)
        self.top_frame.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.top_label = QtWidgets.QLabel(self.top_frame)
        self.top_label.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.top_label.setFont(font)
        self.top_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_label.setObjectName("top_label")
        self.load_csv_pushButton = QtWidgets.QPushButton(self.top_frame, clicked = lambda: self.open_csv())
        self.load_csv_pushButton.setGeometry(QtCore.QRect(440, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.load_csv_pushButton.setFont(font)
        self.load_csv_pushButton.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.load_csv_pushButton.setObjectName("load_csv_pushButton")
        self.loaded_csv_label = QtWidgets.QLabel(self.top_frame)
        self.loaded_csv_label.setGeometry(QtCore.QRect(160, 10, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.loaded_csv_label.setFont(font)
        self.loaded_csv_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loaded_csv_label.setText("")
        self.loaded_csv_label.setObjectName("loaded_csv_label")
        self.bottom_frame = QtWidgets.QFrame(self.centralwidget)
        self.bottom_frame.setGeometry(QtCore.QRect(20, 70, 591, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bottom_frame.setFont(font)
        self.bottom_frame.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.x_axis_selection_label = QtWidgets.QLabel(self.bottom_frame)
        self.x_axis_selection_label.setGeometry(QtCore.QRect(20, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_axis_selection_label.setFont(font)
        self.x_axis_selection_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.x_axis_selection_label.setObjectName("x_axis_selection_label")
        self.y_axis_selection_label = QtWidgets.QLabel(self.bottom_frame)
        self.y_axis_selection_label.setGeometry(QtCore.QRect(20, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.y_axis_selection_label.setFont(font)
        self.y_axis_selection_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.y_axis_selection_label.setObjectName("y_axis_selection_label")
        self.x_axis_name_label = QtWidgets.QLabel(self.bottom_frame)
        self.x_axis_name_label.setGeometry(QtCore.QRect(330, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.x_axis_name_label.setFont(font)
        self.x_axis_name_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.x_axis_name_label.setObjectName("x_axis_name_label")
        self.y_axis_name_label = QtWidgets.QLabel(self.bottom_frame)
        self.y_axis_name_label.setGeometry(QtCore.QRect(330, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.y_axis_name_label.setFont(font)
        self.y_axis_name_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.y_axis_name_label.setObjectName("y_axis_name_label")
        self.x_axis_comboBox = QtWidgets.QComboBox(self.bottom_frame)
        self.x_axis_comboBox.setEnabled(False)
        self.x_axis_comboBox.setGeometry(QtCore.QRect(150, 70, 151, 22))
        self.x_axis_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_axis_comboBox.setObjectName("x_axis_comboBox")
        self.y_axis_comboBox = QtWidgets.QComboBox(self.bottom_frame)
        self.y_axis_comboBox.setEnabled(False)
        self.y_axis_comboBox.setGeometry(QtCore.QRect(150, 100, 151, 22))
        self.y_axis_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_axis_comboBox.setObjectName("y_axis_comboBox")
        self.graph__label = QtWidgets.QLabel(self.bottom_frame)
        self.graph__label.setGeometry(QtCore.QRect(20, 40, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.graph__label.setFont(font)
        self.graph__label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.graph__label.setObjectName("graph__label")
        self.graph_type_comboBox = QtWidgets.QComboBox(self.bottom_frame)
        self.graph_type_comboBox.setEnabled(False)
        self.graph_type_comboBox.setGeometry(QtCore.QRect(150, 40, 151, 22))
        self.graph_type_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_type_comboBox.setObjectName("graph_type_comboBox")
        self.graph_type_comboBox.addItems([
            "line",
            "bar",
            "scatter",
            "hist",
            "box"
        ])
        self.x_axis_lineEdit = QtWidgets.QLineEdit(self.bottom_frame)
        self.x_axis_lineEdit.setEnabled(False)
        self.x_axis_lineEdit.setGeometry(QtCore.QRect(410, 70, 161, 20))
        self.x_axis_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x_axis_lineEdit.setObjectName("x_axis_lineEdit")
        self.y_axis_lineEdit = QtWidgets.QLineEdit(self.bottom_frame)
        self.y_axis_lineEdit.setEnabled(False)
        self.y_axis_lineEdit.setGeometry(QtCore.QRect(410, 100, 161, 20))
        self.y_axis_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y_axis_lineEdit.setObjectName("y_axis_lineEdit")
        self.graph_name_label = QtWidgets.QLabel(self.bottom_frame)
        self.graph_name_label.setGeometry(QtCore.QRect(20, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.graph_name_label.setFont(font)
        self.graph_name_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.graph_name_label.setObjectName("graph_name_label")
        self.graph_name_lineEdit = QtWidgets.QLineEdit(self.bottom_frame)
        self.graph_name_lineEdit.setEnabled(False)
        self.graph_name_lineEdit.setGeometry(QtCore.QRect(150, 10, 151, 20))
        self.graph_name_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_name_lineEdit.setObjectName("graph_name_lineEdit")
        self.save_to_graph_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plot_to_graph())
        self.save_to_graph_pushButton.setEnabled(False)
        self.save_to_graph_pushButton.setGeometry(QtCore.QRect(480, 220, 111, 31))
        self.save_to_graph_pushButton.setObjectName("save_to_csvpushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graph_type_comboBox.currentIndexChanged.connect(self.validate_input)
        self.x_axis_comboBox.currentIndexChanged.connect(self.validate_input)
        self.y_axis_comboBox.currentIndexChanged.connect(self.validate_input)
        self.graph_name_lineEdit.textChanged.connect(self.validate_input)
        self.x_axis_lineEdit.textChanged.connect(self.validate_input)
        self.y_axis_lineEdit.textChanged.connect(self.validate_input)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CSV Plotter"))
        self.top_label.setText(_translate("MainWindow", "CSV Plotter"))
        self.load_csv_pushButton.setText(_translate("MainWindow", "Load CSV"))
        self.x_axis_selection_label.setText(_translate("MainWindow", "X Axis:"))
        self.y_axis_selection_label.setText(_translate("MainWindow", "Y Axis:"))
        self.x_axis_name_label.setText(_translate("MainWindow", "Label:"))
        self.y_axis_name_label.setText(_translate("MainWindow", "Label:"))
        self.graph__label.setText(_translate("MainWindow", "Graph type:"))
        self.graph_name_label.setText(_translate("MainWindow", "Graph name:"))
        self.save_to_graph_pushButton.setText(_translate("MainWindow", "Plot to graph"))

### Functions:

    def validate_input(self):
        all_fields_valid = (
            self.graph_type_comboBox.currentText().strip() != "" and
            self.x_axis_comboBox.currentText().strip() != "" and
            self.y_axis_comboBox.currentText().strip() != "" and
            self.graph_name_lineEdit.text().strip() != "" and
            self.x_axis_lineEdit.text().strip() != "" and
            self.y_axis_lineEdit.text().strip() != ""
        )
        self.save_to_graph_pushButton.setEnabled(all_fields_valid)

    def open_csv(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Open CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
            options = options
        )
        if filename:
            try:
                self.statusbar.showMessage(f"File loaded: {filename}")
                self.graph_name_lineEdit.setEnabled(True)
                self.graph_name_lineEdit.clear()
                self.graph_type_comboBox.setEnabled(True)
                self.x_axis_lineEdit.setEnabled(True)
                self.x_axis_lineEdit.clear()
                self.y_axis_lineEdit.setEnabled(True)
                self.y_axis_lineEdit.clear()
                self.x_axis_comboBox.setEnabled(True)
                self.y_axis_comboBox.setEnabled(True)
                self.df = pd.read_csv(filename)
                headers = self.df.columns.tolist()
                for h in headers:
                    self.x_axis_comboBox.addItem(h)
                    self.y_axis_comboBox.addItem(h)
            except Exception as e:
                QMessageBox.critical(None, "Import failed", f"An error occured:\n{str(e)}")

    def plot_to_graph(self):
        graph_name = self.graph_name_lineEdit.text()
        graph_type = self.graph_type_comboBox.currentText()
        x_axis = self.x_axis_comboBox.currentText()
        y_axis = self.y_axis_comboBox.currentText()
        x_label = self.x_axis_lineEdit.text()
        y_label = self.y_axis_lineEdit.text()

        try:
            plot_func = getattr(self.df.plot, graph_type)
            ax = plot_func(x = x_axis, y = y_axis)
            ax.set_xlabel(x_label)
            ax.set_label(y_label)
            ax.set_title(graph_name)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            plt.show()
        except Exception as e:
            QMessageBox.critical(None, "Plotting failed", f"An error occured:\n{str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())