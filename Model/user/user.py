from request import request as Request

class User:
    def __init__(self, p_nickname, p_password, p_sauce, p_requestList: Request):
        self.m_nickname = p_nickname
        self.m_password = p_password
        self.m_sauce = p_sauce
        self.m_requestList = p_requestList
