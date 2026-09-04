import time
from game import xo, processor, layer
from Quiz import qfirst
from coffe_ import cof
from shapes import main_shape, get_facts
from Calc import main


codm = "Alexcia"

print(f"🤖 Hello, my name is {codm}!")

name = input("👤 What is your name: ").lower().strip()

while any(char.isdigit() for char in name) or any(not char.isalpha() for char in name):

    print("❌ Invalid Response")

    name = input("👤 What is your name: ").lower().strip()
while True:
    if name == "":

        print("❌ This field can't be empty!")

        name = input("👤 What is your name: ").lower().strip()

    else:

        print(f"😊 Nice to meet you {name}!")

        break

layer()
time.sleep(1)

print(
    f"🤖 So {name}, I am {codm}, an Arithmetic and Logical Assistant "
    f"and I am always at your service!"
)

print(f"🎮 I, {codm}, welcome you to the Farr090 Math Arcade!")

services = {
    "Mathematical Calculations":
        "➕ Addition, ➖ Subtraction, ➗ Division, ✖️ Multiplication, Powers and Roots",

    "Math Quiz":
        "🧠 Choosing math questions and answering them",

    "Shapes":
        "📐 Understanding different shapes, their properties and calculations",

    "Coffee Shop":
        "☕ Visit the official lounge of the Math Arcade",

    "Games Store":
        "🎮 Play games that suit your curious and diverse mind"
}
time.sleep(1)

print(f"\n🎯 So {name}, here is a list of my services:\n")

time.sleep(1)
for service, description in services.items():
    print(f"🔹 {service} → {description}")


layer()


def main_section():

    while True:
        time.sleep(7)

        main_option = input(
            f"\n🤔 So which of my services may I offer you {name}? "
        ).lower().strip()

        if main_option == "math quiz":

            processor()

            print(f"💡 Here is another fun fact for you {name}!")
            time.sleep(1)

            layer()

            print(f"🧠 So {name}, do you know that {get_facts()}?")

            layer()

            time.sleep(5)

            qfirst(name)

        elif main_option == "games store" or main_option == "games":

            processor()

            print(f"💡 Here is another fun fact for you {name}!")
            time.sleep(1)

            layer()

            print(f"🧠 So {name}, do you know that {get_facts()}?")

            layer()

            time.sleep(5)

            xo(name)

        elif main_option == "coffee shop" or main_option == "coffe shop":

            processor()

            print(f"💡 Here is another fun fact for you {name}!")
            time.sleep(1)

            layer()

            print(f"🧠 So {name}, do you know that {get_facts()}?")

            layer()

            time.sleep(5)

            cof(name, codm)

        elif main_option == "shapes" or main_option == "shapes section" :

            processor()

            print(f"💡 Here is another fun fact for you {name}!")
            time.sleep(1)

            layer()

            print(f"🧠 So {name}, do you know that {get_facts()}?")

            layer()

            time.sleep(5)

            main_shape(name)

        elif main_option == "calculator" or main_option == "math calculator":

            processor()

            print(f"💡 Here is another fun fact for you {name}!")
            time.sleep(1)

            layer()

            print(f"🧠 So {name}, do you know that {get_facts()}?")

            layer()

            time.sleep(5)

            main(name)

        else:

            print(
                f"❌ Sorry {name}, that service is unavailable."
            )

            print("\n📋 Available services:")

            for service in services:
                print(f"🔹 {service}")


if __name__ == "__main__":
    main_section()