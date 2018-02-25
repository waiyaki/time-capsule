# -*- coding: utf-8 -*-
"""
    * Linux : Spyder *
Created on Sun Jun  1 15:46:01 2014

@author: bugtraq : Waiyaki
"""
from __future__ import division
from __future__ import print_function

from random import randint
import sys

class Student(object):
    def __init__(self, name):
        self.name = name
    
    def resolve_sign(self, v1, v2, sign):
        """
        Function resolves the sign given and executes the appropriate type
        of computation.
        """
        if sign == '*' or sign == 'x':
            return v1 * v2
        elif sign == '+':
            return v1 + v2
        elif sign == '-':
            return v1 - v2
        elif sign == '/':
            return v1 / v2
            
    def verify(self, trial, v1, v2, sign, count, fail):
        """
        Function checks the validity of users input to avoid errors.
        """
        self.check_exit(trial, count, fail)
        
        while len(trial) < 1:
            # Case where the user hits "Enter" without first giving the answer.
            print("Please try again:\n")
            trial = raw_input("{:2d}. {:2d} {} {:2d} = ".format(count, v1, sign, v2))
            self.check_exit(trial, count, fail)
        while True:
            try:
                trial = int(trial) # convert the input from a str to an int
                break
            except ValueError:#Case when the users input can't be converted to int
                print("Incorrect answer. Please enter a number:\n")
                trial = raw_input("{:2d}. {:2d} {} {:2d} = ".format(count, v1, sign, v2))
                self.check_exit(trial, count, fail)
        return trial
    
    def check_exit(self, trial, count, fail):
        if trial in ['exit', 'e']:
            print("""
            Out of the {} questions you attempted, you scored {} and
            failed {}.
            You did not finish this level.
            
            Goodbye. Hope to see you soon.
            """.format(count, (count) - fail, fail))
            sys.exit(1)
        else:
            pass
        
    def Maths(self, lim1, lim2, level, sign, q=25):
        '''
        Gives the student an exercise of mathematics questions, checks them
        and computes the percentage score.
        '''
        print("\n{}\n".format(level))
        print("Please type in the correct answers to the given question\n"\
        "or type 'exit' to finish.\n")
        count = 0
        fail = 0

        while count <= q:
            v1 = randint(lim1, lim2)
            v2 = randint(lim1, lim2)
            
            if sign == '/':
                while True:
                    if v1 % v2 != 0:
                        v2 = randint(lim1, lim2)
                    elif v2 == v1:
                        v1 = randint(lim1, lim2)
                    else:
                        break
            elif sign == '-':
                while v1 < v2:
                    v1 = randint(lim1, lim2)
            
            ans = self.resolve_sign(v1, v2, sign)
            
            trial = raw_input("{:2d}. {:2d} {} {:2d} = ".format(count, v1, sign, v2))
            
            trial = self.verify(trial, v1, v2, sign, count, fail)            
            
            if trial != ans:
                fail += 1
                while trial != ans:
                    print("{} is not the correct answer. Please try again.\n".format(trial))
                    trial = raw_input("{:2d}. {:2d} {} {:2d} = ".format(count, v1, sign, v2))
                    trial = self.verify(trial, v1, v2, sign, count, fail)      
            print("     Correct!\n")
            count += 1 
        count -= 1
        score = count - fail
        print("You got {} out of {} and failed {}.".format(score, count, fail))
        print("Your percentage score is {:.2f} %".format((score/count)*100))
        
    def practice(self, lev, level, numbers, elements):
        """
        Gives the user a practice exercise that teaches the user multiplication.
        """
        print("\n",lev)
        count = 0
        fail = 0
        print("\nYou are in Multiplication Practice, level ", level,"\n")
        print("Please type in the correct answers to the given question\n"\
        "or type 'exit' to finish.\n")
        
        cont = 'yes'
        for element in elements:
            if cont in ['yes', 'y']:
                for i in xrange(2, numbers):
                    ans = element * i
                    
                    if element % 2 == 0:
                        trial = raw_input("{:20d}. {:2d} x {:2d} = ".format(count, element, i))
                    else:
                        trial = raw_input("{:2d}. {:2d} x {:2d} = ".format(count, element, i))
                    
                    trial = self.verify(trial, element, i, 'x', count, fail)
                    
                    if trial != ans:
                        fail += 1
                        while trial != ans:
                            if element % 2 == 0:
                                print("{:22d} is not the correct answer. Please try again:\n".format(trial))
                                trial = raw_input("{:20d}. {:2d} x {:2d} = ".format(count, element, i))
                            else:
                                print("{:2d} is not the correct answer. Please try again:\n".format(trial))
                                trial = raw_input("{:2d}. {:2d} x {:2d} = ".format(count, element, i))
                            trial = self.verify(trial, element, i, 'x', count, fail)
                    count += 1
                print("\nDo you want to continue with practice (yes or no)?")
                cont = raw_input("> ")
                while True:
                    if len(cont) < 1 or cont not in ['yes', 'no', 'y', 'n']:
                        print("Do you want to continue with practice (yes or no)?")
                        cont = raw_input("> ")
                    else:
                        break
            else:
                break
        count = count - 1
        score = count - fail
        print("You scored {} out of {} and failed {}.".format(score, count, fail))
        print("Your percentage score is {:.2f} %".format((score/count)*100))
        
