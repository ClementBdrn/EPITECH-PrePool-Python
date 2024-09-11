"""
    Clément BADRONE
    Last Update : 11/09/2024
    EPITECH Pre-Pool PreMSC
"""

import string

def Task_1_1(p_mot):
    """Store a string in a variable. Then, print it."""

    print(p_mot)


##Task_1_1("test")


def Task_1_2(p_mot):
    """Print the 1st character of your string. And also the 5th one."""

    print(f'1st char : {p_mot[0]}\n5th char : {p_mot[4]}')


##Task_1_2("bonjour")


def Task_1_3(p_mot):
    """Print the last character of your string."""

    print(f'Last character : {p_mot[-1]}')


##Task_1_3("bonjour")


def Task_1_4(p_mot):
    """In one line, print from the 5th to the 10th character of this string"""

    print(f'5th to 10th char : {p_mot[4:10]}')


##Task_1_4("abcdefghijkl")


def Task_2_1(p_mot):
    """Write a snippet of code that transforms any string in lower case."""

    print(p_mot.lower())


##Task_2_1("BoNjoUr")


def Task_2_2(p_phrase):
    """Write a snippet of code that replaces every “tu” in a string by “ta”."""

    val = ""
    # Loop over all the characters of the string
    for i in range(len(p_phrase)):
        if len(val) > 0:
            #If the last value of "val" is "t" and the char of p_phrase is "u", we change the "u" a "a"
            if val[-1] == "t" and p_phrase[i] == "u":
                val += "a"
            else:
                val += p_phrase[i]
        else :
            val += p_phrase[i]
    print(val)


##Task_2_2("tutu on the tuki-kata")


def Task_2_3():
    """Explain the following code and its printed result"""

    string = "hello world"
    position = string.find("e")
    # If string doesn't conatain "a" it will print -1, else it will print the index
    print(position)


##Task_2_3()


def Task_2_4():
    """Can you predict the result of the following snippet of code?"""
    
    p = "abcdefghij"
    # First : jhfdb
    # Second : jhfdb
    # Third : bdfhj
    # Fourth : hj
    print(p[::-2][:5][::-1][3:])


##Task_2_4()


def Task_2_5():
    """Can you simplify the previous code?"""

    p = "abcdefghij"
    print(p[7::2])


##Task_2_5()


def Task_2_6(p_mot):
    """Write a snippet of code that prints 10 times a given string."""

    for i in range(10):
        print(p_mot)


##Task_2_6("test")


def Task_2_7(p):
    """Rewrite the previous code in as few characters as possible."""

    for i in range(10):
        print(p)


##Task_2_7("test")


def Task_2_8():
    """Debug the following code:"""

    s1 = "Hello"
    s2 = 42
    # We have to convert s2 type in a string
    concat = s1 + str(s2)
    print(concat)


##Task_2_8()


def Task_2_9():
    """Complete the following code so that it prints The string "42 is the answer" contains 16 characters."""

    string1 = "42"
    string2 = "is"
    string3 = "the answer"
    concat = string1 + " " + string2 + " " + string3
    print(f'The string "{concat}" contains {len(concat)} characters.')


##Task_2_9()


def Challenge(p_phrase):
    """Write a snippet of code that counts the number of occurrences of the strings “Cat”, “Garden” and “Mice” in any string."""

    # Initializing variables
    cat = 0
    garden = 0
    mice = 0
    compt = 0

    # Loop 2 times, first time to read from left to right, and the second time from right to left
    for i in range(2):
        # Check if we are in the second time
        if compt > 0:
            p_phrase = p_phrase[::-1]
        # Loop over all the string
        for i in range(len(p_phrase)):
            if p_phrase[i].lower() == "c":
                if i+2 < len(p_phrase):
                    if p_phrase[i+1].lower() == "a" and p_phrase[i+2] == "t":
                        cat+=1
            elif p_phrase[i].lower() == "g":
                if i+5 < len(p_phrase):
                    if p_phrase[i+1].lower() == "a" and p_phrase[i+2].lower() == "r" and p_phrase[i+3].lower() == "d" and p_phrase[i+4].lower() == "e" and p_phrase[i+5].lower() == "n":
                        garden+=1
            elif p_phrase[i].lower() == "m":
                if i+3 < len(p_phrase):
                    if p_phrase[i+1].lower() == "i" and p_phrase[i+2].lower() == "c" and p_phrase[i+3].lower() == "e":
                        mice+=1
        compt+=1
    print(f'Nb "Cat" = {cat}\nNb "Garden" = {garden}\nNb "Mice" = {mice}\nTotal = {cat+garden+mice}')


