import re                                 # Pour les expressions régulières (regex)
from collections import Counter           # Pour compter les IPs rapidement
import matplotlib.pyplot as plt           # Pour créer des graphiques
import csv                                # Pour exporter au format CSV
import json                               # Pour exporter au format JSON

# -----------------------------------------------------------
# Étape 1 – Définir le chemin vers le fichier log
# Ici, le fichier se trouve dans un dossier sur le bureau
# On utilise une chaîne brute (r"...") pour éviter les erreurs de \ dans les chemins Windows
# -----------------------------------------------------------
chemin_fichier = r"C:\Users\abila\Desktop\Python IRS\auth.log"

# -----------------------------------------------------------
# Étape 2 – Lire toutes les lignes du fichier
# Chaque ligne représente une tentative de connexion
# -----------------------------------------------------------
with open(chemin_fichier, "r") as fichier:
    lignes = fichier.readlines()

# -----------------------------------------------------------
# Étape 3 – Définir une expression régulière pour extraire les adresses IP
# Format IP : 4 groupes de 1 à 3 chiffres séparés par des points (ex : 192.168.0.1)
# -----------------------------------------------------------
regex_ip = r"(\d{1,3}(?:\.\d{1,3}){3})"

# -----------------------------------------------------------
# Étape 4 – Parcourir les lignes et séparer :
# - les lignes d’échec de connexion ("Failed password")
# - les lignes de connexion réussie ("Accepted password")
# -----------------------------------------------------------
failed_ips = []   # Liste des IPs ayant échoué
success_ips = []  # Liste des IPs ayant réussi

for ligne in lignes:
    if "Failed password" in ligne:
        match = re.search(regex_ip, ligne)  # On cherche une IP dans la ligne
        if match:
            failed_ips.append(match.group(1))  # Ajouter l’IP trouvée à la liste des échecs
    elif "Accepted password" in ligne:
        match = re.search(regex_ip, ligne)  # On cherche une IP dans la ligne
        if match:
            success_ips.append(match.group(1))  # Ajouter l’IP trouvée à la liste des réussites

# -----------------------------------------------------------
# Étape 5 – Compter combien de fois chaque IP apparaît
# -----------------------------------------------------------
failed_counter = Counter(failed_ips)     # Nombre d’échecs par IP
success_counter = Counter(success_ips)   # Nombre de réussites par IP

# -----------------------------------------------------------
# Étape 6 – Sélectionner les 5 IPs avec le plus d’échecs
# .most_common(5) retourne une liste des 5 IPs les plus fréquentes
# -----------------------------------------------------------
top_failed = failed_counter.most_common(5)

# -----------------------------------------------------------
# Étape 7 – Extraire les IPs et leur nombre d’échecs pour les afficher dans un graphique
# -----------------------------------------------------------
ips = [ip for ip, _ in top_failed]
counts = [count for _, count in top_failed]

# -----------------------------------------------------------
# Étape 8 – Créer un graphique de barres avec matplotlib
# Chaque barre représente une IP et son nombre d’échecs
# -----------------------------------------------------------
plt.figure(figsize=(10, 6))  # Taille de la figure
plt.bar(ips, counts, color='red')  # Barres rouges pour les échecs
plt.xlabel("Adresse IP")  # Nom de l’axe X
plt.ylabel("Nombre d’échecs")  # Nom de l’axe Y
plt.title("Top 5 des IPs ayant échoué à se connecter")  # Titre du graphique
plt.grid(True, linestyle='--', axis='y')  # Afficher une grille horizontale
plt.tight_layout()  # Ajuster les marges automatiquement
plt.show()  # Afficher le graphique

# -----------------------------------------------------------
# Étape 9 – BONUS : Comparer les IPs ayant échoué et celles ayant réussi
# -----------------------------------------------------------
print("\nComparaison des IPs (échecs vs réussites) :")
for ip in set(failed_counter.keys()).union(success_counter.keys()):
    print(f"{ip} - Échecs : {failed_counter.get(ip, 0)} | Réussites : {success_counter.get(ip, 0)}")

# -----------------------------------------------------------
# Étape 10 – BONUS : Exporter les résultats dans un fichier CSV
# Le fichier contiendra : IP, nombre d’échecs, nombre de réussites
# -----------------------------------------------------------
csv_path = r"C:\Users\abila\Desktop\Python IRS\resultats_ips.csv"
with open(csv_path, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["IP", "Echecs", "Reussites"])  # En-tête
    for ip in set(failed_counter.keys()).union(success_counter.keys()):
        writ
