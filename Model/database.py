from user.user import User
from request.request import Request
import sys
DEFAULT_SAUCE = 50

class Database:
    def __init__(self):
        self.m_requestList = []
        self.m_userList = []

    def LoadDatabase(self):
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
                    tabRequests.append(self.m_requestList[int(id)])

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
        lines.append('0\n')
        lines.append(']\n')

        self.m_userList.append(User(nickname, password, DEFAULT_SAUCE))

        try:
            sortie = open('./user/user_database.txt', "w")
        except:
            sys.exit("Impossible de créer le fichier ./user/user_database.txt")

        sortie.writelines(lines)
        sortie.close()

    def GetAllUsers(self):
        return self.m_userList

db = Database()
db.LoadDatabase()
print(db.GetAllUsers())