import csv
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
class ContactBook:
    def __init__(self):
        self._contacts = []
    def add(self, name, phone, email):
        print('name: {}, phone: {}, email: {}'.format(name, phone, email))
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break
    def search(self, name):
        for  contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
            else:
                self._not_found()
    def update(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name==name:
                new_name = input('actualizar el nombre del contacto: ')
                self._contacts[idx].name = new_name
                self._save()
                break
    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))
            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))
    def _print_contact(self, contact):
        print('---*---*---*---*---*---*---*---*---*')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('---*---*---*---*---*---*---*---*---*')
    def _not_found(self):
        print('*******')
        print('¡No Encontrado!')
        print('*******')

def run():
    contact_book = ContactBook()
    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            try:
                print(idx)
                if idx == 0:
                    continue
                contact_book.add(row[0], row[1], row[2])
            except:
                pass
    while True:
        command = str(input('''
        ¿Que deseas hacer?

        [a]ñadir contacto
        [ac]tualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        '''))
        if command == 'a':
            print('añadir contacto')
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telfono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)
        elif command == 'ac':
            print('actualizar contacto')
            name=str(input('Escribe el nombre del contacto: '))
            contact_book.update(name)
        elif command == 'b':
            print('buscar contacto')
            name=str(input('Escribe el nombre del contacto: '))
            contact_book.search(name)
        elif command == 'e':
            print('eliminar contacto')
            name=str(input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
        elif command == 'l':
            print('listar contactos')
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('comando no encontrado')
if __name__ == '__main__':
    run()
