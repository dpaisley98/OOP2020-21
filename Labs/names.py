import datetime

class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def _init_(self, title, f_name, l_name):
        if title not in self.TITLES:
            raise ValueError("Not a valid title: ", title)

        self.title = title
        self.firstname = f_name
        self.lastname = l_name

        today = datetime.datetime.now().strftime("%A")
        if today == "Monday":
            print(today)

p = Person()
p._init_("Ms", "Jina", "Park")
print(p.TITLES)
print(Person.TITLES)
print(p.firstname)
