from user.user import User
from request.request import Request
import sys
DEFAULT_SAUCE = 50

class Database:
    def __init__(self):
        self.m_requestList = []
        self.m_userList = []

    def LoadDatabase(self):
        # Chargement des requêtes
        try:
            entree = open('./request/request_database.txt', "r")
        except:
            sys.exit("Impossible de lire le fichier ./request/request_database.txt")

        lines = entree.readlines()
        entree.close()
        requestLines = []
        i = 0
        for j in lines:
            requestLines.append(lines[i].replace('\n', ''))
            i = i + 1

        for line in range(len(requestLines)):
            if requestLines[line] == ']' or requestLines[line] == ']\n':
                self.m_requestList.append(Request(requestLines[line-4], requestLines[line-3], requestLines[line-2], requestLines[line-1]))

        # Chargement des utilisateurs
        try:
            entree = open('./user/user_database.txt', "r")
        except:
            sys.exit("Impossible de lire le fichier './user/user_database.txt'")

        lines = entree.readlines()
        entree.close()
        userLines = []
        i = 0
        for j in lines:
            userLines.append(lines[i].replace('\n', ''))
            i = i + 1

        for line in range(len(lines)):
            if userLines[line] == ']' or userLines[line] == ']\n':
                requests = userLines[line-1].split(',')
                tabRequests = []
                for id in requests:
                    if id.isnumeric():
                        for request in self.m_requestList:
                            if request.m_id == id:
                                tabRequests.append(request)

                self.m_userList.append(User(userLines[line-4], userLines[line-3], userLines[line-2]))
                self.m_userList[len(self.m_userList)-1].m_requestList.append(tabRequests)

    def AddUser(self, nickname, password):
        try:
            entree = open('./user/user_database.txt', "r")
        except:
            sys.exit("Impossible de créer le fichier ./user/user_database.txt")

        lines = entree.readlines()
        entree.close()

        lines.append('[\n')
        lines.append(nickname + '\n')
        lines.append(password + '\n')
        lines.append(str(DEFAULT_SAUCE) + '\n')
        lines.append('\n')
        lines.append(']\n')

        self.m_userList.append(User(nickname, password, DEFAULT_SAUCE))

        try:
            sortie = open('./user/user_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./user/user_database.txt")

        sortie.writelines(lines)
        sortie.close()

    def AddRequest(self, user, link, text, sauce):
        # Ajout de la requête à request_database
        try:
            entree = open('./request/request_database.txt', "r")
        except:
            sys.exit("Impossible d'ouvrir le fichier ./request/request_database.txt")

        lines = entree.readlines()
        entree.close()

        newid = int(lines[len(lines)-5])+1

        lines.append('[\n')
        lines.append(str(newid) + '\n')
        lines.append(link + '\n')
        lines.append(text + '\n')
        lines.append(str(sauce) + '\n')
        lines.append(']\n')

        self.m_requestList.append(Request(newid, link, text, sauce))

        try:
            sortie = open('./request/request_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./request/request_database.txt.txt")

        sortie.writelines(lines)
        sortie.close()

        # Ajout de la requête à son user

        user.m_requestList.append(newid)

        try:
            entree = open('./user/user_database.txt', "r")
        except:
            sys.exit("Impossible d'ouvrir le fichier ./user/user_database.txt")

        lines = entree.readlines()
        entree.close()

        for line in range(len(lines)):
            if user.m_nickname + '\n' == lines[line]:
                if user.m_password + '\n' == lines[line+1]:
                    if len(lines[line+3]) > 1:
                        lines[line+3] = lines[line+3].replace('\n', '') + ',' + str(newid) + '\n'
                    else:
                        lines[line + 3] = lines[line + 3].replace('\n', '') + str(newid) + '\n'

        try:
            sortie = open('./user/user_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./user/user_database.txt")

        sortie.writelines(lines)
        sortie.close()

    def DeleteRequest(self, request):
        try:
            entree = open('./user/user_database.txt', "r")
        except:
            sys.exit("Impossible d'ouvrir le fichier ./user/user_database.txt")

        lines = entree.readlines()
        entree.close()

        # Suppression de la requête de la database
        if request in self.m_requestList:
            self.m_requestList.remove(request)

        # Suppression de la requête de la liste de l'utilisateur
        for user in self.m_userList:
            if request in user.m_requestList:
                user.m_requestList.remove(request)
            # Suppression de la requête de user_database
            for line in range(len(lines)):
                if user.m_nickname + '\n' == lines[line]:
                    if user.m_password + '\n' == lines[line + 1]:
                        if len(lines[line + 3]) > 2:
                            lines[line + 3] = lines[line + 3].replace(',' + request.m_id, '')
                        else:
                            lines[line + 3] = lines[line + 3].replace(request.m_id, '')

        try:
            sortie = open('./user/user_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./user/user_database.txt")

        sortie.writelines(lines)
        sortie.close()

        # Suppression de la requête de request_database
        try:
            entree = open('./request/request_database.txt', "r")
        except:
            sys.exit("Impossible d'ouvrir le fichier ./request/request_database.txt")

        lines = entree.readlines()
        entree.close()

        line = 0
        while line < len(lines):
            if request.m_id + '\n' == lines[line]:
                for i in range(6):
                    lines.pop(line-1)
            line += 1

        try:
            sortie = open('./request/request_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./request/request_database.txt")

        sortie.writelines(lines)
        sortie.close()

    def GetAllUsers(self):
        return self.m_userList

    def GetAllRequests(self):
        return self.m_requestList

db = Database()
db.LoadDatabase()
# db.AddUser('Test', 'Testing')
# db.AddRequest(db.m_userList[2], 'berserk', "quel mangaka ?", 10)
db.DeleteRequest(db.m_requestList[1])
db.AddRequest(db.m_userList[0], 'vimeo.com', 'site?', 10)
print(db.GetAllRequests())
