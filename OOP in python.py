#object oritented programming in python
class Person:
    def __init__(self, name, age):
        self.name = name          # public attribute
        self._age = age           # protected attribute

    def introduce(self):
        return f"My name is {self.name} and I am {self._age} years old."


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"I am {self.name}, a student with ID {self.student_id}."


class Professor(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"I am Prof. {self.name}, I teach {self.subject}."


# ---- Using the classes ----
student = Student("Ali", 21, "CS-102")
professor = Professor("Dr. Ahmed", 45, "Algorithms")

print(student.introduce())
print(professor.introduce())
# Output:
# I am Ali, a student with ID CS-102.
# I am Prof. Dr. Ahmed, I teach Algorithms.
# Example of encapsulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}. New balance: {self.__balance}"
        return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return self.__balance
# ---- Using the BankAccount class ----
account = BankAccount("John Doe", 1000)
print(account.deposit(500))  # Deposited: 500. New balance: 1500
print(account.withdraw(200))  # Withdrew: 200. New balance:
print(account.get_balance())  # 1300
