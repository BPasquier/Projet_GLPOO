import sys
DEFAULT_SAUCE = 50

def GetLines(path):
    try:
        entree = open(path, "r")
    except:
        sys.exit(f"Impossible de lire le fichier {path}")

    lines = entree.readlines()
    entree.close()
    return lines

def OutputLines(path, lines):
    try:
        sortie = open(path, "w")
    except:
        sys.exit(f"Impossible d'ouvrir le fichier {path}")

    sortie.writelines(lines)
    sortie.close()

class User:
    def __init__(self, p_nickname, p_password, p_sauce):
        self.m_nickname = p_nickname
        self.m_password = p_password
        self.m_sauce = p_sauce
        self.m_requestList = []

class Request:
    def __init__(self, p_id, p_link, p_text, p_sauce):
        self.m_id = p_id
        self.m_link = p_link
        self.m_text = p_text
        self.m_sauce = p_sauce
        self.m_answerList = []

class Answer:
    def __init__(self, p_requestID, p_text, p_user: User):
        self.m_requestID = p_requestID
        self.m_text = p_text
        self.m_user = p_user


class Database:
    def __init__(self):
        self.m_requestList = []
        self.m_userList = []

    def LoadDatabase(self):
        # Chargement des requêtes
        lines = GetLines('./model/request_database.txt')
        print('a')
        requestLines = []
        i = 0
        for j in lines:
            requestLines.append(lines[i].replace('\n', ''))
            i = i + 1

        for line in range(len(requestLines)):
            if requestLines[line] == ']' or requestLines[line] == ']\n':
                self.m_requestList.append(Request(requestLines[line-4], requestLines[line-3], requestLines[line-2], requestLines[line-1]))

        # Chargement des utilisateurs
        lines = GetLines('./model/user_database.txt')
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
                self.m_userList[len(self.m_userList)-1].m_requestList = tabRequests

        # Chargement des réponses
        lines = GetLines('./model/answer_database.txt')
        answerLines = []
        i = 0
        for j in lines:
            answerLines.append(lines[i].replace('\n', ''))
            i = i + 1

        for line in range(len(answerLines)):
            if answerLines[line] == ']':
                for request in self.m_requestList:
                    if answerLines[line-3] == request.m_id:
                        for user in self.m_userList:
                            if user.m_nickname == answerLines[line-1]:
                                request.m_answerList.append(Answer(request.m_id, answerLines[line-2], user))

    def AddUser(self, nickname, password):
        lines = GetLines('./model/user_database.txt')

        lines.append('[\n')
        lines.append(nickname + '\n')
        lines.append(password + '\n')
        lines.append(str(DEFAULT_SAUCE) + '\n')
        lines.append('\n')
        lines.append(']\n')

        self.m_userList.append(User(nickname, password, DEFAULT_SAUCE))

        OutputLines('./model/user_database.txt', lines)

    def AddRequest(self, user, link, text, sauce):
        # Ajout de la requête à request_database
        lines = GetLines('./model/request_database.txt')

        if len(lines) > 5:
            newid = int(lines[len(lines)-5])+1
        else:
            newid = 0

        lines.append('[\n')
        lines.append(str(newid) + '\n')
        lines.append(link + '\n')
        lines.append(text + '\n')
        lines.append(str(sauce) + '\n')
        lines.append(']\n')

        self.m_requestList.append(Request(newid, link, text, sauce))

        OutputLines('./model/request_database.txt', lines)

        # Ajout de la requête à son user

        user.m_requestList.append(self.m_requestList[len(self.m_requestList) - 1])

        lines = GetLines('./model/user_database.txt')

        for line in range(len(lines)):
            if user.m_nickname + '\n' == lines[line]:
                if user.m_password + '\n' == lines[line+1]:
                    if len(lines[line+3]) > 1:
                        lines[line+3] = lines[line+3].replace('\n', '') + ',' + str(newid) + '\n'
                    else:
                        lines[line + 3] = lines[line + 3].replace('\n', '') + str(newid) + '\n'

        OutputLines('./model/user_database.txt', lines)

    def AddAnswer(self, request, text, user):
        # Ajout de la réponse à answer_database
        lines = GetLines('./model/answer_database.txt')
        requestid = request.m_id

        lines.append('[\n')
        lines.append(str(requestid) + '\n')
        lines.append(text + '\n')
        lines.append(user.m_nickname + '\n')
        lines.append(']\n')

        OutputLines('./model/answer_database.txt', lines)

        # Ajout de la réponse à sa requête
        for dbrequest in self.m_requestList:
            if dbrequest.m_id == requestid:
                dbrequest.m_answerList.append(Answer(requestid, text, user))

    def DeleteRequest(self, request):
        lines = GetLines('./model/user_database.txt')

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
                            lines[line + 3] = lines[line + 3].replace(',' + str(request.m_id), '')
                        else:
                            lines[line + 3] = lines[line + 3].replace(str(request.m_id), '')

        OutputLines('./model/user_database.txt', lines)

        # Suppression de la requête de request_database
        lines = GetLines('./model/request_database.txt')

        line = 0
        while line < len(lines):
            if str(request.m_id) + '\n' == lines[line] and lines[line-1] == '[\n':
                for i in range(6):
                    lines.pop(line-1)
            line += 1

        OutputLines('./model/request_database.txt', lines)

    def DeleteUser(self, user):
        lines = GetLines('./model/request_database.txt')

        # Suppression des requêtes associées à l'utilisateur
        while len(user.m_requestList) != 0:
            self.DeleteRequest(user.m_requestList[0])

        # Suppression de l'utilisateur
        if user in self.m_userList:
            self.m_userList.remove(user)

        line = 0
        while line < len(lines):
            if user.m_nickname + '\n' == lines[line]:
                if user.m_password + '\n' == lines[line+1]:
                    for i in range(6):
                        lines.pop(line - 1)
            line += 1

        OutputLines('./model/request_database.txt', lines)

    def DeleteAnswer(self, answer):
        lines = GetLines('./model/answer_database.txt')

        for request in self.m_requestList:
            if answer in request.m_answerList:
                request.m_answerList.remove(answer)

        line = 0
        while line < len(lines):
            if answer.m_requestID + '\n' == lines[line]:
                if answer.m_text + '\n' == lines[line+1]:
                    if answer.m_user.m_nickname + '\n' == lines[line + 2]:
                        for i in range(5):
                            lines.pop(line - 1)
            line += 1

        OutputLines('./model/answer_database.txt', lines)

    def GetAllUsers(self):
        return self.m_userList

    def GetAllRequests(self):
        return self.m_requestList
'''
db = Database()
db.LoadDatabase()

db.AddUser('Nick', 'Testing')
db.AddRequest(db.m_userList[1], 'image1.png', "source ?", 10)
db.AddRequest(db.m_userList[1], 'image1.png', "source ?", 10)

# db.DeleteAnswer(db.m_userList[0].m_requestList[0].m_answerList[0])
# db.AddAnswer(db.m_requestList[0], "Kentaro Miura RIP", db.m_userList[0])
# db.DeleteRequest(db.m_requestList[1])
# db.AddRequest(db.m_userList[0], 'yahoo.com', 'site?', 10)
# db.DeleteUser(db.m_userList[1])
print(db.m_userList[0].m_requestList[0].m_answerList[1].m_user.m_nickname)
'''