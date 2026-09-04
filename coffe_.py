import time
from random import choice
from shapes import bye
from game import layer, processor


facts_about_coffee = [
    "Coffee beans are not actually beans. They are the seeds inside a fruit called a coffee cherry, which means coffee is technically a fruit seed rather than a bean.",

    "Coffee plants can naturally produce caffeine as a chemical defence. The caffeine can help discourage some insects from feeding on the plant.",

    "Coffee contains hundreds of aroma compounds, and roasting creates many additional compounds that contribute to the smell and flavour of the finished coffee.",

    "The colour of a coffee bean changes dramatically during roasting because heat triggers chemical reactions such as the Maillard reaction and caramelisation, producing new flavours and aromas.",

    "Coffee cherries do not all ripen at exactly the same time. On the same plant, ripe, unripe and overripe cherries can exist together, which is one reason selective harvesting can require so much work.",

    "Some coffee plants can live for decades and produce coffee for many years, although their productivity and health can change as they age.",

    "The coffee plant is related to gardenia and quinine-producing plants because coffee belongs to the Rubiaceae family, a large family of flowering plants.",

    "Decaffeinated coffee is not completely caffeine-free. Most decaffeination methods remove the vast majority of caffeine, but a small amount can remain.",

    "Espresso does not mean a particular type of coffee bean. Espresso is a brewing method that uses pressure to force hot water through finely ground coffee.",

    "The word espresso is connected to the Italian idea of something being pressed out or made expressly for someone, reflecting the way the drink is prepared and served.",

    "Coffee grounds can contain useful organic material, which is why used grounds are sometimes added to compost rather than simply thrown away.",

    "The coffee fruit itself can be used for products other than roasted coffee. The fruit pulp and other parts of the cherry can be processed into different food and beverage products.",

    "Coffee beans can absorb smells from their surroundings. This is one reason coffee is normally stored in containers that limit exposure to air and strong odours.",

    "Green coffee beans are much denser and less aromatic than roasted beans. Roasting dramatically changes their physical structure, colour, smell and flavour.",

    "Freshly roasted coffee releases carbon dioxide for a period of time after roasting. This is why coffee can continue releasing gas even after it has been packaged.",

    "Coffee extraction is a balancing act. Water temperature, grind size, brewing time and the amount of coffee can all change which compounds are extracted into the drink.",

    "Grinding coffee dramatically increases the surface area exposed to air. This is one reason whole coffee beans generally retain their qualities longer than already-ground coffee when stored properly.",

    "Arabica and Robusta are different species of coffee. Robusta is generally more resistant to some diseases and contains more caffeine than Arabica.",

    "Coffee cherries can change colour as they ripen. Depending on the variety, ripe cherries may become red, yellow or another colour rather than always being red.",

    "The Coffee Belt is not a single country or region. It is a broad area around the equator where conditions such as temperature, rainfall and altitude can support coffee cultivation.",

    "Coffee can be grown at surprisingly high elevations. In some regions, farmers cultivate coffee on mountain slopes where cooler temperatures can slow the development of the cherries.",

    "A coffee bean can have a major effect on flavour even before it reaches the roasting stage. Variety, altitude, soil, climate, processing and fermentation can all influence the final cup.",

    "Coffee processing can involve fermentation. After harvesting, microorganisms can help break down parts of the fruit surrounding the coffee seeds, influencing how the final coffee tastes.",

    "Some specialty coffees are deliberately fermented using controlled processes to develop unusual flavour profiles. The fermentation is carefully managed rather than simply allowing the fruit to spoil.",

    "Coffee has a natural chemical compound called chlorogenic acid, which is one of the compounds contributing to the chemistry and flavour of coffee.",

    "The caffeine content of coffee is affected by more than just the number of scoops used. The coffee species, brewing method, serving size and extraction conditions can all influence how much caffeine ends up in the cup.",

    "Coffee roasting is not simply about making beans darker. Different roasting profiles can bring out very different flavour characteristics from the same green coffee.",

    "The inside of a coffee cherry usually contains two seeds pressed together. These are the seeds that eventually become the familiar roasted coffee beans.",

    "Sometimes a coffee cherry develops only one rounded seed instead of the usual pair. This is called a peaberry, and it can occur naturally during the development of the fruit.",

    "Coffee is one of the world's major agricultural commodities, meaning its production connects farmers, exporters, traders, roasters, cafés and consumers across many countries."
]


