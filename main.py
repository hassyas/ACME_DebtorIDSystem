import os
import CRUD

clear_needed = False  # Initialize a flag to determine if screen clearing is needed

def clear_screen():
    if os.name == 'posix':
        os.system('clear')  # For Unix/Linux/Mac
    elif os.name == 'nt':
        os.system('cls')    # For Windows

def main_menu():
    global clear_needed  # Use the global variable
    if clear_needed:
        clear_screen()
        clear_needed = False  # Set to False after the first run
    else:
        clear_needed = True  # Set to True after subsequent runs
    print("+++++++Main Menu+++++++")
    print("1. Read debtor database")
    print("2. Add new debtor to database")
    print("3. Update existing debtor in database")
    print("4. Delete existing debtor in database")
    print("5. Exit program")

def sub_menu0():
    clear_screen()
    while True:
        print("+++++++Sub Menu Read+++++++")
        print("1. Search all debtor in database")
        print("2. Filter by score range in database")
        print("3. Search by CIN")
        print("4. Back to main menu")

        option = int(input("Enter sub-menu option: "))
        clear_screen()
        if option == 1:
            clear_screen()
            CRUD.read_console()
        elif option == 2:
            clear_screen()
            min_score = int(input("Enter the minimum score: "))
            max_score = int(input("Enter the maximum score: "))
            CRUD.read_console_by_score(min_score, max_score)
        elif option == 3:
            clear_screen()
            target_cin = input("Enter the Credit Identification Number (CIN): ")
            CRUD.read_console_by_cin(target_cin)  # Call the new function for CIN search
        elif option == 4:
            clear_screen()
            return
        else:
            clear_screen()
            print("Invalid option")

def sub_menu1():
    clear_screen()
    while True:
        print("+++++++Sub Menu Add+++++++")
        print("1. Add new debtor to database")
        print("2. Back to main menu")

        option = int(input("Enter sub-menu option: "))
        clear_screen()
        if option == 1:
            clear_screen()
            CRUD.create_console()
        elif option == 2:
            clear_screen()
            return
        else:
            clear_screen()
            print("Invalid option")

def sub_menu2():
    clear_screen()
    while True:
        print("+++++++Sub Menu Update+++++++")
        print("1. Update existing debtor database")
        print("2. Back to main menu")

        option = int(input("Enter sub-menu option: "))
        clear_screen()
        if option == 1:
            clear_screen()
            CRUD.update_console()
        elif option == 2:
            clear_screen()
            return
        else:
            clear_screen()
            print("Invalid option")

def sub_menu3():
    clear_screen()
    while True:
        print("+++++++Sub Menu Delete+++++++")
        print("1. Delete existing debtor database")
        print("2. Back to main menu")

        option = int(input("Enter sub-menu option: "))
        clear_screen()
        if option == 1:
            clear_screen()
            CRUD.delete_console()
        elif option == 2:
            clear_screen()
            return
        else:
            clear_screen()
            print("Invalid option")
        
def main():
    global clear_needed  # Use the global variable
    clear_needed = False # Set it to True initially
    print("===============================================")
    print("WELCOME TO ACME DEBTOR IDENTIFICATION SYSTEM")
    print("DEBTOR IDENTIFICATION MADE EASY!")
    print("PROGRAMMED BY: HASSYA & CO")
    print("===============================================")

    # Check if the database is available or not
    CRUD.init_console()
    print("===============================================")

    option = None

    while option != 0:
        main_menu()
        option = int(input("Enter your option: "))

        if option == 1:
            sub_menu0()
        elif option == 2:
            sub_menu1()
        elif option == 3:
            sub_menu2()
        elif option == 4:
            sub_menu3()
        elif option == 5:
            done_exec = input("Do you want to exit? (yes/no): ")
            if done_exec.lower() == "yes":
                break
            else:
                print("Invalid option")
        else:
            print("Invalid option")

    print("You have exited the program")

if __name__ == "__main__":
    main()