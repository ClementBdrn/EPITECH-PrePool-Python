"""
    Clément BADRONE
    Last Update 17/09/2024
    EPITECH Pre-Pool PreMSC
"""

import random
import turtle

def printMot(mot, penalties):
    """Convert the word 'list' in a 'string' to print"""
    motAfficher = ""
    for char in mot:
        motAfficher += char
    print(f"{motAfficher} / {penalties} pénalitées \n")

def testMot(mot, motFinal):
    """Check if the actual word is the word we want to find"""
    strMot = ""
    for char in mot:
        strMot += char
    if strMot == motFinal:
        return True
    return False

def supprAccents(motFinal):
    """Allows you to remove accents from letters with"""
    tableau = { 'éèêẽ' : 'e'
        , 'ç'    : 'c'
        , 'àâã'  : 'a'
        , 'ù'    : 'u'
        , 'îï'   : 'i'
    }

    mot = ""
    for char in motFinal:
        for k in tableau:
            if char in k: 
                char = tableau[k]
        mot+=char

    return mot.upper()

def checkLettre(lettre, penalties, mot, motFinal, pen, erreurs):
    """Check if the letter guessed is in the word we try to find"""
    isLettreIn = False
    compt = 0

    # Loop over all the characters of the word
    for i in range(len(motFinal)):
        if motFinal[i] == lettre:
            compt += 1
            mot[i] = lettre
            isLettreIn = True

    # Draw letters in the word
    if isLettreIn:
        print(f"Il y a {compt} '{lettre}'")
        penalties += 1
        drawMot(mot, pen)

    # Draw the actual state of the 'pendu'
    else:
        print(f"Il n'y a aucun '{lettre}'")
        penalties += 3
        erreurs +=1
        drawPendu(erreurs, pen)
        
    return [penalties, mot, erreurs]

def checkPossibleMot(lettreUtilisees, motPossibles, mot, motFinal):
    """List all possible words based on letters present and not present in the word"""

    # List all the letters that are in the searched word
    bonnesLettres = ""
    for char in mot:
        if char != '_' and char not in bonnesLettres:
            bonnesLettres += char.upper()
    
    # List all the letters that are not in the searched word
    mauvaisesLettres = ""
    for char in lettreUtilisees:
        if char not in bonnesLettres and char not in mauvaisesLettres:
            mauvaisesLettres+= char

    # Depending on the good and bad letters, list the possible words
    mots = []
    for ligne in motPossibles:
        isValide = True

        if len(bonnesLettres) == 0:
            isBonnes = True
        else:
            isBonnes = False

        isMauvaises = False
        motLigne = ligne.strip()

        # Checks possible words based on the position of the letters
        for j in range(len(mot)):
            if mot[j] != "_" and mot[j] != ligne[j]:
               isValide = False
               break

        # Check if the word contains the letters or doesnt 
        if isValide:
            for i in range(len(ligne)):
                if ligne[i] in mauvaisesLettres:
                    isMauvaises = True
                if ligne[i] in bonnesLettres:
                    isBonnes = True

        # If the word is valide add him in the list
        if isValide and isBonnes and isMauvaises == False:
            mots.append(motLigne)
    return mots

def CheatHangman(mot, motFinal, penalties, lettreUtilisees, all_mots, pen, erreurs):
    """Create an AI to find the hidden word"""

    # Add the frequencies of each letters
    frequences = { 'A' : 7.636, 'B' : 0.901, 'C' : 3.260, 'D' : 3.669, 'E' : 14.715, 'F' : 1.066, 'G' : 0.866, 'H' : 0.737,
                    'I' : 7.529, 'J' : 0.613, 'K' : 0.074, 'L' : 5.456, 'M' : 2.968, 'N' : 7.095, 'O' : 5.796, 'P' : 2.521, 
                    'Q' : 1.362, 'R' : 6.693, 'S' : 7.948, 'T' : 7.244, 'U' : 6.311, 'V' : 1.838, 'W' : 0.049, 'X' : 0.427,
                    'Y' : 0.128, 'Z' : 1.326}

    # Add all the possible words depending of the length of the word
    motPossibles = []
    for ligne in all_mots:
        motLigne = ligne.strip().upper()
        if len(lettreUtilisees) > 0:
            if len(motLigne) == len(motFinal) and all(char in lettreUtilisees for char in motLigne):
                motPossibles.append(supprAccents(motLigne.lower()))
        else:
            if len(motLigne) == len(motFinal):
                motPossibles.append(supprAccents(motLigne.lower()))

    # Delete the letters of the frequencies dictionnary
    for char in lettreUtilisees:
        if char in frequences:
            del frequences[char]

    # Loop until the word has been found
    win = False
    while win == False:

        #Check if the bot send a letter
        if len(motPossibles) == 1:
            win = testMot(motPossibles[0], motFinal)
            if win:
                drawMot(motPossibles[0], pen)
                return [penalties, True]

        # Get the letter with the max 
        lettre = max(frequences, key=frequences.get)

        # Check if the letter is in the final word
        val = checkLettre(lettre, penalties, mot, motFinal, pen, erreurs)
        penalties = val[0]
        mot = val[1]
        erreurs = val[2]

        # You lost
        if erreurs == 10:
            print(f"\nVous avez perdu !!! \nLe mot était : '{motFinal}'")
            return [penalties, False]

        # Delete from the frequencies dictionnary the last letter guessed
        del frequences[lettre]
        win = testMot(mot, motFinal)

        if win == False:
            printMot(mot, penalties)

        lettreUtilisees += lettre

        # Check all the possible word after the guess
        motPossibles = checkPossibleMot(lettreUtilisees, motPossibles, mot, motFinal)

    return [penalties, True]

