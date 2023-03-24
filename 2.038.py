# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# имя
# номер
# коммент

def menu():
    dict_phnbk = {}
    while True:
        anc = int(input('''Меню:
    1. Показать все контакты
    2. Найти контакт
    3. Добавить контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выход
Выберите пункт меню: '''))

        if anc == 1:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                print(dict_phnbk)
        elif anc == 2:
            cntc_find(dict_phnbk)
        elif anc == 3:
            value_new_cnt = add_cntc(dict_phnbk)
            print(value_new_cnt)
            dict_phnbk.update(value_new_cnt)
            save_dir(dict_phnbk)
        elif anc == 4:
            cntc_change(dict_phnbk)
            save_dir(dict_phnbk)
        elif anc == 5:
            cntc_dell(dict_phnbk)
            save_dir(dict_phnbk)
        elif anc == 6:
            print('End')
            break
        else:
            print('Введите ещё раз')


def open_read_dir():
    dict_phnbk = {}
    with open('phonebook.txt', 'r') as f:
        for line_cntc in f.readlines():
            key, value = line_cntc.strip().split(':')
            dict_phnbk[key] = value
        return dict_phnbk


def save_dir(dict_phnbk):
    str_phnbk = ''
    print(dict_phnbk)
    for key, value in dict_phnbk.items():
        str_phnbk += f'{key}:{value} \n'
    with open('phonebook.txt', 'w') as f:
        f.write(str_phnbk)


def add_cntc(dict_phnbk, new_cntc_in = [0]):
    if len(new_cntc_in) < 2:
        name_cntc = input('Введите Имя: ')
        phone_cntc = input('Введите телефон: ')
        comment_cntc = input('Введите комментарий: ')
        cntc_list = [phone_cntc, comment_cntc]
    else:
        name_cntc, cntc_list = tuple(new_cntc_in)
    dict_phnbk.setdefault(name_cntc, cntc_list)
    print(f'Контакт {name_cntc} добавлен!')
    return dict_phnbk


def cntc_find(dict_phnbk):
    name_cntc = input('Введите Имя: ')
    if name_cntc in dict_phnbk:
        print(f'{name_cntc}: {dict_phnbk[name_cntc]}')
        return [name_cntc, dict_phnbk[name_cntc]]
    else:
        print(f'Не найдено')


def cntc_change(dict_phnbk):
    name_cntc = input('Введите Имя изменяемого контакта: ')
    if name_cntc in dict_phnbk:
        print(f'{name_cntc}: {dict_phnbk[name_cntc]}')
        phone = input('Введите новый номер: ')
        comment = input('Введите новый комментарий: ')
        dict_phnbk[name_cntc] = phone, comment
        print(f'Контакт {name_cntc} изменен!')
    else:
        print(f'Не найдено')


def cntc_dell(dict_phnbk):
    name_cntc = input('Введите Имя для удаления: ')
    if name_cntc in dict_phnbk:
        del dict_phnbk[name_cntc]
        print(f'Контакт {name_cntc} удален!')
    else:
        print(f'Не найдено')
menu()
