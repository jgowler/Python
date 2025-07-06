from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import csv
import sys
import win32evtlog
import datetime
import win32security
import win32evtlogutil



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 711)
        MainWindow.setStyleSheet("background-color: rgb(78, 78, 80);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(20, 10, 20, 10)
        main_layout.setSpacing(10)

        self.top_frame = QtWidgets.QFrame(self.centralwidget)
        self.top_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.top_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.top_frame.setObjectName("top_frame")
        main_layout.addWidget(self.top_frame)

        top_layout = QtWidgets.QHBoxLayout(self.top_frame)
        top_layout.setContentsMargins(5, 5, 5, 5)
        top_layout.setSpacing(0)

        self.top_label = QtWidgets.QLabel(self.top_frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.top_label.setFont(font)
        self.top_label.setAlignment(QtCore.Qt.AlignCenter)
        self.top_label.setObjectName("top_label")
        top_layout.addWidget(self.top_label)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        main_layout.addWidget(self.frame)

        filter_layout = QtWidgets.QGridLayout(self.frame)
        filter_layout.setContentsMargins(10, 10, 10, 10)
        filter_layout.setHorizontalSpacing(15)
        filter_layout.setVerticalSpacing(10)

        self.log_type_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log_type_label.setFont(font)
        self.log_type_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.log_type_label.setObjectName("log_type_label")
        filter_layout.addWidget(self.log_type_label, 0, 0)

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Application")
        self.comboBox.addItem("System")
        self.comboBox.addItem("Security")
        self.comboBox.addItem("Setup")
        filter_layout.addWidget(self.comboBox, 0, 1, 1, 2)

        self.event_id_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.event_id_label.setFont(font)
        self.event_id_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.event_id_label.setObjectName("event_id_label")
        filter_layout.addWidget(self.event_id_label, 1, 0)

        self.event_id_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.event_id_lineEdit.setObjectName("event_id_lineEdit")
        filter_layout.addWidget(self.event_id_lineEdit, 1, 1, 1, 2)

        self.errors_checkBox = QtWidgets.QCheckBox(self.frame)
        self.errors_checkBox.setObjectName("errors_checkBox")
        self.errors_checkBox.stateChanged.connect(self.update_search_button_state)
        filter_layout.addWidget(self.errors_checkBox, 2, 0)

        self.warnings_checkBox = QtWidgets.QCheckBox(self.frame)
        self.warnings_checkBox.setObjectName("warnings_checkBox")
        self.warnings_checkBox.stateChanged.connect(self.update_search_button_state)
        filter_layout.addWidget(self.warnings_checkBox, 2, 1)

        self.info_checkBox = QtWidgets.QCheckBox(self.frame)
        self.info_checkBox.setObjectName("info_checkBox")
        self.info_checkBox.stateChanged.connect(self.update_search_button_state)
        filter_layout.addWidget(self.info_checkBox, 2, 2)

        self.start_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.start_label.setFont(font)
        self.start_label.setObjectName("start_label")
        filter_layout.addWidget(self.start_label, 0, 3)

        self.start_dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.start_dateTimeEdit.setCalendarPopup(True)
        self.start_dateTimeEdit.setDateTime(QDateTime.currentDateTime().addDays(-1))
        self.start_dateTimeEdit.setObjectName("start_dateTimeEdit")
        filter_layout.addWidget(self.start_dateTimeEdit, 0, 4)

        self.end_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.end_label.setFont(font)
        self.end_label.setObjectName("end_label")
        filter_layout.addWidget(self.end_label, 1, 3)

        self.end_dateTimeEdit = QtWidgets.QDateTimeEdit(self.frame)
        self.end_dateTimeEdit.setCalendarPopup(True)
        self.end_dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.end_dateTimeEdit.setObjectName("end_dateTimeEdit")
        filter_layout.addWidget(self.end_dateTimeEdit, 1, 4)

        self.search_pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.on_search())
        self.search_pushButton.setEnabled(False)
        self.search_pushButton.setStyleSheet("background-color: rgb(14, 99, 156);\ncolor: rgb(212, 212, 212);")
        self.search_pushButton.setObjectName("search_pushButton")
        filter_layout.addWidget(self.search_pushButton, 0, 5, 1, 1)

        self.export_pushButton = QtWidgets.QPushButton(self.frame, clicked = lambda: self.export_to_csv())
        self.export_pushButton.setEnabled(False)
        self.export_pushButton.setStyleSheet("background-color: rgb(14, 99, 156);\ncolor: rgb(212, 212, 212);")
        self.export_pushButton.setObjectName("export_pushButton")
        filter_layout.addWidget(self.export_pushButton, 1, 5, 1, 1)

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        main_layout.addWidget(self.frame_2)

        frame2_layout = QtWidgets.QVBoxLayout(self.frame_2)
        frame2_layout.setContentsMargins(10, 10, 10, 10)

        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels([
            "Event ID", "Source", "Level", "Time", "User", "Message"
        ])
        self.tableWidget.itemDoubleClicked.connect(self.show_full_message)
        # Stretch last column (Message) and allow all headers to stretch proportionally
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        frame2_layout.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Event Viewer Searcher"))
        self.top_label.setText(_translate("MainWindow", "Windows Event Viewer Log Analyser"))
        self.log_type_label.setText(_translate("MainWindow", "Log Type:"))
        self.event_id_label.setText(_translate("MainWindow", "Event IDs:"))
        self.errors_checkBox.setText(_translate("MainWindow", "Include Errors"))
        self.warnings_checkBox.setText(_translate("MainWindow", "Include Warnings"))
        self.info_checkBox.setText(_translate("MainWindow", "Include Information"))
        self.start_label.setText(_translate("MainWindow", "Start:"))
        self.end_label.setText(_translate("MainWindow", "End:"))
        self.search_pushButton.setText(_translate("MainWindow", "Search"))
        self.export_pushButton.setText(_translate("MainWindow", "Export to CSV"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Event ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Level"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "User"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Message"))

    def update_search_button_state(self):
        # Enable search button only if at least one of the checkboxes is checked
        if self.errors_checkBox.isChecked() or self.warnings_checkBox.isChecked() or self.info_checkBox.isChecked():
            self.search_pushButton.setEnabled(True)
        else:
            self.search_pushButton.setEnabled(False)

    def on_search(self):
        start = self.start_dateTimeEdit.dateTime().toPyDateTime()
        end = self.end_dateTimeEdit.dateTime().toPyDateTime()

        if start > end:
            self.statusbar.showMessage("ERROR: Start time must be before End time")
            return

        self.search_pushButton.setEnabled(False)
        self.statusbar.showMessage("Searching...")
        ### Update statusbar
        QtWidgets.QApplication.processEvents()

        count = self.query_events(start, end)

        QtWidgets.QApplication.processEvents()
        self.statusbar.showMessage(f"Search Complete - {count} events found")
        self.search_pushButton.setEnabled(True)

    def show_full_message(self, item):
        # Get the row of the clicked item
        row = item.row()
        
        message_item = self.tableWidget.item(row, 5)
        if message_item:
            full_message = message_item.text()
        else:
            full_message = "No message available."

        msg_box = QMessageBox()
        msg_box.setWindowTitle("Full Event Message")
        msg_box.setText(full_message)
        msg_box.exec_()


    def export_to_csv(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(
            None,
            "Save CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
            options=options
        )
        if filename:
            try:
                with open(filename, mode = "w", newline = '', encoding = 'utf-8') as file:
                    writer = csv.writer(file)

                    headers = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(self.tableWidget.columnCount())]
                    writer.writerow(headers)

                    for row in range(self.tableWidget.rowCount()):
                        row_data = []
                        for col in range(self.tableWidget.columnCount()):
                            item = self.tableWidget.item(row, col)
                            row_data.append(item.text() if item else "")
                        writer.writerow(row_data)

                QMessageBox.information(None, "Export successful", f"Data exported to {filename}")

            except Exception as e:
                QMessageBox.critical(None, "Export failed", f"An error occured:\n{str(e)}")


    def query_events(self, start, end):
        self.tableWidget.setRowCount(0)  # Clear previous results

        server = 'localhost'
        log_type = self.comboBox.currentText()
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        hand = win32evtlog.OpenEventLog(server, log_type)
        total = win32evtlog.GetNumberOfEventLogRecords(hand)

        count = 0
        stop = False

        while not stop:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break

            for ev_obj in events:
                event_time = ev_obj.TimeGenerated.Format()
                event_datetime = datetime.datetime.strptime(event_time, "%a %b %d %H:%M:%S %Y")

                # Filter by date range
                if not (start <= event_datetime <= end):
                    continue

                # Filter by selected event types
                allowed_levels = []
                if self.errors_checkBox.isChecked():
                    allowed_levels.extend([1, 16])  # Error + Failure Audit
                if self.warnings_checkBox.isChecked():
                    allowed_levels.append(2)        # Warning
                if self.info_checkBox.isChecked():
                    allowed_levels.extend([4, 8])   # Information + Success Audit

                if ev_obj.EventType not in allowed_levels:
                    continue

                level_str = {
                    1: 'Error',
                    2: 'Warning',
                    4: 'Information',
                    8: 'Success Audit',
                    16: 'Failure Audit'
                }.get(ev_obj.EventType, str(ev_obj.EventType))

                # Filter by Event ID (optional)
                event_ids = self.event_id_lineEdit.text().strip()
                if event_ids:
                    allowed_ids = [eid.strip() for eid in event_ids.split(",")]
                    if str(ev_obj.EventID & 0xFFFF) not in allowed_ids:
                        continue

                # Add row to table
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)

                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ev_obj.EventID & 0xFFFF)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(ev_obj.SourceName)))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(level_str))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(event_datetime)))

                # User column
                user = "N/A"
                if ev_obj.Sid:
                    try:
                        user_name, domain, _ = win32security.LookupAccountSid(None, ev_obj.Sid)
                        user = f"{domain}\\{user_name}"
                    except Exception:
                        user = "N/A"

                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(user))

                # Message column with SafeFormatMessage
                try:
                    message = win32evtlogutil.SafeFormatMessage(ev_obj, log_type)
                except Exception:
                    message = "N/A"
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(message))

                count += 1
                if count >= 500:
                    stop = True
                    break

            self.export_pushButton.setEnabled(True)
        return count



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())