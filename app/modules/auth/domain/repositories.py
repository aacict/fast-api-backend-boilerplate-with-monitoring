from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def find_by_email(self, email:str):
        pass

    @abstractmethod
    def create_user(self, email:str, hashed_password:str, full_name:str):
        pass