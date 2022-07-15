#print('Atharva Raut')

#print('o----') imaginary dog
#print(' ||||')

#print('*' * 10) multiplication

#name = input('What is your name? ') QUESTIION AND ANSWER
#color = input('what is your favorite color? ')
#print(name + ' likes ' + color)

#weight_kg = input('weight: ') THE TYPE OF VARIABLE IS IMP WHILE USING IT
#weight_lbs = int(weight_kg) * 2.2
#print(weight_lbs)

#name = 'jennifer'
#print(name [1:-1]) INDEX NO. TO THE ALPHABATES

#first = 'Atharva'
#last = 'Raut'
#message = first + ' [' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(message)
#print(msg)

#course = 'Python for Beginners'
#print(course.upper()) TO MAKE  THE STRING ALL UPPER CASE
#print(course.lower()) TO MAKE THE STRING ALL TO LOWER CASE
#print(course)
#print(course.find('P')) TO FIND THE INDEX OF THE ALPHABATE
#print(course.replace('Beginners', 'Absolute Beginners')) TO REPLACE THE VALUE
#print('Python' in course) IN THE IN FUNCTION ITS CHECKS IF THE DEFINED VALUE IS IN THE STRING AND THE OUPUT IS IN THE FORM OF BOOLEAN I.E. TRUE OR FALSE

#x = 10 + 3 * 2 OPRATOR PRECEDENCE
#x+= 3 OGMENTED ASSIGNMENT OPRATOR
#print(x)

#THE ORDER OF OPRATOR PRECEDENCE IS,
#BRACKETS OF DIVISION, MUTIPLICATION, ADDITION AND SUBTRACTION
#EXPONENTIAL 2**3
#MULTIPLICATION OR DIVISION
#ADDITION AND SUBTACTION

#import math
#x = 2.9
#print(round(x)) ROUND OFF
#print(abs(-2.9)) TURNS NEGATIVE TO POSITIVE
#print(math.ceil(x)) SAME AS ROUND
#print(math.floor(x)) BRINGS THE NUMBER TO THE LOWER FORM I.E. IF THE NO. IS 2.9 THEN THE NO. WILL BECOME 2

#is_hot = True
#is_cold = False
#if is_hot: THE IS FUNCTION IS CASE SENSETIVE AMD THE IS FUNCTION ALWAYS HAVE ONLY 2 ANS I.E. TRUE OR FALSE
#    print("It's a hot day")
#    print("Drink plenty of water")
#elif is_cold:
#    print("It's a cold day")
#    print("Wear warm clothes")
#else:
#    print("It's a lovely day")
#print("Enjoy your day")

#price = 1000000
#has_good_credit = True THE QUWESTION WAS THAT IF THE PRICE OF THE IS $1M AND THE BUYER HAS GOOD CREDIT THEN THEY NEED TO PUT DOWN BY 10%
#OTHERWISE THEY NEED TO PUT DOWN BY 20% AND IN THE END PRINT THE DOWN PAYMENT
#if has_good_credit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f"Down paymnet: ${down_payment}")

#name = 'Atharva Ajay Raut'
#if len(name) < 3:
#    print("name must be at least 3 characters") IF LENGTH OF  THE NAME IS LESS THAN 3 CHARACTERS THEN THE OUTPUT SHOULD BE <- THIS LINE
#elif len(name) > 50:
#    print("name can be a maximum of 50 characters") AND IF THE LENGHT OF THE NAME IS GREATER THAN 50 CHARACTERS THEN THE OUTPUT SHOULD BE <- THIS LINE
#else :
#    print("name looks good") AND IF THE LENGTH OF THE NAME IS BETWEEN THESE 2 THEN THE OUTPUT SHOULD BE <- THSI LINE

#weight = int(input("Weight= "))
#unit = input("(L)bs or (K)g: ") IT'S A WEIGHT CONVERTER FROM KG TO LBS OR FROM LBS TO KG
#if unit.upper() == "L" : SO FIRST WE HAVE TO TAKE THE INPUT FROM THE USER AND CONVERT THAT STING TO INTEGER
#    converted = weight * 0.45 AND THEN WE HAV ETO ASK THE USER IF THE WEIGHT U GAVE IS IN KG OR LBS
#    print(f"you are{converted} Kilos") AFTER THAT WE DONT HAVE TO MAKE THAT CASE SENSITIVE SO THEN APPLY UPPER FINCTION AND THEN IN THE IF STATEMNET
#else: WE CONVERT THE WEIGHT TO KG IN THE FROM LBS BY MULTIPLYING IT BY .45 AND IN THE ELSWE WE DIVIDE IT BY .45 AND WE PUT THAT THE ANS IS A WHOLE NO.
#    converted = weight // 0.45
#    print(f"you are {converted} pounds")

