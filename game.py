from random import choice
import time


xo_facts = [
    "Tic-Tac-Toe is one of the simplest strategy games to learn because it only uses a 3-by-3 grid, but players still have to think ahead to prevent their opponent from creating a winning line.",
    "The modern version of Tic-Tac-Toe is related to older pencil-and-paper games that were played in different forms long before the game became popular under its current name.",
    "If both players understand the best strategy and make no mistakes, a normal game of Tic-Tac-Toe will always end in a draw rather than producing a winner.",
    "The game has a surprisingly small number of possible positions compared with games like chess, which makes Tic-Tac-Toe an excellent example for teaching computers how to search through possible moves.",
    "A computer can be programmed to play perfect Tic-Tac-Toe by examining the possible moves that could follow each decision and choosing moves that prevent the opponent from eventually winning.",
    "The center square is strategically important because it is part of four possible winning lines: the middle row, the middle column, and the two diagonals.",
    "A player who controls two corners can sometimes create a special situation called a fork, where they threaten to win in two different places and force the opponent to block only one of them.",
    "Tic-Tac-Toe is often used in programming tutorials because its rules are simple enough for beginners while still introducing concepts such as loops, lists, functions, conditions, game states, and algorithms.",
    "The game is sometimes called Noughts and Crosses, especially in British English, while the names Tic-Tac-Toe and Xs and Os are more commonly associated with American usage.",
    "Tic-Tac-Toe can be used to demonstrate artificial intelligence techniques such as the minimax algorithm, which allows a computer player to consider possible future moves instead of simply choosing a random square."
]


def get_xo_facts():
    return choice(xo_facts)


def layer():
    print("=" * 50)


def intro():
    layer()
    print(
        "🕹️ WELCOME TO THE GAME STORE OF THE FARR090 MATH ARCADE 🕹️"
        " — This is where you can play to your heart's content!"
    )
    layer()


def processor():
    for _ in range(3):
        print("   ⏳ Processing...")
        time.sleep(1)


def xo(name):
    intro()
    time.sleep(2)

    print(
        f"🎲 So {name}, here's an interesting fun fact "
        "about Tic-Tac-Toe that most people don't know!"
    )

    print(
        f"💡 So {name}, do you know that {get_xo_facts()}"
    )

    layer()
    time.sleep(5)

    options = ("rock", "paper", "scissors")
    streak = 0

    while True:
        computer = choice(options)

        player = input(
            "✊✋✌️ Enter a choice (rock, paper, scissors): "
        ).strip().lower()

        while player not in options:
            processor()
            print(
                f"❌ {name}, you have to choose between "
                "rock, paper, and scissors."
            )
            time.sleep(1)

            player = input(
                "✊✋✌️ Enter a choice (rock, paper, scissors): "
            ).strip().lower()

        processor()

        print(f"🧑 Player: {player}")
        print(f"🤖 Computer: {computer}")

        if player == computer:
            layer()
            print(f"🤝 It's a tie, {name}!")
            layer()

            streak = 0

        elif (
            (player == "rock" and computer == "scissors")
            or
            (player == "paper" and computer == "rock")
            or
            (player == "scissors" and computer == "paper")
        ):
            processor()
            layer()

            streak += 1

            print(f"🎉 HOORAY! YOU WIN, {name}! 🎉")
            print(f"🔥 Current win streak: {streak}")

            print(
                "🎁 Just because you won, "
                "here's another fun fact for you!"
            )

            time.sleep(2)

            print(
                f"💡 So {name}, do you know that {get_xo_facts()}"
            )

            time.sleep(5)

            print("😎 Cool, right?")
            layer()

        else:
            processor()

            print(f"😢 You lose, {name}!")
            streak = 0

        contrib = input(
            f"🔁 Would you like to continue, {name}? (yes/no): "
        ).strip().lower()

        while contrib not in ("yes", "no"):
            print("❌ Invalid response.")

            contrib = input(
                f"🔁 Would you like to continue, {name}? (yes/no): "
            ).strip().lower()

        if contrib == "yes":
            processor()
            layer()

            print(
                f"🚀 ROCK ON, {name}! Current Streak: {streak}"
            )

            layer()

        elif contrib == "no":
            print("👍 Okay then!")
            print(f"🙏 Thanks for playing, {name}!")
            exit()

