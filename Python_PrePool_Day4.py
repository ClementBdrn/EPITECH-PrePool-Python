"""
    Clément BADRONE
    Last Update 12/09/2024
    EPITECH Pre-Pool PreMSC
"""

def Task_1_1():
    """Evaluate and explain the following lines"""

    42 > 12 # return True
    #12 = 12 # Error !
    12 == 12 # return True
    "hello" == "world" # return False
    218 >= 118 # return True
    "a".upper() == "A" # return True
    1 * 2 * 3 * 4 <= 9 # return False
    "z" in "azerty" # return True

def Task_1_2():
    """Ask an integer to the user"""

    number = int(input("Give me a number : \n"))
    if number == 42:
        print("Correct Answer")
    else:
        print("Bad Answer")

#Task_1_2()

def Task_1_3():
    """Ask an integer to the user:
    ✓ if it's odd, display “This integer is odd” ;
    ✓ if it's even, display “This integer is even”."""

    number = int(input("Give me a number : \n"))
    if number%2 == 0:
        print("This integer is even")
    else:
        print("This integer is odd")

#Task_1_3()

def Task_1_4():
    """Ask the user to input a string:
    ✓ if it's “open sesame”, display “access granted” ;
    ✓ if it's "will you open, you goddamn !¤*@¡‘, display”access fucking granted" ;
    ✓ else, display “permission denied”."""

    password = input("Input a string : \n")
    if password == "open sesame":
        print("access granted")
    elif password == "will you open, you goddamn":
        print("acces fucking granted")
    else:
        print("permission denied")

#Task_1_4()

def Task_1_5():
    """Ask the user to input an integer:
    ✓ if it's 42, display “OK” ;
    ✓ if it's smaller or equal than 21, display “OK” ;
    ✓ if it's even, display “OK” ;
    ✓ if this integer divided by 2 is smaller than 21 (excluded), display “OK” ;
    ✓ finally, if it's is odd and greater or equal than 45, display “OK” ;
    ✓ in any other cases, display “You got wrong my poor friend!”."""

    integer = int(input("Give me a number : \n"))
    if integer == 42 or integer <= 21 or integer%2==0 or integer/2 < 21 or (integer%2!=0 and integer >= 45):
        print("OK")
    else:
        print("You got wrong my poor friend !")

#Task_1_5()

def Task_1_6():
    """Execute and fix the following code"""

    a = 42
    b = 41
    if a == b:
        print("A and B are the sames")
    if b <= a:
        print("B is equal or lower as A")
    if b != a:
        print("B his different from A")

#Task_1_6()

def Task_2_1():
    """Display all integers from 1 to 1000"""

    for i in range(1000):
        print(i+1)

#Task_2_1()

def Task_2_2():
    """Ask the user a string.
    Display all the characters of this string twice"""

    string = input("Give me a string : \n")
    val = ""
    for char in string:
        val+=char
        val+=char
    print(val)

#Task_2_2()

def Task_2_3():
    """Print all integers divisible by 7 from 10 000 to 1."""

    multiple = []
    for i in range(1,10001):
        if i % 7 == 0:
            multiple.append(i)
    print(multiple)

#Task_2_3()

def Task_2_4():
    """For all integers from -30 to 30:
    ✓ if it's a multiple of 3, display “Fizz”
    ✓ if it's a multiple of 5, display “Buzz”
    ✓ if it's a multiple of 3 and 5, display “FizzBuzz”
    ✓ if it does not meet any of the previous conditions, just print the integer itself"""

    for i in range(-30,31):
        if i % 3 == 0 and i % 5 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

#Task_2_4()

def Task_2_5():
    """Generate the lyrics of the song “99 bottles of beer”.
    The songs ends when there is no more bottles on the wall."""

    bottles = 99
    print(f'{bottles} bottles on the wall.')
    while bottles > 0:
        if bottles > 1:
            print(f'{bottles} bottles of beer. \nTake one down, pass it around. \n\n{bottles-1} bottles of beer on the wall.')
        else:
            print(f'{bottles} bottle of beer. \nTake one down, pass it around.')    
        bottles-=1
    print("No more bottles of beer on the wall. \n\nNo more bottles of beer. \nGo to the store and buy some more. \n")

#Task_2_5()

