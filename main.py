import sys
import re

from controller.sauce_controller import SauceController
from model.database import Database
from vue.menu import Dialog

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog,
                               QDialogButtonBox, QGridLayout, QGroupBox,
                               QFormLayout, QHBoxLayout, QLabel, QLineEdit,
                               QMenu, QMenuBar, QPushButton, QSpinBox,
                               QTextEdit, QVBoxLayout, QWidget, QStackedLayout, QInputDialog, QPlainTextDocumentLayout)

def run():
	bdd = Database()
	bdd.LoadDatabase()
	admin_controller = SauceController(bdd)
<<<<<<< HEAD
	test = admin_controller.Create_Post("Koufano", "Salut c'est moi et je post un truc c'est qui le papa du fils de naruto ?", "https://www.youtube.com/watch?v=q1wpfoSOgQ0")
	print (test)
=======

	admin_controller.Create_Post("Paul", "ouba", "zefzcsqcqef")
	admin_controller.Create_Post("Paul", "ouba", "zefzcsqcqef")
	admin_controller.Create_Post("Paul", "c'est lui", "zefzcsqcqef")
	admin_controller.Create_Post("Paul", "le marsupilami", "zefzcsqcqef")



	app = QApplication(sys.argv)
	window = Dialog(admin_controller)
	window.show()

	exit(app.exec_())
>>>>>>> 73d569f (Menu complet + Application réponse)

	sys.exit()

if __name__ == '__main__':
	run()