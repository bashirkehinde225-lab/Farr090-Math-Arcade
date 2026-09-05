import time
from game import processor, layer
from shapes import bye, get_facts


def math(name):
    time.sleep(1)
    layer()
    print(f"WELCOME TO THE GENERAL MATH QUIZ {name.upper()} 🧠📐-\nThis is the quiz that tests your knowledge of general math knowledge, its early pioneers, trying to scrutinize not on your calculating or arithmetic abilities but the core concepts for mathematics in general")
    layer()
    time.sleep(3)

    print(f"So {name}, you are now about to take your quiz 📝")

    q_count_option = int(input("How many seconds should your countdown be (Enter a number): "))

    processor()
    print(f"Get ready {name}, your test starts in: ⏳")

    for i in range(q_count_option, 0, -1):
        print(i)
        time.sleep(1)

    print(f"⏰ Time is up {name}, Answer the following questions: ")

    general_math_quiz = {
        "Which mathematician is traditionally associated with the Pythagorean theorem?\n[A] Euclid  [B] Pythagoras  [C] Archimedes  [D] Aristotle": "B",
        "Which formula gives the area of a triangle?\n[A] base × height  [B] 2 × base × height  [C] 1/2 × base × height  [D] base + height": "C",
        "Who is known for developing important methods for calculating the value of π using polygons?\n[A] Archimedes  [B] Pythagoras  [C] Euler  [D] Newton": "A",
        "What is the name of the mathematical branch that deals mainly with shapes, sizes, angles, and properties of space?\n[A] Algebra  [B] Geometry  [C] Statistics  [D] Calculus": "B",
        "Which mathematician wrote the famous mathematical work called Elements, which became one of the most influential works in geometry?\n[A] Euclid  [B] Fibonacci  [C] Gauss  [D] Pascal": "A",
        "What formula is commonly used to find the circumference of a circle?\n[A] πr²  [B] 2πr  [C] πd²  [D] r² + π": "B",
        "Which sequence is famously associated with Leonardo of Pisa, better known as Fibonacci?\n[A] 1, 3, 5, 7, 9  [B] 2, 4, 8, 16, 32  [C] 1, 1, 2, 3, 5, 8  [D] 2, 3, 5, 7, 11": "C",
        "Which mathematical concept is represented by the symbol ∞?\n[A] Zero  [B] Infinity  [C] Pi  [D] Undefined": "B",
        "Which mathematician is strongly associated with the development of calculus, independently of Leibniz?\n[A] Isaac Newton  [B] Euclid  [C] Pythagoras  [D] Archimedes": "A",
        "What is the name of the theorem stating that the angles inside a triangle add up to 180° in Euclidean geometry?\n[A] Pythagorean theorem  [B] Angle Sum Theorem  [C] Binomial theorem  [D] Fundamental theorem": "B"
    }

    mark = 0
    for question, answer in general_math_quiz.items():
        print("\n" + question)
        user_answer = input("Your answer (type the option in capital letter): ").upper()

        if user_answer == answer:
            print("✅ Correct!")
            mark += 1
            print(f"🏆 Score: {mark}/10")
        else:
            print(f"❌ Wrong! The correct answer was {answer}")
            print(f"📊 Score: {mark}/10")

        input("\n👉 Press Enter for the next question...")

    percentage = mark / 10 * 100
    time.sleep(2)
    print(f"\n🎯 You got {percentage}%")

    if percentage >= 50:
        print(f"🎉 Congrats {name}, You passed!")
        time.sleep(2)
        bye(name)
    else:
        print(f"😔 Sorry {name}, you lost\n💪 Never give up {name}!")
        time.sleep(2)
        bye(name)


