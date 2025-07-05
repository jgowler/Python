from playwright.sync_api import sync_playwright, Playwright
import threading # Allow app to run in the background
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
import os
from datetime import datetime # Import Date/Time info
from PyQt5.QtWidgets import QMessageBox, QLabel, QMainWindow, QApplication, QFileDialog

# Create / connect to database
connection = sqlite3.connect('bills.db')
# Cursor
c = connection.cursor()
# Create a Table:
c.execute("""CREATE TABLE if not exists bill_list(
          list_bills text)
          """)
# Commit changes:
connection.commit()
# Close connection
connection.close()

# Variables:
today_date = datetime.now().strftime("%d-%m-%Y")
url = "https://tramitacion.senado.cl/appsenado/templates/tramitacion/"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(464, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Save_As_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save_location())
        self.Save_As_pushButton.setGeometry(QtCore.QRect(280, 140, 121, 51))
        self.Save_As_pushButton.setObjectName("Save_As_pushButton")
        self.Download_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.download_files())
        self.Download_pushButton.setEnabled(False)
        self.Download_pushButton.setGeometry(QtCore.QRect(280, 200, 121, 51))
        self.Download_pushButton.setObjectName("Download_pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 256, 181))
        self.listWidget.setObjectName("listWidget")
        self.list_label = QtWidgets.QLabel(self.centralwidget)
        self.list_label.setGeometry(QtCore.QRect(10, 12, 91, 21))
        self.list_label.setObjectName("list_label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(290, 260, 171, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Add_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_bill())
        self.Add_pushButton.setGeometry(QtCore.QRect(180, 40, 81, 23))
        self.Add_pushButton.setObjectName("Add_pushButton")
        self.Remove_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_bill())
        self.Remove_pushButton.setGeometry(QtCore.QRect(10, 260, 75, 23))
        self.Remove_pushButton.setObjectName("Remove_pushButton")
        self.Clear_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.clear_bills())
        self.Clear_pushButton.setGeometry(QtCore.QRect(190, 260, 75, 23))
        self.Clear_pushButton.setObjectName("Clear_pushButton")
        self.entry_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_lineEdit.setGeometry(QtCore.QRect(10, 40, 161, 21))
        self.entry_lineEdit.setText("")
        self.entry_lineEdit.setObjectName("entry_lineEdit")
        self.database_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.save_to_db())
        self.database_pushButton.setGeometry(QtCore.QRect(280, 80, 121, 51))
        self.database_pushButton.setObjectName("database_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 464, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Select a save location")
        MainWindow.setStatusBar(self.statusbar)
        location = ""

        # Get all items from database:
        self.get_db()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BillDownloader"))
        self.Save_As_pushButton.setText(_translate("MainWindow", "Save files to..."))
        self.Download_pushButton.setText(_translate("MainWindow", "Download Bills"))
        self.list_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Bills</span></p></body></html>"))
        self.Add_pushButton.setText(_translate("MainWindow", "Add"))
        self.Remove_pushButton.setText(_translate("MainWindow", "Remove"))
        self.Clear_pushButton.setText(_translate("MainWindow", "Clear"))
        self.database_pushButton.setText(_translate("MainWindow", "Save bills to database"))

### Functions:

    def get_db(self):
        # Connect to DB:
        db = sqlite3.connect('bills.db')
        # Create cursor:
        c = db.cursor()
        # Get all contents form bill_list table:
        c.execute("SELECT * FROM bill_list")
        # Store contents in variable:
        records = c.fetchall()
        # Commit changes:
        db.commit()
        # Close connection to DB:
        db.close()

        for record in records:
            # Returns a tuple from DB, convert to string and select first item in tuple:
            self.listWidget.addItem(str(record[0]))

    def add_bill(self):
        item = self.entry_lineEdit.text()
        self.listWidget.addItem(item)
        self.entry_lineEdit.clear()

    def remove_bill(self):
        clicked = self.listWidget.currentRow()
        self.listWidget.takeItem(clicked)

    def clear_bills(self):
        self.listWidget.clear()

    def save_location(self):
        global location
        location = QFileDialog.getExistingDirectory()
        if location:
            self.Download_pushButton.setEnabled(True)
            self.statusbar.showMessage("Click Download when ready")

    def download_files(self):
        global location, today_date, url
        bill_numbers = []
        prog = 0
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        
        for index in range(self.listWidget.count()):
            item_text = self.listWidget.item(index).text()
            bill_numbers.append(item_text)

        total = len(bill_numbers)
        prog = 0

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, slow_mo=50)
            context = browser.new_context(accept_downloads=True)
            page = context.new_page()
            
            # For each of the bills specified in the .env file...:
            for bill in bill_numbers:
                filename = f"{bill}_{today_date}.xlsx"
                filepath = os.path.join(location, filename)
                self.statusbar.showMessage(f"Downloading {bill} to {location}")
                QApplication.processEvents()

                # Go to the website...
                page.goto(url)
                
                # Perform the following actions...:
                page.fill('input#txtNBoletin', bill)
                page.press('input#txtNBoletin', 'Enter')
                # Wait for the page to load. This can be determined by the network going idle as page will be loaded:
                page.wait_for_load_state('networkidle')
                # Click the button on the site to initiate the document download:
                page.click('button#btnExcel')

                # Set up the download location:
                with page.expect_download() as download_info:
                    download = download_info.value
                    download.save_as(filepath)

                prog += 1
                progress_percent = int((prog / total) * 100)
                self.progressBar.setValue(progress_percent)
                QApplication.processEvents()

            browser.close()
            self.statusbar.showMessage(f"All {len(bill_numbers)} bills have been downloaded to {location}")

    def save_to_db(self):
        db = sqlite3.connect('bills.db')
        c = db.cursor()
        c.execute("DELETE FROM bill_list;")

        for index in range(self.listWidget.count()):
            item_text = self.listWidget.item(index).text()
            c.execute("INSERT INTO bill_list VALUES (?)", (item_text,))
    
        db.commit()
        db.close()

        # Create MessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Saved to database.")
        msg.setText("Your bill numbers have been saved to the database.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
