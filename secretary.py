documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {'1': ['2207 876234', '11-2'],
               '2': ['10006'],
               '3': []
               }


def people_search(doc_list=documents):
    '''Поиск владельца документа по его номеру, по умолчанию используется массив "documents".'''

    while True:
        doc_num = input('Введите номер документа: ')
        for elem in doc_list:
            if doc_num in elem["number"]:
                return f'Владелец документа - {elem["name"]}'
        return f'Такого номера не существует, попробуйте еще раз.'


def shelf_search(shelf_list=directories):
    '''Поиск номера полки по номеру документа, по умолчанию используется массив "directories".'''

    while True:
        doc_num = input('Введите номер документа: ')
        for key, val in shelf_list.items():
            if doc_num in val:
                return f'Документ {doc_num} на полке {key}'
        return 'Такого номера не существует, попробуйте еще раз.'


def list_of_documents(doc_list=documents):
    '''Функция выводит список документов в формате "тип_документа номер_документа имя_владельца",
    по умолчанию используется массив "documents".'''

    list = []
    for elem in doc_list:
        list.append(' '.join(str(x) for x in elem.values()))

    return list


def add_doc(doc_list=documents, shelf_list=directories):
    '''Добавление нового документа в каталог и в перечень полок,
    по умолчанию используются массивы "documents" и "directories".'''

    doc_number = input('Введите номер добавляемого документа: ')
    doc_type = input('Введите тип добавляемого документа: ')
    name = input('Введите имя владельца добавляемого документа: ')
    shelf_number = input('Введите номер полки добавляемого документа: ')

    while shelf_number not in shelf_list.keys():
        shelf_number = input('Такой полки нет, попробуйте снова: ')

    doc_list.append({"type": doc_type, "number": doc_number, "name": name})

    shelf_list.update([(shelf_number, shelf_list.get(shelf_number) + [doc_number])])

    return f'Документ {doc_type} добавлен на {shelf_number} полку.'


def delete_doc(doc_list=documents, shelf_list=directories):
    '''Удаление документа из списка и с полки по его номеру,
    по умолчанию используются массивы "documents" и "directories".'''

    delete_doc = input('Введите номер удаляемого документа: ')

    for id, elem in enumerate(doc_list):
        if elem["number"] == delete_doc:
            del doc_list[id]

    for key, val in shelf_list.items():
        if delete_doc in val:
            val.remove(delete_doc)

    return f'Документ {delete_doc} удален.'


def move_doc(shelf_list=directories):
    '''Перемещение документа на другую полку по его номеру,
    по умолчанию используется массив "directories".'''

    move_doc = input('Введите номер перемещаемого документа: ')
    new_shelf = input('Введите номер целевой полки перемещаемого документа: ')

    for key, val in shelf_list.items():
        if move_doc in val:
            old_shelf = key
            val.remove(move_doc)

    shelf_list.update([(new_shelf,
                        shelf_list.get(new_shelf) + [move_doc]
                        )])

    return f'Документ {move_doc} перемещен с полки {old_shelf} на полку {new_shelf}.'


def add_shelf(shelf_list=directories):
    '''Добавление новой полки, по умолчанию используется массив "directories".'''

    new_shelf = input('Введите номер новой полки: ')

    while new_shelf in shelf_list.keys():
        new_shelf = input('Такая полка уже существует, введите другой номер: ')

    shelf_list[new_shelf] = []
    return f'Полка {new_shelf} создана.'


def secretary_program():
    print('''Программа каталогизации.
        Возможные команды:
        'p' - поиск человека по номеру документа;
        's' - поиск номера полки по номеру документа;
        'l' - вывод списка документов в формате (тип_документа номер_документа имя_владельца);
        'a' - добавление документа в библиотеку;
        'd' - удаление документа из библиотеки;
        'm' - перемещение документа на другую полку;
        'as' - добавление новой полки;
        'q' - выход из программы.''', '\n')

    loop = True
    while loop:
        prg = {'p': people_search,
               's': shelf_search,
               'l': list_of_documents,
               'a': add_doc,
               'd': delete_doc,
               'm': move_doc,
               'as': add_shelf,
               }

        command = input('Введите команду: ')

        if command in prg.keys():
            print(prg[command]())
        elif command == 'q':
            print('Работа программы закончена.')
            break
        else:
            print('Такой команды нет, попробуйте снова: ')


if __name__ == '__main__':
    secretary_program()
