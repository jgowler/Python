import sys
import csv
import sqlite3
from PySide6.QtCore import Signal, QSize, QRect, Qt, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QFrame,
    QLabel,
    QPushButton,
    QTextEdit,
    QGroupBox,
    QComboBox,
    QTableView,
    QFileDialog,
    QStatusBar,
    QMenuBar,
    QMessageBox,
    QAbstractItemView,
    QInputDialog,
)
from PySide6.QtSql import QSqlDatabase, QSqlTableModel


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
        self.pushButton_Add_to_DB.setEnabled(False)

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
        self.tableView_DB.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

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

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("CSV to Db")
        self.label_Top.setText("CSV to Database")
        self.pushButton_Select_CSV.setText("Select CSV File")
        self.label_Select_CSV.setText(
            "<---No CSV file selected. Please select a CSV file to continue"
        )
        self.pushButton_Validate_CSV_Headers.setText("Check Headers against DB")
        self.label_Validate_Headers.setText("<---No CSV file loaded")
        self.label_Status.setText("Select a CSV file to begin.")
        self.pushButton_Add_to_DB.setText("Add Rows to DB")
        self.label_Logs_Output.setText("Log Output")
        self.groupBox_DB.setTitle("Database Table Output")
        self.pushButton_Add_Table_to_DB.setText("Add Table to DB")
        self.groupBox_Table.setTitle("Database Table Operations")
        self.pushButton_Search.setText("Search Table")
        self.pushButton_Export_Table_to_CSV.setText("Export Table to CSV")
        self.pushButton_Backup_DB.setText("Backup DB")
        self.pushButton_Remove_Table_from_DB.setText("Remove Table from DB")
        self.pushButton_Restore_DB.setText("Restore DB")


