import os


def import_data(path):
    name = input('Enter Full Name:\n')
    number = input('Enter phone number:\n')
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.write(f'\n{name};{number}')


def export_data(phonebook_path, export_path):
    name = input('Enter Full Name:\n')
    phonebook = open(phonebook_path, 'r', encoding='utf-8')
    check_contact = 0
    for contact in phonebook:
        if name in contact:
            print(contact)
            with open(export_path, 'w', encoding='utf-8') as pb:
                pb.write(contact)
        else:
            check_contact += 1
    if check_contact == 0:
        print('This contact is not in the phone book')
    phonebook.close()


def create_phone_book(path):
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.write('\t---Phonebook---\n')
        pb.write('Name;Phone')


# file = open('file.txt', 'r', encoding='utf-8')
# file.close
# if os.path.getsize('file.txt') == 0:
#     print('empty')
# else:
#     print('fill')


# print(os.path.getsize('file.txt'))