##Challenge("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN")


def Task_3_1():
    """Ask the user his/her name and then greet him/her with “Hello username”."""

    name = input("What's your name ? : \n")
    print(f'Hello {name} !')


##Task_3_1()


def Task_3_2():
    """Ask the user his/her name and then greet him/her with “Hello Username”, with the user's name
    always printed with its first (and only the first) letter capitalized."""

    name = input("What's your name ? : \n")
    print(f'Hello {name[0].upper()}{name[1:]} !')


##Task_3_2()


def Task_3_3():
    """Prompt the user for two numbers and then print “The sum of the two provided numbers is sum”"""

    n1 = int(input("1st number : \n"))
    n2 = int(input("2nd number : \n"))
    print(f'The sum of the two numbers is {n1+n2}')


##Task_3_3()


def Task_3_4():
    n1 = int(input("Give a number : \n"))
    print(f'{type(n1)}')



##Task_3_4()


def Task_3_5(p_phrase):
    """Write a program that extracts the first word of each sentences into a string, and then join them
    to make a new sentence."""

    val = ""
    compt = 0
    # Create a variable with all the char that can end a sentence
    endSentence = [".", "?", "!"]
    for i in range(len(p_phrase)):
        if(compt != i or compt == 0):
            # Check if we are at the end of the sentence
            if p_phrase[i] in endSentence:
                for char in p_phrase[compt:i]:
                    if char != " ":
                        if len(val) > 1:
                            val+=char.lower()
                        else:
                            val+=char.upper()
                    else:
                        val+= " "
                        i+=2
                        compt=i
                        break
    val+="."
    print(val)
    

##Task_3_5("This is a test. Is it possible to fly? Good things come to those who never give up.")


