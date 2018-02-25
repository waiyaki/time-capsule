# -*- coding: utf-8 -*-
"""
@Ubuntu Linux ~ Bugtraq II-Black Widow
Created on Fri Jun 20 14:18:35 2014

@author: Waiyaki ~ #Spyder
"""

from random import randint
import sqlite3
import string
import time
import sys
import os


class Student(object):
    """
    Class contains all the necessary methods to let kids learn maths,
    especially integer multiplication, all on their own.
    """

    def __init__(self, name):
        self.name = name

    def connect(self):
        """
        Method connects to the database if it exists, creates one and
        the necessary tables/columns in it otherwise.
        """
        db_name = 'students.db'
        create = not os.path.exists(db_name)

        connection = sqlite3.connect(db_name)

        if create:
            c = connection.cursor()
            c.execute("CREATE TABLE student ("
                      "id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, "
                      "name TEXT UNIQUE NOT NULL, "
                      "time_spent FLOAT DEFAULT 0.0, "
                      "maths_time FLOAT DEFAULT 0.0, "
                      "practice_time FLOAT DEFAULT 0.0, "
                      "points FLOAT DEFAULT 0.0, "
                      "exercises INTEGER DEFAULT 0, "
                      "practices INTEGER DEFAULT 0, "
                      "highest_score FLOAT DEFAULT 0.0, "
                      "lowest_score FLOAT DEFAULT 100.0)")
            connection.commit()
        return connection

    def user(self, repeat):
        """
        Method reads in a name, corrects it, checks whether the name is in
        the database, if not, it registers the new user, otherwise, it uses
        the username already in the database.
        """
        connection = self.connect()
        c = connection.cursor()

        usr_name = self.name
        self.name_exit(usr_name)
        usr_name = self.check_name(usr_name)

        c.execute("SELECT name FROM student")
        names = []
        for row in c.fetchall():
            names.append(row)

        loop = True
        while loop:
            if len(names) != 0:
                for name in names:
                    name = str(name)
                    name = name.strip("(',)")
                    if usr_name in name:
                        geek_print(
                            "\nIs your name {} (yes or no)?".format(name))
                        ans = input("> ")
                        ans = ans.lower()
                        if ans in 'yes':
                            usr_name = name
                            loop = False  # Will discontinue while loop
                            break  # Out of for
                    elif repeat:
                        # In case user is repeating with a different username
                        geek_print("\nWhat is your name?")
                        usr_name = input("> ")
                        usr_name = self.check_name(usr_name)
                        repeat = False  # Prevents this elif from another execution
                        break  # Out of the for loop, so that the loop can start
                        # over at the while loop so that the new name can be
                        # evaluated
                else:
                    geek_print("""
                    You must be a new user.
                    To register, please enter your full name
                    or enter 'exit' or 'quit' to finish
                    """)
                    new_user = input("> ")
                    new_user = self.check_name(new_user)
                    usr_name = self.register(new_user)
                    loop = False
            else:
                geek_print("""
                You must be a new user.
                To register, please enter your full name
                or enter 'exit' or 'quit' to finish
                """)
                new_user = input("> ")
                new_user = self.check_name(new_user)
                usr_name = self.register(new_user)
                loop = False

        connection.commit()
        return usr_name

    def check_reg_name(self, name):
        """
        Method checks the registration name.
        Name has to be at least 2 strings to increase chances of
        uniqueness, e.g Janet Lagat Kiplagat
        """
        name = name.split(' ')
        while len(name) <= 2 or len(name) > 4:
            geek_print("""
            Please enter your full name:
            e.g Janet Lagat Kiplagat """)
            name = input("> ")
            name = name.split(' ')

        name = ' '.join(name)
        name = self.check_name(name)
        return name

    def register(self, name):
        """
        Method registers a new user
        """
        try:
            connection = self.connect()
            c = connection.cursor()

            name = self.check_reg_name(name)
            c.execute("INSERT INTO student (name) VALUES (?)", (name,))

            connection.commit()
            return name
        except:
            output = """
            \n\n{0} is already in the database. I am going to assume \n{0} is your name.
            """.format(name)
            geek_print(output)
            return name

    def check_name_length(self, name):
        """
        Method checks the length of the name.
        Name length has to be not less than 3.
        """
        while True:
            # Name has to be 3 or more characters long.
            if len(name) >= 3:
                self.name_exit(name)
                break
            else:
                geek_print("Please enter your full name:")
                name = input("> ")
        return name

    def check_name(self, name):
        """
        Method checks name, strips excess whitespace, capitalizes
        as needed.
        """
        # Check length
        name = self.check_name_length(name)

        # Strip whitespace (When the user hits spacebar twice?)
        word = ''
        results = []
        whitespace = string.whitespace
        for char in name:
            if char in whitespace:
                if word:
                    results.append(word)
                    word = ''
            else:
                word += char
        if word:
            results.append(word)
        name = ' '.join(results)

        # Capitalize
        name = name.lower()
        name = name.split(' ')
        for i in range(len(name)):
            name[i] = name[i][0].upper() + name[i][1:]

        name = ' '.join(name)

        return name

    def name_exit(self, text):
        """
        Method checks whether the user wants to quit, from their
        name input.
        """
        text = text.lower()
        exit_statements = ["\nProgram will now exit.",
                           "\n\nIt was nice having you around...",
                           "\n\nI hope to see you some time again soon..."
                           "\n\nGOODBYE!\n"
                           ]
        time_delay = 1
        while len(text) > 1:
            if text in 'exitquit':
                for i in range(len(exit_statements)):
                    for char in exit_statements[i]:
                        print(char, end='')
                        time.sleep(0.02)
                    time_delay -= 0.25
                    time.sleep(time_delay)
                sys.exit()
            else:
                pass
            break

    def load_stats(self, name):
        """
        Method loads the user's data from the database
        """
        time_spent = []
        maths_time = []
        practice_time = []
        points = []
        exercises = []
        practices = []
        highest_score = []
        lowest_score = []

        connection = self.connect()
        c = connection.cursor()

        rows = [time_spent, maths_time, practice_time, points,
                exercises, practices, highest_score, lowest_score]
        columns = ['time_spent', 'maths_time', 'practice_time', 'points',
                   'exercises', 'practices', 'highest_score', 'lowest_score']
        # try:
        for i in range(len(columns)):
            sql = '''SELECT ''' + \
                columns[i] + ''' FROM student WHERE name="{}"'''.format(name)
            c.execute(sql)
            for row in c.fetchone():
                rows[i].append(row)
        return rows
        # except TypeError:
        # pass
        # print("\nNo prior records for {} found.\n".format(name))

    def view_stats(self, name):
        """
        Method prints out the user's performance, given the user's name.
        """
        rows = self.load_stats(name)
        time_spent = rows[0][0]
        total_time = (time_spent) / 60
        string = """
        Results for:
            {}:
                Points accumulated so far               : {:<5.2f} points
                Number of math exercises done so far    : {:<5d} exercises
                Number of practice exercises done so far: {:<5d} practice exercises
                Highest score (in percentage)           : {:<5.2f} %
                Lowest score                            : {:<5.2f} %
                Total time spent in class               : {:<5.2f} minutes
                \n
                """.format(name, rows[3][0], rows[4][0], rows[5][0], rows[6][0],
                           rows[7][0], total_time)

        geek_print(string)

    def update_data(self, name, column, value):
        """
        Method updates the database.
        """
        connection = self.connect()
        c = connection.cursor()
        c.execute("UPDATE student SET {}={} WHERE name='{}'".format(
            column, value, name))
        connection.commit()

    def get_level(self):
        """
        Method gets the class level  of the user.
        """
        output = "\nPlease choose your class:"
        geek_print(output)
        print("""
        Exercise Questions
        ___________________
        1. Level 1: (Class 2 - 3)
        2. Level 2: (Class 3 - 4)
        3. Level 3: (Class 4 - 5)

        Practice Multiplication Questions
        ___________________
        4. Class 2 - 3
        5. Class 4 - 5
        """)
        levels = "1,2,3,4,5"
        levels = levels.split(',')

        level = input("> ")
        while True:
            if level not in levels:
                self.name_exit(level)
                print("Please enter your correct level:")
                level = input("> ")
            else:
                break
        return level

    def practice_pref(self, level):
        """
        Method similar to self.limits(level), but for the practice
        method.
        """
        level = str(level)
        if level == '4':
            numbers = 11
            elements = [i for i in range(2, 11)]
        elif level == '5':
            numbers = 16
            elements = [i for i in range(9, 21)]
        return numbers, elements

    def get_operation(self):
        """
        Method gets the preferred choice of maths from the user.
        """
        output = "\nPlease select the maths you want to do: "
        geek_print(output)
        print("""
        Exercises.
        ______________
        1. Multiplication
        2. Addition
        3. Subtraction
        4. Division
        """)
        pref_op = input("> ")
        self.name_exit(pref_op)

        return pref_op

    def limits(self, level):
        """
        Method determines the max and min limits within which
        mathematical questions should be bound, according to the user's
        class level.
        """
        level = str(level)
        if level == '1':
            lim1 = 2
            lim2 = 16
            return lim1, lim2
        elif level == '2':
            lim1 = 2
            lim2 = 100
            return lim1, lim2
        elif level == '3':
            lim1 = 2
            lim2 = 1000
            return lim1, lim2
        elif level == '4' or level == '5':
            # These are practice levels
            pass

    def check_level_pref(self, value):
        """
        Checks validity of users input to prevent errors.
        Checks level and practice preference inputs
        """
        while True:
            while len(value) < 1:
                geek_print("Please choose the maths you want to do: ")
                value = input("> ")
                self.name_exit(value)

            while True:
                try:
                    value = int(value)
                    while value > 5:
                        geek_print("Error. Please choose another exercise.")
                        value = eval(input("> "))
                    break
                except (NameError, ValueError):
                    geek_print("Please enter a number 1, 2, 3, or 4: ")
                    value = input("> ")
                    self.name_exit(value)
            break
        return value

    def resolve_sign(self, v1, v2, sign):
        """
        Method resolves the sign given and executes the appropriate type
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
        Method checks the validity of users input to avoid errors.
        """
        while len(trial) < 1:
            # Case where the user hits "Enter" without first giving the answer.
            geek_print("Please try again:\n")
            trial = input("{:2d}. {:2d} {} {:2d} = ".format(count, v1,
                                                            sign, v2))
        while True:
            try:
                trial = int(trial)  # convert the input from a str to an int
                break
            except ValueError:
                self.check_exit(trial, count, fail)
                # Case when the users input can't be converted to int
                geek_print("Incorrect answer. Please enter a number:\n")
                trial = input("{:2d}. {:2d} {} {:2d} = ".format(count, v1,
                                                                sign, v2))
        self.check_exit(trial, count, fail)
        return trial

    def check_exit(self, trial, count, fail):
        """
        Method checks whether the user wishes to exit from their
        input.
        """
        trial = str(trial)
        trial = trial.lower()
        while len(trial) > 1:
            if trial in 'exitquit':
                output = """
                Out of the {} questions you attempted, you scored {} and
                failed {}.
                You did not finish this level.\n\n
                """.format(count, (count) - fail, fail)
                geek_print(output)
                exit_statements = ["\n\nPlease wait...",
                                   "\n\nCleaning up......",
                                   "\n\nIt was nice having you around. Hope to see you soon...",
                                   "\n\nPreparing to exit......",
                                   "\n\nProgram will now exit.",
                                   "\n\nGOODBYE!\n\n"]
                delay = 1
                for i in range(len(exit_statements)):
                    for char in exit_statements[i]:
                        print(char, end='')
                        time.sleep(0.02)
                    delay -= 0.15
                    time.sleep(delay)
                sys.exit()
            else:
                break
        else:
            pass

    def process_levels_prefs(self, level, pref):
        """
        Method processes the level and preferences of the user to adjust the
        limits according to the level the user is in.
        """
        lim1, lim2 = self.limits(level)
        if pref == 1:
            lev = 'Multiplication Exercise: Level ' + str(level)
            sign = 'x'
            return (lim1, lim2, lev, sign)
        elif pref == 2:
            lev = 'Addition Exercise: Level ' + str(level)
            sign = '+'
            return (lim1, lim2, lev, sign)
        elif pref == 3:
            lev = 'Subtraction Exercise: Level ' + str(level)
            sign = '-'
            return (lim1, lim2, lev, sign)
        elif pref == 4:
            lev = 'Division Exercise: Level ' + str(level)
            sign = '/'
            return (lim1, lim2, lev, sign)

    def Maths(self, name, level, pref, q=2):
        '''
        Gives the student an exercise of mathematics questions, checks them
        and computes the percentage score.
        '''
        t1 = time.time()
        lim1, lim2, lev, sign = self.process_levels_prefs(level, pref)
        print("\n{}\n".format(lev))
        geek_print("Please type in the correct answers to the given question\n"
                   "or type 'exit' or 'quit' to finish.\n")
        count = 0
        fail = 0
        rows = self.load_stats(name)

        while count <= q:
            count += 1
            if (level == 1 or level == 2) and sign == '/':
                # Increase the upper limit when the operation is a division
                lim2 = 100
                v1 = randint(lim1, lim2)
                # The divisor should always be between lim1 and 10 for this
                # level
                v2 = randint(lim1, 10)
            else:
                v1 = randint(lim1, lim2)
                v2 = randint(lim1, lim2)
            if sign == '/':
                # Ensure that the question involves numbers that are perfectly
                #   divisible
                if level == 1 or level == 2:
                    v2 = is_divisible(v1, v2, lim1, 10)
                else:
                    v2 = is_divisible(v1, v2, lim1, lim2)
            elif sign == '-':
                while v1 < v2:
                    v1 = randint(lim1, lim2)
            elif sign == '*' or 'x':
                v1 = randint(lim1, 13)
                v2 = randint(lim1, 10)

            ans = self.resolve_sign(v1, v2, sign)
            trial = input("{:2d}. {:2d} {} {:2d} = ".format(count, v1,
                                                            sign, v2))

            trial = self.verify(trial, v1, v2, sign, count, fail)

            if trial != ans:
                fail += 1
                while trial != ans:
                    geek_print(
                        "{} is not the correct answer. Please try again.\n".format(trial))
                    trial = input("{:2d}. {:2d} {} {:2d} = ".format(count, v1,
                                                                    sign, v2))
                    trial = self.verify(trial, v1, v2, sign, count, fail)
            print("     Correct!\n")
        score = count - fail
        percent = (score / count) * 100
        points = percent * 0.2  # 100% = 20 points
        geek_print("You got {} out of {} and failed {}.".format(
            score, count, fail))
        geek_print("Your percentage score is {:.2f} %".format(percent))
        geek_print(
            "\nCongratulations! You have added {:.2f} points!".format(points))

        # Gather the data to update the database
        maths_time = time.time() - t1
        time_spent = rows[0][0] + maths_time
        time_in_maths = rows[1][0] + maths_time
        points_in_db = rows[3][0] + points
        exercises = rows[4][0] + 1
        highest_score = rows[6][0]
        lowest_score = rows[7][0]
        if percent > highest_score:
            self.update_data(name, 'highest_score', percent)
        if percent < lowest_score:
            self.update_data(name, 'lowest_score', percent)
        updates = ['time_spent', 'maths_time', 'points', 'exercises']
        update_values = [time_spent, time_in_maths, points_in_db, exercises]
        # Update the database
        for i in range(len(updates)):
            self.update_data(name, updates[i], update_values[i])

    def practice(self, name, level):
        """
        Gives the user a practice exercise that teaches the user multiplication.
        """
        t1 = time.time()
        lev = 'Multiplication Practice Questions: Level ' + str(level)
        geek_print(lev)
        count = 0
        fail = 0
        numbers, elements = self.practice_pref(level)

        geek_print(
            "\nYou are in Multiplication Practice, level {}\n".format(level))
        geek_print("""
        Please type in the correct answers to the given question\n
        or type 'exit' to finish.
        """)
        cont = 'yes'
        for element in elements:
            cont = cont.lower()
            if cont in ['yes', 'y']:
                for i in range(2, numbers):
                    ans = element * i

                    if element % 2 == 0:
                        trial = input("{:20d}. {:2d} x {:2d} = ".format(count,
                                                                        element, i))
                    else:
                        trial = input("{:2d}. {:2d} x {:2d} = ".format(count,
                                                                       element, i))

                    trial = self.verify(trial, element, i, 'x', count, fail)

                    if trial != ans:
                        fail += 1
                        while trial != ans:
                            if element % 2 == 0:
                                print(
                                    "{:22d} is not the correct answer. Please try again:\n".format(trial))
                                trial = input(
                                    "{:20d}. {:2d} x {:2d} = ".format(count, element, i))
                            else:
                                print(
                                    "{:2d} is not the correct answer. Please try again:\n".format(trial))
                                trial = input(
                                    "{:2d}. {:2d} x {:2d} = ".format(count, element, i))
                            trial = self.verify(
                                trial, element, i, 'x', count, fail)
                    count += 1
                if element % 3 == 0:
                    geek_print(
                        "\nDo you want to continue with practice (yes or no)?")
                    cont = input("> ")
                    while True:
                        if len(cont) < 1 or cont not in ['yes', 'no', 'y', 'n']:
                            geek_print(
                                "Do you want to continue with practice (yes or no)?")
                            cont = input("> ")
                        else:
                            break
            else:
                break
        count = count - 1
        score = count - fail
        geek_print("You scored {} out of {} and failed {}.".format(
            score, count, fail))
        geek_print("Your percentage score is {:.2f} %".format(
            (score / count) * 100))
        prac_time = time.time() - t1
        connection = self.connect()
        # Update database
        c = connection.cursor()
        c.execute(
            "SELECT time_spent, practice_time, practices FROM student WHERE name=?", (name,))
        rows = []
        for row in c.fetchall():
            rows.append(row)
        total_time = rows[0][0] + prac_time
        practice_time = rows[0][1] + prac_time
        practices = rows[0][2] + 1
        columns = ["time_spent", "practice_time", "practices"]
        values = [total_time, practice_time, practices]
        for i in range(len(columns)):
            self.update_data(name, columns[i], values[i])


