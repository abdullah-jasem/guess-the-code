import random


def one() -> list:
    return ["How many clearly visible known moons do we have?",
            "What's the first odd prime number?",
            "How many vowels are in the word \"sun\"?",
            "What is the value of True in Computer Science?",
            "What is the atomic number of hydrogen?"]


def two():
    return ["1+1 equals to?",
            "What's the first even prime number?",
            "How much eyes does an average human have?",
            "What is the atomic number of helium?",
            "How many hemispheres does the Earth have?"]


def three():
    return ["1+2 equals to?",
            "How many sides does a triangle have?",
            "In a game of Rock, Paper or Scissors. How many outcomes are there?",
            "While driving, how many colors are in a traffic signal?",
            "Which position is Earth in this solar system?"]


def four():
    return ["8/2 is equal to?",
            "How many seasons are in a year?",
            "How many sides does a square have?",
            "Square root of 16 is?"]


def five():
    return ["10/2 is equal to?",
            "How many fingers does an average hand have?",
            "In a school week, how many days are there?",
            "How many sides does a pentagon have?"]


def six():
    return ["12/2 is equal to?",
            "How many sides does a hexagon have?",
            "Square root of 36 is?",
            "In 1971, how many emirates of the United Arab Emirates 🇦🇪 united?",
            "How many members are in the Gulf Cooperation Council?"]


def seven():
    return ["14/2 is equal to?",
            "How many sides does a heptagon have?",
            "How many emirates are in the United Arab Emirates 🇦🇪",
            "Square root of 49 is?"]


def eight():
    return ["16/2 is equal to?",
            "What is the atomic number of oxygen?",
            "How many sides does an octagon have?",
            "♾️rotated by 90º is?"]


def nine():
    return ["18/2 is equal to?",
            "How many planets are there in the Solar System (including Pluto)",
            "Ii is in which number position in the Alphabet?",
            "3x3 is equal to?"]


class Questions:
    question = ""
    def __init__(self, num):
        if num == "1":
            self.question = random.choice(one())
        elif num == "2":
            self.question = random.choice(two())
        elif num == "3":
            self.question = random.choice(three())
        elif num == "4":
            self.question = random.choice(four())
        elif num == "5":
            self.question = random.choice(five())
        elif num == "6":
            self.question = random.choice(six())
        elif num == "7":
            self.question = random.choice(seven())
        elif num == "8":
            self.question = random.choice(eight())
        elif num == "9":
            self.question = random.choice(nine())