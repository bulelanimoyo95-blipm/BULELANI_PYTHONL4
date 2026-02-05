from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def _base_contact_label(self):
        return f"{self.name} <{self.email}>"

    @abstractmethod
    def contact_label(self):
        pass

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }
