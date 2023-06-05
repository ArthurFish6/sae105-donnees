#coding:UTF-8
import tools_sae
import tools_date
import tools_constantes
from projet6 import *
global JOUR_TRAV
JOUR_TRAV = ["lundi", "mardi", "mercredi", "jeudi", "vendredi"]
global JOURS
JOURS = {0: "dimanche", 1: "lundi", 2: "mardi", 3: "mercredi", 4: "jeudi", 5: "vendredi", 6: "samedi"}

global MOIS
MOIS = {0: "janvier", 1: "février", 2: "mars", 3: "avril", 4: "mai", 5: "juin", 6: "juillet", 7: "août", 8: "septembre",
        9: "octobre", 10: "novembre", 11: "décembre"}

global GROUPES
GROUPES = ["B1G1", "B1G2", "B1G3", "B1G4",
           "B2G1", "B2G2", "B2GA"]

def stock_calendrier(chemin):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                           STOCK_CALENDRIER                           |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |            *****Utilise une fonction dit "externe"*****
         |   [?] Retourne une variable qui garde en mémoire un fichier .ics     |
         |                                                                      |                                             .........
         |   [*] PATH  STR                                                      |                                       [%] Fonction simplifé
         |                                                                      |                                             .........
         +----------------------------------------------------------------------+
    """#doc

    #code
    return tools_sae.lecture_fichier(chemin)

def ajout_element_fin(cal, sep):
    """
         +------------------------------------------------------------------+
         |                                                                  |
         |                          AJOUT_ELEMENT_FIN                       |
         |                                                                  |
         +------------------------------------------------------------------+
         |                                                                  |
         |   [?] Ajoute un élément à la fin d'une liste                     |
         |                                                                  |
         |   [*] LISTE LISTE                           [*] ALL ALL          |
         |                                                                  |
         +------------------------------------------------------------------+
    """#doc

    #code
    cal = list(cal)
    indice = len(cal) - 1

    if cal[indice] != sep:
        cal.append(sep)

        return cal
    return cal

def splits2(liste, sep):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                      SPLITS2                                    |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] découpe du texte a partir d'un séparateur et l'ajoute dans une liste      |
         |                                                                                 |
         |   [*] LISTE  LISTE                                    [*] sep                   |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc
    liste = ajout_element_fin(liste, sep)
    liste = suppr_doublons(liste, sep, 1)
    li = []
    li2 = []
    for element in liste:
        if element != sep:
            li.append(element)
        if element == sep:
            li = "".join(li)
            li2.append(li)
            li = []
    count = -1
    for item in li2:
        count += 1
        if item == sep:
            li2[count] = ""
    return li2


def splits(liste, sep):
    """
         +--------------------------------------------------------------------------------+
         |                                                                                 |
         |                                 SPLITS                                          |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] découpe du texte a partir d'un séparateur et l'ajoute dans une liste      |
         |                                                                                 |
         |   [*] LISTE  LISTE                                    [*] sep                   |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    liste = liste + sep
    li = []
    li2 = []
    for element in liste:
        if element != sep:
            li.append(element)
        if element == sep:
            li = "".join(li)
            li2.append(li)
            li = []
    count = -1
    for item in li2:
        count += 1
        if item == sep:
            li2[count] = ""
    return li2

def lecture(calendrier, sep = "", special = 0):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                                 LECTURE                              |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Retourne une variable avec le calendrier en ligne par ligne    |
         |                                                                      |
         |   [*] CALENDRIER STR                                                 |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                          PARAMETRES OPTIONELS                        |
         +----------------------------------------------------------------------+
         |                                                                      |
         |                       [/] Par defaut sep="" |  special               |
         |                                                                      |
         |                       [0] Par defaut                                 |
         |                       [1] ACTIVE  >  ajout_element_fin               |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    #---------------------------------------------------
    if special == 1:
        calendrier = ajout_element_fin(calendrier, sep)
    # ---------------------------------------------------
    liste = []
    texte = ""
    calendrier_par_ligne = []

    for line in calendrier:
        liste.append(line)

        if line == "\n":
            texte = "".join(liste)
            calendrier_par_ligne.append(texte)
            liste = []
            texte = ""
    return calendrier_par_ligne

def extrait_partie_evenement(calendrier, separateur, separate = 0):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                         EXTRAIT_PARTIT_EVENEMENT                     |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Retourne le contenu d'un évènement                             |
         |                                                                      |
         |   [*] CALENDRIER STR                      [*] TEXTE: STR             |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                          PARAMETRES OPTIONELS                        |
         +----------------------------------------------------------------------+
         |                                                                      |
         |                            [/] separate                              |
         |                                                                      |
         |               [0] Par defaut                                         |
         |               [1] ACTIVE  >  Délimite par défaut avec un "|"         |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    calendrier_par_ligne = lecture(calendrier, "\n", 1)
    liste = []
    liste2 = []
    liste3 = []
    liste4 = []
    initialise = 0#Permet d'ajouer du contenu que si initialise est a 1 | initialise est à 1 que si il rempli une condition (ççç)

    for block in calendrier_par_ligne:
        for car in block:
            liste2.append(car)
            liste3 = "".join(liste2)

            if car == "\n":
                liste2 = []

            if liste3 == separateur:#ççç
                initialise = 1
            # ---------------------------------------------------
            if separate == 1:
                if initialise == 1 and car == "|":
                   car = ";"
            # ---------------------------------------------------

            if initialise == 1:
                liste4.append(car)

            if car == "\n" and initialise == 1:
                liste5 = []
                liste = []
                del liste4[0]
                liste4.pop()
                return liste4

def inserts(liste, pos, element):
    """
         +------------------------------------------------------------------+
         |                                                                  |
         |                               INSERTS                            |
         |                                                                  |
         +------------------------------------------------------------------+
         |                                                                  |
         |   [?] Insère un item à un endroit dans une liste                 |
         |                                                                  |
         |   [*] LISTE LISTE       [*] CHIFFRE INT     [*] ALL ALL          |
         |                                                                  |
         +------------------------------------------------------------------+
    """#doc

    #code
    new_li = []
    indice = -1
    pos = pos -1

    while indice < pos-1:
        indice += 1
        new_li.append(liste[indice])

    new_li.append(element)
    indice = -1

    for item in liste:
        indice += 1
        if indice >= pos:
            new_li.append(item)
    return new_li



def del_doublons(liste, double):
    final = []
    for element in liste:
        if element not in double:
            final.append(element)
    return final

def suppr_doublons(liste, double, delet=2):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                              SUPPR_DOUBLONS                          |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Supprimes les deux premier doublons côte à côte                |
         |                                                                      |
         |   [*] LISTE LISTE    [*] CHIFFRE|TEXTE   INT|STR     [*] ALL ALL     |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    # code
    liste = list(liste)
    count = 0
    indice = -1
    final = []
    db = []
    on = 1
    verif = "off"
    INDICE2 = 0#CONSTANT

    for element in liste:
        indice += 1

        if element == double:
            if element in db:

                del liste[indice]
                if delet ==2:
                    del liste[indice-1]
                db = []

                if on == 1:#CONSTANT++
                    INDICE2 = indice
                    on == 0
                    verif = "on"

            else:
                db.append(element)

    if verif == "on":
        return inserts(liste, INDICE2, "|")
    else:
        return liste

def regroupement(liste, sep, desc):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                              REGROUPEMENT                            |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Regroupe le contenu d'un évènement                             |
         |                                                                      |
         |   [*] LISTE LISTE        [*]  TEXTE STR        [*] TEXT: STR         |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    liste = separe_partie_evenement(liste, sep, desc)
    on = 0
    liste2 = []
    liste3 = []

    for element in liste:

        if on == 1 and element == sep:
            liste3.append("".join(liste2))
            liste2 = []

        if on == 1:
            if element != sep:
                liste2.append(element)

        if element == sep:
            on = 1

    return liste3

def decoupe_premiere_partie(liste, sep, special=0):
    """
         +------------------------------------------------------------------------+
         |                                                                        |
         |                          DECOUPE_PREMIERE_PARTIE                       |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                                                                        |
         |   [?] Retourne tout le contenu avant le prémier délimiteur             |
         |                                                                        |
         |   [*] LISTE LISSTE                                [*] TEXTE: STR       |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                          PARAMETRES OPTIONELS                          |
         +------------------------------------------------------------------------+
         |                                                                        |
         |                            [/] special                                 |
         |                                                                        |
         |  [0] Par defaut                                                        |
         |  [1] ACTIVE  > liste = separe_partit_evenement(liste, "SUMMARY:", 1)   |
         |                                                                        |
         +------------------------------------------------------------------------+
    """#doc

    #code
    # -----------------------------------------------------------
    if special == 1:
        liste = extrait_partie_evenement(liste, "SUMMARY:", 1)
    # -----------------------------------------------------------
    liste2 = []

    for element in liste:

        if element == sep:
            liste2 = "".join(liste2)
            return liste2

        liste2.append(element)

def decoupe_deuxieme_partie(liste, sep):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                          DECOUPE_DEUXIEME_PARTIE                     |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Retourne tout le contenu avant le prémier délimiteur           |
         |                                                                      |
         |   [*] LISTE LISSTE                               [*] TEXTE: STR      |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    liste2 = []
    on = 0

    for element in liste:

        if on == 1:
            liste2.append(element)

        if element == sep:
            on = 1

    liste2 = "".join(liste2)

    return liste2