class MainWindow(QMainWindow):
    status_signal = Signal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db_filename = "mydatabase.db"
        self.conn = None
        self.csv_headers = []
        self.csv_filepath = None

        # Signals
        self.status_signal.connect(self.update_status)
        self.ui.pushButton_Select_CSV.clicked.connect(self.handle_csv_selection)
        self.ui.pushButton_Validate_CSV_Headers.clicked.connect(
            self.validate_csv_headers
        )
        self.ui.pushButton_Add_to_DB.clicked.connect(self.add_csv_rows_to_db)
        self.ui.comboBox_select_table.currentIndexChanged.connect(
            self.load_table_to_view
        )
        self.ui.pushButton_Search.clicked.connect(self.search_table)
        self.ui.pushButton_Add_Table_to_DB.clicked.connect(self.create_sample_table)
        self.ui.pushButton_Remove_Table_from_DB.clicked.connect(
            self.remove_selected_table
        )
        self.ui.pushButton_Export_Table_to_CSV.clicked.connect(self.export_table_to_csv)
        self.ui.pushButton_Backup_DB.clicked.connect(self.backup_db)
        self.ui.pushButton_Restore_DB.clicked.connect(self.restore_db)

        self.init_db()
        self.load_tables_into_combobox()
        self.ui.pushButton_Validate_CSV_Headers.setEnabled(False)
        self.ui.pushButton_Add_to_DB.setEnabled(False)

    def init_db(self):
        try:
            self.conn = sqlite3.connect(self.db_filename)
            self.status_signal.emit(f"Connected to DB: {self.db_filename}")
        except Exception as e:
            self.status_signal.emit(f"DB connection error: {e}")

    def ask_yes_no(self, message):
        reply = QMessageBox.question(
            self, "Confirm", message, QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        return reply == QMessageBox.Yes

    def load_tables_into_combobox(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
            )
            tables = cursor.fetchall()
            self.ui.comboBox_select_table.clear()
            for table in tables:
                self.ui.comboBox_select_table.addItem(table[0])
            if tables:
                self.load_table_to_view()
        except Exception as e:
            self.status_signal.emit(f"Failed to load tables: {e}")

    def handle_csv_selection(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open CSV File", "", "CSV Files (*.csv)"
        )
        if not file_name:
            self.status_signal.emit("No file selected.")
            return

        success, message, headers = self.read_csv(file_name)
        if success:
            self.csv_filepath = file_name
            self.csv_headers = headers
            self.status_signal.emit(f"Loaded CSV: {file_name} ({len(headers)} columns)")
            self.ui.label_Select_CSV.setText(file_name)
            self.ui.pushButton_Validate_CSV_Headers.setEnabled(True)
            self.ui.label_Validate_Headers.setText("<---Ready to validate headers.")
            self.ui.pushButton_Add_to_DB.setEnabled(True)
        else:
            self.status_signal.emit(f"Error loading CSV: {message}")
            self.ui.pushButton_Validate_CSV_Headers.setEnabled(False)
            self.ui.pushButton_Add_to_DB.setEnabled(False)

    def read_csv(self, file_path):
        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
            return True, "CSV loaded successfully.", headers
        except Exception as e:
            return False, str(e), []

    def validate_csv_headers(self):
        if not self.csv_headers:
            self.status_signal.emit("No CSV loaded to validate.")
            return

        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            self.status_signal.emit("No table selected for validation.")
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_info = cursor.fetchall()
            db_columns = [col[1] for col in columns_info]

            missing_in_db = [col for col in self.csv_headers if col not in db_columns]
            missing_in_csv = [col for col in db_columns if col not in self.csv_headers]

            validation_message = ""
            if missing_in_db:
                validation_message += f"Columns in CSV missing in DB: {missing_in_db}. "

                reply = self.ask_yes_no(
                    f"Would you like to add {missing_in_db} to {table_name}?"
                )
                if reply:
                    for col in missing_in_db:
                        try:
                            cursor.execute(
                                f"ALTER TABLE {table_name} ADD COLUMN '{col}' TEXT"
                            )
                        except Exception as e:
                            self.status_signal.emit(
                                f"Failed to add column '{col}' to {table_name}: {e}"
                            )
                    self.conn.commit()

                    cursor.execute(f"PRAGMA table_info({table_name})")
                    columns_info = cursor.fetchall()
                    db_columns = [col[1] for col in columns_info]

                    missing_in_db = [
                        col for col in self.csv_headers if col not in db_columns
                    ]

            if missing_in_csv:
                validation_message += (
                    f"Columns in DB missing in CSV: {missing_in_csv}. "
                )
            if not missing_in_db and not missing_in_csv:
                validation_message = "CSV headers match DB table columns."

            self.ui.label_Validate_Headers.setText(validation_message)
            self.status_signal.emit(validation_message)

            if not missing_in_db and not missing_in_csv:
                self.ui.pushButton_Add_to_DB.setEnabled(True)
            else:
                self.ui.pushButton_Add_to_DB.setEnabled(False)

        except Exception as e:
            self.status_signal.emit(f"Header validation failed: {e}")
            self.ui.pushButton_Add_to_DB.setEnabled(False)

    def add_csv_rows_to_db(self):
        if not self.csv_filepath:
            self.status_signal.emit("No CSV file loaded.")
            return

        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            self.status_signal.emit("No DB table selected.")
            return

        try:
            cursor = self.conn.cursor()
            with open(self.csv_filepath, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                inserted_rows = 0
                for row in reader:
                    columns = ", ".join(row.keys())
                    placeholders = ", ".join("?" for _ in row)
                    values = tuple(row[col] for col in row.keys())
                    sql = (
                        f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
                    )
                    cursor.execute(sql, values)
                    inserted_rows += 1
                self.conn.commit()
                self.status_signal.emit(
                    f"Inserted {inserted_rows} rows into {table_name}"
                )
                self.load_table_to_view()
        except Exception as e:
            self.status_signal.emit(f"Error inserting rows: {e}")

    def load_table_to_view(self):
        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            return

        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(self.db_filename)
        if not db.open():
            self.status_signal.emit("Cannot open DB with QSqlTableModel")
            return

        model = QSqlTableModel(self, db)
        model.setTable(table_name)
        model.select()

        self.ui.tableView_DB.setModel(model)
        self.ui.tableView_DB.resizeColumnsToContents()

    def create_sample_table(self):
        table_name, ok = QInputDialog.getText(
            self, "Create new table", "Enter new Table name"
        )
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    email TEXT
                )
                """
            )
            self.conn.commit()
            self.status_signal.emit(f"Created table '{table_name}' (or already exists)")
            self.load_tables_into_combobox()
        except Exception as e:
            self.status_signal.emit(f"Failed to create table: {e}")

    def remove_selected_table(self):
        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            self.status_signal.emit("No table selected to remove.")
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Remove",
            f"Are you sure you want to drop table '{table_name}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirm == QMessageBox.StandardButton.Yes:
            try:
                cursor = self.conn.cursor()
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                self.conn.commit()
                self.status_signal.emit(f"Table '{table_name}' dropped.")
                self.load_tables_into_combobox()
                self.ui.tableView_DB.setModel(None)
            except Exception as e:
                self.status_signal.emit(f"Error dropping table: {e}")

    def export_table_to_csv(self):
        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            self.status_signal.emit("No table selected to export.")
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save CSV File", f"{table_name}.csv", "CSV Files (*.csv)"
        )
        if not file_path:
            return

        try:
            cursor = self.conn.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]

            with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(headers)
                writer.writerows(rows)

            self.status_signal.emit(f"Exported table '{table_name}' to {file_path}")
        except Exception as e:
            self.status_signal.emit(f"Error exporting table: {e}")

    def backup_db(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Backup DB", "backup.db", "Database Files (*.db)"
        )
        if not file_path:
            return

        try:
            self.conn.backup(sqlite3.connect(file_path))
            self.status_signal.emit(f"Backup saved to {file_path}")
        except Exception as e:
            self.status_signal.emit(f"Backup failed: {e}")

    def restore_db(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Restore DB", "", "Database Files (*.db)"
        )
        if not file_path:
            return

        confirm = QMessageBox.question(
            self,
            "Confirm Restore",
            "Restoring will overwrite the current database. Continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if confirm != QMessageBox.StandardButton.Yes:
            return

        try:
            self.conn.close()
            import shutil

            shutil.copyfile(file_path, self.db_filename)
            self.init_db()
            self.load_tables_into_combobox()
            self.status_signal.emit(f"Database restored from {file_path}")
        except Exception as e:
            self.status_signal.emit(f"Restore failed: {e}")

    def search_table(self):
        table_name = self.ui.comboBox_select_table.currentText()
        if not table_name:
            self.status_signal.emit("No table selected for search.")
            return

        search_term, ok = QInputDialog.getText(self, "Search Db", "Find...")

        try:
            cursor = self.conn.cursor()
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns_info = cursor.fetchall()
            text_columns = [col[1] for col in columns_info if col[2] == "TEXT"]

            if not text_columns:
                self.status_signal.emit(
                    "No text columns to search in the selected table."
                )
                return

            where_clauses = " OR ".join([f"{col} LIKE ?" for col in text_columns])
            params = tuple(["%" + search_term + "%"] * len(text_columns))

            sql = f"SELECT * FROM {table_name} WHERE {where_clauses}"
            cursor.execute(sql, params)
            rows = cursor.fetchall()

            if rows:
                headers = [desc[0] for desc in cursor.description]

                self.status_signal.emit(
                    f"Found {len(rows)} matching rows for '{search_term}'."
                )
            else:
                self.status_signal.emit(f"No matches found for '{search_term}'.")

        except Exception as e:
            self.status_signal.emit(f"Search failed: {e}")

    def update_status(self, message):
        self.ui.label_Status.setText(message)
        self.ui.textEdit_Log_Output.append(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


"""
TO DO:

When a new CSV is loaded it will fail to update the table if the data already exists in the table. Need to check if it is required to replace, ignore, or append regardless
"""
