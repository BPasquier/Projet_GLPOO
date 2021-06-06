import sys
import os
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget, QStackedLayout, QInputDialog, QPlainTextDocumentLayout)
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import time




def create_User(self):
    loader = QUiLoader()
    inscription = loader.load("Inscription.ui", None)
    #window.pushButton.clicked.connect(lambda: print("OUI"))

    inscription.show()


def connect_User(self):
    loader = QUiLoader()
    connexion = loader.load("Connexion.ui", None)
    #window.pushButton.clicked.connect(lambda: print("OUI"))

    connexion.show()


def application(self):
    loader = QUiLoader()
    application = loader.load("Application.ui", None)
    #window.pushButton.clicked.connect(lambda: print("OUI"))

    application.show()




#===================================================================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    loader = QUiLoader()
    window = loader.load("menu.ui", None)
    window.pushButton.clicked.connect(connect_User)
    window.pushButton_2.clicked.connect(create_User)
    #window.pushButton_3.clicked.connect(leave)

    window.show()

    exit(app.exec_())







