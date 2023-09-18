from . import operations

DB_CUSTOMERS = "customer_data.txt"
TEMPLATE = {
    "Customer_Identification_Number": "XXXXXXXX",
    "Full_Name": "",
    "Birth_Date": "YYYY-MM-DD",
    "Address": "",
    "Credit_Score": "1-5"
}

def init_console():
    try:
        with open(DB_CUSTOMERS,"r") as file:
            print("Database is available")
    except:
        print("Database is not available, please input new database")
        operations.create_first_database()