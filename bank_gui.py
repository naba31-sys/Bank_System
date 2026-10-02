import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

account_numbers = []
account_names = []
balances = []


# =========================
# Add Account
# =========================
def add_account():
    number = number_entry.get()
    name = name_entry.get()
    balance = balance_entry.get()

    if number == "" or name == "" or balance == "":
        messagebox.showerror(
            "Bank System",
            "Please fill all fields"
        )
        return

    if not number.isdigit():
        messagebox.showerror(
            "Bank System",
            "Account number must be a number"
        )
        return

    if not balance.isdigit():
        messagebox.showerror(
            "Bank System",
            "Balance must be a number"
        )
        return

    number = int(number)
    balance = int(balance)

    if number in account_numbers:
        messagebox.showerror(
            "Bank System",
            "Account already exists"
        )
        return

    account_numbers.append(number)
    account_names.append(name)
    balances.append(balance)

    messagebox.showinfo(
        "Bank System",
        "Account Added Successfully"
    )


# =========================
# Show Accounts
# =========================
def show_accounts():
    if len(account_numbers) == 0:
        messagebox.showinfo(
            "Bank System",
            "No accounts found"
        )
        return

    for i in range(len(account_numbers)):
        account_info = (
            f"Number : {account_numbers[i]}\n"
            f"Name : {account_names[i]}\n"
            f"Balance : {balances[i]}"
        )

        messagebox.showinfo(
            "Bank System",
            account_info
        )


# =========================
# Search Account
# =========================
def search_account():
    search_number = search_entry.get()

    if search_number == "":
        messagebox.showerror(
            "Bank System",
            "Please enter account number"
        )
        return

    if not search_number.isdigit():
        messagebox.showerror(
            "Bank System",
            "Account number must be a number"
        )
        return

    search_number = int(search_number)

    if search_number in account_numbers:
        index = account_numbers.index(search_number)

        account_info = (
            f"Number : {account_numbers[index]}\n"
            f"Name : {account_names[index]}\n"
            f"Balance : {balances[index]}"
        )

        messagebox.showinfo(
            "Bank System",
            account_info
        )

    else:
        messagebox.showerror(
            "Bank System",
            "Account Not Found"
        )


# =========================
# Deposit
# =========================
def deposit():
    number = deposit_entry.get()
    amount = deposit_amount_entry.get()

    if number == "" or amount == "":
        messagebox.showerror(
            "Bank System",
            "Please fill all fields"
        )
        return

    if not number.isdigit():
        messagebox.showerror(
            "Bank System",
            "Account number must be a number"
        )
        return

    if not amount.isdigit():
        messagebox.showerror(
            "Bank System",
            "Deposit amount must be a number"
        )
        return

    number = int(number)
    amount = int(amount)

    if amount <= 0:
        messagebox.showerror(
            "Bank System",
            "Deposit amount must be greater than 0"
        )
        return

    if number in account_numbers:
        index = account_numbers.index(number)

        balances[index] = balances[index] + amount

        messagebox.showinfo(
            "Bank System",
            f"Deposit Successful\n"
            f"New Balance : {balances[index]}"
        )

    else:
        messagebox.showerror(
            "Bank System",
            "Account Not Found"
        )


# =========================
# Withdraw
# =========================
def withdraw():
    number = withdraw_entry.get()
    amount = withdraw_amount_entry.get()

    if number == "" or amount == "":
        messagebox.showerror(
            "Bank System",
            "Please fill all fields"
        )
        return

    if not number.isdigit():
        messagebox.showerror(
            "Bank System",
            "Account number must be a number"
        )
        return

    if not amount.isdigit():
        messagebox.showerror(
            "Bank System",
            "Withdraw amount must be a number"
        )
        return

    number = int(number)
    amount = int(amount)

    if amount <= 0:
        messagebox.showerror(
            "Bank System",
            "Withdraw amount must be greater than 0"
        )
        return

    if number in account_numbers:
        index = account_numbers.index(number)

        if amount > balances[index]:
            messagebox.showerror(
                "Bank System",
                "Insufficient Balance"
            )
        else:
            balances[index] = balances[index] - amount

            messagebox.showinfo(
                "Bank System",
                f"Withdraw Successful\n"
                f"New Balance : {balances[index]}"
            )

    else:
        messagebox.showerror(
            "Bank System",
            "Account Not Found"
        )


