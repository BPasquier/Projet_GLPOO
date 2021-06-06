import re

class SauceController :

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def Create_Account(self, Pseudo, Mdp):
        ListeMembres = self._database_engine.GetAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo:
                return 1 #Utlisateur déjà existant
        self._database_engine.AddUser(Pseudo, Mdp)
        return 0 #Utilisateur créé

    def Connexion(self, Pseudo, Mdp):
        ListeMembres = self._database_engine.GetAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo and membre.m_password == Mdp:
                return membre.GetAllRequests()
        return 1

    def Create_Post(self, Pseudo, texte, link):
        ListeMembres = self._database_engine.GetAllUsers()
        for membre in ListeMembres:
            if membre.m_nickname == Pseudo:
                if membre.m_sauce > 10:
                    membre.m_sauce -= 10
                    self._database_engine.AddRequest(membre, link, texte, 10)
                    self._database_engine.UpdateUser(membre)
                    return 0
        return 1
       

    #def Repondre(self, Pseudo, id_Post):
    #    return 0
        
    #def Valider(self, pseudo, id_Post):
    #    return 0
