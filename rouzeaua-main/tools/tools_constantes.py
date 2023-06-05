"""
Module listant toutes les constantes pouvant être utilisées pour faciliter l'écriture du code de la SAE15
"""

# *****************************************************************************
# Les enseignants
#: Liste des enseignants permanents
ENSEIGNANTS_PERMANENTS = ["BARAS CLEO",
                          "DUCHAMP JEAN-MARC",
                          "GOEURIOT LORRAINE",
                          "MORAND ALAIN",
                          "SICLET CYRILLE",
                          "BENECH PHILIPPE",
                          "NOVAKOV EMIL",
                          "THIRIET JEAN MARC",
                          "CHOLLET REMY",
                          "DELNONDEDIEU YVES",
                          "DESPINASSE BRUNO",
                          "DUPONT BELRHALI KARINE",
                          "FAYOLLE GERARD",
                          "KASPER KEVIN",
                          "LUBINEAU DENIS",
                          "ROYER SANDRA",
                          "VEDEL FRANCK",
                          "ESCANDE ERIC",
                          "MARTIN JEROME"]

# *********************************************************
#: Liste de modalités d'enseignement
MODALITES = ["TD", "TP", "CM", "Proj"]

# ************************************************************************
# Les ressources / SAés / module par semestre :

# Liste des modules du semestre 1 découpés en ressources et en SAés
#: Liste des modules (ressources et SAÉs) du semestre 1 de BUT
MODULES_S1 = ["R101-InitRes",
              "R102-ArchiRes",
              "R103-LAN",
              "R104-Eln", # ELN
              "R105-Lignes",
              "R106-ArchiInfo",
              "R107-Python1",
              "R108-Shell",
              "R109-TechnoWeb",
              "R110-Anglais",
              "R111-ExprCom",
              "R112-PPP",
              "R113-MathSignal",
              "R114-MathTx",
              "R115-GestProj",
              "SAÉ101-Hygiène",
              "SAÉ102-ResEnt",
              "SAÉ103-Trans",
              "SAÉ104-WebCV",
              "SAÉ105-Données",
              "SAÉ1Portfolio"]


#: Liste des modules (ressources et SAÉs) du semestre 2 de BUT
MODULES_S2 = ["R201-TechnoIP",
              "R202-AdminSys",
              "R203-ServRes",
              "R204-Téléphonie",
              "R205-Signal",
              "R206-Codage", # Numérisation
              "R207-SGBD",
              "R208-Python2",
              "R209-DevWeb",
              "R210-Anglais",
              "R211-ExprCom",
              "R212-PPP",
              "R213-MathNum",
              "R214-MathAnalyse",
              "SAÉ201-ResEnt",
              "SAÉ202-Mesure",
              "SAÉ203-SolutInfo",
              "SAÉ204-ProjIntégratif",
              "SAÉ2Portfolio"]

#: Liste des modules (ressources et SAÉs) du semestre 3 de BUT
MODULES_S3 = ["R301-ResCampus",
              "R302-ResOp",
              "R303-ServRes",
              "R304-Annuaires",
              "R305-TransNum1",
              "R306-FO",
              "R307-ResAccès",
              "R308-POO",
              "R309-Event",
              "R310-ConfigBDD",
              "R311-Anglais",
              "R312-ExprCom",
              "R313-PPP",
              "R314-MathFourier",
              "R315-GestProj",
              "R3cy16-Pentesting",
              "R3dc16-EcoCloud",
              "R3dc17-Virtu",
              "SAÉ301-SysElec",
              "SAÉ302-AppliCom",
              "SAÉ3Portfolio",
              "SAÉ303-MultiSites",
              "SAÉ3cy04-Pentesting",
              "SAÉ3dc04-InfraVirtu",
              "SAÉ3Alternance"]

#: Listes des modules (ressources et SAÉs) du semestre 4 de BUT
MODULES_S4 = ["R401-InfraSec",
              "R402-TransNum2",
              "R403-Electromag",
              "R404-ResCell",
              "R405-Scripting",
              "R406-Anglais",
              "R407-ExprCom",
              "R4cy09-LANSec",
              "R4cy10-Crypto",
              "R4cy11-ServSec",
              "R4dc09-Container",
              "R4dc10-MicroServ",
              "SAÉ4Portfolio",
              "SAÉ4Stage",
              "SAÉ4Alternance",
              "SAÉ4cy01-Secure",
              "SAÉ4dc01-MicroServ"]

#: Intervention sans module
SANS_CODE = "Autre"

#: Modules du BUT (1ère et 2ème années)
MODULES = MODULES_S1 + MODULES_S2 + MODULES_S3 + MODULES_S4

# *********************************************************************
# Les 3 unités d'enseignements du BUT1

