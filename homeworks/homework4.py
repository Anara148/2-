class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone_number = phone_number
        self.contact_id = contact_id

    @staticmethod
    def validate_phone_number(phone_number):
        return phone_number.isdigit() and len(phone_number) == 10

class ContactList:
    all_contact = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")
        cls.last_id += 1
        new_contact = Contact(name, phone_number, cls.last_id)
        cls.all_contact.append(new_contact)

    @classmethod
    def remove_contact(cls, contact_id):
        len_contact = len(cls.all_contact)
        cls.all_contacts = [
            contact for contact in cls.all_contact
            if contact.contact_id != contact_id
        ]

        if len(cls.all_contact) == len_contact:
            print(f"Ошибка: Контакт с ID {contact_id} не найден.")

print(ContactList.all_contact)
ContactList.add_contact("Вася Печкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contact:
    print(contact.name, contact.phone_number)
#ContactList.add_contact("John Doe", "5551234")

print(ContactList.last_id)

ContactList.add_contact("Вася Пупкин", "0703100222")
ContactList.add_contact("Виктор Романов", "0501123459")
ContactList.add_contact("Саша Трусова", "0702101200")
print(ContactList.last_id)

ContactList.remove_contact(3)
ContactList.remove_contact(5)

for contact in ContactList.all_contact:
    print(contact.name, contact.phone_number, contact.contact_id)