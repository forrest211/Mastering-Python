def add_expense(expenses, amount, category):
    expenses.append({"amount": amount, "category": category})

def print_expenses(expenses):
    for expense in expenses:
        print(expense)
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense["amount"], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense["category"] == category, expenses)

def main():
    expenses = []
    while True:
        print("\nExpense Tracker\n1. Add an expense\n2. List all expenses\n3. Show total expenses")
        print("4. Filter expenses by category\n5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = round(float(input("Enter amount: ")), 2)
            category = input("Enter category: ")
            add_expense(expenses, amount, category)
        
        elif choice == "2":
            print("\nAll Expenses:")
            print_expenses(expenses)

        elif choice == "3":
            print("\nTotal Expenses: ", total_expenses(expenses))
        
        elif choice == "4":
            category = input("Enter a category to filter: ")
            print(f"\nExpenses for {category}:")
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        
        elif choice == "5":
            print("Exiting program.")
            break

        else:
            choice = input("Enter a valid option: ")

if __name__ == "__main__":
    main()