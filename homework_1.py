class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_data = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
person1 = Person("Айдай", 29.11, "доктор", True)
person2 = Person("Атай", 12.4, "певец", False)
person3 = Person("Адина", 25.5, "бухгалтер", True)
print(f" Меня зовут {person1.name}, я родилась {person1.birth_data}, по профессии {person1.occupation}, "
      f" высшего образования есть ({person1.higher_education})")
print(f" Меня зовут {person2.name}, я родился {person2.birth_data}, по профессии {person2.occupation}, "
      f" высшего образования нет ({person2.higher_education})")
print(f" Меня зовут {person3.name}, я родилась {person3.birth_data}, по профессии {person3.occupation}, "
      f" высшего образования есть ({person3.higher_education})")