from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QSplashScreen
from PyQt5.QtGui import QPixmap
import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 480)
        MainWindow.setMinimumSize(QtCore.QSize(700, 480))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_vlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_vlayout.setContentsMargins(20, 10, 20, 10)
        self.main_vlayout.setSpacing(10)

        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setMinimumHeight(50)
        self.top_frame.setMaximumHeight(50)
        self.top_frame.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")

        self.top_frame_layout = QtWidgets.QHBoxLayout(self.top_frame)
        self.top_frame_layout.setContentsMargins(10, 5, 10, 5)
        self.top_frame_layout.setSpacing(10)

        font_title = QtGui.QFont()
        font_title.setPointSize(16)
        font_title.setBold(True)
        font_title.setWeight(75)

        self.top_label = QtWidgets.QLabel(self.top_frame)
        self.top_label.setFont(font_title)
        self.top_label.setObjectName("top_label")
        self.top_frame_layout.addWidget(self.top_label, 0, Qt.AlignLeft)

        self.loaded_csv_label = QtWidgets.QLabel(self.top_frame)
        font_loaded_label = QtGui.QFont()
        font_loaded_label.setPointSize(8)
        font_loaded_label.setItalic(True)
        self.loaded_csv_label.setFont(font_loaded_label)
        self.loaded_csv_label.setObjectName("loaded_csv_label")
        self.top_frame_layout.addWidget(self.loaded_csv_label, 1, Qt.AlignCenter)

        self.load_csv_pushButton = QtWidgets.QPushButton(self.top_frame, clicked=lambda: self.open_csv())
        font_btn = QtGui.QFont()
        font_btn.setPointSize(14)
        self.load_csv_pushButton.setFont(font_btn)
        self.load_csv_pushButton.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.load_csv_pushButton.setObjectName("load_csv_pushButton")
        self.top_frame_layout.addWidget(self.load_csv_pushButton, 0, Qt.AlignRight)

        self.main_vlayout.addWidget(self.top_frame)

        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")

        self.main_frame_layout = QtWidgets.QVBoxLayout(self.main_frame)
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(10)

        self.template_layout = QtWidgets.QHBoxLayout()
        self.template_layout.setContentsMargins(0, 0, 0, 0)
        self.template_layout.setSpacing(10)

        font_label_main = QtGui.QFont()
        font_label_main.setPointSize(14)
        font_label_main.setBold(True)
        font_label_main.setWeight(75)

        self.graph_template_label = QtWidgets.QLabel(self.main_frame)
        self.graph_template_label.setFont(font_label_main)
        self.graph_template_label.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.graph_template_label.setObjectName("graph_template_label")
        self.template_layout.addWidget(self.graph_template_label, 0, Qt.AlignLeft)

        self.graph_template_comboBox = QtWidgets.QComboBox(self.main_frame)
        font_combo = QtGui.QFont()
        font_combo.setPointSize(12)
        self.graph_template_comboBox.setFont(font_combo)
        self.graph_template_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.graph_template_comboBox.setObjectName("graph_template_comboBox")
        self.graph_template_comboBox.addItems([
            "",
            "Successful Login Outside of GB",
            "Login Success vs Failure Count",
            "Login Activity Over Time",
            "Sign-ins by Location",
            "Top Users by Sign-in Count",
            "Sign-ins by Client App",
            "Authentication Type Breakdown",
            "Failed sign-in reasons"
        ])
        self.graph_template_comboBox.setEnabled(False)  # Enable after CSV loaded
        self.template_layout.addWidget(self.graph_template_comboBox, 1)

        self.main_frame_layout.addLayout(self.template_layout)

        self.data_preview_table = QtWidgets.QTableWidget(self.main_frame)
        self.data_preview_table.setObjectName("data_preview_table")
        self.data_preview_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # read-only
        self.data_preview_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.data_preview_table.setMinimumHeight(240)
        self.main_frame_layout.addWidget(self.data_preview_table)

        self.main_vlayout.addWidget(self.main_frame)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addStretch()  # push button to the right

        self.save_to_graph_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plot_to_graph())
        self.save_to_graph_pushButton.setEnabled(False)  # Enable after selection
        font_btn2 = QtGui.QFont()
        font_btn2.setPointSize(14)
        self.save_to_graph_pushButton.setFont(font_btn2)
        self.save_to_graph_pushButton.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.save_to_graph_pushButton.setObjectName("save_to_graph_pushButton")
        self.button_layout.addWidget(self.save_to_graph_pushButton)

        self.main_vlayout.addLayout(self.button_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.graph_template_comboBox.currentIndexChanged.connect(self.graph_template_selection)
        self.graph_template_comboBox.currentIndexChanged.connect(self.validate_input)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EntraGrapher"))
        self.top_label.setText(_translate("MainWindow", "EntraGrapher"))
        self.load_csv_pushButton.setText(_translate("MainWindow", "Load CSV"))
        self.loaded_csv_label.setText("")
        self.graph_template_label.setText(_translate("MainWindow", "Graph Template"))
        self.save_to_graph_pushButton.setText(_translate("MainWindow", "Plot Graph"))

    def populate_table(self, df):
        self.data_preview_table.clear()
        self.data_preview_table.setRowCount(min(len(df), 10))
        self.data_preview_table.setColumnCount(len(df.columns))
        self.data_preview_table.setHorizontalHeaderLabels(df.columns.tolist())
        for i in range(min(len(df), 10)):
            for j, col in enumerate(df.columns):
                item = QtWidgets.QTableWidgetItem(str(df.iloc[i, j]))
                self.data_preview_table.setItem(i, j, item)
        self.data_preview_table.resizeColumnsToContents()

    def validate_input(self):
        template = self.graph_template_comboBox.currentText().strip()
        self.save_to_graph_pushButton.setEnabled(bool(template))

    def open_csv(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            None,
            "Open CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
            options=options
        )
        if filename:
            try:
                self.statusbar.showMessage(f"File loaded: {filename}")
                self.df = pd.read_csv(filename)
                headers = self.df.columns.tolist()

                self.graph_template_comboBox.setEnabled(True)
                self.graph_template_comboBox.setCurrentIndex(0)

                self.populate_table(self.df)
            except Exception as e:
                QMessageBox.critical(None, "Import failed", f"An error occured:\n{str(e)}")

    def plot_to_graph(self):
        if not hasattr(self, "df") or self.df.empty:
            QMessageBox.warning(None, "No Data", "Please load a valid CSV file first.")
            return

        template_select = self.graph_template_comboBox.currentText().strip()

        if template_select == "":
            QMessageBox.warning(None, "No Template Selected", "Please select a graph template to plot.")
            return

        try:
            template_map = {
                "Successful Login Outside of GB": self.successful_login_outside_gb,
                "Login Success vs Failure Count": self.plot_login_success_failure,
                "Login Activity Over Time": self.plot_signins_over_time,
                "Top Users by Sign-in Count": self.plot_top_users,
                "Sign-ins by Location": self.plot_signins_by_location,
                "Sign-ins by Client App": self.plot_signins_by_client_app,
                "Authentication Type Breakdown": self.plot_auth_type_breakdown,
                "Failed sign-in reasons": self.failed_sign_in_reasons
            }

            plot_func = template_map.get(template_select)
            if plot_func:
                plot_func(self.df)
            else:
                QMessageBox.warning(None, "Unknown Template", f"The selected template '{template_select}' is not recognized.")
        except Exception as e:
            QMessageBox.critical(None, "Plotting failed", f"An error occurred:\n{str(e)}")

    def successful_login_outside_gb(self, df):
        if 'Status' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Status' not found in data.")
            return
        elif 'Location' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Location' not found in data.")
            return

        df['Location'] = df['Location'].astype(str).str.strip().str.upper()
        filtered_df = df[(df['Status'] == 'Success') & (~df['Location'].str.contains("GB"))]

        if filtered_df.empty:
            QMessageBox.information(None, "No Data", "No successful logins outside of GB found.")
            return

        plt.figure(figsize=(10, 6))
        sns.countplot(data=filtered_df, x='Location', order=filtered_df['Location'].value_counts().index)
        plt.title("Successful Login Outside of GB by Location")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_login_success_failure(self, df):
        if 'Status' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Status' not found in data.")
            return

        status_counts = df['Status'].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title("Login Success vs Failure Count")
        plt.axis('equal')
        plt.show()

    def plot_signins_over_time(self, df):
        if 'Date' in df.columns:
            date_col = 'Date'
        elif 'Date (UTC)' in df.columns:
            date_col = 'Date (UTC)'
        else:
            QMessageBox.warning(None, "Missing Data", "Neither 'Date' nor 'Date (UTC)' column found in data.")
            return

        df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        df = df.dropna(subset=[date_col])

        counts = df.groupby(df[date_col].dt.date).size().reset_index(name='Count')
        counts.rename(columns={date_col: 'Date'}, inplace=True)

        plt.figure(figsize=(12, 6))
        sns.lineplot(data=counts, x='Date', y='Count')
        plt.title("Login Activity Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sign-in Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


    def plot_top_users(self, df):
        if 'User' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'User' not found in data.")
            return

        user_counts = df['User'].value_counts().head(10)

        plt.figure(figsize=(12, 6))
        sns.barplot(x=user_counts.values, y=user_counts.index, orient='h')
        plt.title("Top Users by Sign-in Count")
        plt.xlabel("Count")
        plt.ylabel("User")
        plt.tight_layout()
        plt.show()

    def plot_signins_by_location(self, df):
        if 'Location' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Location' not found in data.")
            return

        location_counts = df['Location'].value_counts()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=location_counts.index, y=location_counts.values)
        plt.title("Sign-ins by Location")
        plt.xlabel("Location")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_signins_by_client_app(self, df):
        if 'Client app' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Client app' not found in data.")
            return

        app_counts = df['Client app'].value_counts()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=app_counts.index, y=app_counts.values)
        plt.title("Sign-ins by Client App")
        plt.xlabel("Client App")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_auth_type_breakdown(self, df):
        if 'Multifactor authentication auth method' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Multifactor authentication auth method' not found in data.")
            return

        auth_counts = df['Multifactor authentication auth method'].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(auth_counts, labels=auth_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title("Authentication Type Breakdown")
        plt.axis('equal')
        plt.show()

    def failed_sign_in_reasons(self, df):
        if 'Failure reason' not in df.columns:
            QMessageBox.warning(None, "Missing Data", "Column 'Failure reason' not found in data.")
            return

        failure_counts = df['Failure reason'].value_counts()

        plt.figure(figsize=(10, 6))
        sns.barplot(x=failure_counts.index, y=failure_counts.values)
        plt.title("Failed Sign-in Reasons")
        plt.xlabel("Reason")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def graph_template_selection(self):
        self.validate_input()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash_pix = QPixmap("EntraGrapher.png")
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    QTimer.singleShot(3000, splash.close)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    splash.finish(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
