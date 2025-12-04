class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_data = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, я родился {self.birth_data}, работаю {self.occupation}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, я одноклассник Байэля,"
              f" учились вместе в {self.group_name}, я родился {self.birth_data}, работаю {self.occupation}")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, я друг Байэля,"
              f" наше любимое хобби  {self.hobby}, я родился {self.birth_data}, работаю {self.occupation}")

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f" наше общее воспоминание {self.shared_memory}")
people = [
    Person('Байэл', '5.12.2000', 'программистом', True),
    Classmate('Бектур', '5.12.2000', 'программистом', True,
              '11-А'),
    Classmate('Айбек', '5.12.2000', 'программистом', True,
              '11-А'),
    Friend('Алмаз', '5.12.2000', 'программистом', False,
           'играть в компьютерные игры',),
    Friend('Нурсултан', '5.12.2000', 'программистом', False,
           'играть в компьютерные игры',),
    BestFriend('Тагай', '3.12.2000', 'доктором', True,
               'играть в компьютерные игры', 'в детстве вместе поехали в лагер')

]
for person in people:
    person.introduce()
