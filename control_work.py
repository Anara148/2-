class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        old_name = self._name

        self._name = value
        print(f"Имя ({old_name}) изменено на {value}")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            print("Ошибка: возраст не может быть отрицательным!")
            return
        self._age = value
        print(f"Возраст изменен на {value}")

    def make_sound(self):
        return "Животное издает звук"


class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

barsik = Cat("Барсик", 2)
sharik = Dog("Шарик", 4)

print(f"{barsik.name} (возраст {barsik.age} года) говорит: {barsik.make_sound()}")
print(f"{sharik.name} (возраст {sharik.age} года) говорит: {sharik.make_sound()}")

print("-" * 20)

sharik.name = "Рекс"
sharik.age = 3

barsik.name = "Рыжик"
barsik.age = 4

print("-" * 20)

print(f"Теперь {barsik.name}у {barsik.age} года. Говорит: {barsik.make_sound()}")
print(f"Теперь {sharik.name}у {sharik.age} года. Говорит: {sharik.make_sound()}")
