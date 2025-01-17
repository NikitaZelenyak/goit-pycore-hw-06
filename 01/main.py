from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
           if len(value) <= 0:
                  print("Add name")
                  return
           else:
                super().__init__(value)
              

class Phone(Field):
      def __init__(self, value):
            if len(value) == 10:
                  super().__init__(value)
            else:
                  print("Phone must contain 10 symbols")
    

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
          self.phones.append(Phone(phone))
    def find_phone(self, phone):
          for number in self.phones:
                if number.value == phone:
                      return number
    def edit_phone(self, phone, new_phone):
          for index in range(len(self.phones)):
                if self.phones[index] == phone:
                      self.phones[index]= new_phone
                      return
    def remove_phone(self, phone):
          self.phones.remove(phone.value)

    def __str__(self):
       return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
            def __init__(self):
                super().__init__() 
                self.records = []
            def add_record(self, record):
                self.records.append(record)
            def find(self, name):
                for record in self.records:
                    if record.name.value == name:
                         return record
            def delete(self, name):
                 for record in self.records:
                      if record.name.value == name:
                           self.records.remove(record)
                           return

                      
            

# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)



    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")
