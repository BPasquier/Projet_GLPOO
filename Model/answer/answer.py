from user import user as User

class Answer:
    def __init__(self, p_requestID, p_text, p_user: User):
        self.m_requestID = p_requestID
        self.m_text = p_text
        self.m_user = p_user
