## Your Tasks

The `__str__` method of the `Bank` class (in **bank.py**) returns a string containing the accounts in random order. Design and implement a change that causes the accounts to be placed in the string in ascending order of name.

Implement the `__str__` method of the `bank` class so that it sorts the account values before printing them to the console.

In order to sort the account values you will need to define the `__eq__` and `__lt__` methods in the `SavingsAccount` class (in **savingsaccount.py**).

The `__eq__` method should return `True` if the account names are equal during a comparison, `False` otherwise.

The `__lt__` method should return `True` if the name of one account is less than the name of another, `False` otherwise.

The program should output in the following format:

```
Test for createBank:
Name:    Jack
PIN:     1001
Balance: 653.0
Name:    Mark
PIN:     1000
Balance: 377.0
...
...
...
Name:    Name7
PIN:     1006
Balance: 100.0
```

## Instructions

**Task 1**: Modify `__str__` method to return accounts ordered by name.