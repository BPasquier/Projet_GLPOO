"""PySide6 port of the widgets/layouts/basiclayout example from Qt v5.x"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget, QStackedLayout, QInputDialog, QPlainTextDocumentLayout)








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
        self._Mail = QLineEdit("Enter your Email")
        self._Password = QLineEdit("Enter your password")

        button = QPushButton("Signup")
        button.clicked.connect(self.InscriptionDB)

        layout = QVBoxLayout()
        layout.addWidget(self._Name)
        layout.addWidget(self._Mail)
        layout.addWidget(self._Password)
        layout.addWidget(button)

        self._InscriptionMenu.setLayout(layout)

        self._InscriptionMenu.show()

        print("Inscription")

    def connect_User(self):
        self._ConnexionMenu = QGroupBox("Connexion")

        self._Mail = QLineEdit("Enter your email")
        self._Password = QLineEdit("Enter you password")

        button = QPushButton("Connect")
        #button.clicked.connect()

        layout = QVBoxLayout()
        layout.addWidget(self._Mail)
        layout.addWidget(self._Password)
        layout.addWidget(button)

        self._ConnexionMenu.setLayout(layout)

        self._ConnexionMenu.show()


    def InscriptionDB(self):
        print("e")

        self.name = self._Name.text()
        self.email = self._Mail.text()
        self.password = self._Password.text()








