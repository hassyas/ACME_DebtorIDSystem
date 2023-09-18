from . import operations
import re
from . utility import random_CIN
from main import clear_screen
from tabulate import tabulate
from . operations import is_duplicate_cin

def create_console():
    print("Input new debtor database\n")
    
    while True:
        cin = random_CIN(8)  # Generate a random CIN
        if not is_duplicate_cin(cin):
            break

    full_name = input("Full Name:\t")
    address = input("Address:\t")
    
    while True:
        birth_date = input("Birth Date (yyyy-mm-dd):\t")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', birth_date):
            break
        else:
            print("Invalid Birth Date format. Please use yyyy-mm-dd format.")
        
    while True:
        try:
            credit_score = int(input("Credit Score (max 5):\t"))
            if 1 <= credit_score <= 5:  # Check if the input is within the allowed range
                break
            else:
                print("Credit Score must be between 1 and 5.")
        except ValueError:
            print("Credit Score must be an integer.")

    new_debtor_data = f"{cin},{full_name},{birth_date},{address},{credit_score}\n"

    clear_screen()
    print("Here is your new data:")
    print("Credit Identification Number (CIN):", cin)
    print("Full Name:", full_name)
    print("Address:", address)
    print("Birth Date:", birth_date)
    print("Credit Score:", credit_score)

    confirmation = input("Do you want to add this data? (yes/no): ").strip().lower()

    if confirmation == "yes":
        # Append the new debtor data to the customer_data.txt file
        #with open("customer_data.txt", "a",newline="\n") as file:
        operations.write(full_name, birth_date, address, credit_score)
        clear_screen()
        print("Debtor added to the database.")
        return
    else:
        clear_screen()
        print("Data not added.")
        return


def read_console():
    data_file = operations.read()

    header = ["No", "CIN", "Full Name", "Birth Date", "Address", "Credit Score"]
    data = []

    for index, data_line in enumerate(data_file, start=1):
        data_break = data_line.split(",")
             
        cin = data_break[0]
        full_name = data_break[1]
        birth_date = data_break[2]
        address = data_break[3]
        credit_score = data_break[4]

        data.append([index, cin, full_name, birth_date, address, credit_score])

    # Use tabulate to format and print the data
    print(tabulate(data, headers=header, tablefmt="fancy_grid"))

def read_console_by_score(min_score, max_score):
    data_file = operations.read()
    filtered_debtors = []

    filtered_data = []

    for data in data_file:
        data_break = data.split(",")
        Credit_Identification_Number = data_break[0]
        Full_Name = data_break[1]
        Birth_Date = data_break[2]
        Address = data_break[3]
        Credit_Score = data_break[4]

        # Convert the credit_score to an integer and check the range
        if min_score <= int(Credit_Score) <= max_score:
            filtered_data.append([Credit_Identification_Number, Full_Name, Birth_Date, Address, Credit_Score])

    if filtered_data:
        header = ["CIN", "Full Name", "Birth Date", "Address", "Credit Score"]
        print("\nDebtors within the score range:")
        print(tabulate(filtered_data, headers=header, tablefmt="fancy_grid"))
        print("\n")
    else:
        print("No debtors found within the specified score range.")

def read_console_by_cin(target_cin):
    data_file = operations.read()
    filtered_debtors = []

    filtered_data = []

    for data in data_file:
        data_break = data.split(",")
        Credit_Identification_Number = data_break[0]
        Full_Name = data_break[1]
        Birth_Date = data_break[2]
        Address = data_break[3]
        Credit_Score = data_break[4]

        # Check if the CIN matches the target CIN
        if Credit_Identification_Number == target_cin:
            filtered_data.append([Credit_Identification_Number, Full_Name, Birth_Date, Address, Credit_Score])

    if filtered_data:
        header = ["CIN", "Full Name", "Birth Date", "Address", "Credit Score"]
        print("\nDebtors with the specified CIN:")
        print(tabulate(filtered_data, headers=header, tablefmt="fancy_grid"))
        print("\n")
    else:
        print("\n" + "=" * 80)
        print("No debtors found with the specified CIN.")

