import re

from model.dao.member_dao import MemberDAO

class SauceController :

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def Create_Account(self, Pseudo, Mdp):
        with self._database_engine.new_session() as session:
            MemberDAO(session).AddAccount(Pseudo, Mdp)

    def Connexion(self, Pseudo, Mdp):
        with self._database_engine.new_session() as session:
            ListeMembres = MemberDAO(session).getAllAccount()
            for membre in ListeMembres:
                if membre[0] == Pseudo and membre[1] == Mdp:
                    return # Return les posts

    def Create_Post(self, Pseudo, texte):
        with self._database_engine.new_session() as session:
            MemberDAO(session).AddPost(Pseudo, texte)

    def Repondre():


    def Valider():
        
    