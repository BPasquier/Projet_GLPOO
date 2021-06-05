import re

from model.database import database


class SauceController :

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def Create_Account(self, Pseudo, Mdp):
        self.AddUser(Pseudo, Mdp)

    def Connexion(self, Pseudo, Mdp):
        ListeMembres = self.getAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo and membre.m_password == Mdp:
                return membre.m_requestList

    def Create_Post(self, Pseudo, texte):
        self.AddRequest(Pseudo, texte)

    def Repondre():


    def Valider():
        
