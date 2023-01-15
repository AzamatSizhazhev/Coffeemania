import sqlite3
from sys import exit, argv
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt5 import uic


class DBCoffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        with sqlite3.connect('coffee.sqlite') as self.connection:
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


if __name__ == '__main__':
    app = QApplication(argv)
    ex = DBCoffee()
    ex.show()
    exit(app.exec_())
