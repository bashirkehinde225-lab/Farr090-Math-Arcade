# Farr090 Math Arcade

Farr090 Math Arcade is a Python project I built while learning programming.

It has different sections, including:

- Calculator
- Math Quiz
- Shapes and Geometry
- Coffee Shop
- Rock Paper Scissors

I started this project with small pieces of code and slowly added more features. While building it, I learned more about functions, loops, modules, input validation, and debugging.

This project is one of my biggest Python projects so far and is an important part of my learning journey.

## How to Run

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python main.py
on Windows, you add also use:
py main.py


Pasted code.py
Python
look at the shapes file
Tuesday 11:11 AM
1000146743.mp4
File

I scrutinized the video carefully. 👀🐍

What you're practicing

You're working with:

import json
import os
A Python multiline string containing JSON-like data
A "people" list
Dictionaries/objects inside that list
json.dumps()
indent=2
open()
Writing data to a text file
os.path.exists()
os.remove()

So you're not just watching a tutorial—you've actually started experimenting with JSON and file handling. That's good.

⚠️ One important thing I noticed

You have:

main = '''
{
    "people": [
        {
            "name": "alex",
            ...
        }
    ]
}
'''

That means main is actually a Python string, not a Python dictionary.

Then you do:

da = json.dumps(main, indent=2)

This is probably not what you want if your goal is to convert Python data into JSON.

Normally:

main = {
    "people": [
        {
            "name": "alex",
            "phone": "0056756798",
            "emails": "johnsmith@email.com",
            "has_license": False
        }
    ]
}

da = json.dumps(main, indent=2)

Here main is a Python dictionary, and json.dumps() converts it into a JSON-formatted string.

🧠 Another thing

You're using:

d = open("tyt.txt", "w")
d.close()

and later:

d = open("tyt.txt", "a")
d.write(da)
d.close()

This works as file handling practice, but later you should learn the cleaner:

with open("tyt.txt", "w") as d:
    d.write(da)

Don't worry about mastering that yet.

⭐ My verdict

For your current goal of learning basic JSON, this is actually useful practice.

I'd rate what you're doing:

JSON basics: 🟢 Good direction

File handling: 🟢 Good

json.dumps(): 🟢 You're getting into the important stuff

json.load() / json.loads(): 🟡 Make sure you learn these next

APIs: 🔴 Not necessary yet

And most importantly: you don't need another JSON tutorial just because you've seen this one. Finish understanding what you've practiced, build one small project with JSON, then move on to SQLite + SQL.

Yesss, I see what you were trying to do. You're very close. 🔥

The main problem is this part:

json.load(file)
file.update("score": 1000)
What went wrong?

file is the file object, not your loaded dictionary.

When you do:

json.load(file)

you need to store the result:

data = json.load(file)

Now data is your Python dictionary:

{
    "name": "Kenny",
    "score": 850,
    "level": 5,
    "coins": 120
}

Then change the score:

data["score"] = 1000
So the corrected version is:
import json

player = {
    "name": "Kenny",
    "score": 850,
    "level": 5,
    "coins": 120
}

with open("player.json", "w") as f:
    json.dump(player, f, indent=3)

with open("player.json", "r") as file:
    data = json.load(file)

data["score"] = 1000

print(data)

But there's one more important thing.

At this point:

data["score"] = 1000

you've changed the Python dictionary in memory, but you haven't changed the JSON file yet.

To save the new score:

with open("player.json", "w") as file:
    json.dump(data, file, indent=3)

So the complete flow is:

player dictionary
      ↓
   json.dump()
      ↓
 player.json
      ↓
   json.load()
      ↓
data dictionary
      ↓
change score
      ↓
   json.dump()
      ↓
updated player.json

That's exactly the kind of thing JSON is used for in real programs: load saved data → modify it → save it again.

Now for git, that is the laptop am using 
shapes.py
Python
Quiz.py
Python
main.py
Python
game.py
Python
coffe_.py
Python
Calc.py
Python
That is my old math activity project. All the files. I want to look at it deeply. Um, tell me all the errors, amend all the errors. Tell me, give me the clean code, amend all my English, all the English mispronunciation, all the errors in the code. I need to amend it. Don't change anything specifically in my code. So it's normal function. So that's it.
Farr090 Math Arcade

Farr090 Math Arcade is a Python-based terminal application I built while learning and improving my programming skills. The project combines several features into one program, including a calculator, math quiz, shapes and geometry, a coffee shop, and a Rock Paper Scissors game.

The project started as smaller Python exercises and gradually grew into a multi-file application. One of the biggest challenges was connecting the different modules and debugging problems as the project became larger. I also worked on input validation, error handling, code organization, and cleaning up the code without completely changing its original structure.

Main Files
main.py — Main menu and program controller
Quiz.py — Math quiz
shapes.py — Shapes and geometry
game.py — Rock Paper Scissors
coffe_.py — Coffee shop
Calc.py — Calculator
How to Run

Make sure Python 3 is installed, then clone or download the repository.

Open a terminal inside the project folder and run:

python main.py

On Windows, you can also use:

py main.py

This project is mainly a learning milestone for me. It helped me move from writing individual Python exercises to building, organizing, debugging, and releasing a larger application.

am going to copy and paste in the reame file so those code u wrote and use simple and basic english

Absolutely. If you're copying it directly into your README.md, I'll keep the English simple, natural, and basic, like a student wrote it.

# Farr090 Math Arcade

Farr090 Math Arcade is a Python project I built while learning programming.

It has different sections, including:

- Calculator
- Math Quiz
- Shapes and Geometry
- Coffee Shop
- Rock Paper Scissors

I started this project with small pieces of code and slowly added more features. While building it, I learned more about functions, loops, modules, input validation, and debugging.

This project is one of my biggest Python projects so far and is an important part of my learning journey.

## How to Run

Make sure Python is installed on your computer.

Open the project folder in a terminal and run:

```bash
python main.py

On Windows, you can also use:

py main.py

Main Files
main.py - Runs the main program
Quiz.py - Math quiz
shapes.py - Shapes and geometry
game.py - Rock Paper Scissors
coffe_.py - Coffee shop
Calc.py - Calculator
Project Goal

The main goal of this project was to practice Python and learn how to build a larger program using different files and functions.

This project is still part of my learning journey, and I plan to keep improving my programming skills.