# Pour chaque UE, les modules rattachés aux UE (car ayant le coefficient est le plus élévé dans l'UE)
#: UE de la compétence RT1 du semestre 1 de BUT1
UE_S1_RT1_Administrer = ["R101", "R102", "R103", "R104", "R106", "SAÉ101", "SAÉ102"]
#: UE de la compétence RT2 du semestre 1 de BUT1
UE_S1_RT2_Connecter = ["R105", "R110", "R111", "R112", "R113", "R114", "SAÉ101", "SAÉ103", "SAÉ104"]
#: UE de la compétence RT3 du semestre 1 de BUT1
UE_S3_RT3_Programmer = ["R107", "R108", "R109", "R115", "SAÉ104", "SAÉ105", "SAÉ106"]
#: UE1 du BUT1
UE1_RT1_Administrer = ["R101", "R102", "R103", "R104", "R106", "SAÉ11", "SAÉ12"]
#: UE2 du BUT1
UE2_RT2_Connecter = ["R105", "R110", "R111", "R112", "R113", "R114", "SAÉ13"]
#: UE3 du BUT1
UE3_RT3_Programmer = ["R107", "R108", "R109", "R115", "SAÉ14", "SAÉ15", "SAÉ16"]


# Liste des coeffs de chaque module du S1 dans chaque UE, les modules étant listés
# dans l'ordre RESSOURCES + SAES
COEFF_UE_S1_RT1 = [12, 10, 8, 6, 0, 10, 0, 4, 0, 3, 4, 0, 5, 5, 2, 16, 30, 0, 0, 0, 0]
COEFF_UE_S1_RT2 = [4, 0, 6, 9, 5, 0, 0, 0, 0, 5, 5, 0, 5, 5, 3, 6, 0, 22, 6, 0, 0]
COEFF_UE_S1_RT3 = [4, 0, 0, 0, 0, 0, 20, 10, 8, 4, 4, 0, 4, 4, 2, 0, 0, 0, 16, 28, 0]


# *******************************************************************************
# Les thématiques d'enseignement en BUT : Réseau, Télécom, Informatique, Math, Transverses

#: Thématique réseau
THEME_RESEAU = "Réseau"
#: Liste des ressources et SAés du BUT1 dans le thème réseau
MODULES_RESEAU_BUT1 = ['R101', 'R102', 'R103', 'SAÉ102', 'R201', 'R202', 'R203', 'SAÉ201']
#: Liste des ressources et SAés du BUT2 dans le thème réseau
MODULES_RESEAU_BUT2 = ['R301', 'R302', 'R303', 'R304', 'R3cy16', 'R3dc16', 'R3dc17', 'SAÉ303', 'SAÉ3cy04', 'SAÉ3dc04'
                       'R401', 'R4cy09', 'R4cy11', 'R4dc09', 'SAÉ4cy01']

#: Thématique télécommunication
THEME_TELECOM = "Télécommunication"
#: Liste des ressources et des SAés du BUT1 dans le thème télécom
MODULES_TELECOM_BUT1 = ['R104', 'R105', 'R106', 'SAÉ103', 'R204', 'R205', 'R206', 'SAÉ202']
#: Liste des ressources et des SAés du BUT2 dans le thème télécom
MODULES_TELECOM_BUT2 = ['R305', 'R306', 'R307', 'SAÉ301', 'R402', 'R403', 'R404']

#: Thématique informatique
THEME_INFO = "Informatique"
#: Liste des ressources et des SAés du BUT1 dans le thème informatique
MODULES_INFO_BUT1 = ['R107', 'R108', 'R109', 'SAÉ15', 'R207', 'R208', 'R209', 'SAÉ23']
#: Liste des ressources et des SAés du BUT2 dans le thème informatique
MODULES_INFO_BUT2 = ['R308', 'R309', 'R310', 'SAÉ302', 'R405', 'SAÉ4dc01']

#: Thématique mathématiques
THEME_MATHS = "Mathématiques"
#: Liste des ressources et des Saés dans le thème mathématiques
MODULES_MATHS_BUT1 = ['R105', 'R113', 'R114', 'R213', 'R214']
#:Liste des ressources et des SAés du BUT2 dans le thème mathématiques
MODULES_MATHS_BUT2 = ['R314']

#: Thématique transverse
THEME_TRANSVERSES = "Transverses"
#: Liste des ressources et des Saés dans le thème transverses
MODULES_TRANSVERSES_BUT1 = ['R110', 'R111', 'R112', 'R115', 'SAÉ101', 'SAÉ104', 'SAÉ1Portfolio',
                            'R210', 'R211', 'R212', 'SAÉ204', 'SAÉ2Portfolio']
