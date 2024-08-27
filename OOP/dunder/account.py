class Account:
    def __init__(self, balance: int, account_holder: str):
        self.__balance = balance
        self.__account_holder = account_holder

    def deposit(self, amount: int):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: int):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        return f"Account holder: {self.__account_holder}\nAccount balance: {self.__balance}"

    def __repr__(self):
        return f"Account({self.__balance}, '{self.__account_holder}')"

    def __eq__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance == other.__balance and self.__account_holder == other.__account_holder

    def __qt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance > other.__balance

    def __ge__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance >= other.__balance

    def __lt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance < other.__balance

    def __le__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance <= other.__balance

    def __ne__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance != other.__balance

    def __gt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.__balance > other.__balance


if __name__ == "__main__":
    account1 = Account(100, "Alice")
    account2 = Account(100, "Alice")
    account3 = Account(200, "Bob")

    print(account1 == account2)  # Output: True
    print(account1 == account3)  # Output: False
