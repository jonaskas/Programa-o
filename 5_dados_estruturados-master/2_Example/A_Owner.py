"""
Owner class
"""

class Owner():

    def __init__(self, name=None):
        self.name = name
        self.address = None
        self.tel = None
        self.email = None

    def __str__(self):
        return "Name: {}\nAddress{}\ntel:{}\nEmail:{}".format(self.name, self.address, self.tel, self.email)

if __name__ == "__main__":
    person = Owner()
    person.name = "John Doe"
    person.address = "Unknown st. nº 123"
    person.tel = "123-1234"
    person.email = "john.doe@mail.com"

    print(person)
    