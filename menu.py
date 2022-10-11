from methods import create_phone_book, import_data
import os


path = 'PhoneBook.txt'
print('\n\t\t---Phonebook---\n\nSelect menu item:\n\tImport data: number "1"\n\tExport data: number "2"')
choise = 0
while choise < 1 or choise > 2:
    try:
        choise = int(input('Enter number:\t'))
    except ValueError:
        print('Incorrect data! You must enter number, try again!')
        continue
    if choise < 1 or choise > 2:
        print('You must enter 1 or 2, try again!')

if choise == 1:
    if os.path.getsize(path) == 0:
        create_phone_book(path)
    import_data(path)
else:
    print('ok')
