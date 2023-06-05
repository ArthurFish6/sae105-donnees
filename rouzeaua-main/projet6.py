#coding:utf-8


#Modules
import tools_tests
import tools_sae
import tools_constantes
import tools_date

from matplotlib import pyplot as plt
import numpy as np

from tools_fait_maison import *

"""     .--.
    .-._;.--.;_.-.
   (_.'_..--.._'._)
    /.' . 60 . '.\
   // .      / . \\
  |; .      /   . |;
  ||45    ()    15||
  |; .          . |;
   \\ .        . //
    \'._' 30 '_.'/
     '-._'--'_.-'
         `""`
"""

def convertit_date(date):
    """
         +------------------------------------------------------------------------+
         |                                                                        |
         |                             CONVERTIT_DATE                             |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                                                                        |                         
         |   [?] [?]Convertit une date du format aaammjj au format jjmmaaaa          |                                   
         |                                                                        |                                      
         |   [*]prend en paramètre une date au format aaammjj                     |
         |                                                                        |
         +------------------------------------------------------------------------+
    """#doc

    #code
    texte = str(date)
    jj = texte[6:8]
    mm = texte[4:6]
    aaaa = texte[0:4]

    return jj + "-" + mm + "-" + aaaa

def convertit_heure(temps_hhmmss):
    """
         +------------------------------------------------------------------------+
         |                                                                        |
         |                              CONVERTIT_HEURE                           |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                                                                        |                         
         |   [?] [?]Convertit un temps aux format hhmmss au format hhmm           |                                   
         |                                                                        |                                      
         |   [*]prend en paramètre une date au format aaammjj                     |
         |                                                                        |
         +------------------------------------------------------------------------+
    """#doc

    #code
    temps_hhmmss = str(temps_hhmmss)
    heure = temps_hhmmss[0:2]
    minutes = temps_hhmmss[2:4]

    return heure + ":" + minutes


def convertit_date(date):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                            CONVERTIT_DATE                          |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Convertit une date du format aaammjj au format jjmmaaaa      |
         |                                                                    |
         |   [*] DATE  STR {aaammjj}                                          |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    #Extrait les données
    texte = str(date)
    jj = texte[6:8]
    mm = texte[4:6]
    aaaa = texte[0:4]

    return jj + "-" + mm + "-" + aaaa

def calcule_duree(heure_debut, heure_fin):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                             CALCULE DUREE                            |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |
         |   [?] Retourne le résultat de la soustraction de deux durées         |
         |                                                                      |
         |   [*] DURRE  STR {HH:MM}                                             |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    # code
    heure_debut_heure = int(heure_debut[0:2])
    heure_debut_minute = int(heure_debut[3:5])

    duree1 = heure_debut_heure * 60 + heure_debut_minute

    heure_fin_heure = int(heure_fin[0:2])
    heure_fin_minute = int(heure_fin[3:5])
    duree2 = heure_fin_heure * 60 + heure_fin_minute

    heures_calculer = duree2 - duree1
    minutes = heures_calculer % 60
    heure = heures_calculer // 60

    heure = heure + 100#permet d'avoir le format 00: si vide
    heures = str(heure)
    minutes = minutes + 100#permet d'avoir le format :00 si vide
    minutes = str(minutes)

    return heures[1:4] + ":" + minutes[1:4]

def calcule_nombre_minute_duree(minutes):
    """
         +------------------------------------------------------------------------+
         |                                                                        |
         |                       CALCULE_NOMBRE_MINUTE_DUREE                      |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                                                                        |                                           .........
         |   [?] Retourne la conversion de minutes en une durée au format hh:mm   |                                     [%] Fonction simplifé
         |                                                                        |                                           .........
         |   [*] MINUTE  INT                                                      |
         |                                                                        |
         +------------------------------------------------------------------------+
    """#doc
    h = int(minutes) // 60
    m = int(minutes) % 60
    #code
    return f"{h}:{m}"

def calcule_nombre_minutes(hhmm):
    """
         +--------------------------------------------------------------+
         |                                                              |
         |                     CALCULE_NOMBRE_MINUTES                   |
         |                                                              |
         +--------------------------------------------------------------+
         |                                                              |                                                      .........
         |   [?] Retourne la conversion d'une durée en minutes          |                                               [%] Fonction simplifé
         |                                                              |                                                      .........
         |   [*] DUREE  STR {HH:MM}                                     |
         |                                                              |
         +--------------------------------------------------------------+
    """#doc

    #code
    return (int(hhmm[3:5])) + (int(hhmm[0:2])*60)

