from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime
import json

class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = float(amount)

    def to_dict(self):
        return {
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

class ExpenseManage:
    def __init__(self, filename='expense.json'):
        self.filename = filename
        self.expenses = []
        self.load_expense()

    def load_expense(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.expenses = [Expense(**exp) for exp in data]

    def save_expenses(self):
        with open(self.filename, "w") as file:
            json.dump([exp.to_dict() for exp in self.expenses], file, indent=4)

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def delete_expense(self, index):
        del self.expenses[index]
        self.save_expenses()

    def update_expense(self, index, expense):
        self.expenses[index] = expense
        self.save_expenses()

    def total_amount(self):
        return sum(exp.amount for exp in self.expenses)

class ExpenseApp:
    def __init__(self, root):
        self.root = root
        self.manager = ExpenseManage()

        self.root.title("Expense Management System")
        self.root.geometry('600x550')

        self.create_widget()
        self.refresh_list()

    def create_widget(self):
        Label(self.root, text="Date (YYYY-MM-DD)", fg="blue").pack()
        self.date_entry = Entry(self.root)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.date_entry.pack()

        Label(self.root, text="Category", fg='blue').pack()
        self.category_entry = Entry(self.root)
        self.category_entry.pack()

        Label(self.root, text="Description", fg='blue').pack()
        self.description_entry = Entry(self.root)
        self.description_entry.pack()

        Label(self.root, text="Amount", fg="blue").pack()
        self.amount_entry = Entry(self.root)
        self.amount_entry.pack()

        Button(self.root, text="Add Expense",
               command=self.add_expense, bg='green').pack(pady=5)

        Button(self.root, text="Update Selected",
               command=self.update_expense, bg='orange').pack(pady=5)

        Button(self.root, text="Delete Selected",
               command=self.delete_expense, bg='red').pack(pady=5)

        self.listbox = Listbox(self.root, width=80)
        self.listbox.pack(pady=10)

        self.listbox.bind("<<ListboxSelect>>", self.load_selected)

        self.total_label = Label(self.root, text="Total: ₹0", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=10)


    def add_expense(self):
        date = self.date_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()
        amount = self.amount_entry.get()

        if not date or not category or not description or not amount:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return

        expense = Expense(date, category, description, amount)
        self.manager.add_expense(expense)

        messagebox.showinfo("Success", "Expense Added!")

        self.refresh_list()
        self.clear_fields()


    def delete_expense(self):
        selected = self.listbox.curselection()
        if selected:
            self.manager.delete_expense(selected[0])
            self.refresh_list()

    def update_expense(self):
        selected = self.listbox.curselection()
        if selected:
            date = self.date_entry.get()
            category = self.category_entry.get()
            description = self.description_entry.get()
            amount = self.amount_entry.get()

            if not date or not category or not description or not amount:
                messagebox.showerror("Error", "All fields required!")
                return

            try:
                float(amount)
            except ValueError:
                messagebox.showerror("Error", "Amount must be number!")
                return

            updated = Expense(date, category, description, amount)
            self.manager.update_expense(selected[0], updated)
            self.refresh_list()
            self.clear_fields()


    def load_selected(self, event):
        selected = self.listbox.curselection()
        if selected:
            exp = self.manager.expenses[selected[0]]

            self.date_entry.delete(0, END)
            self.category_entry.delete(0, END)
            self.description_entry.delete(0, END)
            self.amount_entry.delete(0, END)

            self.date_entry.insert(0, exp.date)
            self.category_entry.insert(0, exp.category)
            self.description_entry.insert(0, exp.description)
            self.amount_entry.insert(0, exp.amount)

    def refresh_list(self):
        self.listbox.delete(0, END)
        for exp in self.manager.expenses:
            self.listbox.insert(
                END,
                f"{exp.date} | {exp.category} | {exp.description} | ₹{exp.amount}"
            )

        self.total_label.config(text=f"Total: ₹{self.manager.total_amount():.2f}")

    def clear_fields(self):
        self.category_entry.delete(0, END)
        self.description_entry.delete(0, END)
        self.amount_entry.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = ExpenseApp(root)
    root.mainloop()