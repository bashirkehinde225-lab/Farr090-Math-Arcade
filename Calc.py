import time
from random import choice
from game import processor, layer


facts = [
    "The word 'calculator' comes from the Latin 'calculi', meaning small stones used for counting.",
    "The world's first mechanical calculator was invented by Blaise Pascal in 1642.",
    "An abacus is considered one of the earliest calculation devices, dating back to around 2700 BC.",
    "The Casio Mini, released in 1972, helped make calculators affordable for everyday people.",
    "Early electronic pocket calculators could cost more than a color television.",

    "Gottfried Wilhelm Leibniz developed a mechanical calculator called the Step Reckoner that could perform addition, subtraction, multiplication, and division.",

    "Charles Babbage designed the Difference Engine, a mechanical machine intended to calculate mathematical tables automatically.",

    "Ada Lovelace wrote an algorithm for Babbage's Analytical Engine and is widely regarded as one of the earliest computer programmers.",

    "The Analytical Engine was designed to use punched cards, an idea inspired by machines used in textile manufacturing.",

    "Mechanical calculators used gears, wheels, and other physical components to perform mathematical operations.",

    "The slide rule was widely used by scientists and engineers before electronic calculators became common.",

    "A slide rule can perform multiplication, division, powers, roots, and other calculations using logarithmic scales.",

    "Logarithms made difficult multiplication and division problems much easier to calculate before electronic calculators existed.",

    "Electronic calculators became much smaller when manufacturers began using integrated circuits instead of large collections of individual electronic components.",

    "The first commercial electronic desktop calculators appeared before pocket calculators became widespread.",

    "Pocket calculators became increasingly affordable during the 1970s as electronic components became smaller and cheaper.",

    "Modern scientific calculators can evaluate trigonometric functions, logarithms, powers, statistics, and many other mathematical operations.",

    "Some calculators can solve equations and manipulate algebraic expressions instead of only performing basic arithmetic.",

    "Calculators use electronic circuits to represent and process numerical information.",

    "A calculator does not 'understand' mathematics like a human does. It follows programmed rules and algorithms to produce results.",

    "Many modern calculators use binary logic internally even though they display numbers using the decimal system.",

    "The decimal system is based on powers of 10, while binary uses only two digits: 0 and 1.",

    "Floating-point calculations allow computers and calculators to represent very large and very small numbers, although some decimal values cannot be represented perfectly in binary floating-point.",

    "The equals button on a calculator tells the device to evaluate the mathematical expression that has been entered.",

    "Calculators can make arithmetic much faster, but understanding the mathematics behind the calculation is still important for checking whether an answer makes sense.",

    "The basic arithmetic operations are addition, subtraction, multiplication, and division.",

    "The percentage symbol is commonly used to represent a value as a fraction of 100.",

    "The square root of a number is a value that, when multiplied by itself, produces the original number.",

    "Exponentiation is a mathematical operation that represents repeated multiplication when the exponent is a positive whole number.",

    "The modulo operation gives the remainder left after one number is divided by another.",

    "Integer division gives the whole-number part of a division result, rather than the full decimal result.",

    "Calculators can be programmed to follow the order of operations so that expressions are evaluated in the correct mathematical sequence.",

    "Parentheses can be used to control the order in which parts of a mathematical expression are calculated.",

    "Computers and calculators can perform millions or even billions of mathematical operations very quickly, depending on their hardware and software.",

    "The mathematics used inside computers includes binary arithmetic, Boolean logic, numerical methods, and algorithms.",

    "Modern computers use processors containing billions of transistors to perform calculations and other operations.",

    "A calculator is essentially a specialized computing device designed to process numerical instructions."
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
        operation = input(
            "Enter an operation (+, -, *, /, **, %, //): "
        ).strip()

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
        answer = input(
            "Would you like to continue? (yes/no): "
        ).strip().lower()

        if answer in ("yes", "no"):
            return answer

        print("❌ Please type yes or no.")


def main(name):
    layer()

    print("\n✨ FARR090 CALCULATOR ✨\n")
    time.sleep(1)

    print(f"Hey {name}! Welcome to the Farr090 Calculator.\n")
    layer()

    answer = input(
        "Would you like to hear a fun fact about calculators? "
        "(yes/no): "
    ).strip().lower()

    while answer not in ("yes", "no"):
        print("❌ Please type yes or no.")

        answer = input(
            "Would you like to hear a fun fact about calculators? "
            "(yes/no): "
        ).strip().lower()

    if answer == "yes":
        print(f"\nOkay, {name}! 👍")
        processor()

        time.sleep(1)

        print(
            f"\nDid you know that:\n{get_calc_facts()}"
        )

        time.sleep(5)

        print("Pretty cool, right? 😁\n")
        time.sleep(1)

    else:
        print("\nAlright, let's get calculating! 👍\n")

    while True:
        layer()

        print("🧮 NEW CALCULATION")

        operation = get_operation()

        num1 = get_number()
        num2 = get_number()

        result = calculate(num1, num2, operation)

        processor()

        print(f"{name}, your answer is: {result}")

        layer()

        answer = yes_or_no()

        if answer == "no":
            print(
                f"\nThanks for using Farr090 Calculator, {name}!"
            )

            time.sleep(1)

            print(
                f"💡 Here is a quick fact before you go:\n"
                f"Did you know that {get_calc_facts()}"
            )

            time.sleep(2)

            print("Calculator closed. 👋")
            break

        print("\n🔄 Starting another calculation...")

        print(
            f"💡 Quick fact: {get_calc_facts()}\n"
        )

        time.sleep(2)