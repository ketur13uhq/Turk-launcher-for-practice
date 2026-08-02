import os
import urllib.parse
import webbrowser

RESET = chr(27) + '[0m'
VERT = chr(27) + '[92m'
JAUNE = chr(27) + '[93m'
ROUGE = chr(27) + '[91m'
CYAN = chr(27) + '[96m'
MAGENTA = chr(27) + '[95m'
BLEU = chr(27) + '[94m'
BLANC = chr(27) + '[97m'
ORANGE = chr(27) + '[38;5;208m'

TITRE = r"""
 _______ _    _ _____  _  __
|__   __| |  | |  __ \| |/ /
   | |  | |  | | |__) | ' /
   | |  | |  | |  _  /|  <
   | |  | |__| | | \ \| . \
   |_|   \____/|_|  \_\_|\_\
"""

MESSAGE_ACCUEIL = "Salut, je viens d'ouvrir cette conversation via mon menu perso. Je n'ai pas encore de question precise, demande-moi sur quoi j'ai besoin d'aide."
CHATGPT_URL = "https://chat.openai.com/?q=" + urllib.parse.quote(MESSAGE_ACCUEIL)


# ============================================================
#  CATEGORIES. Chaque section : (titre, couleur, {nom: url})
#  Les numeros s'enchainent automatiquement entre sections.
# ============================================================
CATEGORIES = [
    ("ASSISTANT IA", VERT, {
        "Claude ~": "https://claude.ai",
        "ChatGPT ~": CHATGPT_URL,
        "Grok ~": "https://grok.com",
        "Gemini ~": "https://gemini.google.com",
    }),
    ("APPRENDRE A CODER", CYAN, {
        "freeCodeCamp": "https://www.freecodecamp.org",
        "Codecademy ~": "https://www.codecademy.com",
        "OpenClassrooms ~": "https://openclassrooms.com",
        "W3Schools": "https://www.w3schools.com",
    }),
    ("APPRENDRE PYTHON", ORANGE, {
        "Learn Python": "https://www.learnpython.org",
        "CS50 Python (Harvard)": "https://cs50.harvard.edu/python/",
        "Real Python ~": "https://realpython.com",
        "Sololearn Python ~": "https://www.sololearn.com/learning/1073",
    }),
    ("DOCUMENTATION", MAGENTA, {
        "Python Docs": "https://docs.python.org/3/",
        "MDN Web Docs": "https://developer.mozilla.org",
        "Stack Overflow": "https://stackoverflow.com",
        "GitHub Docs": "https://docs.github.com",
    }),
    ("OUTILS DEV", BLEU, {
        "GitHub ~": "https://github.com",
        "Replit ~": "https://replit.com",
        "CodePen ~": "https://codepen.io",
        "Regex101": "https://regex101.com",
    }),
    ("SUGGESTIONS & SUIVI", ROUGE, {
        "TikTok (@turk13uhq)": "https://www.tiktok.com/@turk13uhq",
    }),
]

EDITEURS_ANDROID = ("EDITEURS", JAUNE, {
    "Pydroid3 ~": "https://play.google.com/store/apps/details?id=ru.iiec.pydroid3",
    "Acode": "https://play.google.com/store/apps/details?id=com.foxdebug.acode",
    "Termux": "https://f-droid.org/en/packages/com.termux/",
    "QPython": "https://play.google.com/store/apps/details?id=org.qpython.qpy3",
})

EDITEURS_IOS = ("EDITEURS", JAUNE, {
    "a-Shell": "https://apps.apple.com/app/a-shell/id1473805438",
    "Carnets": "https://apps.apple.com/app/carnets-jupyter/id1450994949",
    "iSH Shell": "https://apps.apple.com/app/ish-shell/id1436902243",
})


def clear():
    # os.system('clear') et les codes ANSI ne marchent pas sur tous les
    # terminaux (ex: la console integree d'Acode les ignore parfois).
    # On ajoute donc un filet de securite qui marche PARTOUT : pousser
    # l'ancien contenu hors de l'ecran avec des lignes vides (mais pas
    # trop, sinon le nouveau texte se retrouve trop bas / hors ecran).
    print(chr(27) + "[2J" + chr(27) + "[H", end='')
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 30)