def setupScreen():
    """Setup the screen from turtle"""
    window = turtle.Screen()
    window.title("Le Jeu du Pendu")
    window.bgcolor("white")

    pen = turtle.Turtle()
    pen.speed(3)

    return [window, pen]

def drawPendu(nbErreurs, pen):
    """Draw the bars according to the number of errors"""
    match nbErreurs:
        case 1:
            pen.penup()
            pen.goto(100,0)
            pen.pendown()
            pen.goto(200,0)
        case 2:
            pen.penup()
            pen.goto(150,0)
            pen.pendown()
            pen.goto(150, 175)
        case 3:
            pen.penup()
            pen.goto(150,10)
            pen.pendown()
            pen.goto(160,0)
        case 4:
            pen.penup()
            pen.goto(150, 175)
            pen.pendown()
            pen.goto(225,175)
        case 5:
            pen.penup()
            pen.goto(150,165)
            pen.pendown()
            pen.goto(160,175)
        case 6:
            pen.penup()
            pen.goto(225, 175)
            pen.pendown()
            pen.goto(225,150)
        case 7:
            pen.penup()
            pen.goto(225,130)
            pen.pendown()
            pen.circle(10)
        case 8:
            pen.penup()
            pen.goto(225,130)
            pen.pendown()
            pen.goto(225,90)
        case 9:
            pen.penup()
            pen.goto(225,120)
            pen.pendown()
            pen.goto(215,110)
            pen.penup()
            pen.goto(225,120)
            pen.pendown()
            pen.goto(235,110)
        case 10:
            pen.penup()
            pen.goto(225,90)
            pen.pendown()
            pen.goto(215,80)
            pen.penup()
            pen.goto(225,90)
            pen.pendown()
            pen.goto(235,80)
            
def drawMot(mot, pen):
    """Draw the word we are guessing"""
    pen.penup()
    pen.goto(-300, 0)

    for char in mot:
        pen.write(char, font=("Arial", 24, "normal"))
        pen.forward(30)

        

def Hangman_Game():
    """Hangman game !!!"""

    # Setup the graphical interface using turtle
    turtleData = setupScreen()

    pen = turtleData[1]

    # Import the lists of french words
    with open("mots.txt", encoding='utf8', mode="r") as fichier:
        all_mots = fichier.readlines()
    motFinal = random.choice(all_mots).strip().upper()

    # Delete the accents from the final word
    motFinal = supprAccents(motFinal.lower())

    win = False
    mot = []

    # Create the word with underscore
    for _ in range(len(motFinal)):
        mot += "_"
    drawMot(mot, pen)

    lettreUtilisees = ""
    penalties = 0
    erreurs = 0
    isGodMod = False

    # Loop until the player guess the right word
    while win == False:

        # Ask the user for a letter or a word
        lettre = turtle.textinput("Lettre","\nRenseignez une lettre ou un mot : \n").upper()

        # Enter in 'godmod' (let the AI play)
        if lettre == "-CHEAT":
            isGodMod = True

        if isGodMod:
            val = CheatHangman(mot, motFinal, penalties, lettreUtilisees, all_mots, pen, erreurs)
            penalties = val[0]
            win = val[1]

            if win == False:
                print(f"\nVous avez perdu !!! \nLe mot était : '{motFinal}'")
                return
            break

        # Check if the letter is already guessed
        if lettre in lettreUtilisees:
            print(f"La lettre {lettre} a déjà était utilisées ! Essayez en une autre.")
            printMot(mot, penalties)
        else:

            # Check if the player input a letter
            if len(lettre) == 1:

                #Check if the letter is inside the word to guess
                val = checkLettre(lettre,penalties, mot, motFinal, pen, erreurs)

                penalties = val[0]
                mot = val[1]
                erreurs = val[2]
                lettreUtilisees += lettre
                
                # You lost
                if erreurs == 10:
                    print(f"\nVous avez perdu !!! \nLe mot était : '{motFinal}'")
                    return

                # Check if the player wins
                win = testMot(mot, motFinal)
            else:
                if lettre == motFinal:
                    win = True
                else:
                    print(f"Mauvaise Réponse !")
                    penalties += 5

            if win == False:
                printMot(mot, penalties)
    
    print(f"BRAVO ! \nVous avez trouvé le mot '{motFinal}' en {penalties} pénalitées !")


Hangman_Game()