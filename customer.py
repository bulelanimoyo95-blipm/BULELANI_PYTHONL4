class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def contact_label(self):
        return f"{self.name} <{self.email}>"


class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def contact_label(self):
        return f"Customer: {self.name} <{self.email}>"

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email
        }

