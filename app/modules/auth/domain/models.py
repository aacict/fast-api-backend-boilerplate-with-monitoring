class User:
    def __init__(self, email: str, password_hash: str, full_name: str):
        self.email = email
        self.password_hash = password_hash
        self.full_name = full_name