def calcule_heure_fin(heure_debut, duree):
    """
         +---------------------------------------------------------------------+
         |                                                                     |
         |                          CALCULE_HEURE_FIN                          |
         |                                                                     |
         +---------------------------------------------------------------------+
         |                                                                     |
         |   [?] Retourne l'heure au format hhmm de la fin d'un évènement      |
         |                                                                     |
         |   [*] DUREE DEBUT  STR {HH:MM}  [*] DUREE                           |
         |                                                                     |
         +---------------------------------------------------------------------+
    """#doc

    #code
    heure_debut = calcule_nombre_minutes(heure_debut)
    duree = calcule_nombre_minutes(duree)

    if heure_debut + duree > 1440:
        compter = 0

        while heure_debut != 1440:
            heure_debut += 1
            compter += 1

        duree = duree - compter
        heure_debut = 0
        heure_debut = heure_debut + duree
        minutes = heure_debut + duree

        if minutes == 1440:
            return "00:00"
        return calcule_nombre_minute_duree(minutes // 2)
    minutes = heure_debut + duree

    if minutes == 1440:
        return "00:00"

    first = []
    second = []
    line = (calcule_nombre_minute_duree(minutes))
    limiter = 0
    for item in line:
        if item == ":":
            limiter = 1
            continue
        if limiter == 0:
            first.append(item)
        if limiter == 1:
            second.append(item)


    first = int("".join(first))
    first = first + 100
    first = str(first)
    first = list(first)
    del first[0]
    first = "".join(first)

    second = int("".join(second))
    second = second + 100
    second = str(second)

    second = list(second)
    del second[0]
    second = "".join(second)
    return f"{first}:{second}"

calcule_heure_fin("08:00", "01:00")

def compare_heures(heure1, heure2):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                 COMPARE_HEURES                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] COMPARE DEUX HEURES  : [1 si H1 > H2] [-1 si H1 < H2 0] [si H1 = H2]      |
         |                                                                                 |
         |   [*] HEURE1 STR {HH:MM}                  [*] HEURE2 STR {HH:MM}                |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    heure1 = calcule_nombre_minutes(heure1)
    heure2 = calcule_nombre_minutes(heure2)

    if heure1 < heure2:
        return -1

    if heure1 > heure2:
        return 1
    return 0

def compare_dates(date1, date2):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                  COMPARE_DATES                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] COMPARE DEUX DATES  : [1 si D1 > D2] [-1 si D1 < D2 0] [si D1 = D2]       |
         |                                                                                 |
         |   [*] DATE1 STR {aaammjj}                  [*] DATE2 STR {aaammjj}              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    annee_date1 = int(date1[6:10])
    jour_date1 = int(date1[0:2])
    mois_date1 = int(date1[3:5])

    annee_date2 = int(date2[6:10])
    jour_date2 = int(date2[0:2])
    mois_date2 = int(date2[3:5])

    if annee_date1 < annee_date2:
        return -1

    if annee_date1 == annee_date2:
        if mois_date1 < mois_date2:
            return -1

        if mois_date1 > mois_date2:
            return 1

        if mois_date1 == mois_date2:
            if jour_date1 < jour_date2:
                return -1

            if jour_date1 > jour_date2:
                return 1
            return 0

    return 1

def est_date_dans_intervalle(date, debut, fin):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                             EST_DATE_DANS_INTERVALLE                            |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne [True si date => intervalle] [sinon Fale]                        |
         |                                                                                 |
         |   [*] DATE STR {aaammjj}   [*] DATE STR {aaammjj}   [*] DATE STR {aaammjj}      |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code:
    if compare_dates(date, debut) == 1 or 0:
        if compare_dates(date, fin) == -1 or 0:
            return True
    return False

def compare_dates(date1, date2):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                  COMPARE_DATES                                  |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] COMPARE DEUX DATES  : [1 si D1 > D2] [-1 si D1 < D2 0] [si D1 = D2]       |
         |                                                                                 |
         |   [*] DATE1 STR {aaammjj}                  [*] DATE2 STR {aaammjj}              |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    annee1 = jour_minutes(date1)
    annee2 = jour_minutes(date2)

    if annee1 > annee2:
        return 1
    elif annee1 < annee2:
        return -1
    return 0