def Task_2_6():
    """Write a program that takes an n integer as input and displays, for each integer from 2 to n/2, the
    list of its multiples strictly smaller than n, in descending order."""

    num = int(input("Give me a number : \n"))
    val = ""
    for i in range(2, int(num/2+1)):
        temp = i
        while temp < num:
            val += str(temp) + " "
            temp+=i
        print(val)
        val = ""

#Task_2_6()

def Challenge():
    """Write the shortest possible code that realizes the following:
    ✓ ask the user for an integer and a string ;
    ✓ if this integer is 0, then quit ;
    ✓ if the string contains a vowel, display the integer ;
    ✓ if the integer is greater or equal than 42, display the integer ;
    ✓ else display the string"""

    s = input("Give me a string : \n")
    n = int(input("Give me a number : \n"))
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    for char in s:
        if char.lower() in vowel:
            print(n)
    if n >= 42:
        print(n)
    elif n == 0:
        return
    else:
        print(s)

#Challenge()

def Task_3_1():
    """Prompt the user for a message to be encrypted and for a key.
    Then print the result of the encryption of Caesar Cipher."""

    key = int(input("Give me a number between 1 and 25 : \n"))
    if (key > 25):
        print("Key is to big")
        Task_3_1()
        return
    text = input("Give me a text : \n")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    for char in text:
        pos= alphabet.find(char)
        if pos == -1:
            newText+= char
        elif key+pos > 25:
            newText += alphabet[key+pos-26]
        else:
            newText += alphabet[key+pos]
    print(newText)

#Task_3_1()

def Task_3_2(key, text):
    """Write a program that can decrypt any Caesar-ciphered text"""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    for char in text:
        pos = alphabet.find(char)
        if pos == -1:
            newText+= char
        elif pos-key < 0:
            newText += alphabet[pos-key+26]
        else:
            newText+= alphabet[pos-key]
    print(newText)

#Task_3_2(14, "pcbxcif")

def Task_3_3_Encrypt(key, text):
    """Write a program that can encrypt and decrypt a text using a Vigenere code."""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    text = text.lower()
    key.lower()
    compt = 0
    index = 0
    for i in range(len(text)):
        if index+1 < i:
            index = i-compt
        while index >= len(key):
            index -= len(key)
        pos1 = alphabet.find(text[i])
        pos2 = alphabet.find(key[index])
        if pos1 < 0:
            newText+=text[i]
            compt+=1
        else:
            if pos1+pos2 > 25:
                newText+=alphabet[pos1+pos2-26]
            else:
                newText += alphabet[pos1+pos2]
    print(newText)

#Task_3_3_Encrypt("musique", "j'adore ecouter la radio toute la journee")

def Task_3_3_Decrypt(key, text):
    """Write a program that can encrypt and decrypt a text using a Vigenere code."""    

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newText = ""
    text = text.lower()
    key.lower()
    compt = 0
    index = 0
    for i in range(len(text)):
        if index+1 < i:
            index = i-compt
        while index >= len(key):
            index -= len(key)
        pos1 = alphabet.find(text[i])
        pos2 = alphabet.find(key[index])
        if pos1 < 0:
            newText+=text[i]
            compt+=1
        else:
            if pos1-pos2 < 0:
                newText+=alphabet[pos1-pos2+26]
            else:
                newText += alphabet[pos1-pos2]
    print(newText)

Task_3_3_Decrypt("musique", "v'uvwhy ioimbul pm lslyi xaolm bu naojvuy")

#def Task_3_4(text, taille_key):
#    """Write a program that can decrypt an English Vigenere-ciphered text given the length of the key,
#    but without knowing the key."""

#    with open("mots.txt", encoding='utf8', mode="r") as fichier:
#        all_mots = [mot.strip('\n') for mot in fichier.readlines()] 
#
#    text = text.lower()
#    mots_corrects = 0
#    mots_max = 0
#    liste_mots = []
#    key = []
#    for _ in range(taille_key):
#        key.append(0)

#    compt = 0
#    for i in range(len(text)):
#        if compt %25 > 0:
#            if compt % 25 > 25 :
#                print()
#            else:
#                print()

    # Test le nbr de mots corrects
#    for mot in liste_mots:
#        if mot in liste_mots:
#            mots_corrects+=1
#    if mots_corrects > mots_max:
#        mots_max = mots_corrects

#Task_3_4("v'uvwhy ioimbul pm lslyi xaolm bu naojvuy", 5)