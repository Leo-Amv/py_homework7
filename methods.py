import os


def import_data(path):
    name = input('Enter Full Name:\n')
    number = input('Enter phone number:\n')
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.writelines(f'\n{name}')
        pb.write(f'\t\t{number}')


def export_data(path):
    print('Enter Full Name:')
    contact = input()


def create_phone_book(path):
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.write('\t\t---Phonebook---\n\n')
        pb.write('|Full Name|\t\t\t|Phone number|\n')


# file = open('file.txt', 'r', encoding='utf-8')
# file.close
# if os.path.getsize('file.txt') == 0:
#     print('empty')
# else:
#     print('fill')


# print(os.path.getsize('file.txt'))