def Task_3_6(p_phrase):
    """Write a program that counts the frequency of each letter from a given text and infers the language of this very text."""

    # Create a dictionnary with the frequencies of all the letter for a language
    frequence_langues = {
        'french' : { 'a' : 7.636, 'b' : 0.901, 'c' : 3.260, 'd' : 3.669, 'e' : 14.715, 'f' : 1.066, 'g' : 0.866, 'h' : 0.737,
                    'i' : 7.529, 'j' : 0.613, 'k' : 0.074, 'l' : 5.456, 'm' : 2.968, 'n' : 7.095, 'o' : 5.796, 'p' : 2.521, 
                    'q' : 1.362, 'r' : 6.693, 's' : 7.948, 't' : 7.244, 'u' : 6.311, 'v' : 1.838, 'w' : 0.049, 'x' : 0.427,
                    'y' : 0.128, 'z' : 0.326},

        'english': { 'a' : 8.167, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702, 'f' : 2.228, 'g' : 2.015, 'h' : 6.094,
                    'i' : 6.966, 'j' : 0.153, 'k' : 0.772, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 'p' : 1.929, 
                    'q' : 0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 'u' : 2.758, 'v' : 0.978, 'w' : 2.360, 'x' : 0.150,
                    'y' : 1.974, 'z' : 0.074},

        'spanish': { 'a' : 12.525, 'b' : 1.415, 'c' : 4.679, 'd' : 5.816, 'e' : 13.681, 'f' : 0.692, 'g' : 1.008, 'h' : 0.703,
                    'i' : 6.247, 'j' : 0.493, 'k' : 0.011, 'l' : 4.967, 'm' : 3.157, 'n' : 6.712, 'o' : 8.683, 'p' : 2.510, 
                    'q' : 0.877, 'r' : 6.871, 's' : 7.977, 't' : 4.632, 'u' : 2.927, 'v' : 0.898, 'w' : 0.017, 'x' : 0.215,
                    'y' : 0.898, 'z' : 0.467},

        'german': { 'a' : 6.516, 'b' : 1.886, 'c' : 3.062, 'd' : 5.076, 'e' : 17.396, 'f' : 1.656, 'g' : 3.009, 'h' : 4.577,
                    'i' : 7.550, 'j' : 0.268, 'k' : 1.217, 'l' : 3.437, 'm' : 2.534, 'n' : 9.776, 'o' : 2.514, 'p' : 0.790, 
                    'q' : 0.018, 'r' : 7.003, 's' : 7.270, 't' : 6.154, 'u' : 4.346, 'v' : 0.846, 'w' : 1.891, 'x' : 0.034,
                    'y' : 0.039, 'z' : 1.134},

        'portuguese': { 'a' : 14.634, 'b' : 1.043, 'c' : 3.882, 'd' : 4.992, 'e' : 12.570, 'f' : 1.023, 'g' : 1.303, 'h' : 0.781,
                    'i' : 6.186, 'j' : 0.397, 'k' : 0.015, 'l' : 2.779, 'm' : 4.738, 'n' : 4.446, 'o' : 9.735, 'p' : 2.523, 
                    'q' : 1.204, 'r' : 6.530, 's' : 6.805, 't' : 4.336, 'u' : 3.639, 'v' : 1.575, 'w' : 0.037, 'x' : 0.253,
                    'y' : 0.006, 'z' : 0.470},

        'italian': { 'a' : 11.745, 'b' : 0.927, 'c' : 4.501, 'd' : 3.736, 'e' : 11.792, 'f' : 1.153, 'g' : 1.644, 'h' : 0.636,
                    'i' : 10.143, 'j' : 0.011, 'k' : 0.009, 'l' : 6.510, 'm' : 2.512, 'n' : 6.883, 'o' : 9.832, 'p' : 3.056, 
                    'q' : 0.505, 'r' : 6.367, 's' : 4.981, 't' : 5.623, 'u' : 3.011, 'v' : 2.097, 'w' : 0.033, 'x' : 0.003,
                    'y' : 0.020, 'z' : 1.181}
    }

    p_phrase = p_phrase.lower()
    # Create a blank dictionnary 
    compt_lettres = {lettre:0 for lettre in string.ascii_lowercase}
    total_lettres = 0

    # Stock inside the blank dictionnary the number of times each letter appears
    for char in p_phrase:
        if char in compt_lettres:
            compt_lettres[char] += 1
            total_lettres += 1

    # Calculate the frequency of each letter based on the total number of letters
    frequence = {lettre:round((compt_lettres[lettre]/total_lettres)*100, 3) for lettre in compt_lettres}

    ecart_min = float('inf')
    langue_finale = ""

    # Loop over each language and frequency of the base dictionnary
    for langue, frequence_langue in frequence_langues.items():
        ecart = 0
        # Calculate the sum of the differences between each letter frequency
        for lettre in frequence:
            ecart += (frequence[lettre] - frequence_langue.get(lettre, 0))**2
        # Check if the new difference is smaller than the last one
        if ecart < ecart_min:
            # Change the difference and language according to the retrieved values
            ecart_min = ecart
            langue_finale = langue 

    print(langue_finale)

