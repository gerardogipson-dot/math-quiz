import sys
import operator
import numpy as np

#global variables
initial_blood = 10
initial_hater_blood = 30
blood_point = initial_blood
hater_blood = initial_hater_blood

#define operators
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

#utility function
def return_game(current_name): #ask users if they want to play again
    print("\nDo you want to play our game for another time?")
    print("If you would like to replay the game, input 1.")
    print("Else, enter other character.")
    character = input("Enter your choice: ")
    if character == "1": #reset blood point for new game
        global blood_point, hater_blood
        blood_point = initial_blood
        hater_blood = initial_hater_blood
        start_menu(current_name)
    else:
        print("Thanks for playing! Bye bye~ ^v^")
        sys.exit(0)

def judge(current_name): #check win/loss    
    if hater_blood <= 0:
        print("\nThanks for your fight!!! We win!!! ٩(๑•̀ω•́๑)۶")
        return_game(current_name)
        return True # win (GO)
    elif blood_point <= 0:
        print("\nOh no! You lose!! Please work hard for your Mathematics T-T ")
        return_game(current_name)
        return True # loss (GO)
    return False # Game continues

def check_blood(): #display current HP
    print(f"\nYour blood is {blood_point} HP.")
    print(f"The MATH HATER's blood is {hater_blood} HP.")
    input("\nPress Enter to return to the menu...")

def rule(current_name): #display rules
    print(f"\nHero {current_name}'s Guide to Battle")
    print("In this game, you must battle the MATH HATER to save the Kingdom of Mathematics!")
    print("Your HP: You start with 10 blood points (HP).")
    print("HATER HP: The MATH HATER starts with 30 blood points (HP).")
    print("Winning: If you answer correctly, the HATER loses HP.")
    print("    Level 1: HATER loses 1 HP")
    print("    Level 2: HATER loses 2 HP")
    print("    Level 3: HATER loses 3 HP")
    print("Losing: If you answer incorrectly, you lose 2 HP.")
    print("Victory Condition: You win when the MATH HATER's blood reaches 0.")
    print("Loss Condition: You lose when your blood reaches 0.")
    input("\nPress Enter to return to the menu...")

def end_game():
    print("\nThank you for fighting for our country, bye bye~")
    sys.exit(0)


def game_1(): #simple addtion and substraction
    global hater_blood, blood_point
    min_num, max_num = 1, 10
    num1 = np.random.randint(min_num, max_num + 1)
    num2 = np.random.randint(min_num, max_num + 1)
    op_symbol = np.random.choice(["+", "-"])
    op_func = operators[op_symbol]
    ans = op_func(num1, num2)

    if op_symbol == "-" and ans < 0: #ensure substraction result is not -ve in lvl 1
        num1, num2 = num2, num1 
        ans = op_func(num1, num2)
    
    print(f"\nLevel 1: HATER HP: {hater_blood} | Your HP: {blood_point}")
    
    while True:
        try:
            answer = int(input(f"Please calculate: {num1} {op_symbol} {num2} = ")) 
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    if ans == answer:
        hater_blood -= 1
        print("Correct! The MATH HATER loses 1 HP.")
    else:
        blood_point -= 2
        print(f"Incorrect! The correct answer was {int(ans)}. You lose 2 HP.")

def game_2(): #addtion, substraction,simple division
    global hater_blood, blood_point
    min_num, max_num = 4, 20
    num1 = np.random.randint(min_num, max_num + 1)
    num2 = np.random.randint(min_num, max_num + 1)
    op_symbol = np.random.choice(["+", "-", "/"])
    op_func = operators[op_symbol]
    
    if op_symbol == "/": #ensure division is exact and results in whole number
        num2 = np.random.randint(2, 11) 
        k = np.random.randint(1, 11) 
        num1 = num2 * k
    
    ans = op_func(num1, num2)

    if op_symbol == "-" and ans < 0: #ensure substraction results is not -ve
        num1, num2 = num2, num1
        ans = op_func(num1, num2)

    print(f"\nLevel 2: HATER HP: {hater_blood} | Your HP: {blood_point}")
    
    while True:
        try:
            answer = float(input(f"Please calculate: {num1} {op_symbol} {num2} = "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    if abs(ans - answer) < 1e-9: 
        hater_blood -= 2
        print("Correct! The MATH HATER loses 2 HP.")
    else:
        blood_point -= 2
        print(f"Incorrect! The correct answer was {ans}. You lose 2 HP.")

def game_3(): #division and multiplication
    global hater_blood, blood_point
    min_num, max_num = 4, 20
    
    op_symbol = np.random.choice(["/", "*"]) 
    op_func = operators[op_symbol]
    
    if op_symbol == "/":
        num2 = np.random.randint(2, 11)
        k = np.random.randint(1, 11)
        num1 = num2 * k
    else: 
        num1 = np.random.randint(min_num, max_num + 1)
        num2 = np.random.randint(min_num, max_num + 1)

    ans = op_func(num1, num2)

    print(f"\nLevel 3: HATER HP: {hater_blood} | Your HP: {blood_point}")

    while True:
        try:
            answer = float(input(f"Please calculate: {num1} {op_symbol} {num2} = ")) 
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    if abs(ans - answer) < 1e-9: 
        hater_blood -= 3
        print("Correct! The MATH HATER loses 3 HP.")
    else:
        blood_point -= 2
        print(f"Incorrect! The correct answer was {ans}. You lose 2 HP.")

def game_choose(level, current_name):
    if level == 1:
        game_1()
    elif level == 2:
        game_2()
    elif level == 3:
        game_3()
    
    return judge(current_name)

def game(current_name):
    
    while True: # lvl selection
        try:
            level = int(input(f"\n{current_name}, please choose your level (1=Simple, 2=Normal, 3=Hard): "))
            if level in (1, 2, 3):
                break
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a *NUMBER* (1, 2, or 3).")
            
    print(f"\n--- Starting 10-Question Battle (Level {level}) ---")

    for i in range(1, 11): #question
        print(f"\n--- Question {i}/10 ---")
        is_game_over = game_choose(level, current_name)
        if is_game_over:
            return 
    
    print("\n--- 10 Questions Completed! ---")
    judge(current_name)


# menu
def self_intro(): #display welcome msg and ask player name
    print("\n" + "*"*60)
    print("*"+" "*58+"*")
    print("*"+" "*15+"WELCOME TO MATH QUIZ BATTLE!"+" "*15+"*")
    print("*"+" "*58+"*")
    print("*"*60)
    print("\nHello hero, could you tell me your name?")
    name = str(input("Enter your name: "))
    return name

def start_menu(current_name): #main menu and story introduction
    print(f"\nHello, hero {current_name}!")
    print("In the Kingdom of Mathematics, everyone loves solving mathematical questions.")
    print("But one day, a MATH HATER intrudes and wants to ruin mathematics!!!")
    print("As our hero, please fight with the MATH HATER to protect our country!")
    choose(current_name) 

def choose(current_name): #handle main menu choices
    while True:
        print("Enter the serial number and start your GAME!")
        print("1. Start the game")
        print("2. Check blood (HP)")
        print("3. Check the rule")
        print("4. Exit the game")
        
        try:
            chose = int(input("Please enter your choice: "))
            
            if chose == 1:
                game(current_name)
            elif chose == 2:
                check_blood()
            elif chose == 3:
                rule(current_name)
            elif chose == 4:
                end_game()
            else:
                print("Please enter a valid number (1-4).")
                input("Press Enter to continue...")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            

name = self_intro()
start_menu(name)