def get_coffee_facts():
    return choice(facts_about_coffee)


def payment_method(name):
    payment_options = ["cash", "transfer", "credit"]

    while True:
        payment = input(
            "\n💳 How would you like to pay? "
            "(cash 💰 / transfer 🏦 / credit 💳): "
        ).strip().lower()

        if payment in payment_options:
            break

        print("❌ Please choose cash, transfer, or credit.")

    print("⏳ Processing your payment...")

    for _ in range(3):
        print("   • Processing...")
        time.sleep(1)

    print(
        f"\n✅ {payment.title()} payment successful! 🎉 {name}"
    )

    bye(name)


def innocence_checking(name):
    while True:
        evil = input(
            f"😈 So, are you evil, {name}? (yes/no): "
        ).strip().lower()

        if evil == "yes":
            processor()
            print(f"🚪 Get out now, evil {name}!")
            exit()

        elif evil == "no":
            processor()
            layer()

            print(
                f"☕ You are welcome to B$K Coffee Shop, {name}, "
                "the lounge of the Farr090 Math Arcade!"
            )

            layer()
            break

        else:
            print("❌ You have to enter yes or no.")


def order(name, codm):
    menu_items = [
        "cappuccino",
        "black coffee",
        "frenzo",
        "green asian tea",
        "latte",
        "espresso",
        "mocha",
        "americano",
        "hot chocolate",
        "iced coffee",
        "caramel macchiato",
        "vanilla latte",
        "chai tea",
        "lemon tea",
        "strawberry milkshake",
        "croissant",
        "chocolate muffin",
        "blueberry muffin",
        "chocolate chip cookie",
        "brownie",
        "donut",
        "cinnamon roll",
        "banana bread",
        "cheesecake",
        "sandwich"
    ]

    while True:
        q1 = input(
            "👀 Would you like to see our menu? (yes/no): "
        ).strip().lower()

        if q1 == "":
            print("❌ This field can't be empty.")

        elif q1 == "yes":
            print("✅ Okay then!")
            time.sleep(1)

            print("\n--- Here is a list of our menu ---")

            for i, item in enumerate(menu_items, 1):
                print(f"{i}. {item.title()}")
                time.sleep(1)

            break

        elif q1 == "no":
            print(
                f"😌 Well, I, {codm}, will be here when "
                f"you are ready, {name}."
            )

            input("⏸️ Press Enter when you are ready...")
            break

        else:
            print("❌ Please enter yes or no.")

    while True:
        drink_choice = input(
            f"\n🍽️ What would you like to have today, {name}? "
        ).strip().lower()

        if drink_choice in menu_items:
            processor()

            print("✅ Okay then!")

            print(
                f"🎁 Here is another fun fact for you, {name}!"
            )

            time.sleep(1)
            layer()

            print(
                f"💡 So {name}, do you know that "
                f"{get_coffee_facts()}"
            )

            layer()
            time.sleep(5)

            payment_method(name)
            break

        else:
            print(
                f"❌ Sorry {name}, that is not on our menu."
            )


def cof(name, codm):
    innocence_checking(name)

    print(
        f"☕ So {name}, we hope you didn't mind the good-or-bad test. "
        "Here at the lounge, we follow strict rules."
    )

    time.sleep(2)

    print(
        f"🎉 Well {name}, since you passed the test, "
        "here is a cool coffee fact that most people don't know!"
    )

    time.sleep(1)
    layer()

    print(
        f"💡 So {name}, do you know that "
        f"{get_coffee_facts()}"
    )

    layer()
    time.sleep(4)

    print("😎 Cool, right?")

    order(name, codm)