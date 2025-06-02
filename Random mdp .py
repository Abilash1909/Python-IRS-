import random
import string

def generer_mot_de_passe(taille=12):
    if taille < 12:
        print("Erreur : la longueur minimale est de 12 caractères.")
        return None

    # Au moins un de chaque
    maj = random.choice(string.ascii_uppercase)
    min = random.choice(string.ascii_lowercase)
    chiffre = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Le reste des caractères
    autres_caracteres = string.ascii_letters + string.digits + string.punctuation
    reste = [random.choice(autres_caracteres) for _ in range(taille - 4)]

    # Mélanger le tout
    mot_de_passe_liste = [maj, min, chiffre, special] + reste
    random.shuffle(mot_de_passe_liste)

    return ''.join(mot_de_passe_liste)

# Boucle utilisateur
while True:
    try:
        longueur = int(input("Entrez la longueur du mot de passe (minimum 12) : "))
        mot_de_passe = generer_mot_de_passe(longueur)
        if mot_de_passe:
            print("Mot de passe généré :", mot_de_passe)
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

