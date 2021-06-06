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
	print (admin_controller._database_engine.GetAllUsers()[2].m_sauce)

	#print(admin_controller._database_engine.GetAllUsers()[2].m_nickname)

	sys.exit()

if __name__ == '__main__':
	run()