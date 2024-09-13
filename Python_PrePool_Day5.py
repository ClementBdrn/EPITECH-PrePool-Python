"""
    Clément BADRONE
    Last Update 13/09/2024
    EPITECH Pre-Pool PreMSC
"""

import time
import random

def Task_1_1():
    """Create a list that contains 5 numbers and print the first one."""

    liste = [1, 2, 3, 4, 5]
    print(liste[0])

#Task_1_1()

def Task_1_2():
    """Display the last element of your list"""

    liste = [1, 2, 3, 4, 5]
    print(liste[-1])

#Task_1_2()

def Task_1_3():
    """Add a 6th element in your list."""

    liste = [1, 2, 3, 4, 5]
    liste.append(6)

#Task_1_3()

def Task_1_4():
    """Display all the elements of your list."""

    liste = [1, 2, 3, 4, 5, 6]
    for i in liste:
        print(i)

#Task_1_4()

def Task_1_5():
    """Delete the last element and display all the remaining elements."""

    liste = [1, 2, 3, 4, 5, 6]
    liste = liste[:-1]
    for i in liste:
        print(i)

#Task_1_5()

def Task_1_6():
    """Add an element at the beginning of the list and display all its elements."""

    liste = [1, 2, 3, 4, 5]
    newListe = [0] + liste
    for i in newListe:
        print(i)

#Task_1_6()

def Task_1_7():
    """Display the sub-list from the 2nd to the 5th elements."""

    liste = [0, 1, 2, 3, 4, 5]
    print(liste[1:5])

#Task_1_7()

def Task_1_8():
    """Reverse the list by creating a new list with the same elements, but starting from the end.
    Display all the elements of this new list."""

    liste = [0, 1, 2, 3, 4, 5]
    newListe = liste[::-1]
    for i in newListe:
        print(i)

#Task_1_8()

def Task_1_9():
    """Display one element out of two of the list."""

    liste = [0, 1, 2, 3, 4, 5]
    print(liste[::2])

#Task_1_9()

def Task_1_10():
    """Add 17 elements at the end of your list"""

    liste = [0, 1, 2, 3, 4, 5]
    for i in range(17):
        liste.append(liste[-1]+1)
    print(liste)

#Task_1_10()

def Task_1_11():
    """What does the following code make?"""

    my_first_list = [4, 5, 6]
    my_second_list = [1, 2, 3]
    # Append all the elements of the second_list inside the first one
    my_first_list.extend(my_second_list)
    
    my_first_list = [7, 8, 9]
    my_second_list = [4, 5, 6]
    # Append all the elements of the second_list inside the first one
    my_first_list = [*my_first_list, *my_second_list]

#Task_1_11()

def Task_2_1():
    """Create a list of 10 numbers.
    Print the result of the multiplication of all elements of this list."""

    liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mult = 1
    for i in liste:
        mult *= i
    print(mult)

#Task_2_1()

def Task_2_2():
    """Test this code and try to explain it"""

    # Loop over all the elemnts of the list and add them 10. 3 + 10, 2 + 10, ...
    [x+10 for x in [3, 2, 6, 7, 1, 4]]

#Task_2_2()

def Task_2_3():
    """Test this code and try to explain it"""

    # Loop over all the elements of the list and multiply them by themselves. 3 * 3, 2 * 2
    list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))

Task_2_3()

def Task_2_4():
    """Browse the list and display both the smallest and the biggest elements"""

    liste = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    print(min(liste), max(liste))

#Task_2_4()

def Task_2_5():
    """Display all the elements smaller than 7."""

    liste = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    for i in liste:
        if i < 7:
            print(i)

#Task_2_5()

def Task_2_6():
    """Sort your list in descending order."""

    liste = list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]))
    length = len(liste)
    for _ in range(length):
        for i in range(length):
            # Check if we're not on the last element of the list
            if i + 1 < length:
                # Check if the actual value is greater than the next one
                if liste[i] < liste[i + 1]:
                    temp = liste[i]
                    liste[i] = liste[i + 1]
                    liste[i + 1] = temp
        length -= 1
    print(liste)

#Task_2_6()

def Task_2_7():
    """Test this code and try to explain it """

    # Loop over all the elements of the list, if x is even, divide him by 2, if x is even, multiply him by 2
    [x//2 if x%2==0 else x*2 for x in [42, 3, 4, 18, 3, 10]]

#Task_2_7()

def Task_2_8():
    """Test this code and try to explain it"""

    # Filter the list with inside all the numbers greater than 10
    list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10]))

#Task_2_8()

def Task_2_9():
    """Test this code and try to explain it"""

    # This code create a list of all the elements and them index related
    [*enumerate([42, 3, 4, 18, 3, 10])]

#Task_2_9()

def Task_2_10():
    """Test this code and try to explain it"""

    first_name = ["Jackie", "Bruce", "Arnold", "Sylsvester"]
    last_name = ["Stallone", "Shwarzeneger", "Willis", "Chan"]
    
    # Creates a list of tuples containing the element of both lists having the same index
    magic = [*zip(first_name, last_name[::-1])]

    print(magic[0])
    print(magic[3])
    print(magic[1][0])
    print(magic[0][1])
    print(magic[2])

#Task_2_10()

