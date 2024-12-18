"""
File: savingsaccount.py
Programming Exercise 10.3
This module defines the SavingsAccount class.
"""

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def getBalance(self):
        """Returns the current balance."""
        return self.balance

    def getName(self):
        """Returns the current name."""
        return self.name

    def getPin(self):
        """Returns the current pin."""
        return self.pin

    def deposit(self, amount):
        """If the amount is valid, adds it
        to the balance and returns None;
        otherwise, returns an error message."""
        self.balance += amount
        return None

    def withdraw(self, amount):
        """If the amount is valid, sunstract it
        from the balance and returns None;
        otherwise, returns an error message."""
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __eq__(self, other):
        """Returns True if names are equal or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        return self.name == other.name

    def __lt__(self, other):
        """Returns True if name of self is less than
        name of other, or False otherwise."""
        return self.name < other.name
