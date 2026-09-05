import time
from game import processor, layer
from random import choice

facts = [
    "The word 'calculator' comes from the Latin 'calculi', meaning small stones used for counting.",
    "The world's first mechanical calculator was invented by Blaise Pascal in 1642.",
    "An abacus is considered one of the earliest calculation devices, dating back to around 2700 BC.",
    "The Casio Mini, released in 1972, helped make calculators affordable for everyday people.",
    "Early electronic pocket calculators could cost more than a color television."
]


def get_calc_facts():
    return choice(facts)


def get_number():
    while True:
        try:
            return float(input("Enter a value: "))
        except ValueError:
            print("❌ Please enter a valid number.")


def get_operation():
    operations = ["+", "-", "*", "/", "**", "%", "//"]
    while True:
        operation = input("Enter an operation (+, -, *, /, **, %, //): ").strip()
        if operation in operations:
            return operation
        print("❌ That's not a valid operation.")


def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            return "You can't divide by zero."
        return num1 / num2
    if operation == "**":
        return num1 ** num2
    if operation == "%":
        if num2 == 0:
            return "You can't use zero as the second number here."
        return num1 % num2
    if operation == "//":
        if num2 == 0:
            return "You can't divide by zero."
        return num1 // num2


def yes_or_no():
    while True:
        answer = input("Would you love to continue ").strip().lower()
        if answer == "yes" or answer == "no":
            return answer
        print("❌ Please type yes or no.")


def main(name):
    layer()
    print("\n✨ FARR090 CALCULATOR ✨\n")
    time.sleep(1)
    print(f"\nHey {name}! Welcome to the Farr090 Calculator.\n")
    layer()

    answer = input("Would you like to hear a fun fact about calculators? (yes/no): ").lower()
    if answer == "yes":
        print(f"\nOkay {name} 👍")
        processor()
        time.sleep(1)
        print(f"\nDid you know that:\n{get_calc_facts()}")
        time.sleep(5)
        print("Pretty cool right? 😁\n")
    else:
        print("\nAlright, let's get calculating 👍\n")

    while True:
        layer()
        print("NEW CALCULATION")
        num1 = get_number()
        num2 = get_number()
        operation = get_operation()
        result = calculate(num1, num2, operation)
        processor()
        print(f"{name}, your answer is: {result}")
        layer()

        answer = yes_or_no()

        if answer == "no":
            print(f"\nThanks for using Farr090 Calculator, {name}!")
            time.sleep(1)
            print(f"Here is quick fact before you go \nDid you know that: {get_calc_facts()}")
            print("Calculator closed. 👋")
            break

        print(f"\n🔄 Starting another calculation...")
        print(f"💡 Quick fact: {get_calc_facts()}\n")
        time.sleep(2) 
