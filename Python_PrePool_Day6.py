"""
    Clément BADRONE
    Last Update 16/09/2024
    EPITECH Pre-Pool PreMSC
"""

import time

def Task_1_1():
    """Can you explain this piece of code?"""

    def f(x):
        return 2*x+1
    def g():
        return 7
    
    # Return 2 * 2 + 1 = 5
    y = f(2)
    print(y)

    # Return 2*5+1 + 7 = 18 
    y = f(5) + g()
    print(y)

#Task_1_1()

def Task_1_2():
    """Using the following functions, display a lettuce-tomato-double ham sandwich in your terminal."""

    def bread():
        print("</////////>")

    def lettuce():
        print("~~~~~~~~~~~")

    def tomato():
        print("0 0 0 0 0 0")

    def ham():
        print("===========")

    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

#Task_1_2()

def Task_1_3():
    """Make 42 of those lettuce-tomato-double ham sandwiches"""

    def bread():
        print("</////////>")

    def lettuce():
        print("~~~~~~~~~~~")

    def tomato():
        print("0 0 0 0 0 0")

    def ham():
        print("===========")

    for i in range(42):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

#Task_1_3()

def Task_1_4(p_iterations):
    """Write a function that takes the number of sandwiches to prepare as a parameter and displays
    as many sandwiches as requested."""

    def bread():
        print("</////////>")

    def lettuce():
        print("~~~~~~~~~~~")

    def tomato():
        print("0 0 0 0 0 0")

    def ham():
        print("===========")

    for i in range(p_iterations):
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()

#Task_1_4(3)

def Task_1_5(p_iterations, isVeggie=False):
    """Add a new parameter to your previous function.
    It should provide the possibility to make a vegetarian sandwich (double vegetables and no ham).
    If this option is not specified, by default, the sandwich must be a lettuce-tomato-double ham
    one."""

    def bread():
        print("</////////>")

    def lettuce():
        print("~~~~~~~~~~~")

    def tomato():
        print("0 0 0 0 0 0")

    def ham():
        print("===========")

    for i in range(p_iterations):
        bread()
        if isVeggie:
            lettuce()
            lettuce()
            tomato()
            tomato()
        else:
            lettuce()
            tomato()
            ham()
            ham()
        bread()

#Task_1_5(3, True)

def Challenge():
    """Write a little program that computes the power function as fast as possible.
    How long does it take to compute 4284?
    How long does it take to compute 42168?
    """

    start_time = time.time()
    a = 42
    for _ in range(168):
        a*=42
    print(time.time() - start_time, a)

#Challenge()

def Task_2_1(p_string):
    """Write a recursive function that tests if a string is a palindrome, such as “kayak”, “never odd or
    even” or “Was it a car or a cat I saw?”.
    """

    p_string = p_string.strip()
    if len(p_string) <=1:
        return True
    
    if p_string[0] == p_string[-1]:
        return Task_2_1(p_string[1:-1])
    else:
        return False
    
#print(Task_2_1("never odd or even"))

def Task_2_2():
    """Write a program that lists all the files and directories in the current directories, as well as all files
    and directories in its sub-directories and so on.
    """

    import os
    path = "."
    for root, d_names, f_names in os.walk(path):
        print(root, d_names, f_names)

#Task_2_2()

def Task_3_1():
    """Write 5 functions, each taking a string s and an integer n as parameters and returning a boolean:"""

    def funA(s, n):
        # If 's' contains at least 'n' lowercase letters
        compt = 0
        for char in s:
            if str.islower(char):
                compt+=1
        if compt >= n:
            return True
        return False
        
    def funB(s, n):
        # If 's' contains at least 'n' uppercase letters
        compt = 0
        for char in s:
            if str.isupper(char):
                compt+=1
        if compt >= n:
            return True
        return False

    def funC(s, n):
        # If 's' contains at least 'n' characters
        if len(s)>= n:
            return True
        return False
    
    def funD(s, n):
        # If 's' contains at least 'n' special characters
        special = "!@#$%^&*()-+?_=,<>/"
        compt = 0
        for char in s:
            if char in special:
                compt += 1
        if compt >= n:
            return True
        return False
    
    def funE(s, n):
        # If 's' contains at least 'n' numbers
        num = "0123456789"
        compt = 0
        for char in s:
            if char in num:
                compt+=1

        if compt >= n:
            return True
        return False
    
    print(funA("TesT", 2))
    print(funA("miaou", 3))

    print(funB("TesT", 2))
    print(funB("miaou", 3))

    print(funC("test", 4))
    print(funC("miaou", 10))

    print(funD("te$t!", 2))
    print(funD("$=/!", 20))

    print(funE("134", 3))
    print(funE("test", 4))

#Task_3_1()

def Task_3_2():
    """Write a generic function that checks if a password is valid.
    This function should be callable the following way:"""

    def check_password(funct, nbMin, password):
        if not isinstance(nbMin, int) or nbMin < 0:
            print(f"Le paramètre 'nbMin' doit être un entier positif ou nul !")
            return False
        if not isinstance(funct, str):
            print(f"Le paramètre 'funct' doit être une chaine de caractères !")
            return False
        if not isinstance(password, str):
            print(f"Le paramètre 'password' doit être une chaîne de caractères !")
            return False

        # Check lowercase letters
        def lower(pwd, nbMin):
            compt = 0
            for char in pwd:
                if str.islower(char):
                    compt+=1
            return compt >= nbMin

        # Check special letters
        def special(pwd, nbMin):
            spe = "!@#$%^&*()-+?_=,<>/"
            compt = 0
            for char in pwd:
                if char in spe:
                    compt += 1
            return compt >= nbMin
        
        # Check 'number' letters
        def number(pwd, nbMin):
            num = "0123456789"
            compt = 0
            for char in pwd:
                if char in num:
                    compt+=1
            return compt >= nbMin
        
        # Check 'upper' letters
        def upper(pwd, nbMin):
            compt = 0
            for char in pwd:
                if str.isupper(char):
                    compt+=1
            return compt >= nbMin
        
        # Check length of the password
        def length(pwd, nbMin):
            if len(pwd) >= nbMin:
                return True
            return False

        # Switch case on the function name
        isValid = False
        match funct.lower():
            case "lower":
                isValid = lower(password, nbMin)
            case "special":
                isValid = special(password, nbMin)
            case "number":
                isValid = number(password, nbMin)
            case "upper":
                isValid = upper(password, nbMin)
            case "length":
                isValid = length(password, nbMin)
            case default:
                print(f"La fonction '{funct}' n'est pas recconue ! Choississez une fonction valide.")
                return False

        # Return boolean value
        if isValid:
            return True
        return False
    
    mdp = "Monmotdepasse!"
    print(check_password(5, 4, mdp))
    print(check_password("miaou", 3, mdp))
    print(check_password("lower", -156, mdp))
    print(check_password("lower", "4", mdp))
    print(check_password("lower", 4, 54))
    print(check_password("lower", 4, mdp) and check_password("special", 1, mdp) and check_password("upper", 1, mdp))
    
#Task_3_2()

