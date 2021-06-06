"""PySide6 port of the widgets/layouts/basiclayout example from Qt v5.x"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget)


class Dialog(QDialog):
    num_grid_rows = 3
    num_buttons = 4

    def __init__(self):
        super().__init__()

        self.create_menu()
        self.create_Inscription()
        self.create_Connexion()

        #self.create_grid_group_box()
        #self.create_form_group_box()


        button_box = QDialogButtonBox(QDialogButtonBox.Cancel)

        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.setMenuBar(self._menu_bar)
        main_layout.addWidget(self._Inscription)
        main_layout.addWidget(self._Connexion)

        main_layout.addWidget(button_box)
        self.setLayout(main_layout)

        self.setWindowTitle("CrowdSaucing")

    def create_menu(self):
        self._menu_bar = QMenuBar()

        self._file_menu = QMenu("CrowdSaucing", self)
        self._exit_action = self._file_menu.addAction("E&xit")
        self._menu_bar.addMenu(self._file_menu)

        self._exit_action.triggered.connect(self.accept)

    def create_Inscription(self):
        self._Inscription = QGroupBox("Première connexion")
        button = QPushButton("Inscription", self)
        button.click()
        layout = QVBoxLayout()
        layout.addWidget(button)


        self._Inscription.setLayout(layout)


    def create_Connexion(self):
        self._Connexion = QGroupBox("Déjà inscrit ?")
        button = QPushButton("Connexion")
        layout = QVBoxLayout()
        layout.addWidget(button)


        self._Connexion.setLayout(layout)


    def CreateUser(self):
        1 == 1





if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec())