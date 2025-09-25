# #1 unittest1
#
# შექმენით Calculator კლასი add, subtract, multiply, divide მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს ყველა მეთოდს.
# გაითვალისწინეთ 0-ზე გაყოფაც.
# გამოიყენეთ unittest მოდული
# გამოიყენეთ setup მეთოდი.

import unittest

class Calculator:
    def __init__(self):
        pass

    def add(self, a,b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise AssertionError("division by zero")
        return a / b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        actual = self.calculator.add(6, 2)
        expected = 8
        self.assertEqual(actual, expected)

    def test_subtract(self):
        actual = self.calculator.subtract(6, 2)
        expected = 4
        self.assertEqual(actual, expected)

    def test_miltiply(self):
        actual = self.calculator.multiply(6, 2)
        expected = 12
        self.assertEqual(actual, expected)

    def test_divide(self):
        actual = self.calculator.divide(6, 2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(AssertionError) as cm:
            self.calculator.divide(20, 0)

# #2 unittest2
#
# შექმენით BankAccount კლასი deposit და withdraw მეთოდებით. დაწერეთ unittest რომელიც ამოწმებს:
#
# - სწორი ბალანსი
#
# - უარყოფითი თანხის შეტანისას შეცდომა
#
# - თანხის გამოტანა ბალანსზე მეტისას შეცდომა

import unittest

class BankAccount:
    def __init__(self):
        self._current_balance = 0

    def check_balance(self):
        return self._current_balance

    def deposit(self, amount):
        self._current_balance += amount

    def withdraw(self, amount):
        self._current_balance -= amount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.balance = BankAccount()

    def test_deposit(self):
        self.balance.deposit(10)
        actual = self.balance.check_balance()
        expected = 10
        self.assertEqual(actual, expected)

    def test_withdraw(self):
        self.balance.deposit(20)
        self.balance.withdraw(5)
        actual = self.balance.check_balance()
        expected = 15
        self.assertEqual(actual, expected)

    def test_initial_balance(self):
        actual = self.balance.check_balance()
        expected = 0
        self.assertEqual(actual, expected)

    def test_negative_withdraw(self):
        self.balance.deposit(5)
        self.balance.withdraw(20)
        actual = self.balance.check_balance()
        expected = -15
        self.assertEqual(actual, expected)

    def test_negative_deposite(self):
        self.balance.deposit(-15)
        actual = self.balance.check_balance()
        expected = -15
        self.assertEqual(actual, expected)