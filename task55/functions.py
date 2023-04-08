def show_data() -> None:
    '''Выводит информацию из справочника'''
    with open('book.txt', 'r', encoding='utf-8') as f:
        print(f.read())


def add_data() -> None:
    '''Добавляет информацию в справочник'''
    fio = input('Введите ФИО: ')
    tel_number = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as f:
        f.write(f'\n{fio}| {tel_number}')
    print('Успешно!')


def find_data() -> None:
    '''Осуществляет поиск по справочнику'''
    data = input('Введите данные для поиска: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.read()
    print("Результаты поиска: ")
    print(search(tel_book, data))


def search(book: str, info: str) -> str:
    '''Находит в строке записи по определенному критерию поиска'''
    book = book.split('\n')
    return '\n'.join([post for post in book if info in post])


def change_data() -> None:
    '''Изменяет данные в справочнике'''
    data = input('Введите имя или фамилию для изменения данных: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.readlines()
    changed = False
    with open('book.txt', 'w', encoding='utf-8') as f:
        for i, line in enumerate(tel_book):
            if data in line:
                print(f'Найдена запись: {line}')
                new_fio = input('Введите новое ФИО: ')
                new_tel_number = input('Введите новый номер телефона: ')
                if len(new_fio) == 0:
                    new_fio = line.split(' | ')[0]
                if len(new_tel_number) == 0:
                    new_tel_number = line.split(' | ')[1]
                tel_book[i] = f'{new_fio} | {new_tel_number}\n'
                print('Запись изменена успешно')
                changed = True
        f.writelines(tel_book)
    if not changed:
        print('Запись не найдена')


def remove_data() -> None:
    '''Удаляет данные из справочника'''
    data = input('Введите имя или фамилию для удаления данных: ')
    with open('book.txt', 'r', encoding='utf-8') as f:
        tel_book = f.readlines()
    deleted = False
    with open('book.txt', 'w', encoding='utf-8') as f:
        for line in tel_book:
            if data not in line:
                f.write(line)
            else:
                deleted = True
        if deleted:
            print('Запись удалена успешно')
        else:
            print('Запись не найдена')