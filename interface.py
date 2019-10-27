# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtInterface1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import csv
import numpy as np
import file_translator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QTableWidget, QTableWidgetItem

"""
Global Methods
"""
def init_label(window, text, x = 0, y = 0):
    """
    initializes QLabel objects
    window - window which label will be initialized on
    text - label text
    x - x-coordinate
    y - y-coordinate
    """
    label = QLabel(text, window)
    label.move(x,y)
    return label

def init_textbox(window, width = 0, height = 0, x = 0, y = 0):
    """
    initializes QLineEdit objects
    window - window which QLineEdit will be initialized on
    width - width of QLineEdit
    height - height of QLineEdit
    x - x-coordinate
    y - y-coordinate
    """
    textbox = QLineEdit(window)
    textbox.move(x,y)
    textbox.resize(width, height)
    return textbox

def init_button(window, text, func, x = 0, y = 0):
    """
    initializes QPushButton object
    window - window which QPushButton will be initialized on
    text - button text
    func - linked function to button
    x - x-coordinate
    y - y-coordinate
    """
    button = QPushButton(text, window)
    button.clicked.connect(func)
    button.move(x, y)
    return button
"""
classes
"""
class Registration(QWidget):
    """
    First page of app
    Registers new user into database
    based on information provided in
    textboxes
    """
    def __init__(self):
        """
        Initializes window dimmensions to 640 x 480
        """
        super().__init__()
        self.title = "Class Schedule App"
        
        #Window Dimmensions
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        
    def initUI(self):
        """
        Initializes UI components
        """
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # label and textbox for income
        self.class_label = init_label(self, "Class", 20, 80)
        self.class_textbox = init_textbox(self, 140, 40, 80, 80)
        
        # Create a button in the window
        self.button = init_button(self, 'Register', self.on_click, 80, 200)

        # Creates table to see all user information
        self.class_display = QTableWidget(self)
        self.class_display.move(260, 20)
        #self.update_name_table()
        self.classes = []
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        new_class = self.class_textbox.text().strip()
        self.classes.append(new_class)
        self.class_display.setRowCount(len(self.classes))
        self.class_display.setColumnCount()
        self.class_display.setHorizontalHeaderLabels(["Class"])
        for count, clas in enumerate(self.classes):
            self.class_display.setItem(count, 0, QTableWidgetItem(clas))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Registration()
    MainWindow.show()
    sys.exit(app.exec_())
