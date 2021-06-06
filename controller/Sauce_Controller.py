import re

class SauceController :

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def Create_Account(self, Pseudo, Mdp):
        ListeMembres = self.getAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo:
                return 1
            else :
                self.AddUser(Pseudo, Mdp)
                return 0

    def Connexion(self, Pseudo, Mdp):
        ListeMembres = self.getAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo and membre.m_password == Mdp:
                return membre.m_requestList

    def Create_Post(self, Pseudo, texte):
        ListeMembres = self.getAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo:
                if membre.m_sauce > 10:
                    membre.m_sauce -= 10
                    self.AddRequest(Pseudo, texte)
                    return 0
        return 1
       

    #def Repondre(self, Pseudo, id_Post):
    #    return 0
        
    #def Valider(self, pseudo, id_Post):
    #    return 0
