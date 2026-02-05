from person import Person

class Customer(Person):
    def __init__(self, name, email):
        super().__init__(name, email)

    def contact_label(self):
        return f"Customer: {self._base_contact_label()}"