#i = 1    HERE THE VALUE OF I IS 1 AMD THE IN THE WHILE LOOP THE IS CONDITION IS IF I IS LESS THAN 5 PRINT *
#while i <= 5:  AND THEN IN THE NEXT LINE I + 1 MEANS THE VALUE OF I IS INCREASEED BY 1 I.E. 2 THEN BECAUSE 2 IS LESS THAN 5 THE LOOP GOES ON TILL THE VALUE
#    print('*' * i)  OF I IS GREATER THAN 5 AND THEN ONCE THE VALUE OF I IS 6 THE LOOP ENDS THEN THE DONE MESSAGE APPEARS
#    i = i + 1
#print('Done')

#THE GUESS GAME
#secret_number = 9 FIRST DESCRIBE THE NO. THAT SHOULD BE SECRET AND THEN DECIDE HOWMANY GUESSES U WANT TO TO GIVE TO THE USER
#guess_count = 0
#guess_limit = 3  THEN WITH THE HELP OF WHILE LOOP STATE THAT THE GUESS COUNT IS LESS THAN GUESS LIMIT
#while guess_count < guess_limit:  THEN TAKE THE INPUT FROM THE USER IN THE FORM OF INTEGR AND THEN ADD ONE COUNT TO IT
#        guess = int(input('Guess: ')) IF THE GUESS IS CORRECT THEN PRINT YOU WON AND BREAK THE LOOP
#        guess_count += 1 AFTER THAT IF THE GUESS IS WRONG THEN RUN THE LOOP ONCE AGAIN TILL THE GUESS LIMIT IS THERE
#        if guess == secret_number: ONCE THE LIMIT IS THERE PRINT YOU FAILED
#            print("You Won!")
#            break
#else:
#    print("Aap iss game ke hakdaar nahi hai!")

#THE CAR GAME
#command = ""
#started = False  IN THIS GAME THERE ARE 4 COMMANDS THAT RUNS THE GAME SO AT FIRST WE STATE THAT THE IS STARTED TO FALSE
#while True:  SO IN THE WHILE LOOP WE TAKE THE INPUT FROM THE USER IN ANY CASE THAT COMMAND WILL TURN INTO LOWER CASE AND
#    command = input("> ").lower() WITH THE HELP OF IF STATEMENT WE PUT THE CONDITIONS THAT IF THE USER TYPES HELP ALL THE
#    if command == "start": COMMANDS WILL BE PRINTED WITH THERE WORK.
#        if started: SO NOW IF THE USER WRITES START IT WILL PRINT THE CAR STARTED AND IF THE USER WRITES THE START COMMAND
#            print("Car already started!") AGAIN THEN THE COMMAND WILL APPEAR THAT THE CAR IS ALREADY STARTED.
#        else:  THIS CONDITION GOES SAME WITH THE STOP COMMAND. AND THE LAST COMMAND IS QUIT COMMAND IF THE USER WRITES QUIT
#            started = True THE CODE GETS TERMINATED MEANS THE GAME IS OVER.
#            print("Car Started!") AND THE USER TYPES ANY OTHER COMMAND OTHER THAN THESE THEN THE STATEMENT WILL APPEAR THAT
#    elif command == "stop": SORRY I DON'T UNDERSTAND  THAT
#        if not started:
#            print("Car is already stopped!")
#        else:
#            started = False
#            print("Car Stopped!")
#    elif command == "help":
#        print("""
#start - To start the car
#stop - To stop the car
#quit - To quit
#        """)
#    elif command == "quit":
#        break
#    else:
#        print("Sorry! I don't understand that")

# For Loop

#prices = [30, 60, 90]
#total = 0  IN THIS WE HAVE TO PRINT THE TOTAL OF THE PRICES IN THE LIST
#for price in prices:  FOR THAT WE USE FOR LOOP WHICH WILL TAKE THE FIRST ITEM THEN IT WILL BE IN THE TOTAL THEN AGAIN
#   total += price IT GOESTO THE START AND THIS TIME IT TAKESTHE SECOND ITEM WHICH GETS ADDED TO THE TOTAL AND THE PROCESS
#print(f" {total}") HAPPENS ONE MORE TIME BUT THIS  TIME ONCE THE ITEM IS ADDED TO THE TOTAL IT WILL PRINT THE TOTAL AS THERE
# NO OTHER ITEMS IN THE LIST.

#THIS IS TOPRINT THE ALPHABATE AS LETTER L WITH THE HELP OF x
#numbers = [2, 2, 2, 2, 7]
#for x_count in numbers:
#    output = ''
#    for count in range(x_count):
#        output += 'x'
#    print(output)


#THIS THE SAME AS ABOVE


#for items in numbers:
#    print('x' * items)

#LISTS

#TO PRINT THE MAX NO. IN THE LIST
#numbers = [2, 4, 5, 7, 12, 14, 6]
#max = numbers[0]
#for number in numbers:
#    if number > max:
#        max = number
#print(max)

#TO PRINT THE MATRIX NUMBERS IN ONE LIST
#matrix = [
#    [1, 2, 3],
#    [4, 5, 6],
#    [7, 8, 9],
#]
#for row in matrix:
#    for item in row:
#        print(item)