def Challenge():
    """Create a list of 1 000 000 random integers and sort it as fast as possible."""

    def sorting(liste):
        if len(liste) <= 1:
            return liste
        pivot = liste[len(liste) // 2]
        left = [x for x in liste if x < pivot]
        middle = [x for x in liste if x == pivot]
        right = [x for x in liste if x > pivot]

        # Recursive function 
        return sorting(left) + middle + sorting(right) 

    start_time = time.time()

    liste_rand = [random.randint(1, 1000000) for _ in range(1000000)]
    liste_rand = sorting(liste_rand)
    print(liste_rand[:100])

    duration = time.time() - start_time
    print(duration)
    
#Challenge()

def Task_3_1():
    """Create a dictionary stored in a student variable.
    This dictionary must contain 2 key/value pairs.
    The keys must be “name” and “academic_year”.
    The associated values are up to you, but please keep them coherent!"""

    student = {
        'name':'Clément',
        'academic_year':'2025'
    }

def Task_3_2():
    """In your student dictionary, add a units key.
    The value associated to units is an array of 3 elements.
    Each element of this array is a dictionary of 3 keys: name, credits, grade:
    """

    student = {
        'name':'Clément',
        'academic_year':'2025',
        'units':['Java', 22, 'A']
    }

def Task_3_3():
    """Create a new dictionary named grade_weight_mapping.
    This dictionary contains 5 keys (“A”, “B”, “C”, “D”, “E”) and their respective values (4, 3, 2, 1, 0).
    
    In your student dictionary, add a total_credits name. Give it the correct value according to the
    amount of credits you've given to each units in the previous task.
    Also add a GPA key and give it the correct value."""

    student = {
        'name':'Clément',
        'academic_year':'2025',
        'units':[
            {
                'name' : 'Java', 'credit' : 4, 'grade' : 'A'
            },

            {
                'name' : 'Web Developpement', 'credit' : 1, 'grade' : 'D'
            },

            {
                'name' : 'Network and System Administration', 'credit' : 2, 'grade' : 'C'
            }
        ],
        'total_credits' : 7,
        'GPA': 2.3
    }

    grade_weight_mapping = {
        'A':4,
        'B':3,
        'C':2,
        'D':1,
        'E':0
    }

def Task_3_4():
    """Create an array and store at least 3 students (as defined in previous tasks) in it.
    Write some code to:
    ✓ sort this array by student’s name in alphabetical order
    ✓ sort this array by GPA in both ascending and descending order"""

    students = [
        {'name':'Clément', 'academic_year':'2025', 'units':[
            {
                'name' : 'Java', 'credit' : 4, 'grade' : 'A'
            },

            {
                'name' : 'Web Developpement', 'credit' : 1, 'grade' : 'D'
            },

            {
                'name' : 'Network and System Administration', 'credit' : 2, 'grade' : 'C'
            }
        ], 'total_credits' : 7, 'GPA': 2.3},

        {'name':'Baptiste', 'academic_year':'2025', 'units':[
            {
                'name' : 'Java', 'credit' : 1, 'grade' : 'D'
            },

            {
                'name' : 'Web Developpement', 'credit' : 1, 'grade' : 'D'
            },

            {
                'name' : 'Network and System Administration', 'credit' : 0, 'grade' : 'E'
            }
        ], 'total_credits' :2, 'GPA': 0.6},

        {'name':'Salsa', 'academic_year':'2027', 'units':[
            {
                'name' : 'Java', 'credit' : 3, 'grade' : 'B'
            },

            {
                'name' : 'Web Developpement', 'credit' : 3, 'grade' : 'B'
            },

            {
                'name' : 'Network and System Administration', 'credit' : 3, 'grade' : 'B'
            }
        ], 'total_credits' :9, 'GPA': 3}
    ]

    # Use the sorted function to sort the list 
    sort_name = sorted(students, key=lambda student : student["name"])
    sort_gpa_asc = sorted(students, key=lambda student : student["GPA"])
    sort_gpa_dsc = sorted(students, key=lambda student : student["GPA"], reverse=True)

    print(f'{sort_name} \n')
    print(f'{sort_gpa_asc} \n')
    print(f'{sort_gpa_dsc} \n')

#Task_3_4()

def Task_4_1():
    """Let's consider a list of names (the ambassador's banquet guests).
    Write a program that displays:
    ✓ “welcome in” if a given name belongs to this list ;
    ✓ and “get lost!” otherwise."""

    guest_list = ["Stéphane", "Thierry", "Didier", "Philippe", "Michel", "Jacques"]
    name = input("Give me your name : ")
    if name in guest_list:
        print("Welcome in !")
    else :
        print("Get lost !")

#Task_4_1()

def Task_4_2():
    """Write a program that deletes all the duplicated elements in a list"""

    liste = [1, 2, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 9]
    for i in liste:
        nb = liste.count(i)
        for _ in range(nb-1):
            liste.remove(i)
    print(liste)

#Task_4_2()

def Task_4_3():
    """Let consider a list of meetings. Each meeting is a list containing the day, the time of the meeting
    and the name of all the participants.
    For instance ["Monday, "3:30 PM", "Joe", "Samantha"].
    Write a program that, given a name, displays all the meetings in which this person is involved."""

    liste_meetings = [
        ["Monday", "3:30 PM", "Joe", "Samantha"],
        ["Monday", "4:30 PM", "Paul", "Seb"],
        ["Tuesday", "7:30 PM", "Joe", "Paul"],
        ["Wednesday", "2:30 AM", "Marc", "Michel"],
        ["Wednesday", "4:30 PM", "Michel", "Samantha"],
        ["Friday", "8:30 PM", "Samantha", "Paul"],
        ["Saturday", "11:30 AM", "Pierre", "Clément"],
        ["Sunday", "1:30 PM", "Clément", "Thierry"],
    ]

    liste = []

    name = input("Give me a name : \n")
    name = name[0].upper() + name[1:]
    compt = 0
    for list in liste_meetings:
        if name in list:
            compt += 1
            liste.append(list)
    if compt <= 0:
        print(f'{name} does not have meeting this week.')
    else :
        print(f'{name} has {compt} meeting this week : \n{liste}')

#Task_4_3()