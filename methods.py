import os


def import_data(path):
    name = input('Enter Full Name:\n')
    number = input('Enter phone number:\n')
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.write(f'\n{name};{number}')


def export_request():
    answer = input('\nDo you want to export contact? Enter: "y" or "n"\t')
    if answer == 'y':
        return True
    else:
        return False


def continue_request():
    answer = input('\nDo you want to continue? Enter: "y" or "n"\t')
    if answer == 'y':
        return True
    else:
        return False


def export_data(contact, export_path):
    with open(export_path, 'w', encoding='utf-8') as export_file:
        export_file.write(contact)


def find_contact(phonebook_path):
    name = input('Enter Full Name:\n')
    phonebook = open(phonebook_path, 'r', encoding='utf-8')
    phonebook.seek(29)
    found = False
    for contact in phonebook:
        if name in contact:
            found = True
            print(f'Found contact:\t{contact}')
            return contact
    if not found:
        print('This contact is not in the phone book')
        return False
    phonebook.close()


def create_phone_book(path):
    with open(path, 'a+', encoding='utf-8') as pb:
        pb.write('\t--Phonebook--\n')
        pb.write('Name;Phone')


def show_phonebook(path):
    phonebook = open(path, 'r', encoding='utf-8')
    for line in phonebook:
        print(line)
    phonebook.close
