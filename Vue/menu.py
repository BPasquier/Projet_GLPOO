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


class Dialog(QDialog):

    def __init__(self):
        super().__init__()


        self.create_menu()


    def create_menu(self):

        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("CrowdSaucing", self)
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)

        self.create_Inscription()
        self.create_Connexion()


        button_box = QDialogButtonBox(QDialogButtonBox.Cancel)

        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self._menu_bar)
        main_layout.addWidget(self._Inscription)
        main_layout.addWidget(self._Connexion)


        main_layout.addWidget(button_box)

        self.setLayout(main_layout)
        self.setWindowTitle("CrowdSaucing")




    def create_Inscription(self):
        self._Inscription = QGroupBox("Première connexion")
        button = QPushButton("Inscription")
        button.clicked.connect(self.create_User)
        layout = QVBoxLayout()
        layout.addWidget(button)


        self._Inscription.setLayout(layout)


    def create_Connexion(self):
        self._Connexion = QGroupBox("Déjà inscrit ?")
        button = QPushButton("Connexion")
        button.clicked.connect(self.connect_User)
        layout = QVBoxLayout()
        layout.addWidget(button)


        self._Connexion.setLayout(layout)


    def create_User(self):

        self._InscriptionMenu = QGroupBox("Inscription")

        self._Name = QLineEdit("Enter your name")
        self._Password = QLineEdit("Enter your password")

        button = QPushButton("Signup")
        button.clicked.connect(self.InscriptionDB)

        layout = QVBoxLayout()
        layout.addWidget(self._Name)
        layout.addWidget(self._Password)
        layout.addWidget(button)

        self._InscriptionMenu.setLayout(layout)

        self._InscriptionMenu.show()

        print("Inscription")

    def connect_User(self):
        self._ConnexionMenu = QGroupBox("Connexion")

        self._Name = QLineEdit("Enter your nom")
        self._Password = QLineEdit("Enter you password")

        button = QPushButton("Connect")
        button.clicked.connect(self.ConnexionDB)

        layout = QVBoxLayout()
        layout.addWidget(self._Name)
        layout.addWidget(self._Password)
        layout.addWidget(button)

        self._ConnexionMenu.setLayout(layout)

        self._ConnexionMenu.show()


    def InscriptionDB(self):

        self.name = self._Name.text()
        self.password = self._Password.text()

        self._InscriptionMenu.close()

        print(self.name, self.password)


    def ConnexionDB(self):

        self.name = self._Name.text()
        self.password = self._Password.text()

        self._ConnexionMenu.close()

        print(self.name, self.password)




#===================================================================================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dialog()
    window.show()

    exit(app.exec_())







