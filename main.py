import random
import questions

code = random.randint(100000, 999999)
num_to_character = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth"
}
if __name__ == "__main__":
    print("""Guess the code!
    
Instructions are clear & simple:
    👨🏻‍💻 Become a hacker and try to crack the code
    🙋 Each digit is given by answering those questions
 """)

while True:
    answer = input("1. Code\n2. Clues\nEnter 1 or 2: ")
    if not answer.isdigit():
        print("\nPlease enter a number between (1/2)\n")
        continue
    elif int(answer) == 1:
        code_digit = input("""Enter a number between (1-7)
        1. Check First Digit of the code
        2. Check Second Digit of the code
        3. Check Third Digit of the code
        4. Check Fourth Digit of the code
        5. Check Fifth Digit of the code
        6. Check Sixth Digit of the code
        7. Enter the actual code
        """)
        if not code_digit.isdigit():
            print("\nPlease enter a number between (1-7)\n")
            continue
        elif 1 <= int(code_digit) <= 6:
            check_code = input(f"\nEnter the {num_to_character[int(code_digit)]} digit of the code: ")
            if str(code)[int(code_digit) - 1] == check_code[0]:
                print(f"\n✅ That's correct! {num_to_character[int(code_digit)].capitalize()} digit: {check_code[0]}\n")
                continue
            else:
                print(f"\n❌ That's wrong! You can try to get hints.")
                continue
        elif int(code_digit) == 7:
            check_code = input(f"\nEnter the code: ")
            if str(code) == check_code:
                print(f"\n✅ That's correct! You have successfully beaten this computer. {str(code)}")
                break
            else:
                print(f"\n❌ That's wrong! Guess using the digits.")
                continue
        else:
            print("\nPlease enter a number between (1-7)\n")
            continue
    elif int(answer) == 2:
        num = str(code)[random.randint(1, 5)]
        print(questions.Questions(num).question)
    else:
        print("\nPlease enter a number between (1/2)\n")
        continue