def separe_partie_evenement(liste, sep, desc):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                          SEPARE_PARTIT_EVENEMENT                     |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Sépare le contenu d'un évènement par un délimiteur             |
         |                                                                      |
         |   [*] LISTE LISTE        [*]  TEXTE STR         [*] TEXT: STR        |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    liste = extrait_partie_evenement(liste, desc, 1)
    c = 0
    liste2 = []
    liste3 = []
    liste.append("END")#Ajout un élément en fin de liste temporaire pour simplifié la découpe

    for element in liste:

        if element == sep:
            c = 1

        if c == 1:
            liste2.append(element)

        if element == "END":
            liste2.pop()
            liste2.append(sep)
            return liste2

def variable_attribution_evenement(liste, sep, desc):
    """
         +----------------------------------------------------------------------+                  /\
         |                                                                      |                 /  \
         |                     variable_attribution_evenement                   |                /    \
         |                                                                      |               /      \
         +----------------------------------------------------------------------+              /    |   \
         |                                                                      |             /     |    \              [%]____VARIABLE AVEC DES VAALEURS PREDEFINIS____
         |   [?] Regroupe le contenu d'un évènement                             |            /      |     \
         |                                                                      |           /       |      \          ----    theme = ["Journée d'intégration", "FA"]   ----
         |   [*] LISTE LISTE        [*]  TEXTE STR         [*] TEXT: STR        |          /                \      ----              valuation = ["DS", "Eval"]             ----
         |                                                                      |         /         0        \        ----    modalite = ["CM", "TD", "TP", "Proj"]    ----
         +----------------------------------------------------------------------+        +====================+
    """#doc

    #code
    liste_d = decoupe_premiere_partie(liste, sep, 1)
    liste = regroupement(liste, sep, desc)

    liste1 = []
    #Variables pré-définis ~~~~~~~~~~~~~~~~
    modalite = ["CM", "TD", "TP", "Proj"]
    evaluation = ["DS", "Eval"]
    theme = ["Journée d'intégration", "FA"]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    liste1.append(liste_d)

    var1 = ""
    var2 = ""
    var3 = ""

    if len(liste) >= 1:
        if liste[0] in modalite:
            var1 = liste[0]

        elif liste[0] in evaluation:
            var2 = liste[0]
            var1 = ""

        elif liste[0] in theme:
            var3 = liste[0]
            var2 = ""
            var1 = ""
        else:
            var1 = ""

    if len(liste) >= 2:
        if liste[1] in evaluation:
            var2 = liste[1]

        elif liste[1] in theme:
            var2 = ""
            var3 = liste[1]

        else:
            var2 = ""

    if len(liste) >= 3:
        var3 = liste[2]

    liste1 = "".join(liste1)
    return f"{liste1};{var1};{var2};{var3}"

def separation_evenement(calendrier, begin = "BEGIN:VEVENT\n", end = "END:VCALENDAR\n", event = "END:VEVENT\n"):
    """
         +--------------------------------------------------------------------------------+
         |                                                                                |
         |                                 SEPARATION_EVENEMENT                           |
         |                                                                                |
         +--------------------------------------------------------------------------------+
         |                                                                                |
         |   [?] Retourne une liste contenant chaque élémentss entre les délimiteurs      |
         |                                                                                |
         |   [*] LISTE LISTE                                                              |
         |                                                                                |
         +--------------------------------------------------------------------------------+
         |                              PARAMETRES OPTIONELS                              |
         +--------------------------------------------------------------------------------+
         |                                                                                |
         |                            [/] begin | end | event                             |
         |                                                                                |
         |      [begin] Par défaut  "BEGIN:VEVENT\n"                                      |
         |      [end]   Par défaut  "END:VCALENDAR\n"                                     |
         |      [EVENT] Par défaut  "END:VEVENT\n"                                        |
         |                                                                                |
         +--------------------------------------------------------------------------------+
    """#doc

    #code
    calendrier_par_ligne = lecture(calendrier)
    liste = []
    final = []
    initialise = 0#cette variable permet de ne pas ajouter du contenu tant que
                  #Le parcours n'a pas rencontré le premier BEGIN:VEVENT
                  #Ce qui permet de ne pas ajouter les éléments au début du fichier
                  #liens, versions ex..

    for block in calendrier_par_ligne:

        if block == event:#Délimiteur de fin
            block = ""
            liste = "".join(liste)
            final.append(liste)
            liste = []

        if block == begin:#Délimiteur de début
            block = ""
            initialise = 1

        if block == end:#Délimiteur final
            block = ""

        if initialise == 1:
            liste.append(block)

    return final



def extrait_evenements(calendrier):
    """
        +----------------------------------------------------------------------+
        |                                                                      |
        |                           EXTRAIT_EVENEMENT                          |
        |                                                                      |
        +----------------------------------------------------------------------+
        |                                                                      |                                               .........
        |   [?] Retourne une liste d'éléments séparés par ","                  |                                        [%] Fonction simplifé
        |                                                                      |                                               .........
        |   [*] LIST (.isc format) LIST                                        |
        |                                                                      |
        +----------------------------------------------------------------------+
    """#doc

    #code
    return separation_evenement(calendrier)



def minutes_jour(minutes):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                   MINUTES_JOUR                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne des minutes en un une durée sous le format jour                  |
         |                                                                                 |
         |   [*] MINUTES STR                                                               |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    annee = minutes/525600
    mois = (minutes%525600)/43200
    jour = ((minutes%525600)%43200)/1440
    li = [jour, mois, annee]
    for index in range(len(li)):
        li[index] = int(li[index])
        li[index] = li[index] + 100
        li[index] = str(li[index])
    return f"{li[2][1:3]}:{li[1][1:3]}:{li[0][1:3]}"


def jour_minutes(day):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                   JOUR_MINUTES                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne un jour en minutes                                               |
         |                                                                                 |
         |   [*] DATE STR                                                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    annee = int(day[6:10]) * 525600
    mois  = int(day[3:5]) * 43800
    jour = int(day[0:2]) * 1444
    return annee + mois + jour

def finds(chaine, partie):
    for item in range(len(chaine)):
        if chaine[item] == partie:
            return item

def recupere_champ_csv_list(event_csv, nom):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                             RECUPERE_CHAMP_CSV_LIST                             |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne l'evenement correspondant à un champ                             |
         |                                                                                 |
         |   [*] LISTE  LISTE                          [*] TEXTE STR                       |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    li = []
    ref = ["uid", "date", "heure", "duree", "modules", "modalite", "evaluation", "theme", "salles", "profs", "groupes"]
    for index in range(len(event_csv)):
        o = (finds(ref, nom))
        if event_csv[index][o] not in li:
            li.append(event_csv[index][o])
    return li


def suppr(liste, element):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                       SUPPR                                     |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Supprime un élément d'une liste                                           |
         |                                                                                 |
         |   [*] LISTE  LISTE                          [*] TEXTE STR                       |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    li = []
    for i in range(len(liste)):
        if liste[i] != element:
            li.append(liste[i])
    return li

def replace(liste, element, change):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                     REPLACE                                     |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Remplace un élément d'une liste                                           |
         |                                                                                 |
         |   [*] LISTE  LISTE             [*]TEXT STR             [*] TEXTE STR            |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    for i in range(len(liste)):
        if liste[i] == element:
            liste[i] = change
    liste = "".join(liste)
    return liste

def maxL(liste):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                     MAXL                                        |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne le plus grand élément d'une liste                                |
         |                                                                                 |
         |   [*] LISTE  LISTE                                                              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    maxim = liste[0]
    for i in range(len(liste)):
        if liste[i] > maxim:
            maxim = liste[i]
    return maxim

def minL(liste):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                     MINL                                        |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne le plus petit élément d'une liste                                |
         |                                                                                 |
         |   [*] LISTE  LISTE                                                              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    min = liste[0]
    for i in range(len(liste)):
        if min > liste[i]:
            min = liste[i]
    return min

def extrait_date(date):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                 EXTRAIT_DATE                                    |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Extrait et retourne les dates entre elles                                 |
         |                                                                                 |
         |   [*] LISTE  LISTE                                                              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    return [date[0:2], date[3:5], date[6:]]



def regroupe_regulier(liste, case):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                               REGROUPE_REGULIER                                 |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Regroupe des élémément de la même façon à partir d'une "case"             |
         |                                                                                 |
         |   [*] LISTE  LISTE                                                              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    li = []
    li2 = []
    liste.append("END")
    for i in range(0, len(liste)):
        if i % case == 0 and i != 0:
            li2.append("".join(li))
            li = []
        li.append(liste[i])
    return li2





def calcule_nbre_journees_travaillees2(journees, jour):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                       CALCULE_NBRE_JOURNEES_TRAVAILLEES2                        |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne le JOUR des nombres travaillées                                  |
         |                                                                                 |
         |   [*] JOURNEES  LISTE        [*]JOUR TEXT                                       |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    li = []
    g = []
    extracted = []
    for i in JOURS.keys():
        if JOURS[i] == jour:
            med = i
    for item in journees:
        extracted.append(extrait_date(item))
    for i in range(len(extracted)):
        if tools_date.get_numero_jour_semaine(int(extracted[i][0]), int(extracted[i][1]), int(extracted[i][2])) == med:
            g.append(journees[i])
    return g