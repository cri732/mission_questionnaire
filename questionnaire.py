# Import de json pour charger les fichiers de questionnaires générés avec script import
import json


class Question:
    def __init__(self, titre, choix, bonne_reponse):
        self.titre = titre
        self.choix = choix
        self.bonne_reponse = bonne_reponse

<<<<<<< HEAD
    def from_json_data(data):
=======
    def FromJsonData(data):
>>>>>>> 287dc095d9bdd15889f3835fab3bb0c15a89b036
        # Définir les choix de réponses
        choix = [i[0] for i in data["choix"]]
        # Définir la bonne réponse
        bonne_reponse = [i[0] for i in data["choix"] if i[1] == True]
        # Gestion erreur s'il y a plusieurs bonnes réponses ou s'il n'y en a aucune
        if len(bonne_reponse) != 1:
            return None
        question = Question(data["titre"], choix, bonne_reponse[0])
        return question

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)


class Questionnaire:
    def __init__(self, questions, categorie, titre, difficulte):
        self.questions = questions
        self.categorie = categorie
        self.titre = titre
        self.difficulte = difficulte

    def from_json_data(data):
        # Récupérer les questions
        questionnaire_data_questions = data["questions"]
        # Mise en forme des questions
        questions = [Question.from_json_data(i) for i in questionnaire_data_questions]
        return Questionnaire(questions, data["categorie"], data["titre"], data["difficulte"])


    def lancer(self):
        score = 0
        # Afficher infos questionnaire
        print("----------")
        print(f"QUESTIONNAIRE: {self.titre}")
        print(f"    Catégorie: {self.categorie}")
        print(f"    Difficulté: {self.difficulte}")
        print(f"    Nombre de questions: {len(self.questions)}")
        print("----------")
        for question in self.questions:
            if question.poser():
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score


<<<<<<< HEAD
# -------------------- PHASE TESTS : UN SEUL QUESTIONNAIRE --------------------
# # Tester première question
# # Charger un fichier json
# with open('animaux_leschats_debutant.json', "r", encoding="utf-8") as f:
#     questionnaire_data = json.load(f)
# # Récupérer les questions
# questionnaire_data_questions = questionnaire_data["questions"]
# # Mise en forme de la question
# question = Question.from_json_data(questionnaire_data_questions[0])
# # Poser une seule question
# question.poser()

# Tester lancement questionnaire
# Charger un fichier json
with open('animaux_leschats_debutant.json', "r", encoding="utf-8") as f:
    questionnaire_data = json.load(f)
# Créer et lancer le questionnaire
Questionnaire.from_json_data(questionnaire_data).lancer()
print()
=======
"""questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)

# q1 = Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
# q1.poser()

# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)"""


# Questionnaire(
#     (
#     Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
#     Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
#     Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
#     )
# ).lancer()


# Charger un fichier json
with open('animaux_leschats_debutant.json', "r", encoding="utf-8") as f:
    questionnaire_data = json.load(f)
# Récupérer les questions
questionnaire_data_questions = questionnaire_data["questions"]
# Mise en forme de la question
question = Question.FromJsonData(questionnaire_data_questions[0])
# Poser une seule question
question.poser()
>>>>>>> 287dc095d9bdd15889f3835fab3bb0c15a89b036
