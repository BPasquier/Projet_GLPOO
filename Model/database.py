from user.user import User
from request.request import Request
import sys

class Database:
    def __init__(self):
        self.m_requestList = []
        self.m_userList = []

    def LoadDatabase(self, pathUser, pathRequest):
        try:
            entree = open(pathRequest, "r")
        except:
            sys.exit(f"Impossible de lire le fichier {pathRequest}]")

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
            entree = open(pathUser, "r")
        except:
            sys.exit("Impossible de lire le fichier {file]")

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

                self.m_userList.append(User(userLines[line-4], userLines[line-3], userLines[line-2], tabRequests))

db = Database()
db.LoadDatabase('./user/user_database.txt', './request/request_database.txt')
print(db.m_userList[1].m_requestList[0].m_link)