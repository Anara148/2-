from blessed import Terminal
from homework_1 import Person

term = Terminal()

print(term.red + "Apple" + term.normal)
print(term.yellow3 + "banana" + term.normal)
print(term.goldenrod2 + "cherry" + term.normal)
print(term.steelblue3 + "grape" + term.normal)
print(term.mediumorchid + "mango" + term.normal)
print(term.darkturquoise + "orange" + term.normal)
print(term.ivory + "peach" + term.normal)



person1 = Person("Айдана", 19.3, "Учительница", True)
person2 = Person("Адина", 25.5, "Повор", False)
person3 = Person("Мунира", 29.11, "Доктор", True)
person1.introduce()
person2.introduce()
person3.introduce()
