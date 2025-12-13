class Contact:

    def __init__(self, contact_id, name, phone_number):
        self.id = contact_id
        self.name = name
        self.phone_number = phone_number

    @staticmethod
    def validate_phone_number(phone_number):
        if len(str(phone_number)) == 10 and str(phone_number).isdigit():
            return True
        else:
            return False

    def __str__(self):
        return f"[ID: {self.id}] {self.name}: {self.phone_number}"


class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):
            cls.last_id += 1
            new_id = cls.last_id

            new_contact = Contact(new_id, name, phone_number)

            cls.all_contacts.append(new_contact)
            print(f"Контакт '{name}' (ID: {new_id}) успешно добавлен.")
        else:
            raise ValueError(f"Ошибка валидации номера: '{phone_number}' не содержит ровно 10 цифр.")

    @classmethod
    def remove_contact(cls, contact_id):
        contact_to_remove = None
        for contact in cls.all_contacts:
            if contact.id == contact_id:
                contact_to_remove = contact
                break

        if contact_to_remove:
            cls.all_contacts.remove(contact_to_remove)
            print(f"Контакт (ID: {contact_id}, Имя: {contact_to_remove.name}) удален.")
        else:
            print(f"Ошибка: Контакт с ID {contact_id} не найден.")

    @classmethod
    def display_contacts(cls):
        if not cls.all_contacts:
            print("Список контактов пуст.")
        for contact in cls.all_contacts:
            print(contact)


ContactList.display_contacts()

ContactList.add_contact("Иван", "1234567890")  # ID 1
ContactList.add_contact("Мария", "9876543210")  # ID 2
ContactList.add_contact("Алексей", "5555555555")  # ID 3

ContactList.display_contacts()

print("--- Попытка удалить контакт с ID 2 (Мария) ---")
ContactList.remove_contact(2)

ContactList.display_contacts()

print(f"Последний использованный ID: {ContactList.last_id}")