def calc(name):
    layer()
    print(f"WELCOME TO THE CALCULATION QUIZ SUBSECTION 🧮\nThis is the area where you answer questions that are strictly based on thorough calculation, so get your pen and paper ready {name}, it's going to be a hell of a show 🔥")
    layer()
    time.sleep(3)

    print(f"So {name}, you are now about to take your quiz 📝")

    q_count_option = int(input("How many seconds should your countdown be: "))

    processor()
    print(f"Get ready {name}! ⏳")

    for i in range(q_count_option, 0, -1):
        print(i)
        time.sleep(1)

    print(f"⏰ Time is up {name}, Answer the following questions: ")

    math_questions = {
        "A class has 30 students. 18 study Mathematics, 15 study Physics, and 8 study both subjects. How many students study at least one of the two subjects?\n[A] 23  [B] 25  [C] 27  [D] 28": "B",
        "The numbers 4, 7, 8, 10, 11, 15 have what median?\n[A] 8  [B] 8.5  [C] 9  [D] 10": "B",
        "The scores of five students are 6, 8, 8, 10 and 13. What is the mode?\n[A] 6  [B] 8  [C] 10  [D] 13": "B",
        "A bag contains 5 red balls, 3 blue balls and 2 green balls. If one ball is selected at random, what is the probability of selecting a blue ball?\n[A] 1/5  [B] 3/10  [C] 1/3  [D] 2/5": "B",
        "A right-angled triangle has an opposite side of 6 cm and a hypotenuse of 10 cm. What is sin θ?\n[A] 0.4  [B] 0.5  [C] 0.6  [D] 0.8": "C",
        "If tan θ = 1 and θ is an acute angle, what is the value of θ?\n[A] 30°  [B] 45°  [C] 60°  [D] 90°": "B",
        "Solve the trigonometric equation sin θ = 1/2 for 0° ≤ θ ≤ 360°.\n[A] 30° only  [B] 150° only  [C] 30° and 150°  [D] 60° and 300°": "C",
        "Two angles of a triangle are 65° and 45°. What is the size of the third angle?\n[A] 60°  [B] 70°  [C] 80°  [D] 90°": "B",
        "The mean of 5 numbers is 12. Four of the numbers are 8, 10, 13 and 15. What is the fifth number?\n[A] 12  [B] 14  [C] 15  [D] 16": "C",
        "Simplify: 2³ × 2².\n[A] 16  [B] 24  [C] 32  [D] 64": "C"
    }

    mark = 0
    for question, answer in math_questions.items():
        print("\n" + question)
        user_answer = input("Your answer: ").upper()

        if user_answer == answer:
            print("✅ Correct!")
            mark += 1
            print(f"🏆 Score: {mark}/10")
        else:
            print(f"❌ Wrong! The correct answer was {answer}")
            print(f"📊 Score: {mark}/10")

        input("\n👉 Press Enter for the next question...")

    percentage = mark / 10 * 100
    time.sleep(2)
    print(f"\n🎯 You got {percentage}%")

    if percentage >= 50:
        print(f"🎉 Congrats {name}, You passed!")
        time.sleep(2)
        bye(name)
    else:
        print(f"😔 Sorry {name}, you lost")
        time.sleep(2)
        bye(name)


def qfirst(name):
    layer()
    print(
        f"YOU ARE WELCOME TO QUIZILAND {name.upper()} 🧠🎮- "
        "Where questions are answered and answers are being questioned. "
        "The realm where tough and brain-wrecking questions exist because "
        "'When the competition gets tough, The tough gets going' 💪\n"
        "There are two areas of test:"
    )
    layer()

    areas = {
        "Calculation Quiz": "Solve questions that involve unique calculations",
        "General Math Quiz": "Answer questions on the history of Math and its early pioneers"
    }

    print("\n📋 Available areas:")
    for key, value in areas.items():
        print(f"🔹 {key} → {value}")

    while True:
        q_option = input(f"So {name}, which area would you like to cover today: ").lower().strip()
        processor()

        if q_option == "":
            print(f"{name}, this field can't be empty ❗")

        elif q_option == "general math quiz":
            processor()
            print("Ok then 👍")
            print(f"Here is another fun fact for you {name} 💡")
            time.sleep(1)
            layer()
            print(f"So {name}, Do you know that {get_facts()}")
            layer()
            time.sleep(5)
            math(name)
            break

        elif q_option == "calculation quiz":
            processor()
            print("Ok then 👍")
            print(f"Here is another fun fact for you {name} 💡")
            time.sleep(1)
            layer()
            print(f"So {name}, Do you know that {get_facts()}")
            layer()
            time.sleep(5)
            calc(name)
            break

        else:
            print(f"❌ Sorry {name}, that service is unavailable. Please choose again.")
            time.sleep(1)
            print("\n📋 Available areas:")
            for key, value in areas.items():
                print(f"🔹 {key} → {value}")