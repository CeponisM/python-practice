import os
import csv

filename = 'todo.csv'
data = []

# Check for file and load or create
if os.path.exists(filename):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    print('TODO list found. Data loaded.')
else:
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['#', 'ToDo'])
    data = [['#', 'ToDo']]
    print("ToDo file does not exist. Created new ToDo list.")


def save_data():
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def main_menu():
    while True:
        print('\n')
        for row in data:
            print(f"{row[0]:<4} {row[1]}")
        print('\n1. Add entry')
        print('2. Remove entry')
        print('3. Edit entry')
        print('4. Clear List')
        print('5. Exit')

        menu_option = input('\nChoose an option: ').strip().lower()

        if menu_option in ['1', 'add']:
            todo_entry = input("ToDo entry: ").strip()
            new_id = str(len(data))  # generate new ID
            data.append([new_id, todo_entry])
            save_data()
            print(f"Added entry #{new_id}")
            main_menu()

        elif menu_option in ['2', 'remove']:
            todo_entry = input("Entry # to remove: ").strip()
            original_len = len(data)
            data[:] = [row for row in data if row[0] != todo_entry or row[0] == '#']
            if len(data) < original_len:
                save_data()
                print(f"Entry #{todo_entry} removed.")
            else:
                print(f"No entry found with ID #{todo_entry}.")
            main_menu()

        elif menu_option in ['3', 'edit']:
            todo_entry_num = input("Entry # to edit: ").strip()
            for i in range(1, len(data)):  # skip header
                if data[i][0] == todo_entry_num:
                    print("Entry selected:", data[i])
                    new_entry = input("Replace entry with: ").strip()
                    data[i][1] = new_entry
                    save_data()
                    print("Entry updated.")
                    break
            else:
                print(f"No entry found with ID #{todo_entry_num}.")
            main_menu()

        elif menu_option in ['4', 'clear']:
            data[:] = [data[0]]  # keep only header
            save_data()
            print("List cleared.")
            main_menu()

        elif menu_option in ['5', 'exit']:
            save_data()
            print("Data saved. Exiting...")
            return

        else:
            print("Invalid option. Please choose 1-5.")

main_menu()