#: Liste des des ressources et des SAés du BUT2 dans le thème tranverses
MODULES_TRANSVERSES_BUT2 = ['R311', 'R312', 'R313', 'R315', 'SAÉ3Portfolio',
                            'R406', 'R407', 'SAÉ4Portfolio']

# Liste des noms de thèmes
THEMES = [THEME_RESEAU, THEME_INFO, THEME_MATHS, THEME_TELECOM, THEME_TRANSVERSES]

# *******************************************************************************
# Les salles regroupées par fonction pour le département
#: Types de salles
TYPES_SALLES = ["TD", "TP", "Amphi", "Central"]

#: Salles de TD appartenant au département RT
SALLES_TD_RT = ["IUT1_010", "IUT1_06", "IUT1_08",
                "IUT1_112B", "IUT1_119", "IUT1_120",
                "IUT1_120b", "IUT1_121_GE", "IUT1_T23_24"]

#: Salles de TP appartenant au département RT
SALLES_TP_RT = ["IUT1_126", "IUT1_T14 tel", "IUT1_T16 tel2",
                "IUT1_T22 info2", "IUT1_T25 info1", "IUT1_T26 proj",
                "IUT1_T27 res3", "IUT1_T32 res2", "IUT1_T33 res1"]

#: Amphis pour les CM partagés/mutualisés entre plusieurs départements de l'IUT
AMPHI = ["IUT1_AMPHI BELLEDONNE", "IUT1_AMPHI CHARTREUSE"]

#: Autres salles mutualisées/partagées entre plusieurs départements de l'IUT
SALLES_BAT_CENTRAL = ["IUT1_C003", "IUT1_C007", "IUT1_C011",
                      "IUT1_C103", "IUT1_C104", "IUT1_C105",
                      "IUT1_C201", "IUT1_C202", "IUT1_C215"]

# **********************************************************************
# Les groupes (de TD) d'étudiants

#: Groupes de TD du BUT1 et du BUT2
GROUPES = ["B1G1", "B1G2", "B1G3", "B1G4",
           "B2G1", "B2G2", "B2GA"]

# ***********************************************************************
# L'année universitaire 2021-2022

#: Début de l'année universitaire pour les étudiants de S1 et de S3
DEBUT_ANNEE = "01-09-2022"
DEBUT_ANNEE_PROCHAINE = "01-09-2023"

#: Fin d'année universitaire (correspondant à la fin des semestres S2 et S4)
FIN_ANNEE = "31-07-2023"

#: L'heure de début des cours (le matin)
HEURE_DEBUT = "08:00"

#: L'heure de fin (l'après-midi)
HEURE_FIN = "17:30"

# Période de cours entre deux vacances scolaires sous la forme d'une liste [debut_periode, fin_periode],
# la fin de la période indiquant la date (du vendredi) au soir à partir duquel débute les vacances)
#: Période pédagogique entre la Rentrée et la Toussaint
PERIODE1 = [DEBUT_ANNEE, "28-10-2022"]
#: Période pédagogique entre la Toussaint et Noël
PERIODE2 = ["07-11-2022", "20-12-2022"]
#: Période pédagogque entre Noël et les vacances d'Hiver
PERIODE3 = ["03-01-2023", "10-02-2023"]
#: Période pédagogique entre les vacances d'Hiver et celles de Printemps
PERIODE4 = ["20-02-2023", "07-04-2023"]
#: Période pédagogique entre les vacances de Printemps et celles d'Eté
PERIODE5 = ["24-04-2023", FIN_ANNEE]

#: La liste de toutes les périodes
PERIODES_SCOLAIRES = [PERIODE1, PERIODE2, PERIODE3, PERIODE4, PERIODE5]

#: Noms des temps marquants de l'année
NOMS_PERIODES = ["Rentrée", "Toussaint", "Noël", "Hiver", "Printemps", "Eté"]

#: Jours fériés de l'année universitaire
JOURS_FERIES = ["11-11-2022",  # Armistice
                "10-04-2023",  # Lundi de Pâques
                "01-05-2023",  # Fête du travail
                "08-05-2023",  # Victoire 1945
                "18-05-2023",  # Ascension
                "19-05-2023"  # Pont de l'ascension
                ]


# *********************************************************************
# Evènements (donnant lieu à amphi)
EVENEMENTS = ["Conf CyberSécu WatchGuard",
              "Open Day",
              "Réunion partenariale CFA UGA",
              "Infos BUT1",
              "Galette ENEPS",
              "Journée d'intégration",
              "Réunion de rentrée ENEPS",
              "Info Stage",
              "Info mobilités à l'étranger",
              "Réunion de rentrée BUT2-FI",
              "Infos Semestre2",
              "Réunion de rentrée BUT1"]
