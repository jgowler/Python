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
        MainWindow.resize(623, 287)
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
        font.setPointSize(8)
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
            "Line Plot",
            "Bar Plot",
            "Scatter Plot",
            "Histogram",
            "Box Plot"
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
        self.graph_template_label = QtWidgets.QLabel(self.bottom_frame)
        self.graph_template_label.setGeometry(QtCore.QRect(330, 10, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.graph_template_label.setFont(font)
        self.graph_template_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.graph_template_label.setObjectName("graph_template_label")
        self.graph_template_comboBox = QtWidgets.QComboBox(self.bottom_frame)
        self.graph_template_comboBox.setEnabled(False)
        self.graph_template_comboBox.setGeometry(QtCore.QRect(330, 40, 241, 22))
        self.graph_template_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_template_comboBox.setObjectName("graph_template_comboBox")
        self.graph_template_comboBox.addItems([
            "",
            "Login Success vs Failure Count",
            "Login Activity Over Time",
            "Sign-ins by Location",
            "Top Users by Sign-in Count",
            "Sign-ins by Client App",
            "Authentication Type Breakdown",
            "Failed sign-in reasons"
        ])
        self.save_to_graph_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plot_to_graph())
        self.save_to_graph_pushButton.setEnabled(False)
        self.save_to_graph_pushButton.setGeometry(QtCore.QRect(480, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.save_to_graph_pushButton.setFont(font)
        self.save_to_graph_pushButton.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.save_to_graph_pushButton.setObjectName("save_to_graph_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graph_template_comboBox.currentIndexChanged.connect(self.graph_template_selection)
        self.graph_name_lineEdit.textChanged.connect(self.validate_input)
        self.x_axis_lineEdit.textChanged.connect(self.validate_input)
        self.y_axis_lineEdit.textChanged.connect(self.validate_input)
        self.x_axis_comboBox.currentIndexChanged.connect(self.validate_input)
        self.y_axis_comboBox.currentIndexChanged.connect(self.validate_input)
        self.graph_type_comboBox.currentIndexChanged.connect(self.validate_input)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graph Creator"))
        self.top_label.setText(_translate("MainWindow", "Graph Creator"))
        self.load_csv_pushButton.setText(_translate("MainWindow", "Load CSV"))
        self.x_axis_selection_label.setText(_translate("MainWindow", "X Axis Column"))
        self.y_axis_selection_label.setText(_translate("MainWindow", "Y Axis Column"))
        self.x_axis_name_label.setText(_translate("MainWindow", "X Axis Name"))
        self.y_axis_name_label.setText(_translate("MainWindow", "Y Axis Name"))
        self.graph__label.setText(_translate("MainWindow", "Graph Type"))
        self.graph_name_label.setText(_translate("MainWindow", "Graph Name"))
        self.graph_template_label.setText(_translate("MainWindow", "Graph Template"))
        self.save_to_graph_pushButton.setText(_translate("MainWindow", "Plot Graph"))

### Functions:

    def validate_input(self):
        all_fields_valid = (
            self.graph_name_lineEdit.text().strip() != "" and
            self.x_axis_lineEdit.text().strip() != "" and
            self.y_axis_lineEdit.text().strip() != "" and
            self.x_axis_comboBox.currentText().strip() != "" and
            self.y_axis_comboBox.currentText().strip() != "" and
            self.graph_type_comboBox.currentText().strip() != ""
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
                self.graph_template_comboBox.setEnabled(True)
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
        if not hasattr(self, "df") or self.df.empty:
            QMessageBox.warning(None, "No Data", "Please load a valid CSV file first.")
            return

        template_select = self.graph_template_comboBox.currentText().strip()

        if template_select == "":
            graph_type = self.graph_type_comboBox.currentText().strip()
            x_axis = self.x_axis_comboBox.currentText().strip()
            y_axis = self.y_axis_comboBox.currentText().strip()
            graph_name = self.graph_name_lineEdit.text().strip()
            x_label = self.x_axis_lineEdit.text().strip()
            y_label = self.y_axis_lineEdit.text().strip()

            if graph_type == "Line Plot":
                self.df.plot(x=x_axis, y=y_axis, kind="line")
            elif graph_type == "Bar Plot":
                self.df.plot(x=x_axis, y=y_axis, kind="bar")
            elif graph_type == "Scatter Plot":
                self.df.plot(x=x_axis, y=y_axis, kind="scatter")
            elif graph_type == "Histogram":
                self.df.plot(y=y_axis, kind="hist")
            elif graph_type == "Box Plot":
                self.df.plot(y=y_axis, kind="box")
            else:
                QMessageBox.warning(None, "Unknown Graph Type", f"Graph type '{graph_type}' is not recognized.")
                return
            ax = plt.gca()
            ax.set_title(graph_name)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.tick_params(axis='x', labelrotation=45)
            plt.tight_layout()
            plt.subplots_adjust(bottom=0.25)
            plt.show()
        else:
            try:
                if template_select == "Login Success vs Failure Count":
                    self.plot_login_success_failure(self.df)
                elif template_select == "Login Activity Over Time":
                    self.plot_signins_over_time(self.df)
                elif template_select == "Top Users by Sign-in Count":
                    self.plot_top_users(self.df)
                elif template_select == "Sign-ins by Location":
                    self.plot_signins_by_location(self.df)
                elif template_select == "Sign-ins by Client App":
                    self.plot_signins_by_client_app(self.df)
                elif template_select == "Authentication Type Breakdown":
                    self.plot_auth_type_breakdown(self.df)
                elif template_select == "Failed sign-in reasons":
                    self.failed_sign_in_reasons(self.df)
                else:
                    QMessageBox.warning(None, "Unknown Template", f"The selected template '{template_select}' is not recognized.")
            except Exception as e:
                QMessageBox.critical(None, "Plotting failed", f"An error occurred:\n{str(e)}")

    def plot_login_success_failure(self, df):
        if 'Status' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Status' not found in data.")
            return

        counts = df['Status'].dropna().value_counts()
        colors = ['green' if 'success' in status.lower() else 'red' for status in counts.index]

        counts.plot(kind='bar', color=colors)
        plt.title("Login Success vs Failure Count")
        plt.xlabel("Status")
        plt.ylabel("Count")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.show()

    def plot_signins_over_time(self, df):
        if 'Date (UTC)' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Date (UTC)' not found in data.")
            return

        df['Date (UTC)'] = pd.to_datetime(df['Date (UTC)'], errors='coerce')
        if df['Date (UTC)'].isnull().all():
            QMessageBox.warning(None, "Date Parse Error", "Could not parse any timestamps from 'Date (UTC)'.")
            return

        counts = df['Date (UTC)'].dt.date.value_counts().sort_index()
        counts.plot(kind='line', marker='o')
        plt.title("Sign-ins Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sign-in Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_top_users(self, df):
        if 'Username' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Username' not found in data.")
            return

        top_users = df['Username'].dropna().value_counts().head(10)
        top_users.plot(kind='bar')
        plt.title("Top Users by Sign-in Count")
        plt.xlabel("Username")
        plt.ylabel("Sign-in Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_signins_by_location(self, df):
        if 'Location' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Location' not found in data.")
            return

        df = df.dropna(subset=['Location', 'Status'])
        df['Status'] = df['Status'].str.strip().str.lower()
        df['Location'] = df['Location'].str.strip()
        # Group by location and size
        grouped = df.groupby(['Location', 'Status']).size().unstack(fill_value=0)
        top_locations = grouped.sum(axis=1).nlargest(10).index
        grouped_top = grouped.loc[top_locations]

        ax = grouped_top.plot(kind='bar', stacked=False, color=['green', 'red'])
        ax.set_title("Sign-ins by Location and Status")
        ax.set_xlabel("Location")
        ax.set_ylabel("Sign-in Count")
        ax.tick_params(axis='x', labelrotation=45)
        plt.tight_layout()
        plt.subplots_adjust(bottom=0.25)  # Prevent label cutoff
        plt.legend(title="Status")
        plt.show()

    def failed_sign_in_reasons(self, df):
        if 'Failure reason' not in df.columns:
            QMessageBox.warning(None, "Missing data", "Column 'Failure reason' not found in data")
            return
        
        reason = df['Failure reason'].dropna().value_counts().head(10)
        df['Status'] = df['Status'].str.strip().str.lower()
        failed_df = df[df['Status'] == 'failure']  # note lowercase if you're stripping and lowering status
        reason_count = failed_df['Failure reason'].value_counts()

        reason_count.plot(kind='bar', color='red')
        plt.title('Failed sign-in reasons')
        plt.xlabel("Failure reasons")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_signins_by_client_app(self, df):
        if 'Client app' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Client app' not found in data.")
            return

        app_counts = df['Client app'].dropna().value_counts().head(10)
        app_counts.plot(kind='bar')
        plt.title("Sign-ins by Client App")
        plt.xlabel("Client App")
        plt.ylabel("Sign-in Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_auth_type_breakdown(self, df):
        if 'Multifactor authentication auth method' not in df.columns:
            QMessageBox.warninf(None, "MIssing Data", "Column 'Multifactor authentication auth method' not found in data.")
            return
        mfa_counts = df['Multifactor authentication auth method'].dropna().value_counts().head(10)
        mfa_counts.plot(kind='bar')
        plt.title("Authentication Type Breakdown")
        plt.xlabel('Authentication Type Breakdown')
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def graph_template_selection(self):
        template_select = self.graph_template_comboBox.currentText().strip()
        if template_select == "":
            self.graph_type_comboBox.setEnabled(True)
            self.x_axis_comboBox.setEnabled(True)
            self.y_axis_comboBox.setEnabled(True)
            self.graph_name_lineEdit.setEnabled(True)
            self.x_axis_lineEdit.setEnabled(True)
            self.y_axis_lineEdit.setEnabled(True)
            self.validate_input()
        else:
            self.graph_type_comboBox.setEnabled(False)
            self.x_axis_comboBox.setEnabled(False)
            self.y_axis_comboBox.setEnabled(False)
            self.graph_name_lineEdit.setEnabled(False)
            self.x_axis_lineEdit.setEnabled(False)
            self.y_axis_lineEdit.setEnabled(False)
            self.save_to_graph_pushButton.setEnabled(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