def update_console():
    read_console()

    while True:
        target_cin = input("Enter the Credit Identification Number (CIN) of the record to update: ")

        # Validate the CIN format (8 alphanumeric characters)
        if not re.match(r'^[a-zA-Z0-9]{8}$', target_cin):
            print("Invalid CIN format. Please enter 8 alphanumeric characters.")
            continue

        # Check if the entered CIN exists in the database
        data_file = operations.read()
        cin_exists = any(target_cin == data.split(",")[0] for data in data_file)

        if not cin_exists:
            print("CIN does not exist in the database. Please enter a valid CIN.")
            continue

        break

    print("Select the columns to update (comma-separated, e.g., Full Name,Address): ")
    columns_to_update = input("Available columns: Full Name, Address, Birth Date, Credit Score\n").strip().split(",")

    existing_full_name = None
    existing_birth_date = None
    existing_address = None
    existing_credit_score = None

    for data in data_file:
        data_break = data.split(",")
        if data_break[0] == target_cin:
            existing_full_name = data_break[1]
            existing_birth_date = data_break[2]
            existing_address = data_break[3]
            existing_credit_score = data_break[4]
            break  # Stop searching once the record is found

    full_name = None
    address = None
    birth_date = None
    credit_score = None

    if "Full Name" in columns_to_update:
        full_name = input("Full Name: ")

    # Check if "Full Name" is not provided (empty input) and include the existing name
    if "Full Name" not in columns_to_update and existing_full_name:
        full_name = existing_full_name  # Use the existing Full Name

    if "Birth Date" in columns_to_update:
        birth_date = input("Birth Date (yyyy-mm-dd): ")

    # Check if "Birth Date" is not provided (empty input) and include the existing birth date
    if "Birth Date" not in columns_to_update and existing_birth_date:
        birth_date = existing_birth_date  # Use the existing Birth Date

    if "Address" in columns_to_update:
        address = input("Address: ")

    # Check if "Address" is not provided (empty input) and include the existing address
    if "Address" not in columns_to_update and existing_address:
        address = existing_address  # Use the existing Address

    if "Credit Score" in columns_to_update:
        while True:
            try:
                credit_score = int(input("Credit Score (max 5): "))
                if 1 <= credit_score <= 5:  # Check if the input is within the allowed range
                    break
                else:
                    print("Credit Score must be between 1 and 5.")
            except ValueError:
                print("Credit Score must be an integer.")
                
    # Check if "Credit Score" is not provided (empty input) and include the existing credit score
    if "Credit Score" not in columns_to_update and existing_credit_score:
        credit_score = existing_credit_score  # Use the existing Credit Score

    clear_screen()
    # Print updated data, including Birth Date, Address, and Credit Score
    print("\nHere is the updated data:")
    if "Full Name" in columns_to_update:
        print("Full Name:", full_name)
    else:
        print("Full Name:", existing_full_name)  # Print the existing Full Name

    if "Birth Date" in columns_to_update:
        print("Birth Date:", birth_date)
    else:
        print("Birth Date:", existing_birth_date)  # Print the existing Birth Date

    if "Address" in columns_to_update:
        print("Address:", address)
    else:
        print("Address:", existing_address)  # Print the existing Address

    if "Credit Score" in columns_to_update:
        print("Credit Score:", credit_score)
    else:
        print("Credit Score:", existing_credit_score)  # Print the existing Credit Score

    confirmation = input("Do you want to update this data? (yes/no): ").strip().lower()

    if confirmation == "yes":
        # Call the update function from operations.py to update the record
        operations.update(target_cin, full_name, birth_date, address, credit_score)
        print("Record updated in the database.")
    else:
        print("Data not updated.")

def delete_console():
    read_console()
    target_cin = input("Enter the Credit Identification Number (CIN) to delete: ")

    # Validate the CIN format (8 alphanumeric characters)
    if not re.match(r'^[a-zA-Z0-9]{8}$', target_cin):
        print("Invalid CIN format. Please enter 8 alphanumeric characters.")
        return

    data_file = operations.read()
    found = False
    updated_data = []

    for data in data_file:
        data_break = data.split(",")
        existing_cin = data_break[0]

        if existing_cin == target_cin:
            confirmation = input("Are you sure you want to delete this data? (yes/no): ").strip().lower()
            if confirmation == "yes":
                print(f"Data with CIN {target_cin} deleted.")
                found = True
                continue  # Skip writing the deleted record back to the file
            else:
                print(f"Data with CIN {target_cin} not deleted.")
                updated_data.append(data)
        else:
            updated_data.append(data)

    if not found:
        print(f"No data found with CIN {target_cin}.")

    try:
        with open("customer_data.txt", "w", newline="\n") as file:
            file.writelines(updated_data)
    except Exception as e:
        print(f"Failed to update data: {e}")