# =========================
# Delete Account
# =========================
def delete_account():
    number = delete_entry.get()

    if number == "":
        messagebox.showerror(
            "Bank System",
            "Please enter account number"
        )
        return

    if not number.isdigit():
        messagebox.showerror(
            "Bank System",
            "Account number must be a number"
        )
        return

    number = int(number)

    if number in account_numbers:
        index = account_numbers.index(number)

        del account_numbers[index]
        del account_names[index]
        del balances[index]

        messagebox.showinfo(
            "Bank System",
            "Account Deleted Successfully"
        )

    else:
        messagebox.showerror(
            "Bank System",
            "Account Not Found"
        )


# =========================
# GUI
# =========================

root.title("Bank System")
root.geometry("500x600")


# Add Account Frame
account_frame = tk.LabelFrame(
    root,
    text="Add Account",
    padx=10,
    pady=10
)
account_frame.pack(
    padx=20,
    pady=10,
    fill="x"
)


tk.Label(
    account_frame,
    text="Account Number"
).grid(row=0, column=0, padx=5, pady=5)

number_entry = tk.Entry(account_frame)
number_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(
    account_frame,
    text="Account Name"
).grid(row=1, column=0, padx=5, pady=5)

name_entry = tk.Entry(account_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Label(
    account_frame,
    text="Balance"
).grid(row=2, column=0, padx=5, pady=5)

balance_entry = tk.Entry(account_frame)
balance_entry.grid(row=2, column=1, padx=5, pady=5)


button = tk.Button(
    account_frame,
    text="Add Account",
    command=add_account
)
button.grid(
    row=3,
    column=0,
    columnspan=2,
    pady=10
)


# Operations Frame
operations_frame = tk.LabelFrame(
    root,
    text="Account Operations",
    padx=10,
    pady=10
)
operations_frame.pack(
    padx=20,
    pady=10,
    fill="x"
)


# Search
tk.Label(
    operations_frame,
    text="Search Account Number"
).grid(row=0, column=0, padx=5, pady=5)

search_entry = tk.Entry(operations_frame)
search_entry.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(
    operations_frame,
    text="Search Account",
    command=search_account
)
search_button.grid(row=0, column=2, padx=5, pady=5)


# Deposit
tk.Label(
    operations_frame,
    text="Deposit Account Number"
).grid(row=1, column=0, padx=5, pady=5)

deposit_entry = tk.Entry(operations_frame)
deposit_entry.grid(row=1, column=1, padx=5, pady=5)


tk.Label(
    operations_frame,
    text="Deposit Amount"
).grid(row=2, column=0, padx=5, pady=5)

deposit_amount_entry = tk.Entry(operations_frame)
deposit_amount_entry.grid(row=2, column=1, padx=5, pady=5)

deposit_button = tk.Button(
    operations_frame,
    text="Deposit",
    command=deposit
)
deposit_button.grid(row=2, column=2, padx=5, pady=5)


# Withdraw
tk.Label(
    operations_frame,
    text="Withdraw Account Number"
).grid(row=3, column=0, padx=5, pady=5)

withdraw_entry = tk.Entry(operations_frame)
withdraw_entry.grid(row=3, column=1, padx=5, pady=5)


tk.Label(
    operations_frame,
    text="Withdraw Amount"
).grid(row=4, column=0, padx=5, pady=5)

withdraw_amount_entry = tk.Entry(operations_frame)
withdraw_amount_entry.grid(row=4, column=1, padx=5, pady=5)

withdraw_button = tk.Button(
    operations_frame,
    text="Withdraw",
    command=withdraw
)
withdraw_button.grid(row=4, column=2, padx=5, pady=5)


# Delete
tk.Label(
    operations_frame,
    text="Delete Account Number"
).grid(row=5, column=0, padx=5, pady=5)

delete_entry = tk.Entry(operations_frame)
delete_entry.grid(row=5, column=1, padx=5, pady=5)

delete_button = tk.Button(
    operations_frame,
    text="Delete Account",
    command=delete_account
)
delete_button.grid(row=5, column=2, padx=5, pady=5)


# Show Accounts
show_button = tk.Button(
    root,
    text="Show Accounts",
    command=show_accounts
)
show_button.pack(pady=10)


root.mainloop()