import json
print("==========EXPENSES TRACKER==========")
print("====================================")
print("             View Menu")
print("====================================")


def calculate_total(expenses):
    return sum([expense['amount'] for expense in expenses])
    # total = 0
    # for expense in expenses:
    #     total = total + expense['amount']
    # total = sum([expense for expense in expenses])
    

#print(calculate_total(expenses))

def calculate_total_by_category(expenses, category):
    return sum([expense['amount'] for expense in expenses if expense['category']== category])
    # total = 0
    # for expense in expenses:
        # if expense['category'] == category:
            # total = total + expense['amount']
    # return total

def add_expense(expenses, amount, category, description):
    if not expenses:
        next_id = 1
    else:
        ids = [expense["id"] for expense in expenses]
        next_id = max(ids) + 1

    new_expense = {
        "id": next_id,
        "amount": amount,
        "category": category,
        "description": description      
    }
    expenses.append(new_expense)

def display_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for expense in expenses:
        print(f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
    

def delete_expense(expenses, expense_id):
    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            return True
    return False

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            return expenses
    except FileNotFoundError:
        print("File does not exist.")
        return []

expenses = load_expenses()

def show_menu():
    print("====================")
    print("1. Add Expenses")
    print("2. Display Expenses")
    print("3. Calculate Expenses Total")
    print("4. Calculate Expenses Total By Category")
    print("5. Delete Expenses")
    print("6. Exit")
    print("====================")


while True:
    show_menu()

    try:

        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:

        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    break
                else:
                    print("Amount must be greater than 0.")
            except ValueError:
                print("Please enter a valid number for amount.")

        category = input("Enter category:").strip().lower()
        
        description = input("Enter description:").strip().lower()
            
        add_expense(expenses, amount, category, description)
        save_expenses(expenses)

        print("Expenses added")
           
    elif choice == 2:
        display_expenses(expenses)

    elif choice == 3:
        print(f"{calculate_total(expenses):.2f}")

    elif choice == 4:
        category = input("Enter category: ")
        print(f"{calculate_total_by_category(expenses, category):.2f}")

    elif choice == 5:
        while True:
            try:
                expense_id = int(input("Enter expense ID to delete: "))
                break
            except ValueError:
                print("Please enter a valid ID")

        deleted = delete_expense(expenses, expense_id)

        if deleted:
            print("Expense deleted")
            save_expenses(expenses)
        else:
            print("Expense not found")

    elif choice == 6:
        print("Exit")
        break
    else:
        print("Invalid choice")



        