#TO REMOVE THE DUPLOCATES
#numbers = [2, 2, 4, 6, 3, 4, 6, 1]
#uniques = []
#for number in numbers:
#    if number not in uniques:
#        uniques.append(number)
#print(uniques)

#DICTIONARY
#phone = input("Phone: ")
#digits_mapping = {
#    "1" : "One",
#    "2" : "Two",
#    "3" : "Three",
#    "4" : "Four"
#}
#output = ""
#for ch in phone:
#    output += digits_mapping.get(ch, "!") + " "
#print(output)

#How to print emojis in python (Windows + full stop)
#message = input(">")
#words = message.split(' ')
#emojis = {
#    ":)": "😃",
#    ":(": "😢"
#}
#output = ""
#for word in words:
#    output += emojis.get(word, word) + " "
#print(output)

#FUNCTIONS
#def greet_user():
#    print("Hi there!")
#    print("Welcome Aboard")


#greet_user()

#calling the function
#def greet_user(first_name, last_name):
#    print(f'Hi {first_name}, {last_name}!')
#    print('Welcome aboard')
#
#
#greet_user("John", "Smith")

#def square(number):
#    return number * number
#
#
#print(square(3))

#The emoji converter but in the function form differnt from above one

#def emoji_converter(message):
#    words = message.split(" ")
#    emojis = {
#        ":)":"😃",
#        ":(":"😢"
#    }
#    output = ""
#    for word in words:
#        output += emojis.get(word, word) + ' '
#    return output
#
#message = input(">")
#print(emoji_converter(message))

#Exception case
#try:
#    age= int(input("Age: "))
#    income = 20000
#    risk = income / age
#    print(age, risk)
#except ZeroDivisionError:
#    print("Age cannot be 0!")
#except ValueError:
#    print("Invalid Input")

#CLASS

#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#
#
#    def move(self):
#       print("move")
#
#    def draw(self):
#        print("draw")
#
#
#point1= Point(10, 20)
#point1.x = 11
#print(point1.x)

#class Person:
#    def __init__(self, name): #<---- This is a Constructor
#        self.name = name
#
#    def talk(self):
#        print(f"Hi, I'm {self.name}")
#
#john = Person("John Smith")
#john.talk()
#
#bob = Person("Bob Smith")
#bob.talk()

# TILL HERE CODE UPLOADED


#INHERITANCE
#class Mammal:
#    def walk(self):
#        print("walk")
#
#
#class Dog(Mammal):
#    def bark(self):
#        print("bark")
#
#
#class Cat(Mammal):
#    def be_annoying(self):
#        print("annoying")
#
#
#dog1 = Dog()
#dog1.walk()
#dog1.bark()
#
#cat1 = Cat()
#cat1.walk()
#cat1.be_annoying()


#MODULES
# this code is connected to the secondary file so that the code is not compiled in 1 file and the code in  the second file can be used
#import converter  -->>   for any other code or project
#from converter import kg_to_lbs
#
#kg_to_lbs(100)
#
#print(converter.kg_to_lbs(70))

# from converter import find_max
# SO THERE IS A BUILT IN FUNCTION AS MAX SO WE HAVE TO CHANGE THE NAME OF THE VARIABLE FROM MAX TO MAXIMUM
# numbers = [2, 4, 5, 7, 12, 14, 6] -->>
# maximum = find_max(numbers)

# print(maximum)

#RANDOM LIBRARY
# import random
#IN THIS LIBRARY WE CAN GET ANY RANDOM NUMBER OR VARIABLE ONCE WE SET THE RANGE OR GIVE IT A LIST TO CHOOSE
#SO IN THIS WE GAVE IT SO DICE THAT IS IF WE ROLL THE DICE WHAT WILL BE THE OUTCOME SO IT WILL BE A RANDOM FROM 1 TO 6
# class Dice: # WE GAVE THE FUNCTION A TUPLE FROM RANGE 1 TO 6
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())


#NOTE ->>>> THIS CODE SHOULD BE UPLOADED IN DIFFERENT REPO
# THIS IS A FUNCTION THAT IS USED TO SHOW OR BRING THE DIFFERENT DIRECTORY TO A CERTAIN FILE
# from pathlib import Path
#
# path = Path()
# for file in path.glob('*.*'):
#     print(file)

#THIS IS A PROJECT THAT CONNECTS PYTHON AND EXCEL
# import openpyxl as xl FOR THAT WE HAVE TO IMPORT OR INSTALL THIS LIBRARY
# from openpyxl.chart import BarChart, Reference
#
# def process_workbook(filename):
#     wb = xl.load_workbook(filename)
#     sheet = wb['Sheet1']
#
#     for row in range(2, sheet.max_row + 1):
#         cell = sheet.cell(row, 3)
#         corrected_price = cell.value * 0.9
#         corrected_price_cell = sheet.cell(row, 4)
#         corrected_price_cell.value = corrected_price
#
#     values = Reference(sheet,
#             min_row=2,
#             max_row=sheet.max_row,
#             min_col=4,
#             max_col=4)
#
#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart, 'e2')
#
#     wb.save(filename)