#Italian
#Task_3_6("cominciai Poeta, volontieri parlerei a quei due che nsieme vanno, e paion sì al vento esser leggeri.Ed elli a me Vedrai quando saranno più presso a noi e tu allor li priega per quello amor che i mena, ed ei verranno.Sì tosto come il vento a noi li piega, mossi la voce O anime affannate, venite a noi parlar, s altri nol niega. cominciai Poeta che mi guidi, guarda la mia virtù s ell è possente, prima ch a l alto passo tu mi fidi.Tu dici che di Silvïo il parente, corruttibile ancora, ad immortale secolo andò, e fu sensibilmente.Però, se l avversario d ogne male cortese i fu, pensando l alto effetto ch uscir dovea di lui, e l chi e l quale non pare indegno ad omo d intelletto ch e fu de l alma Roma e di suo impero ne l empireo ciel per padre eletto la quale e l quale, a voler dir lo vero, fu stabilita per lo loco santo u siede il successor del maggior Piero. principio del mattino, e l sol montava n sù con quelle stelle ch eran con lui quando l amor divino mosse di prima quelle cose belle sì ch a bene sperar m era cagione di quella fiera a la gaetta pelle l ora del tempo e la dolce stagione ma non sì che paura non mi desse la vista che m apparve d un leone. Quinci non passa mai anima buona e però, se Caron di te si lagna, ben puoi sapere omai che l suo dir suona.Finito questo, la buia campagna tremò sì forte, che de lo spavento la mente di sudore ancor mi bagna.La terra lagrimosa diede vento, che balenò una luce vermiglia la qual mi vinse ciascun sentimento e caddi come l uom cui sonno piglia. Sempre dinanzi a lui ne stanno molte vanno a vicenda ciascuna al giudizio, dicono e odono e poi son giù volte. O tu che vieni al doloroso ospizio, disse Minòs a me quando mi vide, lasciando l atto di cotanto offizio, guarda com entri e di cui tu ti fide non t inganni l ampiezza de l intrare. costì, anima viva, pàrtiti da cotesti che son morti.Ma poi che vide ch io non mi partiva, disse Per altra via, per altri porti verrai a piaggia, non qui, per passare più lieve legno convien che ti porti.E l duca lui Caron, non ti crucciare vuolsi così colà dove si puote ciò che si vuole, e più non dimandare. Poscia ch io v ebbi alcun riconosciuto, vidi e conobbi l ombra di colui che fece per viltade il gran rifiuto.Incontanente intesi e certo fui che questa era la setta d i cattivi, a Dio spiacenti e a nemici sui.Questi sciaurati, che mai non fur vivi, erano ignudi e stimolati molto da mosconi e da vespe ch eran ivi. Quando rispuosi, cominciai Oh lasso, quanti dolci pensier, quanto disio menò costoro al doloroso passo.Poi mi rivolsi a loro e parla io, e cominciai Francesca, i tuoi martìri a lagrimar mi fanno tristo e pio.Ma dimmi al tempo d i dolci sospiri, a che e come concedette amore che conosceste i dubbiosi disiri. ritrasser tutte quante insieme, forte piangendo, a la riva malvagia ch attende ciascun uom che Dio non teme.Caron dimonio, con occhi di bragia loro accennando, tutte le raccoglie batte col remo qualunque s adagia.Come d autunno si levan le foglie l una appresso de l altra, fin che l ramo vede a la terra tutte le sue spoglie, similemente il mal seme d Adamo gittansi di quel lito ad una ad una, per cenni come augel per suo richiamo. parola tua intesa, rispuose del magnanimo quell ombra, l anima tua è da viltade offesa la qual molte fïate l omo ingombra sì che d onrata impresa lo rivolve, come falso veder bestia quand ombra.Da questa tema acciò che tu ti solve, dirotti perch io venni e quel ch io ntesi nel primo punto che di te mi dolve. mezzo del cammin di nostra vita mi ritrovai per una selva oscura, ché la diritta via era smarrita.Ahi quanto a dir qual era è cosa dura esta selva selvaggia e aspra e forte che nel pensier rinova la paura Tant è amara che poco è più morte ma per trattar del ben ch i vi trovai, dirò de l altre cose ch i v ho scorte. Quali fioretti dal notturno gelo chinati e chiusi, poi che l sol li mbianca, si drizzan tutti aperti in loro stelo, tal mi fec io di mia virtude stanca, e tanto buono ardire al cor mi corse, ch i cominciai come persona franca Oh pietosa colei che mi soccorse e te cortese ch ubidisti tosto a le vere parole che ti porse Tu m hai con disiderio il cor disposto sì al venir con le parole tue, ch i son tornato nel primo proposto. dimmi la cagion che non ti guardi de lo scender qua giuso in questo centro de l ampio loco ove tornar tu ardi. Da che tu vuo saver cotanto a dentro, dirotti brievemente, mi rispuose, perch i non temo di venir qua entro.Temer si dee di sole quelle cose c hanno potenza di fare altrui male de l altre no, ché non son paurose. vorrai salire, anima fia a ciò più di me degna con lei ti lascerò nel mio partire ché quello imperador che là sù regna, perch i fu ribellante a la sua legge, non vuol che n sua città per me si vegna.In tutte parti impera e quivi regge quivi è la sua città e l alto seggio oh felice colui cu ivi elegge. Oscura e profonda era e nebulosa tanto che, per ficcar lo viso a fondo, io non vi discernea alcuna cosa. Or discendiam qua giù nel cieco mondo, cominciò il poeta tutto smorto. Io sarò primo, e tu sarai secondo.E io, che del color mi fui accorto, dissi Come verrò, se tu paventi che suoli al mio dubbiare esser conforto.")
#French
##Task_3_6("Sa Majesté descendit à la belle église neuve qui ce jour-là était parée de tous ses rideaux cramoisis. Le roi devait dîner, et aussitôt après remonter en voiture pour aller vénérer la célèbre relique de saint Clément. À peine le roi fut-il à l'église, que Julien galopa vers la maison de M. de Rênal. Là, il quitta en soupirant son bel habit bleu de ciel, son sabre, ses épaulettes, pour reprendre le petit habit noir râpé. Il remonta à cheval, et en quelques instants fut à Bray-le-Haut qui occupe le sommet d'une fort belle colline. L'enthousiasme multiplie ces paysans, pensa Julien. On ne peut se remuer à Verrières, et en voici plus de dix mille autour de cette antique abbaye. À moitié ruinée par le vandalisme révolutionnaire, elle avait été magnifiquement rétablie depuis la À peine arrivé à Verrières, Julien se reprocha son injustice envers Mme de Rênal. Je l'aurais méprisée comme une femmelette, si, par faiblesse, elle avait manqué sa scène avec M. de Rênal ! Elle s'en tire comme un diplomate, et je sympathise avec le vaincu qui est mon ennemi. Il y a dans mon fait petitesse bourgeoise ; ma vanité est choquée, parce que M. de Rênal est un homme ! illustre et vaste corporation à laquelle j'ai l'honneur d'appartenir ; je ne suis qu'un sot. De retour à Vergy, Julien ne descendit au jardin que lorsqu'il fut nuit close. Son âme était fatiguée de ce grand nombre d'émotions puissantes qui l'avaient agitée dans cette journée. Que leur dirai-je ? pensait-il avec inquiétude, en songeant aux dames. Il était loin de voir que son âme était précisément au niveau des petites circonstances qui occupent ordinairement tout l'intérêt des femmes. Souvent Julien était inintelligible pour Mme Derville et même pour son amie, et à son tour ne comprenait qu'à demi tout ce qu'elles lui disaient. Tel était l'effet de la force, et si j'ose parler ainsi de la grandeur des mouvements de passion qui bouleversaient l'âme de ce jeune ambitieux. Chez cet être singulier, c'était presque tous les jours tempête. Verrières est abrité du côté du nord par une haute montagne, c'est une des branches du Jura. Les cimes brisées du Verra se couvrent de neige dès les premiers froids d'octobre. Un torrent, qui se précipite de la montagne, traverse Verrières avant de se jeter dans le Doubs, et donne le mouvement à un grand nombre de scies à bois, c'est une industrie fort simple et qui procure un certain bien-être à la majeure partie des habitants plus paysans que bourgeois. Ce ne sont pas cependant les scies à bois qui ont enrichi cette petite ville. C'est à la fabrique des toiles peintes, dites de Mulhouse, que l'on doit l'aisance générale qui, depuis la chute de Napoléon, a fait rebâtir les façades de presque toutes les maisons de Verrières. La demoiselle se pencha en dehors du comptoir, ce qui lui donna l'occasion de déployer une taille superbe. Julien la remarqua ; toutes ses idées changèrent. La belle demoiselle venait de placer devant lui une tasse, du sucre et un petit pain. Elle hésitait à appeler un garçon pour avoir du café, comprenant bien qu'à l'arrivée de ce garçon, son tête-à-tête avec Julien allait finir. M. Chélan avait refusé les logements que les libéraux les plus considérés du pays lui avaient offerts à l'envi, lorsque sa destitution le chassa du presbytère. Les deux chambres qu'il avait louées étaient encombrées par ses livres. Julien, voulant montrer à Verrières ce que c'était qu'un prêtre, alla prendre chez son père une douzaine de planches de sapin, qu'il porta lui-même sur le dos tout le long de la grande rue. Il emprunta des outils à un ancien camarade, et eut bientôt bâti une sorte de bibliothèque dans laquelle il rangea les livres de M. Chélan. De là le succès du petit paysan Julien. Elle trouva des jouissances douces, et toutes brillantes du charme de la nouveauté, dans la sympathie de cette âme noble et fière. Mme de Rênal lui eut bientôt pardonné son ignorance extrême qui était une grâce de plus, et la rudesse de ses façons qu'elle parvint à corriger. Elle trouva qu'il valait la peine de l'écouter, même quand on parlait des choses les plus communes, même quand il s'agissait d'un pauvre chien écrasé, comme il traversait la rue, par la charrette d'un paysan allant au trot. Le spectacle de cette douleur donnait son gros rire à son mari, tandis qu'elle voyait se contracter les beaux sourcils noirs et si bien arqués de Julien. La générosité, la noblesse d'âme, l'humanité lui semblèrent peu à peu n'exister que chez ce jeune abbé. Elle eut pour lui seul toute la sympathie et même l'admiration que ces vertus excitent chez les âmes bien nées. Une scie à eau se compose d'un hangar au bord d'un ruisseau. Le toit est soutenu par une charpente qui porte sur quatre gros piliers en bois. À huit ou dix pieds d'élévation, au milieu du hangar, on voit une scie qui monte et descend, tandis qu'un mécanisme fort simple pousse contre cette scie une pièce de bois. C'est une roue mise en mouvement par le ruisseau qui fait aller ce double mécanisme ; celui de la scie qui monte et descend, et celui qui pousse doucement la pièce de bois vers la scie, qui la débite en planches. Le clergé s'impatientait. Il attendait son chef dans le cloître sombre et gothique de l'ancienne abbaye. On avait réuni vingt-quatre curés pour figurer l'ancien chapitre de Bray-le-Haut, composé avant 1789 de vingt-quatre chanoines. Après avoir déploré pendant trois quarts d'heure la jeunesse de l'évêque, les curés pensèrent qu'il était convenable que M. le Doyen se retirât vers Monseigneur pour l'avertir que le roi allait arriver, et qu'il était instant de se rendre au chœur. Le grand âge de M. Chélan l'avait fait doyen ; malgré l'humeur qu'il témoignait à Julien, il lui fit signe de suivre. Julien portait fort bien son surplis. Au moyen de je ne sais quel procédé de toilette ecclésiastique, il avait rendu ses beaux cheveux bouclés très plats ; mais, par un oubli qui redoubla la colère de M. Chélan, sous les longs plis de sa soutane on pouvait apercevoir les éperons du garde d'honneur. Ce moment fut affreux ; son âme arrivait dans des pays inconnus. La veille elle avait goûté un bonheur inéprouvé ; maintenant elle se trouvait tout à coup plongée dans un malheur atroce. Elle n'avait aucune idée de telles souffrances, elles troublèrent sa raison. Elle eut un instant la pensée d'avouer à son mari qu'elle craignait d'aimer Julien. C'eût été parler de lui. Heureusement elle rencontra dans sa mémoire un précepte donné jadis par sa tante, la veille de son mariage. Il s'agissait du danger des confidences faites à un mari, qui après tout est un maître. Dans l'excès de sa douleur, elle se tordait les mains. – Vous voyez, Monsieur, que je réclame vos avis, comme si déjà vous occupiez le poste auquel tous les honnêtes gens vous portent. Dans cette malheureuse ville les manufactures prospèrent, le parti libéral devient millionnaire, il aspire au pouvoir, il saura se faire des armes de tout. Consultons l'intérêt du roi, celui de la monarchie, et avant tout l'intérêt de notre sainte religion. À qui pensez-vous, Monsieur, que l'on puisse confier le commandement de la garde d'honneur. Quelques jours avant la Saint-Louis, Julien, se promenant seul et disant son bréviaire dans un petit bois, qu'on appelle le Belvédère, et qui domine le Cours de la Fidélité, avait cherché en vain à éviter ses deux frères, qu'il voyait venir de loin par un sentier solitaire. La jalousie de ces ouvriers grossiers avait été tellement provoquée par le bel habit noir, par l'air extrêmement propre de leur frère, par le mépris sincère qu'il avait pour eux, qu'ils l'avaient battu au point de le laisser évanoui et tout sanglant. Mme de Rênal, se promenant avec M. Valenod et le sous-préfet, arriva par hasard dans le petit bois ; elle vit Julien étendu sur la terre et le crut mort. Son saisissement fut tel, qu'il donna de la jalousie à M. Valenod. Julien releva les yeux avec effort, et d'une voix que le battement de cœur rendait tremblante, il expliqua qu'il désirait parler à M. Pirard, le directeur du séminaire. Sans dire une parole, l'homme noir lui fit signe de le suivre. Ils montèrent deux étages par un large escalier à rampe de bois, dont les marches déjetées penchaient tout à fait du côté opposé au mur, et semblaient prêtes à tomber. Une petite porte, surmontée d'une grande croix de cimetière en bois blanc peint en noir, fut ouverte avec difficulté, et le portier le fit entrer dans une chambre sombre et basse, dont les murs blanchis à la chaux étaient garnis de deux grands tableaux noircis par le temps. Là, Julien fut laissé seul ; il était atterré, son cœur battait violemment ; il eût été heureux d'oser pleurer. Un silence de mort régnait dans toute la maison. Au bout d'un quart d'heure, qui lui parut une journée, le portier à figure sinistre reparut sur le pas d'une porte à l'autre extrémité de la chambre, et, sans daigner parler, lui fit signe d'avancer. Il entra dans une pièce encore plus grande que la première et fort mal éclairée. Les murs aussi étaient blanchis ; mais il n'y avait pas de meubles. Seulement dans un coin près de la porte, Julien vit en passant un lit de bois blanc, deux chaises de paille, et un petit fauteuil en planches de sapin sans coussin. À l'autre extrémité de la chambre, près d'une petite fenêtre à vitres jaunies, garnie de vases de fleurs tenus salement, il aperçut un homme assis devant une table, et couvert d'une soutane délabrée ; il avait l'air en colère, et prenait l'un après l'autre une foule de petits carrés de papier qu'il rangeait sur sa table, après y avoir écrit quelques mots. Il ne s'apercevait pas de la présence de Julien. Celui-ci était immobile debout vers le milieu de la chambre, là où l'avait laissé le portier, qui était ressorti en fermant la porte. Dans une petite ville de l'Aveyron ou des Pyrénées, le moindre incident eût été rendu décisif par le feu du climat. Sous nos cieux plus sombres, un jeune homme pauvre, et qui n'est qu'ambitieux parce que la délicatesse de son cœur lui fait un besoin de quelques-unes des jouissances que donne l'argent, voit tous les jours une femme de trente ans, sincèrement sage, occupée de ses enfants, et qui ne prend nullement dans les romans des exemples de conduite. Tout va lentement, tout se fait peu à peu dans les provinces, il y a plus de naturel.")
#Spanish
##Task_3_6("Quedábanse Castita y Eulalia atontadas con el aroma asiático, vacilando entre la admiración y la envidia pero al fin no tenían más remedio que humillar su soberbia ante el olorcillo aquel de la niña de Arnaiz, y le pedían por Dios que las dejase catarlo más. sólo realizó contratos con las fábricas de Béjar y Alcoy para dar mejor salida a los productos nacionales, sino que introdujo los famosos Sedanes para levitas, y las telas que tanto se usaron del 45 al 55, aquellos patencures, anascotes, cúbicas y chinchillas que ilustran la gloriosa historia de la sastrería moderna. Todas las noches del año le obligaba a rezar el rosario con los dependientes de la casa hasta que cumplió los veinticinco nunca fue a paseo solo, sino en corporación con los susodichos dependientes el teatro no lo cataba sino el día de Pascua, y le hacían un trajecito nuevo cada año, el cual no se ponía más que los domingos. Baldomero, este se echaba a reír y le decía El chico es de buena índole.Déjale que se divierta y que la corra.Los jóvenes del día necesitan despabilarse y ver mucho mundo.No son estos tiempos como los míos, en que no la corría ningún chico del comercio, y nos tenían a todos metidos en un puño hasta que nos casaban. Empezó entonces para Barbarita nueva época de sobresaltos.Si antes sus oraciones fueron pararrayos puestos sobre la cabeza de Juanito para apartar de ella el tifus y las viruelas, después intentaban librarle de otros enemigos no menos atroces.Temía los escándalos que ocasionan lances personales, las pasiones que destruyen la salud y envilecen el alma, los despilfarros, el desorden moral, físico y económico. Aparecía como contratista un tal Albert, de origen belga, que había empezado por introducir paños extranjeros con mala fortuna.Este Albert era hombre muy para el caso, activo, despabilado, seguro en sus tratos aunque no estuvieran escritos.Fue el auxiliar eficacísimo de Casarredonda en sus valiosas contratas de lienzos gallegos para la tropa. Barbarita presumiera, habría podido recortar muy bien los cincuenta y dos años plantándose en los treinta y ocho, sin que nadie le sacara la cuenta, porque la fisonomía y la expresión eran de juventud y gracia, iluminadas por una sonrisa que era la pura miel. Después las corrientes han cambiado otra vez, y al cabo de muchos años ha vuelto a traer España directamente las obras de King-Cheong mas para esto ha sido preciso que viniera la gran vigorización del comercio después del 68 y la robustez de los capitales de nuestros días. Mientras estudió la segunda enseñanza en el colegio de Masarnau, donde estaba a media pensión, su mamá le repasaba las lecciones todas las noches, se las metía en el cerebro a puñados y a empujones, como se mete la lana en un cojín.Ved por dónde aquella señora se convirtió en sibila, intérprete de toda la ciencia humana, pues le descifraba al niño los puntos oscuros que en los libros había, y aclaraba todas sus dudas, allá como Dios le daba a entender. Primero se le ocurrió encargar muchas misas al cura de San Ginés, y no pareciéndole esto bastante, discurrió mandar poner de Manifiesto la Divina Majestad todo el tiempo que el niño estuviese en París.Ya dentro de la Iglesia, pensó que lo del Manifiesto era un lujo desmedido y por lo mismo quizá irreverente. inquietudes de aquella incomparable señora acabaron con el regreso de Juanito. Y quién lo diría Volvió mejor de lo que fue.Tanto hablar de París, y cuando Barbarita creía ver entrar a su hijo hecho una lástima, todo rechupado y anémico, se le ve más gordo y lucio que antes, con mejor color y los ojos más vivos, muchísimo más alegre, más hombre en fin, y con una amplitud de ideas y una puntería de juicio que a todos dejaba pasmados. decadencia del mantón de Manila empezaba a iniciarse, porque si los pañuelos llamados de talle, que eran los más baratos, se vendían bien en Madrid mayormente el día de San Lorenzo, para la parroquia de la chinche y tenían regular salida para Valencia y Málaga, en cambio el gran mantón, los ricos chales de tres, cuatro y cinco mil reales se vendían muy poco, y pasaban meses sin que ninguna parroquiana se atreviera con ellos. disputara esta gloria Juana Trujillo, madre de Baldomero, la cual había muerto el año anterior, porque Asunción probaría ante todas las cancillerías celestiales que a ella se le había ocurrido la sublime idea antes que a su prima.Ni los años, ni las menudencias de la vida han debilitado nunca el profundísimo cariño de estos benditos cónyuges. También pensaba Barbarita, oyendo a su novio, que la procesión iba por dentro y que el pobre chico, a pesar de ser tan grandullón, no tenía alma para sacarla fuera. Me querrá se preguntaba la novia.Pronto hubo de sospechar que si Baldomerito no le hablaba de amor explícitamente, era por pura cortedad y por no saber cómo arrancarse pero que estaba enamorado hasta las gachas, reduciéndose a declararlo con delicadezas, complacencias y puntualidades muy expresivas. travieso y alborotado volviose tan juiciosillo, que al mismo Zalamero daba quince y raya.Entrole la comezón de cumplir religiosamente sus deberes escolásticos y aun de instruirse por su cuenta con lecturas sin tasa y con ejercicios de controversia y palique declamatorio entre amiguitos.")
#English
##Task_3_6("Letter frequency is the number of times letters of the alphabet appear on average in written language. Letter frequency analysis dates back to the Arab mathematician Al-Kindi (c. 801–873 AD), who formally developed the method to break ciphers. Letter frequency analysis gained importance in Europe with the development of movable type in 1450 AD, where one must estimate the amount of type required for each letterform. Linguists use letter frequency analysis as a rudimentary technique for language identification, where it is particularly effective as an indication of whether an unknown writing system is alphabetic, syllabic, or ideographic.")
