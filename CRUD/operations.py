from . import database
from . utility import random_CIN

def create_first_database():
    Full_Name = input("Full Name: (format: First,Last) ")
    Birth_Date = input("Birth Date: (format: YYYY-MM-DD) ")
    Address = input("Address: (format: Street, City) ")
    Credit_Score = input("Credit Score: (format: 1-5) ")

    data = database.TEMPLATE.copy()
    
    data["Credit_Identification_Number"] = random_CIN(8)
    data["Full_Name"] = Full_Name + database.TEMPLATE[ "Full_Name"][len (Full_Name) :]
    data["Birth_Date"] = Birth_Date
    data["Address"] = Address + database.TEMPLATE["Address"][len(Address):]
    data[Credit_Score] = int(Credit_Score)

    data_str = f'{data["Credit_Identification_Number"]},{data["Full_Name"]},{data["Birth_Date"]},{data["Address"]},{Credit_Score}'
    print(data_str)
   
    try:
        with open(database.DB_CUSTOMERS,"w",encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Fail to execute data")
  

    print(data["Credit_Identification_Number"])

def read():
    try:
        with open(database.DB_CUSTOMERS, 'r') as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        print(f"File '{database.DB_CUSTOMERS}' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return []  

def write(Full_Name, Birth_Date, Address, Credit_Score):
    data = database.TEMPLATE.copy()

    data["Credit_Identification_Number"] = random_CIN(8)
    data["Full_Name"] = Full_Name + database.TEMPLATE[ "Full_Name"][len (Full_Name) :]
    data["Birth_Date"] = Birth_Date
    data["Address"] = Address + database.TEMPLATE["Address"][len(Address):]
    data[Credit_Score] = int(Credit_Score)

    data_str = f'{data["Credit_Identification_Number"]},{data["Full_Name"]},{data["Birth_Date"]},{data["Address"]},{Credit_Score}\n'
    print(data_str)
   
    try:
        with open(database.DB_CUSTOMERS,"a",encoding="utf-8", newline="\n") as file:
            file.write(data_str)
    except:
        print("Failed to add data")

def update(target_cin, full_name, birth_date, address, credit_score):
    data_file = read()
    updated_data = []

    for data in data_file:
        data_break = data.split(",")
        existing_cin = data_break[0]

        if existing_cin == target_cin:
            # Update the record with the new data for the specified columns
            if full_name is not None:
                data_break[1] = full_name
            if birth_date is not None:
                data_break[2] = birth_date
            if address is not None:
                data_break[3] = address
            if credit_score is not None:
                data_break[4] = str(credit_score)

        updated_data.append(",".join(data_break))

    try:
        with open(database.DB_CUSTOMERS, "w", encoding="utf-8", newline="\n") as file:
            file.writelines(updated_data)
        print(f"Record with CIN {target_cin} updated in the database.")
    except Exception as e:
        print(f"Failed to update data: {e}")

def delete(target_cin):
    data_file = read()
    updated_data = []

    for data in data_file:
        data_break = data.split(",")
        existing_cin = data_break[0]

        if existing_cin == target_cin:
            continue  # Skip writing the deleted record back to the file

        updated_data.append(data)

    try:
        with open("customer_data.txt", "w", encoding="utf-8", newline="\n") as file:
            file.writelines(updated_data)
        print(f"Record with CIN {target_cin} deleted from the database.")
    except Exception as e:
        print(f"Failed to delete data: {e}")

def is_duplicate_cin(cin_to_check):
    try:
        with open(database.DB_CUSTOMERS, 'r') as file:
            for line in file:
                cin = line.strip().split(',')[0]
                if cin == cin_to_check:
                    print("Duplicate CIN found. Please try again.")
                    return True
        return False
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred while checking for duplicates: {e}")
        return True
