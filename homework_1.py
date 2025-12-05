class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_data = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        education = "есть" if self.higher_education else "нет"
        print(f" Меня зовут {self.name}, я родилась {self.birth_data}, по профессии {self.occupation}, "
              f" высшего образования {education}")
person1 = Person("Айдай", 29.11, "доктор", True)
person2 = Person("Атай", 12.4, "певец", False)
person3 = Person("Адина", 25.5, "бухгалтер", True)
person1.introduce()
person2.introduce()
person3.introduce()