def est_date_dans_intervalle(date, debut, fin):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                             EST_DATE_DANS_INTERVALLE                            |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne [True si date => intervalle] [sinon Fale]                        |
         |                                                                                 |
         |   [*] DATE STR {aaammjj}   [*] DATE STR {aaammjj}   [*] DATE STR {aaammjj}      |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code:
    if compare_dates(date, debut) == 1 or 0:
            if compare_dates(date, fin) == -1 or 0:
                return True
    return False
#----------------------------------------------------------------------------------------------------------------------------------------
def recupere_champ_csv(event_csv1, nom):
    """
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |                                RECUPERE_CHAMP_CSV                               |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
         |                                                                                 |
         |   [?] Retourne l'evenement correspondant à un champ                             |
         |                                                                                 |
         |   [*] LISTE TEXTE STR                          [*] TEXTE STR                    |
         |                                                                                 |
         +---------------------------------------------------------------------------------+
    """#doc

    #code
    event_csv = splits(event_csv1, ";")
    champ = ""
    if nom == "uid":
        champ = event_csv[0]
    elif nom == "date":
        champ = event_csv[1]
    elif nom == "heure":
        champ = event_csv[2]
    elif nom == "duree":
        champ = event_csv[3]
    elif nom == "modules":
        champ = event_csv[4]
    elif nom == "modalite":
        champ = event_csv[5]
    elif nom == "evaluation":
        champ = event_csv[6]
    elif nom == "theme":
        champ = event_csv[7]
    elif nom == "salles":
        champ = event_csv[8]
    elif nom == "profs":
        champ = event_csv[9]
    elif nom == "groupes":
        champ = event_csv[10]
    if champ == "":
        return None
    else:
        return champ
