import sqlite3
from sys import exit, argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PyQt5.QtCore import Qt
from main_ui import Ui_Form
from addEditCoffeeForm import Ui_MainWindow


class DBCoffee(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.Window)
        self.setupUi(self)
        self.setWindowTitle('DB Coffee')
        with sqlite3.connect('../data/coffee.sqlite') as self.connection:
            result_1 = self.connection.cursor().execute('''SELECT * FROM menu''').fetchall()
            result_2 = self.connection.cursor().execute('''SELECT * FROM sortes''').fetchall()

            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(0)

            for i, row in enumerate(result_1):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

            self.tableWidget_2.setColumnCount(7)
            self.tableWidget_2.setRowCount(0)

            for l, item in enumerate(result_2):
                self.tableWidget_2.setRowCount(self.tableWidget.rowCount() + 1)
                for k, element in enumerate(item):
                    self.tableWidget_2.setItem(l, k, QTableWidgetItem(str(element)))


class Editing(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textEdit.setPlainText('SELECT * FROM menu')
        self.pushButton.clicked.connect(self.edit)

    def edit(self):
        query = self.textEdit.toPlainText()
        with sqlite3.connect('../data/coffee.sqlite') as self.con:
            cur = self.con.cursor()
            cur.execute(query)
        self.result()

    def result(self):
        ex = DBCoffee(self)
        ex.show()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Editing()
    ex.show()
    exit(app.exec_())
