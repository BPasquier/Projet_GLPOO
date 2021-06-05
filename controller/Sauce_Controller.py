import re

from model.dao.member_dao import MemberDAO

class SauceController :

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def Create_Account(self, Pseudo, Mdp):
        with self._database_engine.new_session() as session:
            MemberDAO(session).AddUser(Pseudo, Mdp)

    def Connexion(self, Pseudo, Mdp):
        with self._database_engine.new_session() as session:
            ListeMembres = MemberDAO(session).getAllUsers()
            for membre in ListeMembres:
                if membre.m_nickname == Pseudo and membre.m_password == Mdp:
                    return membre.m_requestList

    def Create_Post(self, Pseudo, texte):
        with self._database_engine.new_session() as session:
            MemberDAO(session).AddRequest(Pseudo, texte)

    def Repondre():


    def Valider():
        
    