def get_name():
    print("""
    WELCOME TO THE MATHEMATICS LESSON.
    
    Please start by entering your name below.\n""")
    
    name = raw_input("What is your name: ")
    while True:
        # Name has to be 3 or more characters long.
        if len(name) >= 3:
            break
        else:
            print("Please enter your name:")
            name = raw_input("> ")
            
    # Check and correct the Capitalization of user's name.        
    name = name.split(' ')
    for i in xrange(len(name)):
        name[i] = name[i][0].upper()+name[i][1:]
        
    name = ' '.join(name)
    
    return name
  
def get_level():
    """
    Function gets the class level  of the user.
    """
    print("Please choose the number you want:")
    print("""
    Exercise Questions
    ___________________
    1. Level 1: (Class 2 - 3)
    2. Level 2: (Class 3 - 4)
    3. Level 3: (Class 4 - 5)
    
    Practice Questions
    ___________________
    4. Class 2 - 3
    5. Class 4 - 5
    """)
    levels = "1,2,3,4,5,6"
    levels = levels.split(',')
    
    level = raw_input("> ")
    while True:
        if level not in levels:
            print("Please enter your correct level:")
            level = raw_input("> ")
        else:
            break    
    return level
    
def get_operation():
    """
    Function gets the preferred choice of maths from the user.
    """
    print("\nPlease select the maths you want to do: ")
    print("""
    Exercises.
    ______________
    1. Multiplication
    2. Addition
    3. Subtraction
    4. Division
    """)
    pref = raw_input("> ")
    
    return pref

def check_level_pref(level, pref):
    """
    Checks validity of users input to prevent errors.
    """
    while True:
        while len(pref) < 1:
            print("Please choose the maths you want to do: ")
            pref = raw_input("> ")
        
        while True:
            try:
                pref = int(pref)
                while pref > 5:
                    print("Error. Please choose another exercise.")
                    pref = eval(raw_input("> "))
                break
            except (NameError, ValueError):
                print("Please enter a number 1, 2, 3, or 4: ")
                pref = raw_input("> ")
                
        while len(level) < 1:
            print("Please choose levels 1, 2 or 3:")
            level = raw_input("> ")
            
        while True:
            try:
                level = int(level)
                while level > 5:
                    print("Error. Please choose another level.")
                    level = raw_input("> ")
                break
            except ValueError:
                print("Please enter a number 1, 2 or 3: ")
                level = raw_input("> ")
        break
    return level, pref

def practice_pref(level):
    print("""
    Practice Questions
    __________________
    
    5. Multiplication Practice
    """)
    if level == '4':
        numbers = 11
        elements = [i for i in xrange(2, 11)]
    elif level == '5':
        numbers = 16
        elements = [i for i in xrange(9, 21)]
    pref = raw_input("> ")
        
    return pref, numbers, elements

def limits(level):    
    if level == '1':
        lim1 = 2
        lim2 = 10
    elif level == '2':
        lim1 = 2
        lim2 = 20
    elif level == '3':
        lim1 = 2
        lim2 = 100
        
    return lim1, lim2
    
def user():
    """
    Function consolidates other functions, gets data from the user and passes 
    the data on to the relevant functions for processing.
    """
    name = get_name()
    student = Student(name)
    
    print("\n{}".format(name))
    print("______________________________________________\n")
    
    level = get_level()
    if level == '4' or level == '5':
        pref, numbers, elements = practice_pref(level)
    else:        
        pref = get_operation()
        lim1, lim2 = limits(level)
        
    level, pref = check_level_pref(level, pref)    
    
    if (level==1 or level==2) and (pref == 1 or pref == 4):
        lim2 = lim2/2
        
    if pref == 1:
        lev = 'Multiplication Exercise: Level ' + str(level)
        sign = 'x'
        student.Maths(lim1, lim2, lev, sign)
    elif pref == 2:
        lev = 'Addition Exercise: Level ' + str(level)
        sign = '+'
        student.Maths(lim1, lim2, lev, sign)
    elif pref == 3:
        lev = 'Subtraction Exercise: Level ' + str(level)
        sign = '-'
        student.Maths(lim1, lim2, lev, sign)
    elif pref == 4:
        lev = 'Division Exercise: Level ' + str(level)
        sign = '/'
        student.Maths(lim1, lim2, lev, sign)
    elif pref == 5:
        lev = 'Multiplication Practice Questions: Level ' + str(level)
        student.practice(lev, level, numbers, elements)
        
# Call the function "user()" to commence execution    
user()
   
while True:
    print("\n\nDo you want to start over(yes or no)?")
    repeat = raw_input("> ")
    while True:
        if len(repeat) < 1 or repeat not in ['yes', 'no', 'y', 'n']:
            print("\n\nDo you want to start over(yes or no)?")
            repeat = raw_input("> ")
        else:
            break
        
    if repeat not in ['yes', 'y']:
        print("""
        I HOPE YOU ENJOYED THE LESSON.
        I HOPE TO SEE YOU SOON.
        
        Goodbye....
        """)
        sys.exit(1)
    else:
        print("""
        WELCOME BACK.\n\n\n
        """)
        user()