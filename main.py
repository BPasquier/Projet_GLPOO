import sys
import re

from controller.sauce_controller import SauceController
from model.database import Database

def run():
	bdd = Database()
	bdd.LoadDatabase()
	admin_controller = SauceController(bdd)
	
	#print(admin_controller._database_engine.GetAllUsers()[1].m_nickname)


	sys.exit()

if __name__ == '__main__':
	run()