# Bank Management System CLI

## Description

This is a simple Bank Management System developed in Python, utilizing the `pickle` module for data serialization. The system allows users to create accounts, deposit and withdraw money, check balances, and modify or delete accounts.

## Features

- Create a new account
- Deposit money into an account
- Withdraw money from an account
- Check account balance
- List all account holders
- Close an account
- Modify account details

## Code Overview

### Classes

- **Account**: A class to manage account details.

### Functions

- **intro()**: Displays the introductory message.
- **writeAccount()**: Writes a new account to the data file.
- **displayAll()**: Displays all account details.
- **displaySp(num)**: Displays details of a specific account by account number.
- **depositAndWithdraw(num1, num2)**: Handles deposits and withdrawals.
- **deleteAccount(num)**: Deletes an account based on account number.
- **modifyAccount(num)**: Modifies account details.
- **writeAccountsFile(account)**: Writes an account to the data file.

## Setup Instructions

1. **Clone the repository**:
    bash
    git clone https://github.com/YourUsername/BankManagementSystem.git
    

2. **Navigate to the project directory**:
    bash
    cd BankManagementSystem
    

3. **Run the Python script**:
    bash
    python bank_management_system.py
    

## Usage

1. Start the application.
2. Select an option from the menu to perform operations such as creating a new account, depositing money, withdrawing money, checking balance, listing all accounts, closing an account, or modifying account details.

## Sample Output

plaintext
**********************
BANK MANAGEMENT SYSTEM
**********************
Press Enter To Continue:
MAIN MENU
1. NEW ACCOUNT
2. DEPOSIT AMOUNT
3. WITHDRAW AMOUNT
4. BALANCE ENQUIRY
5. ALL ACCOUNT HOLDER LIST
6. CLOSE AN ACCOUNT
7. MODIFY AN ACCOUNT
8. EXIT
Select Your Option (1-8)


## Credits

- **Mustafa Pinjari**: [LinkedIn](https://www.linkedin.com/in/mustafa-pinjari-287625256/) | [GitHub](https://github.com/MustafaPinjari)

Thank you for using the Bank Management System! Feel free to contribute or report any issues.

---

*Happy Coding! 🚀*