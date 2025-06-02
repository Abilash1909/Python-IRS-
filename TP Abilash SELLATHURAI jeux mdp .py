import random
import os

# Fonction pour charger les mots depuis un fichier s'il existe
def charger_mots_de_passe():
    if os.path.exists("mots_de_passe.txt"):
        with open("mots_de_passe.txt", "r") as f:
            return [ligne.strip() for ligne in f if ligne.strip()]
    else:
        return [
            "123456", "password", "admin", "123456789",
            "qwerty", "abc123", "letmein", "welcome",
            "monkey", "football"
        ]

# 1. Charger ou définir la liste
mots_de_passe_faibles = charger_mots_de_passe()

# 2. Choisir un mot de passe aléatoire
mot_de_passe = random.choice(mots_de_passe_faibles)

# 3. Paramètres bonus
max_essais = int(input("Nombre maximum d'essais ? (0 = illimité) : "))
triche = input("Activer le mode triche ? (o/n) : ").lower() == "o"
if triche:
    print(f"[TRICHE] Le mot de passe est : {mot_de_passe}")

# 4. Initialisation
essais = 0
historique = []

print("Devine le mot de passe parmi les plus utilisés.")

# 5. Boucle principale
while True:
    proposition = input("Ta proposition : ")
    essais += 1
    historique.append(proposition)

    if proposition == mot_de_passe:
        print(f"\nMot de passe trouvé en {essais} essais. Bravo !")
        break

    # Indices
    print("Mot de passe incorrect.")
    if len(proposition) < len(mot_de_passe):
        print("Indice : le mot de passe est plus long.")
    elif len(proposition) > len(mot_de_passe):
        print("Indice : le mot de passe est plus court.")

    if proposition and mot_de_passe.startswith(proposition[0]):
        print("Indice : le mot de passe commence par la même lettre.")

    lettres_communes = set(proposition) & set(mot_de_passe)
    print(f"Lettres communes : {', '.join(lettres_communes)}")

    # Vérification de la limite d'essais
    if max_essais > 0 and essais >= max_essais:
        print(f"\nTu as atteint le nombre maximum d'essais. Le mot de passe était : {mot_de_passe}")
        break

# 6. Affichage de l'historique
print("\nHistorique des tentatives :")
for i, tentative in enumerate(historique, 1):
    print(f"{i}. {tentative}")