def is_divisible(v1, v2, lim1, lim2):
    while True:
        # Count - try to avoid infinite loop? Maybe the number (v2) is prime?
        count = 1
        while v1 % v2 != 0 or v1 == v2:
            count += 1
            v2 = randint(lim1, lim2)
            if count % 10 == 0:
                v1 = randint(lim1, lim2)
        break
    return v2


def geek_print(string):
    """
    Function renders output in a way that attracts the eyes
    of the user.
    """
    for char in string:
        print(char, end='', flush=True)
        time.sleep(0.02)
        if char == '\n':
            time.sleep(0.01)
    print("\n")


def main(name, repeat=False):
    """
    Function initializes execution
    """
    student = Student(name)
    name = student.user(repeat)

    # Read database, get statistics, print them?
    geek_print("\nDo you want to view your performance so far (yes or no)?")
    view = input("> ")
    view = view.lower()
    if view in 'yes':
        student.view_stats(name)
    else:
        geek_print("\n\n------> Program will not show performance. <------\n\n")
        time.sleep(0.5)

    # Get the user's class, choice of math operations, check them
    level = student.get_level()
    if level == '4' or level == '5':
        level = student.check_level_pref(level)
        student.practice(name, level)
    else:
        level = student.check_level_pref(level)
        pref_op = student.get_operation()  # preferred mathematical operation
        pref_op = student.check_level_pref(pref_op)

        # Call up the Maths method, process user's level and preference, execute
        # the necessary computations.
        student.Maths(name, level, pref_op)
    return name


def init():
    geek_print("""
    WELCOME TO THE MATHEMATICS LESSON.

    Please start by entering your name below:

    """)
    # Get name, process it.
    geek_print("What is your name? \n")
    name = input("> ")
    name = main(name)

    while True:
        print("\n\nDo you want to start over (yes or no)? ")
        repeat = input("> ")
        while not repeat.isalpha():
            print("\nPlease enter the correct choice.\nDo you want to"
                  " start over (yes or no)? ")
            repeat = input("> ")

        repeat = repeat.lower()
        if repeat in 'yes':
            rep = True  # Is repeating?
            name = main(name, rep)
        else:
            geek_print("""
            Congratulations for your efforts.
            It was nice having you around.
            Hope to see you soon.
            \n\n{0}GOODBYE!{0}
            """.format('.' * 20))
            sys.exit()


if __name__ == '__main__':
    init()
