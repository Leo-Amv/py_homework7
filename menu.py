from methods import continue_request, create_phone_book, export_data, export_request, find_contact, import_data, show_phonebook
import os


path = 'PhoneBook.csv'
exp_path = 'ExportContact.txt'


def menu(path, exp_path):
    if os.path.getsize(path) == 0:
        create_phone_book(path)
    print('\n\t\t---Phonebook---\n\nSelect menu item:\n\tAdd contact: number "1"\n\tFind contact: number "2"\n\tShow phonebook: number "3"')
    choise = 0
    while choise < 1 or choise > 3:
        try:
            choise = int(input('Enter number:\t'))
        except ValueError:
            print('Incorrect data! You must enter number, try again!')
            continue
        if choise < 1 or choise > 3:
            print('You must enter 1 or 2, try again!')

    if choise == 1:
        import_data(path)
        if continue_request():
            menu(path, exp_path)
    elif choise == 2:
        contact = find_contact(path)
        if contact and export_request():
            export_data(contact, exp_path)
        if continue_request():
            menu(path, exp_path)
    elif choise == 3:
        show_phonebook(path)
        if continue_request():
            menu(path, exp_path)
    else:
        print('ok')
