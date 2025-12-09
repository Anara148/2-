from datetime import datetime
class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.__birth_date = datetime.strptime(birth_date, "%d.%m.%Y")
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def age(self):
        today = datetime.today()
        year = today.year - self.__birth_date.year
        if (today.month, today.day) < (self.__birth_date.month, self.__birth_date.day):
            year -= 1
        return year
    @property
    def birth_date(self):
        return self.__birth_date.strftime("%d.%m.%Y")
    @property
    def occupation(self):
        return self.__occupation
    @property
    def higher_education(self):
        education = "есть" if self.__higher_education else "нет"
        return education
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, я родился {self.birth_date}, мне {self.age} лет, "
              f" работаю {self.occupation}, у меня {self.higher_education} высшее образования ")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, classmate_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        self.classmate_name = classmate_name
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, мне {self.age} лет, я одноклассник {self.classmate_name},"
              f" учились вместе в {self.group_name}, я родился {self.birth_date}, работаю {self.occupation}"
              f" у меня {self.higher_education} высшее образования")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_name = friend_name
    def introduce(self):
        print(f" Привет, меня зовут {self.name}, мне {self.age} лет, я друг {self.friend_name},"
              f" наше любимое хобби  {self.hobby}, я родился {self.birth_date}, работаю {self.occupation}"
              f" у меня {self.higher_education} высшего образования")


people = [
    Person('Байэл', '5.12.2000', 'программистом', True),
    Classmate('Бектур', '5.12.2000', 'программистом', True,
              '11-А', 'Байэля'),
    Classmate('Айбек', '5.12.2000', 'программистом', True,
              '11-А', 'Байэля'),
    Friend('Алмаз', '5.12.2000', 'программистом', False,
           'играть в компьютерные игры', 'Байэля'),
    Friend('Нурсултан', '5.12.2000', 'программистом', False,
           'играть в компьютерные игры', 'Байэля')


]
for person in people:
    person.introduce()