def afficher_titre_centre(largeur=40):
    lignes = TITRE.strip('\n').split('\n')
    largeur_max = max(len(l) for l in lignes)
    espace = max(0, (largeur - largeur_max) // 2)
    for l in lignes:
        print(ROUGE + (' ' * espace) + l + RESET)


def afficher_titre(titre, couleur):
    print(couleur + "[ " + titre + " ]" + RESET)


def afficher_liste(noms, couleur, depart):
    for i, nom in enumerate(noms, depart):
        print(couleur + " [" + str(i) + "] " + RESET + nom)


def ligne_pointillee(couleur, longueur=40):
    print(couleur + '.' * longueur + RESET)


def afficher_page_aide():
    clear()
    afficher_titre_centre()
    print()
    ligne_pointillee(BLANC)
    print()
    print(VERT + "COMMENT UTILISER CE MENU" + RESET)
    print()
    print("1. Chaque ligne a un numero entre crochets, ex : [3] Grok")
    print("2. Tape ce numero puis appuie sur Entree")
    print("3. Le lien correspondant s'ouvre dans ton navigateur")
    print()
    print(JAUNE + "LES CATEGORIES" + RESET)
    print()
    print("- ASSISTANT IA : les IA conversationnelles (Claude, ChatGPT...)")
    print("- EDITEURS : les applis pour coder sur ton telephone")
    print("- APPRENDRE A CODER : des sites gratuits pour debuter")
    print("- APPRENDRE PYTHON : des sites 100% centres sur le Python")
    print("- DOCUMENTATION : ou chercher quand t'es bloque sur du code")
    print("- OUTILS DEV : des sites utiles pour coder au quotidien")
    print("- SUGGESTIONS & SUIVI : mon TikTok, pour proposer des idees")
    print()
    print(CYAN + "LES SYMBOLES" + RESET)
    print()
    print("- Rien apres le nom = 100% gratuit")
    print("- ~ apres le nom = gratuit avec option payante (freemium)")
    print()
    print(MAGENTA + "A SAVOIR" + RESET)
    print()
    print("- Il te faut une connexion internet pour ouvrir les liens")
    print("- Certains liens demandent d'etre deja connecte au service")
    print("- Si un lien ne s'ouvre pas, il s'affiche en texte a copier")
    print()
    ligne_pointillee(BLANC)
    input("Appuie sur Entree pour revenir au menu...")


def ouvrir(nom, url):
    print("Ouverture de " + nom + " : " + url)
    try:
        webbrowser.open(url)
    except Exception:
        print("Impossible d'ouvrir automatiquement, copie ce lien : " + url)
    input("Appuie sur Entree pour continuer...")


def choisir_os():
    clear()
    afficher_titre_centre()
    print()
    print("Tu es sur quel systeme ?")
    print("[1] Android")
    print("[2] iOS")
    while True:
        choix = input(">> ").strip()
        if choix == '1':
            return EDITEURS_ANDROID
        elif choix == '2':
            return EDITEURS_IOS
        print("wsh t'es dyslexique ou quoi mdr")


def menu():
    editeurs = choisir_os()
    categories = CATEGORIES[:1] + [editeurs] + CATEGORIES[1:]

    while True:
        clear()
        afficher_titre_centre()
        print()
        ligne_pointillee(BLANC)
        print()

        compteur = 1
        # on garde en memoire a quel numero correspond quel item
        table_numeros = {}
        for titre, couleur, items in categories:
            noms = list(items.keys())
            afficher_titre(titre, couleur)
            afficher_liste(noms, couleur, compteur)
            for nom in noms:
                table_numeros[compteur] = (nom, items[nom])
                compteur += 1
            print()

        ligne_pointillee(BLANC)
        print(BLANC + "~ = freemium   (rien = gratuit)" + RESET)
        print("Tape un numero (ou 'aide')")
        choix = input(">> ").strip()

        if choix.lower() == 'aide':
            afficher_page_aide()
            continue

        try:
            num = int(choix)
        except ValueError:
            print("wsh t'es dyslexique ou quoi mdr")
            input("Appuie sur Entree pour continuer...")
            continue

        if num in table_numeros:
            nom, url = table_numeros[num]
            ouvrir(nom, url)
        else:
            print("wsh t'es dyslexique ou quoi mdr")
            input("Appuie sur Entree pour continuer...")


if __name__ == '__main__':
    menu()
