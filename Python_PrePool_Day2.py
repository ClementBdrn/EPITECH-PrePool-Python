"""
    Clément BADRONE
    Last Update : 10/09/2024
    EPITECH Pre-Pool PreMSC
"""


def Task_2_1(p_iterations):
    """Compute 1 + 11 + 111 + ... + 111111111. \n
    Also computes this number power 2, power 3, power 4, power 5, power 6 and power 7.
    """

    num = "1"
    sum = 1
    # Loop over a given number of iterations
    for i in range(p_iterations):
        # Add '1' to the previous number
        num += "1"
        sum += int(num)
    print(sum)
    # Loop to compute the number on the requested power
    for i in range(6):
        print(sum ** (i + 2))


##Task_2_1(11)


def Task_2_1_v2(p_iterations):
    """Compute 1 + 11 + 111 + ... + 111111111. \n
    Also computes this number power 2, power 3, power 4, power 5, power 6 and power 7.
    """

    num = 1
    sum = 0
    # Loop over a given number of iterations
    for i in range(p_iterations):
        sum += num
        # Add '1' to the previous number
        num = num * 10 + 1
    print(sum)
    # Loop to compute this number on the requested power
    for i in range(6):
        print(sum ** (i + 2))


##Task_2_1_v2(10)


def Task_2_2():
    """Computes 171024 in less than 10 lines of code."""

    val = 17**1024
    print(val)


##Task_2_2()


def Task_3_1(p_numerator, p_denominator):
    """Write a snippet of code that computes the result, as well as both the quotient and the remainder
    of the euclidean division 42/4."""

    result = p_numerator / p_denominator
    quotient = p_numerator // p_denominator
    rest = p_numerator % p_denominator
    print(f"Résultat = {result}\nQuotient = {quotient}\nReste = {rest}")


##Task_3_1(21, 2)


def Task_3_2(p_num):
    """Write a snippet of code in order to check if a number is odd or even."""

    if p_num % 2 == 0:
        return print("Nombre pair")
    else:
        return print("Nombre impair")


##Task_3_2(11)


def Task_3_3(p_num):
    """Write a snippet of code that calculates the sum of the digits of 123434565."""

    sum = 0
    # Convert int to string
    str_num = str(p_num)
    for i in str_num:
        sum += int(i)
    print(sum)


##Task_3_3(93629027)


def Task_3_4(p_num):
    """Write a snippet of code that extracts the integer part of the numbers."""

    val = ""
    isInt = True
    # Convert the number to a string
    str_num = str(p_num)
    # Loop over all the char
    for i in range(len(str_num)):
        # Indicate that from this value, numbers will be decimal
        if str_num[i] == "." or str_num[i] == ",":
            isInt = False
        # If the number is an int
        if isInt:
            val += str_num[i]
    print(val)


##Task_3_4(10879.3286321)


def Task_3_5(p_num):
    """Write a snippet of code that extracts the decimal part of the numbers."""

    val = ""
    isDecimal = False
    # Convert the number to a string
    str_num = str(p_num)
    # Loop over all the char
    for i in range(len(str_num)):
        # If the number is decimal
        if isDecimal:
            val += str_num[i]
        # Indicate that from this value, numbers will be decimal
        if str_num[i] == "." or str_num[i] == ",":
            isDecimal = True
    print(val)


##Task_3_5(10983.37291)


def Task_4_1(p_iterations):
    """Calculate the first 6 decimals of Pi."""

    val = 0
    # Loop for a given numbers of iterations
    for i in range(p_iterations):
        if i % 2 == 0:
            # Add the value
            val += 1 / (i * 2 + 1)
        else:
            # Substract the value
            val -= 1 / (i * 2 + 1)
    # Allows tou to have the final value of Pi
    result = 4 * val
    print(str(result)[:8])


##Task_4_1(2000000)


def Task_4_2(p_iterations, p_num=1):
    """Calculate the first 6 decimals of Pi."""

    if p_iterations == 0:
        return 0

    # Recursive loop using a method of calculating Pi
    return (p_num**2) / (6 + Task_4_2(p_iterations - 1, p_num + 2))


##print(str(3 + Task_4_2(100))[:8])


def SortListDecrease(p_list):
    """Sort a list in descending order."""

    # Create a list to stock the sorted list
    resultList = []
    valMax = p_list[0]
    for j in range(len(p_list)):
        for i in p_list:
            # Check if the actual value is greater than the valMax
            if valMax < i:
                valMax = i
        # Add in the result list the greater value
        resultList.append(valMax)
        # Remove from the parameter list the greater value
        p_list.remove(valMax)
        valMax = 0
    print(resultList)


# SortListDecrease([4, 8, 10, 36, 2, 0, 76, 45, 200])


def SortListBubble(p_list):
    """Sort a list using a bubble sort."""

    for j in range(len(p_list)):
        for i in range(len(p_list)):
            # Check if we're not on the last element of the list
            if i + 1 < len(p_list):
                # Check if the actual value is greater than the next one
                if p_list[i] > p_list[i + 1]:
                    temp = p_list[i]
                    p_list[i] = p_list[i + 1]
                    p_list[i + 1] = temp
    print(p_list)


##SortListBubble([4, 8, 10, 36, 2, 0, 76, 45, 200])


def SortListBubble_v2(p_list):
    """Sort a list using a bubble sort."""

    length = len(p_list)
    for j in range(length):
        for i in range(length):
            # Check if we're not on the last element of the list
            if i + 1 < length:
                # Check if the actual value is greater than the next one
                if p_list[i] > p_list[i + 1]:
                    temp = p_list[i]
                    p_list[i] = p_list[i + 1]
                    p_list[i + 1] = temp
        length -= 1
    print(p_list)


##SortListBubble_v2([4, 8, 10, 36, 2, 0, 76, 45, 200])
