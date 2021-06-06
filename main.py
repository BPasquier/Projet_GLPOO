import sys
import re

from controller.sauce_controller import SauceController
from model.database import Database

def run():
	bdd = Database()
	bdd.LoadDatabase()
	admin_controller = SauceController(bdd)
	test = admin_controller.Create_Post("Koufano", "Salut c'est moi et je post un truc c'est qui le papa du fils de naruto ?", "https://www.youtube.com/watch?v=q1wpfoSOgQ0")
	print (test)

	sys.exit()

if __name__ == '__main__':
	run()