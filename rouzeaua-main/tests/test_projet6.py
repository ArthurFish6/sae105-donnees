import inspect

import pytest

import tools_introspection
import tools_tests

# Import du sphinx_projet
try:
    import projet6
except:
    pass
MODULE = "projet6"


@pytest.mark.echeance4
class TestExtraitListeJourneesTravaillees:
    FONCTION = "extrait_liste_journees_travaillees"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["quelques_creneaux1.csv"])
        print("---------------------------------------------------------------", events)
        res = projet6.extrait_liste_journees_travaillees(events)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data, attendu", [
        pytest.param("quelques_creneaux1", "data1", id="quelques_creneaux1"),
        pytest.param("quelques_creneaux2", "data2", id="quelques_creneaux2"),
    ])
    def test_valeur_retour(self, datadir, data, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        attendu = tools_tests.lecture_fichier_yaml(datadir[f"_expected/{attendu}.yaml"])
        resultat = projet6.extrait_liste_journees_travaillees(events)
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestExtraitPeriode:
    FONCTION = "extrait_periode"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 1, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        journees = tools_tests.lecture_fichier_yaml(datadir["data1.yaml"])
        res = projet6.extrait_periode(journees)
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")


    @pytest.mark.parametrize("data, attendu", [
        pytest.param("data1", ['12-09-2022', '22-05-2023'], id="data1"),
        pytest.param("data2", ['16-12-2022', '04-01-2023'], id="data2"),
    ])
    def test_valeur_retour(self, datadir, data, attendu):
        events = tools_tests.lecture_fichier_yaml(datadir[f"{data}.yaml"])
        resultat = projet6.extrait_periode(events)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestCalculeNbreJourneesTravaillees:
    FONCTION = "calcule_nbre_journees_travaillees"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        journees = tools_tests.lecture_fichier_yaml(datadir["liste.yaml"])
        res = projet6.calcule_nbre_journees_travaillees(journees, "lundi")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")


    @pytest.mark.parametrize("jour, attendu", [
        pytest.param("lundi", 4, id="lundi"),
        pytest.param("mardi", 3, id="mardi"),
        pytest.param("jeudi", 2, id="jeudi"),
    ])
    def test_valeur_retour(self, datadir, jour, attendu):
        liste_dates = tools_tests.lecture_fichier_yaml(datadir[f"liste.yaml"])
        resultat = projet6.calcule_nbre_journees_travaillees(liste_dates, jour)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestCalculeNbreJourneesOuvrees:
    FONCTION = "calcule_nbre_journees_ouvrees"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet6.calcule_nbre_journees_ouvrees("10-10-2022", "20-10-2022", "lundi")
        assert isinstance(res, int), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")


    @pytest.mark.parametrize("date_debut, date_fin, jour, attendu", [
        pytest.param("10-10-2022", "20-10-2022", "lundi", 2, id="lundi du 10-10 au 20-10"),
        pytest.param("01-09-2022", "01-10-2022", "mardi", 4, id="mardi du 01-09 au 10-09"),
        pytest.param("20-10-2022", "03-11-2022", "jeudi", 2, id="vacances toussaint"),
        pytest.param("03-11-2022", "20-11-2022", "vendredi", 1, id="toussaint ferie")
    ])
    def test_valeur_retour(self, datadir, date_debut, date_fin, jour, attendu):
        resultat = projet6.calcule_nbre_journees_ouvrees(date_debut, date_fin, jour)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestEstDansSemestre:
    FONCTION = "est_dans_semestre"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 1)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self):
        res = projet6.est_dans_semestre("R107-Python1", "S1")
        assert isinstance(res, bool), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type bool")

    @pytest.mark.parametrize("module, semestre, attendu", [
        pytest.param("R107-Python1", "S1", True, id="R107-Python1 en S1"),
        pytest.param("R107-Python1", "S2", False, id="R107-Python1 en S2"),
        pytest.param("R209-DevWeb", "S2", True, id="R209-DevWeb en S2"),
        pytest.param("SAÉ2Portfolio", "S2", True, id="SAÉ2Portfolio en S3"),
        pytest.param("SAÉ3cy04-Pentesting", "S2", False, id="SAÉ3cy04-Pentesting en S2"),
        pytest.param("SAÉ4Stage", "S4", True, id="SAÉ4Stage en S4"),
        pytest.param("Club Cyber", "S1", False, id="Club Cyber en S1")
    ])
    def test_valeur_retour(self, datadir, module, semestre, attendu):
        resultat = projet6.est_dans_semestre(module, semestre)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")

