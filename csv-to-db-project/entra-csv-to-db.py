from PySide6.QtCore import (
    QCoreApplication,
    QSize,
    QRect,
    Qt,
    QMetaObject,
)
from PySide6.QtGui import (
    QFont,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGroupBox,
    QLabel,
    QMainWindow,
    QMenuBar,
    QPushButton,
    QStatusBar,
    QTableView,
    QTextEdit,
    QWidget,
    QFileDialog,
    QInputDialog,
)

import sys
import sqlite3
import csv


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1274, 693)
        MainWindow.setMinimumSize(QSize(1274, 693))
        MainWindow.setMaximumSize(QSize(1274, 693))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_Top_Frame = QFrame(self.centralwidget)
        self.frame_Top_Frame.setObjectName("frame_Top_Frame")
        self.frame_Top_Frame.setGeometry(QRect(10, 10, 551, 51))
        self.frame_Top_Frame.setStyleSheet("background-color: rgb(58, 58, 212);")
        self.frame_Top_Frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Top_Frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_Top = QLabel(self.frame_Top_Frame)
        self.label_Top.setObjectName("label_Top")
        self.label_Top.setGeometry(QRect(8, 15, 541, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_Top.setFont(font)
        self.label_Top.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_Select_CSV = QFrame(self.centralwidget)
        self.frame_Select_CSV.setObjectName("frame_Select_CSV")
        self.frame_Select_CSV.setGeometry(QRect(10, 70, 541, 51))
        self.frame_Select_CSV.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Select_CSV.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_Select_CSV = QPushButton(self.frame_Select_CSV)
        self.pushButton_Select_CSV.setObjectName("pushButton_Select_CSV")
        self.pushButton_Select_CSV.setGeometry(QRect(10, 10, 151, 31))
        self.label_Select_CSV = QLabel(self.frame_Select_CSV)
        self.label_Select_CSV.setObjectName("label_Select_CSV")
        self.label_Select_CSV.setGeometry(QRect(170, 20, 371, 21))
        self.label_Select_CSV.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.frame_Seperator = QFrame(self.centralwidget)
        self.frame_Seperator.setObjectName("frame_Seperator")
        self.frame_Seperator.setGeometry(QRect(9, 130, 551, 16))
        self.frame_Seperator.setStyleSheet("background-color: rgb(58, 58, 212);")
        self.frame_Seperator.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Seperator.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(10, 160, 541, 51))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.pushButton_Validate_CSV_Headers = QPushButton(self.frame)
        self.pushButton_Validate_CSV_Headers.setObjectName(
            "pushButton_Validate_CSV_Headers"
        )
        self.pushButton_Validate_CSV_Headers.setGeometry(QRect(10, 10, 151, 31))
        self.pushButton_Validate_CSV_Headers.setEnabled(False)
        self.label_Validate_Headers = QLabel(self.frame)
        self.label_Validate_Headers.setObjectName("label_Validate_Headers")
        self.label_Validate_Headers.setGeometry(QRect(170, 20, 371, 21))
        self.label_Validate_Headers.setAlignment(
            Qt.AlignmentFlag.AlignRight
            | Qt.AlignmentFlag.AlignTrailing
            | Qt.AlignmentFlag.AlignVCenter
        )
        self.label_Status = QLabel(self.centralwidget)
        self.label_Status.setObjectName("label_Status")
        self.label_Status.setGeometry(QRect(20, 240, 531, 21))
        self.frame_Seperator_2 = QFrame(self.centralwidget)
        self.frame_Seperator_2.setObjectName("frame_Seperator_2")
        self.frame_Seperator_2.setGeometry(QRect(10, 280, 551, 16))
        self.frame_Seperator_2.setStyleSheet("background-color: rgb(58, 58, 212);")
        self.frame_Seperator_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Seperator_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_Add_to_DB = QPushButton(self.centralwidget)
        self.pushButton_Add_to_DB.setObjectName("pushButton_Add_to_DB")
        self.pushButton_Add_to_DB.setGeometry(QRect(20, 360, 151, 31))
        self.frame_Seperator_3 = QFrame(self.centralwidget)
        self.frame_Seperator_3.setObjectName("frame_Seperator_3")
        self.frame_Seperator_3.setGeometry(QRect(560, 10, 20, 631))
        self.frame_Seperator_3.setStyleSheet("background-color: rgb(58, 58, 212);")
        self.frame_Seperator_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Seperator_3.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit_Log_Output = QTextEdit(self.centralwidget)
        self.textEdit_Log_Output.setObjectName("textEdit_Log_Output")
        self.textEdit_Log_Output.setGeometry(QRect(180, 340, 361, 291))
        font1 = QFont()
        font1.setFamily("Consolas")
        self.textEdit_Log_Output.setFont(font1)
        self.textEdit_Log_Output.setReadOnly(True)
        self.label_Logs_Output = QLabel(self.centralwidget)
        self.label_Logs_Output.setObjectName("label_Logs_Output")
        self.label_Logs_Output.setGeometry(QRect(178, 310, 371, 20))
        self.label_Logs_Output.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_DB = QGroupBox(self.centralwidget)
        self.groupBox_DB.setObjectName("groupBox_DB")
        self.groupBox_DB.setGeometry(QRect(599, 19, 661, 621))
        self.tableView_DB = QTableView(self.groupBox_DB)
        self.tableView_DB.setObjectName("tableView_DB")
        self.tableView_DB.setGeometry(QRect(10, 20, 641, 591))
        self.pushButton_Add_Table_to_DB = QPushButton(self.centralwidget)
        self.pushButton_Add_Table_to_DB.setObjectName("pushButton_Add_Table_to_DB")
        self.pushButton_Add_Table_to_DB.setGeometry(QRect(20, 400, 151, 31))
        self.groupBox_Table = QGroupBox(self.centralwidget)
        self.groupBox_Table.setObjectName("groupBox_Table")
        self.groupBox_Table.setGeometry(QRect(10, 300, 541, 341))
        self.comboBox_select_table = QComboBox(self.groupBox_Table)
        self.comboBox_select_table.setObjectName("comboBox_select_table")
        self.comboBox_select_table.setGeometry(QRect(8, 30, 151, 22))
        self.pushButton_Search = QPushButton(self.groupBox_Table)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.pushButton_Search.setGeometry(QRect(10, 180, 151, 31))
        self.pushButton_Export_Table_to_CSV = QPushButton(self.groupBox_Table)
        self.pushButton_Export_Table_to_CSV.setObjectName(
            "pushButton_Export_Table_to_CSV"
        )
        self.pushButton_Export_Table_to_CSV.setGeometry(QRect(10, 220, 151, 31))
        self.pushButton_Backup_DB = QPushButton(self.groupBox_Table)
        self.pushButton_Backup_DB.setObjectName("pushButton_Backup_DB")
        self.pushButton_Backup_DB.setGeometry(QRect(10, 260, 151, 31))
        self.pushButton_Remove_Table_from_DB = QPushButton(self.groupBox_Table)
        self.pushButton_Remove_Table_from_DB.setObjectName(
            "pushButton_Remove_Table_from_DB"
        )
        self.pushButton_Remove_Table_from_DB.setGeometry(QRect(10, 140, 151, 31))
        self.pushButton_Restore_DB = QPushButton(self.centralwidget)
        self.pushButton_Restore_DB.setObjectName("pushButton_Restore_DB")
        self.pushButton_Restore_DB.setGeometry(QRect(20, 600, 151, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_Table.raise_()
        self.frame_Top_Frame.raise_()
        self.frame_Select_CSV.raise_()
        self.frame_Seperator.raise_()
        self.frame.raise_()
        self.label_Status.raise_()
        self.frame_Seperator_2.raise_()
        self.pushButton_Add_to_DB.raise_()
        self.frame_Seperator_3.raise_()
        self.textEdit_Log_Output.raise_()
        self.label_Logs_Output.raise_()
        self.groupBox_DB.raise_()
        self.pushButton_Add_Table_to_DB.raise_()
        self.pushButton_Restore_DB.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1274, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        # Connect signals
        self.pushButton_Select_CSV.clicked.connect(self.handle_uploaded_csv)

        QMetaObject.connectSlotsByName(MainWindow)

        self.current_csv_file = None
        self.current_table = None
        self.current_headers = None

    def handle_uploaded_csv(self):
        success, message, headers, file = read_csv(parent=self.centralwidget)
        if success:
            self.label_Status.setText(
                f"CSV '{file}' imported successfully.\nRows inserted: {len(headers)}."
            )
            self.current_csv_file = file
            self.current_table = (
                None  # Table name could be added to return values if needed
            )
            self.current_headers = headers
            self.pushButton_Validate_CSV_Headers.setEnabled(True)
        else:
            if isinstance(message, dict):
                # Specific error message
                self.label_Status.setText(
                    f"Failed: {message.get('message', 'Unknown error')}."
                )
            else:
                self.label_Status.setText(f"Failed: {message}.")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Entra CSV to Db", None)
        )
        self.label_Top.setText(
            QCoreApplication.translate("MainWindow", "Entra CSV to Database", None)
        )
        self.pushButton_Select_CSV.setText(
            QCoreApplication.translate("MainWindow", "Select CSV File", None)
        )
        self.label_Select_CSV.setText(
            QCoreApplication.translate(
                "MainWindow",
                "<---No CSV file selected. Please select a CSV file to continue",
                None,
            )
        )
        self.pushButton_Validate_CSV_Headers.setText(
            QCoreApplication.translate("MainWindow", "Check Headers against DB", None)
        )
        self.label_Validate_Headers.setText(
            QCoreApplication.translate("MainWindow", "<---No CSV file loaded", None)
        )
        self.label_Status.setText(
            QCoreApplication.translate(
                "MainWindow", "Select a CSV file to begin.", None
            )
        )
        self.pushButton_Add_to_DB.setText(
            QCoreApplication.translate("MainWindow", "Add Rows to DB", None)
        )
        self.label_Logs_Output.setText(
            QCoreApplication.translate("MainWindow", "Log Output", None)
        )
        self.groupBox_DB.setTitle(
            QCoreApplication.translate("MainWindow", "Database Table Output", None)
        )
        self.pushButton_Add_Table_to_DB.setText(
            QCoreApplication.translate("MainWindow", "Add Table to DB", None)
        )
        self.groupBox_Table.setTitle(
            QCoreApplication.translate("MainWindow", "Database Table Operations", None)
        )
        self.pushButton_Search.setText(
            QCoreApplication.translate("MainWindow", "Search Table", None)
        )
        self.pushButton_Export_Table_to_CSV.setText(
            QCoreApplication.translate("MainWindow", "Export Table to CSV", None)
        )
        self.pushButton_Backup_DB.setText(
            QCoreApplication.translate("MainWindow", "Backup DB", None)
        )
        self.pushButton_Remove_Table_from_DB.setText(
            QCoreApplication.translate("MainWindow", "Remove Table", None)
        )
        self.pushButton_Restore_DB.setText(
            QCoreApplication.translate("MainWindow", "Restore DB", None)
        )


def read_csv(file=None, db_path=None, parent=None):
    if db_path is None:
        if parent is None:
            return (
                False,
                "No db_path provided and no parent to open file dialog.",
                None,
                None,
            )
        db_path, _ = QFileDialog.getOpenFileName(
            parent, "Select SQLite Database", "", "SQLite Files (*.db);;All Files (*)"
        )
        if not db_path:
            return False, "No database selected.", None, None

    if file is None:
        if parent is None:
            # Cannot open dialog without a parent
            return (
                False,
                "No file provided and no parent to open file dialog.",
                None,
                None,
            )
        file, _ = QFileDialog.getOpenFileName(
            parent, "Open CSV file", "", "CSV Files (*.csv)"
        )
        if not file:
            return False, "No file selected.", None, None

    try:
        conn = sqlite3.connect(db_path)
    except Exception as e:
        return False, f"Failed to open database: {e}", None, None

    cursor = conn.cursor()

    import os

    table_name = os.path.splitext(os.path.basename(file))[0]

    try:
        with open(file, newline="", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader, None)
            if headers is None:
                return False, "CSV file is empty.", None, None

            rows = list(reader)
    except Exception as e:
        return False, f"Failed to read CSV file: {e}", None, None

    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
    )
    table_exists = cursor.fetchone() is not None

    if not table_exists:
        try:
            columns_decl = ", ".join(f'"{col}" TEXT' for col in headers)
            cursor.execute(f"CREATE TABLE '{table_name}' ({columns_decl});")
            conn.commit()
        except Exception as e:
            conn.close()
            return False, f"Failed to create table '{table_name}': {e}", None, None

    cursor.execute(f"PRAGMA table_info('{table_name}');")
    db_columns = [row[1] for row in cursor.fetchall()]

    if db_columns != headers:
        conn.close()
        return (
            False,
            {
                "message": "CSV headers do not match the database table columns.",
                "csv_headers": headers,
                "db_columns": db_columns,
            },
            None,
            None,
        )

    try:
        inserted_count = 0
        placeholders = ", ".join(["?"] * len(headers))
        for row in rows:
            if len(row) != len(headers):
                # Skip invalid rows or handle as needed
                continue
            cursor.execute(
                f"INSERT INTO '{table_name}' ({', '.join(headers)}) VALUES ({placeholders})",
                row,
            )
            inserted_count += 1
        conn.commit()
    except Exception as e:
        conn.close()
        return False, f"Failed to insert rows: {e}", None, None

    conn.close()
    return True, f"Inserted {inserted_count} rows into '{table_name}'", headers, file


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
TO DO:
Disable all other buttons until CSV / Db has been selected.
'''