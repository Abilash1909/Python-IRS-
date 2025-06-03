# Import des bibliothèques nécessaires
import re  # Permet d'utiliser les expressions régulières (regex)
from collections import Counter  # Fournit une structure de données pour compter les éléments

# ---------------------------------------------------------------------
# Étape 1 : Définir le chemin complet vers le fichier "auth.log"
# On utilise ici une chaîne brute (r"...") pour éviter les erreurs dues aux antislashs (\)
# Exemple : \n, \t deviennent littéraux grâce au "r"
# ---------------------------------------------------------------------
chemin_fichier = r"C:\Users\abila\Desktop\Python IRS\auth.log"

# ---------------------------------------------------------------------
# Étape 2 : Ouvrir le fichier log en mode lecture ('r')
# .readlines() lit chaque ligne et les place dans une liste appelée "lignes"
# Chaque élément de cette liste correspond à une ligne du fichier
# ---------------------------------------------------------------------
with open(chemin_fichier, "r") as fichier:
    lignes = fichier.readlines()

# ---------------------------------------------------------------------
# Étape 3 : Filtrer uniquement les lignes contenant le texte "Failed password"
# Cela correspond aux tentatives de connexion SSH échouées
# On utilise une compréhension de liste pour parcourir chaque ligne
# ---------------------------------------------------------------------
lignes_failed = [ligne for ligne in lignes if "Failed password" in ligne]

# ---------------------------------------------------------------------
# Étape 4 : Définir une expression régulière (regex) pour extraire les adresses IP
# Le motif détecte les adresses IPv4 : 4 groupes de 1 à 3 chiffres séparés par des points
# Exemple : 192.168.0.1 ou 203.0.113.45
# ---------------------------------------------------------------------
regex_ip = r"(\d{1,3}(?:\.\d{1,3}){3})"

# ---------------------------------------------------------------------
# Étape 5 : Parcourir les lignes filtrées pour extraire les adresses IP
# - re.search() cherche un motif (IP) dans la ligne
# - Si un match est trouvé, on l’ajoute à une liste d’IPs
# ---------------------------------------------------------------------
ips = []  # Initialiser une liste vide pour stocker les IPs trouvées
for ligne in lignes_failed:
    match = re.search(regex_ip, ligne)  # Appliquer l'expression régulière à la ligne
    if match:  # Si une adresse IP est trouvée
        ips.append(match.group(1))  # Ajouter l'adresse IP à la liste

# ---------------------------------------------------------------------
# Étape 6 : Compter combien de fois chaque adresse IP apparaît
# - Counter transforme la liste d’IPs en un dictionnaire {IP: nombre_occurrences}
# - Utile pour identifier les IPs qui ont tenté plusieurs fois
# ---------------------------------------------------------------------
compteur = Counter(ips)

# ---------------------------------------------------------------------
# Étape 7 : Afficher les 5 IPs les plus fréquentes
# - .most_common(5) retourne les 5 adresses IP les plus présentes dans les échecs
# - On affiche leur nombre d’occurrences à l’écran
# ---------------------------------------------------------------------
print("Top 5 des IPs avec le plus d’échecs de connexion :")
for ip, nombre in compteur.most_common(5):
    print(f"{ip} : {nombre} fois")