#----------------------------------------------------------------------------------------------------------------------------------------
def parse(event):#variable de tools_fait_maison
    """
         +----------------------------------------------------------------------+
         |                                                                      |         /\
         |                                  PARSE                               |        /  \
         |                                                                      |       /  | \
         +----------------------------------------------------------------------+      /   |  \  [%] Varaibles avec des valeurs prédéfinis !
         |                                                                      |     /    |   \
         |   [?] Retourne une listes d'événement regroupé au format texte       |    /     0    \
         |                                                                      |   +------------+
         |   [*] LIST (.isc format) LIST                                        |
         |                                                                      |   Les variables avec desc emmènent vers extrait_evenent + decoupe_1|2_partie
         +----------------------------------------------------------------------+
         |                                                                      |
         |                Valeurs avec des variables prés-définis               |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    #Appel avec des évenement préss-définis
    time = extrait_partie_evenement(event, "DTSTART:")
    time.pop()
    date1 = (decoupe_premiere_partie(time, "T"))
    heure1 = (decoupe_deuxieme_partie(time, "T"))
    dated = convertit_date(date1)
    heured = convertit_heure(heure1)

    end = extrait_partie_evenement(event, "DTEND:")
    end.pop()
    date2 = (decoupe_premiere_partie(end, "T"))
    heure2 = (decoupe_deuxieme_partie(end, "T"))

    datef = convertit_date(date2)
    heuref = convertit_heure(heure2)

    duree = calcule_duree(heured, heuref)
    uid = extrait_partie_evenement(event, "UID:")
    uid = list(uid)
    uid = "".join(uid)
    duree = calcule_duree(heured, heuref)
    date = dated

    location = extrait_partie_evenement(event, "LOCATION:")
    location = "".join(location)
    desc = extrait_partie_evenement(event, "DESCRIPTION:")

    cat = extrait_partie_evenement(event, "CATEGORIES:")
    cat = "".join(cat)

    module = variable_attribution_evenement(event, ";", "SUMMARY:")
    module = suppr_doublons(module, "/")
    module = "".join(module)

    if desc != None:
        desc = "".join(desc)
    else:
        return (f"{uid};{date};{heured};{duree};{module};{location};;{cat}")
    return (f"{uid};{date};{heured};{duree};{module};{location};{desc};{cat}")


def selectionne_semestre(event, semestre):
    final = []
    for k in range(len(event)):
        if est_dans_semestre(recupere_champ_csv(event[k], "modules"), semestre):
            final.append(event[k])
    return final


def selectionne_groupe(event, groupe):
    GROUPES = ["B1G1", "B1G2", "B1G3", "B1G4", "B2G1", "B2G2", "B2GA"]
    li = []
    li2 = []
    for i in range(len(event)):
        li.append("".join(event[i]))

    for j in range(len(li)):
        ac = suppr(recupere_champ_csv(li[j], "groupes"), "|")
        ac = list(ac)
        ac = regroupe_regulier(ac, 4)
        if groupe in ac:
            li2.append(li[j])
    return li2


#----------------------------------------------------------------------------------------------------------------------------------------



def parse_evenement(event):
    """
         +----------------------------------------------------------------------+
         |                                                                      |
         |                            PARSE_EVENEMENT                           |
         |                                                                      |
         +----------------------------------------------------------------------+
         |                                                                      |                                               .........
         |   [?] Retourne au format ics les déscriptions d'événements           |                                        [%] Fonction simplifé
         |                                                                      |                                               .........
         |   [*] LIST (.isc format) LIST                                        |
         |                                                                      |
         +----------------------------------------------------------------------+
    """#doc

    #code
    return parse(event)

def parse_fichier_ics(file):
    """
        +-----------------------------------------------------------------------------------------+
        |                                                                                         |
        |                                       PARSE_FICHIER_ICS                                 |
        |                                                                                         |
        +-----------------------------------------------------------------------------------------+
        |                                                                                         |
        |   [?] Retourne au format csv le contenu d'une liste de texte contenant des événements   |
        |                                                                                         |
        |   [*] LIST {TEXTE INSIDE} LIST=>STR                                                     |
        |                                                                                         |
        +-----------------------------------------------------------------------------------------+
    """#doc

    #code
    ex_event = extrait_evenements(stock_calendrier(file))
    final = []


    for i in range(len(ex_event)):
        final.append(parse_evenement(ex_event[i]))
    return final

def parse_summary(summary):
    """
        +----------------------------------------------------------------------+
        |                                                                      |
        |                            PARSE_SUMMARY                             |
        |                                                                      |
        +----------------------------------------------------------------------+
        |                                                                      |                                               .........
        |   [?] Retourne le champ "SUMMARY:" d'un évènement                    |                                        [%] Fonction simplifé
        |                                                                      |                                               .........
        |   [*] LIST (.isc format) LIST                                        |
        |                                                                      |
        +----------------------------------------------------------------------+
    """#doc

    #code
    final = variable_attribution_evenement(summary, ";", "SUMMARY:")
    return final
#----------------------------------------------------------------------------------------------------------------------------------------


def extrait_liste_journees_travaillees(events_csv):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                  ETRAIT_LISTE_JOURNEES_TRAVAILLEES                 |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Extrait la liste des jours travaillés, correspondant à       |
         |     (au moins) un évènement du calendrier fourni dans events_csv.  |
         |      Chaque jour sera donné sous la forme "JJ-MM-AAAA"             |
         |                                                                    |
         |   [*] events_csv LISTE STR                                          |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    li = []
    final = []
    for item in events_csv:
        item = splits(item, ";")
        li.append(item)
    return recupere_champ_csv_list(li, "date")

def extrait_periode(journee):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                            EXTRAIT_PERIODE                         |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Extrait un periode d'une journee                             |
         |                                                                    |
         |   [*] journee   aux format "JJ-MM-ANNEE                            |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    if journee == []:
        return None
    li = []
    inter = []
    final = []
    for index in range(len(journee)):
        li.append(jour_minutes(journee[index]))
    maxim = maxL(li)
    min = minL(li)
    for index in range(len(li)):
        if li[index] == min:
            inter.append(journee[index])
        elif li[index] == maxim:
            inter.append(journee[index])
    if (compare_dates(inter[0], inter[1])) == 1:
        final.append(inter[1])
        final.append(inter[0])
        return final
    final.append(inter[0])
    final.append(inter[1])
    return final

def calcule_nbre_journees_travaillees(journees, jour):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                            EXTRAIT_PERIODE                         |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Extrait un periode d'une journee                             |
         |                                                                    |
         |   [*] journee   aux format "JJ-MM-ANNEE                            |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    nbre_jours = 0
    date_check = []
    if jour in JOUR_TRAV:
        for date in journees:
            n_jour = int(splits(date, "-")[0])
            mois = int(splits(date, "-")[1])
            annee = int(splits(date, "-")[2])
            if tools_date.JOURS[tools_date.get_numero_jour_semaine(n_jour, mois, annee)] == jour and date not in date_check:
                date_check.append(date)
                nbre_jours += 1
        return nbre_jours

def calcule_nbre_journees_ouvrees(date_debut, date_fin, jour):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                   CALCULE_NBRE_JOURNEES_OUVREES                    |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Retourne le nombre de journées ouvrées                       |
         |                                                                    |
         |   [*] journee   aux format "JJ-MM-ANNEE                            |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    li = []
    ouvree = tools_sae.get_jours_ouvres()
    for i in range(len(ouvree)):
        if ouvree[i] == date_debut or ouvree[i] == date_fin:
            li.append(ouvree[i])
        if est_date_dans_intervalle(ouvree[i], date_debut, date_fin):
            li.append(ouvree[i])
    final= calcule_nbre_journees_travaillees(li, jour)
    return final

def est_dans_semestre(module, semestre):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                           EST_DANS_SEMESTRE                        |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Retourne True | False si un modules                          |
         |       est ou non dans un semestres                                 |
         |                                                                    |
         |   [*] MODULE STR         [*]SEMESTRE STR                           |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc
    liste_semestres = {"S1": tools_constantes.MODULES_S1, "S2": tools_constantes.MODULES_S2, "S3": tools_constantes.MODULES_S3, "S4": tools_constantes.MODULES_S4}
    if len(splits(module, "|")) > 1:
        for i in splits(module, "|"):
            if i in liste_semestres[semestre]:
                return True

    if module in liste_semestres[semestre]:
        return True
    return False

def selectionne_cours_groupe(event, groupe, semestre):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |                           SELECTIONNE_COURS_GROUPE                 |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Retourne le modules auxquels assistes un groupes             |
         |       est ou non dans un semestres                                 |
         |                                                                    |
         |   [*] ENVENT LISTE STR     [*] GROUPE STR    [*] SEMESTRE STR      |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    li = selectionne_groupe(event, groupe)
    return selectionne_semestre(li, semestre)

def calcule_nbre_heures_travailles_par_jour(event_csv, jour):
    """
         +--------------------------------------------------------------------+
         |                                                                    |
         |               CALCULE_NBRE_HEURES_TRAVAILLES_PAR_JOUR              |
         |                                                                    |
         +--------------------------------------------------------------------+
         |                                                                    |
         |   [?] Retourne le nombres d'heures travaillées par jour            |
         |                                                                    |
         |   [*] ENVENT LISTE STR                       [*] JOUR STR          |
         |                                                                    |
         +--------------------------------------------------------------------+
    """#doc

    #code
    heures = 0
    for item in event_csv:
        duree = recupere_champ_csv(item, "duree")
        date = recupere_champ_csv(item, "date")

        n_jour = int(splits(date, "-")[0])
        mois = int(splits(date, "-")[1])
        annee = int(splits(date, "-")[2])

        years = JOURS[tools_date.get_numero_jour_semaine(n_jour, mois, annee)]
        if years == jour:
            heures = heures + calcule_nombre_minutes(duree)
    return heures / 60

def traitement(event_csv, groupe, semestre):
    """
         +---------------------------------------------------------------------+
         |                                                                     |
         |                        TRAITEMENT(de s'est mort)                    |
         |                                                                     |
         +---------------------------------------------------------------------+
         |                                                                     |
         |     [!*!]  Calcule, pour un groupe d’étudiant et un semestre donné, |
         |       le nombre de journées travaillés et le nombre d’heures moyen  |
         |       par jour de la semaine. On distinguera la moyenne             |
         |       sur le nombre de journées réellement travaillées              |
         |        et le nombre de jours ouvrées.                               |
         |                                                                     |
         |       La fonction retourne une liste de chaîne de caractères        |
         |       au format :                                                   |
         |       "<nom jour>;<nb journées travaillés>;                         |
         |       <moyenne heures>;<nb journées ouvrés>;                        |
         |       <moyenne heures ouvrées>"                                     |
         |                                                                     |
         |   [*] ENVENT LISTE STR                       [*] JOUR STR           |
         |                                                                     |
         +---------------------------------------------------------------------+
    """#doc

    #code
    final = []
    moyenne_trav = ""
    moyenne_open = ""
    cours_groupe = selectionne_cours_groupe(event_csv, groupe, semestre)
    journees_travailles = extrait_liste_journees_travaillees(cours_groupe)

    periode = extrait_periode(journees_travailles)

    for jour in JOUR_TRAV:
        n_jours_travailles = calcule_nbre_journees_travaillees(journees_travailles, jour)
        heures_travailles = calcule_nbre_heures_travailles_par_jour(cours_groupe, jour)
        jours_ouvres = calcule_nbre_journees_ouvrees(periode[0], periode[1], jour)

        if heures_travailles != 0.0:
            moyenne_trav = round(heures_travailles / n_jours_travailles, 2)
            moyenne_open = round(heures_travailles / jours_ouvres, 2)
            final.append(f"{jour};{n_jours_travailles};{moyenne_trav:.02f};{jours_ouvres};{moyenne_open:.02f}")#02f 0.02f
    return final

def export_markdwon(res, title):
    """
         +---------------------------------------------------------------------+
         |                                                                     |
         |                        TRAITEMENT(de s'est mort)                    |
         |                                                                     |
         +---------------------------------------------------------------------+
         |                                                                     |
         |     [**] Retourne au format markdwon le rendu                       |
         |           de la fonction traitement                                 |
         |                                                                     |
         |   [*] ENVENT LISTE STR                       [*] JOUR STR           |
         |                                                                     |
         +---------------------------------------------------------------------+
    """#doc

    #code
    li = ["Jour de la semaine", "Nombre de jours travaillés", "Moyenne horaire par jour travaillé", "Nombre de jours ouvrés", "Moyenne horaire par jour ouvré"]
    with open("tableau.md", "w", encoding="utf8") as mdFile:
        mdFile.write(f"# {title} \n")#titre
        mdFile.write(f"|{li[0]}|{li[1]}|{li[2]}|{li[3]}|{li[4]}|\n")#entete
        mdFile.write("|------|------|------|------|------|\n")#tableaux
        #code
        for i in range(len(res)):
            splintercell = splits(res[i], ";")
            mdFile.write(f"|  {splintercell[0]}  |  {splintercell[1]}  |  {splintercell[2]}  |  {splintercell[3]}  |  {splintercell[4]}  |\n")  #entete
        mdFile.close()


def export_png(resultats):
    """
         +------------------------------------------------------------------------+
         |                                                                        |
         |                                EXPORT_PNG                              |
         |                                                                        |
         +------------------------------------------------------------------------+
         |                                                                        |                         
         |   [?] Rend un tableau graphique de la fonction "TRAITEMENT"            |                                   
         |                                                                        |                                      
         |   [*]prend en paramètre le resultat de la fonc "traitement             |
         |                                                                        |
         +------------------------------------------------------------------------+
    """#doc

    #code
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
    m_jours_trav = []
    nb_trav = []
    moyenne_jours_ouvres = []
    nombre_de_jour_ouvres = []
    for i in range(len(resultats)):
        li_jour = resultats[i].split(';')
        m_jours_trav.append(float(li_jour[2]))
        nb_trav.append(float(li_jour[1]))
        moyenne_jours_ouvres.append(float(li_jour[4]))
        nombre_de_jour_ouvres.append(float(li_jour[3]))

    x = np.arange(len(jours))
    width = 0.35
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, m_jours_trav, width, label='jours travaillés')
    rects2 = ax.bar(x + width / 2, moyenne_jours_ouvres, width, label='jours ouvrés')
    ax.set_ylabel('Nombre d\'heures')
    ax.set_title('Heures de cours en moyenne par jour') #défini le titre du diagrame
    ax.set_xticks(x, jours)
    ax.legend(loc=2)
    plt.ylim(0, 8.0)

    for i in range(len(nb_trav)):
        plt.text(0.1 * i * 1.93 + 0.08, 0.05, nb_trav[i], horizontalalignment='center',
                 verticalalignment='center', transform=ax.transAxes)
        plt.text(0.1 * i * 1.93 + 0.15, 0.05, nombre_de_jour_ouvres[i], horizontalalignment='center',
                 verticalalignment='center', transform=ax.transAxes)
    plt.savefig('resultat.png')
    fig.tight_layout()
    plt.savefig('fichier_png')
    plt.show()

def main():
    print("[!]STARTED")
    while True:
        print("Selectionner un event")
        event = input("[?]> ")#fichier ou liste directement
        event = stock_calendrier(event)#lecture du fichier
        print("Selectionner un groupe d'étudiant")
        etu = input("[?]> ")

        print("Selectionner un semestre")
        sem = input("[?]> ")

        save = traitement(event, etu, sem)
        while True:
            print("[1]Markdown\n[2]Graphique")
            choice = input("[?]> ")
            if choice == "1":
                export_markdwon(save, "Tableaux")
                quit()
            if choice == "2":
                export_png(save)
                quit()
            else:
                continue

if __name__ == '__main__':
    main()
    #end