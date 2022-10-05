filename = input('Введите имя файла для чтения: ')
f = open(f'{filename}.txt', encoding='utf-8')
file = f.read().split('\n')
f.close()
database = []


class Contact:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
'''
Иванов Иван,+79042997069,shmelyov.roma@inbox.ru

'''
    def setName(self, newName):
        self.name = newName

    def setNumber(self, newNumber):
        self.number = newNumber

    def setEmail(self, newEmail):
        self.email = newEmail

for i in file:
    buff_lst = i.split(',')
    contact = Contact('Нет данных' if buff_lst[0] == '' else buff_lst[0].strip(),
                      'Нет данных' if buff_lst[1] == '' else buff_lst[1].strip(),
                      'Нет данных' if buff_lst[2] == '' else buff_lst[2].strip())
    database.append(contact)

while True:
    search_input = input('Введите данные для поиска: ')
    if '@' in search_input:
        flag = False
        for i in database:
            if search_input in i.email or search_input == i.email:
                flag = True
                print(f'Вот что нашлось по вашему поиску: {i.name}, {i.number}, {i.email}')
        if not flag:
            print('По вашему запросу ничего не найдено')

    elif '+' in search_input:
        flag = False
        for i in database:
            if search_input in i.number or search_input == i.number:
                flag = True
                print(f'Вот что нашлось по вашему поиску: {i.name}, {i.number}, {i.email}')
        if not flag:
            print('По вашему запросу ничего не найдено')
    elif search_input == 'Контакты без данных':
        flag = False
        for i in database:
            if i.number == 'Нет данных' or i.email == 'Нет данных':
                flag = True
                print(f'Вот что нашлось по вашему поиску: {i.name}, {i.number}, {i.email}')
        if not flag:
            print('По вашему запросу ничего не найдено')

    elif search_input == 'Режим редактирования':
        print('Какой из контактов вы хотите отредактировать? (Введите номер, указанный в скобках в конце контакта)')
        x = 1
        for i in database:
            print(f'{i.name}, {i.number}, {i.email} ({x})')
            x += 1
        editContactNum = int(input())
        if editContactNum < 1 or editContactNum > len(database):
            print('Неверный номер контакта. Просьба заново войти в режим редактирования')
        else:
            contactForEdit = database[editContactNum - 1]
            print(f'Что вы хотите отредактировать в контакте ({contactForEdit.name}, '
                  f'{contactForEdit.number}, {contactForEdit.email})', 'ФИО (1)', 'Телефон (2)', 'email (3)', sep='\n')
            editNum = int(input())
            if editNum == 1:
                contactForEdit.setName(input('Введите новое имя контакта: '))
                print('Контакт успешно изменен')
            elif editNum == 2:
                contactForEdit.setNumber(input('Введите новый номер контакта: '))
                print('Контакт успешно изменен')
            elif editNum == 3:
                contactForEdit.setEmail(input('Введите новый email контакта: '))
                print('Контакт успешно изменен')
            else:
                print('Неверные данные. Просьба заново войти в режим редактирования')

    elif search_input == 'Сохранить изменения':
        filename = input('Введите имя файла для сохранения изменений: ')
        file = open(f'{filename}.txt', 'w', encoding='utf-8')
        for i in database:
            file.write(f'{i.name},{i.number},{i.email}\n')
        file.close()
        print('Изменения успешно сохранены')

    else:
        flag = False
        for i in database:
            if search_input in i.name or search_input == i.name:
                flag = True
                print(f'Вот что нашлось по вашему поиску: {i.name}, {i.number}, {i.email}')
        if not flag:
            print('По вашему запросу ничего не найдено')