@pytest.mark.echeance4
class TestSelectionneCoursGroupe:
    FONCTION = "selectionne_cours_groupe"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["exemple1.csv"])
        res = projet6.selectionne_cours_groupe(events, "B1G3", "S1")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data, groupe, semestre, attendu", [
        pytest.param('exemple1', "B2GA", "S3", "B2GA_S3", id="B2GA au S3"),
        pytest.param('exemple1', "B1G3", "S1", "B1G3_S1", id="B1G3 au S1"),
        pytest.param('exemple1', "B1G3", "S2", "B1G3_S2", id="B1G3 au S2"),
        pytest.param('exemple1', "B2GA", "S4", "B2GA_S4", id="B2GA au S4"),
    ])
    def test_valeur_retour(self, datadir, data, groupe, semestre, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{attendu}.csv"])
        resultat = projet6.selectionne_cours_groupe(events, groupe, semestre)
        assert sorted(resultat) == sorted(attendu), \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")


@pytest.mark.echeance4
class TestCalculeNbreHeuresTravailleesParJour:
    FONCTION = "calcule_nbre_heures_travailles_par_jour"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 2, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["exemple1.csv"])
        res = projet6.calcule_nbre_heures_travailles_par_jour(events, "lundi")
        assert isinstance(res, float), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type int")

    @pytest.mark.parametrize("data, jour, attendu", [
        pytest.param("exemple1", "lundi", 10.0, id="quelques lundi"),
        pytest.param("exemple1", "mardi", 8.0, id="quelques mardi"),
        pytest.param("exemple1", "jeudi", 4.0, id="quelques jeudi"),
    ])
    def test_valeur_retour(self, datadir, data, jour, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        resultat = projet6.calcule_nbre_heures_travailles_par_jour(events, jour)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")



@pytest.mark.echeance4
class TestTraitement:
    FONCTION = "traitement"

    # ---
    def test_declaration_fonction(self):
        message = "La fonction {}.{} doit être déclarée".format(MODULE, self.FONCTION)
        liste = inspect.getmembers(projet6)
        assert self.FONCTION in [liste[i][0] for i in range(len(liste))], \
            tools_tests.affiche_message_erreur(message)

    # ---
    def test_nombre_parametres(self):
        """Teste le nombre de paramètres de la fonction"""
        message = "La fonction {}.{} doit avoir {} paramètre".format(MODULE, self.FONCTION, 2)
        fct = tools_introspection.get_fonction_from_module(self.FONCTION, projet6)
        assert len(inspect.signature(fct).parameters) == 3, \
            tools_tests.affiche_message_erreur(message)

    # Tests du type de la valeur de retour
    def test_type_valeur_retour(self, datadir):
        events = tools_tests.lecture_lignes_fichier_csv(datadir["B1G1.csv"])
        print("----------------->",events, "<---------------------")
        res = projet6.traitement(events, "B1G1", "S1")
        assert isinstance(res, list), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list")
        assert isinstance(res[0], str), \
            tools_tests.affiche_message_erreur("La valeur de retour doit être de type list de str")

    @pytest.mark.parametrize("data, groupe, semestre, attendu", [
        pytest.param("B1G1", "B1G1", "S1", "B1G1_S1", id="B1G1_S1"),
        pytest.param("B1G2", "B1G2", "S1", "B1G2_S1", id="B1G2_S1"),
        pytest.param("B2GA", "B2GA", "S3", "B2GA_S3", id="B2GA_S3"),
    ])
    def test_valeur_retour(self, datadir, data, groupe, semestre, attendu):
        events = tools_tests.lecture_lignes_fichier_csv(datadir[f"{data}.csv"])
        attendu = tools_tests.lecture_lignes_fichier_csv(datadir[f"_expected/{attendu}.csv"])
        resultat = projet6.traitement(events, groupe, semestre)
        assert resultat == attendu, \
            tools_tests.affiche_message_erreur("La valeur de retour ne correspond pas")
