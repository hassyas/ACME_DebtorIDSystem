# Introduction of Code
This is a Python-based Debtor Identification System known as "ACME Debtor Identification System." This system allows the user to operate the debtor information efficiently. It includes features for reading, adding, updating, and deleting debtor records in a database.

    1. Read = Enables the user to read all contents of the database, search by maximum/minimum range of the scores.      or search based on primary key (CIN)
    2. Add/Create = Enables the user to add debtor information into the database
    3. Update = Enables the user to update information of a specific primary key (CIN)
    4. Delete = Enables the user to delete debtor data based on a specific primary key (CIN)

# Breakdown of Score Definition
Credit score details based on BI Checking:

Score 1: Smooth Credit, meaning the borrower always fulfills their obligation to pay installments every month along with interest until it's fully paid off without any delays.

Score 2: DPK Credit or Credit under Special Attention, meaning the borrower is noted for delayed credit installment payments of 1-90 days.

Score 3: Unsmooth Credit, meaning the borrower has recorded late payments of credit installments for 91-120 days.

Score 4: Doubtful Credit, meaning the borrower has recorded late payments of credit installments for 121-180 days.

Score 5: Bad Credit, meaning the borrower has recorded late payments of credit installments for more than 180 days

# Summary of Code Flow 
The uploaded code is a Python program for a Debtor Identification System. It allows users to manage debtor information through a console-based interface. Here's a summary of its flow:

1. The code imports necessary modules, including the `os` module for screen clearing and a custom module named `CRUD` for database operations.

2. It initializes a global flag `clear_needed` to control screen clearing.

3. The `clear_screen` function clears the console screen based on the operating system (Linux/Mac or Windows).

4. The `main_menu` function displays the main menu options, including reading, adding, updating, or deleting debtor records, and exiting the program. It also manages screen clearing.

5. The program defines sub-menus for reading, adding, updating, and deleting debtor records. Each sub-menu handles its specific functionality and can loop until the user decides to return to the main menu.

6. The `main` function is the program's entry point. It initializes the system, displays a welcome message, and checks if the database is available using functions from the `CRUD` module.

7. The main loop in the `main` function continuously displays the main menu, takes user input, and routes the user to the appropriate sub-menu or exits the program based on their choice.

8. The `if __name__ == "__main__"` block ensures that the `main` function is executed when the script is run.

In summary, the code provides a console-based interface for managing debtor records, including reading, adding, updating, and deleting records, with clear screen functionality and a user-friendly menu system. It relies on the `CRUD` module for database operations.

# File Directory
```
├── readme.md          <- The top-level README for developers using this project.
│
├── customer_data.txt  <- Customer database (CIN,Full Name,Birth Date, Address,Credit Score)
│
├── CRUD               <- Folder which contains the various source codes for this project. 
├── main.py            <- Main file for code execution.
├──_pycache_           <- `_pycache_` stores compiled bytecode for faster Python script execution.
```

# Contribute
If you'd like to contribute to ACME Debtor Identification System, check out https://github.com/hassyas/ACME_DebtorIDSystem.git, or feel free to contact me.