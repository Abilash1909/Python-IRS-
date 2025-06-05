import re
from collections import Counter

def lire_log(chemin_fichier):
    """
    Lire toutes les lignes d’un fichier log.
    """
    with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
        return fichier.readlines()

def extraire_ips_failed_password(lignes):
    """
    Extraire toutes les IPs dans les lignes contenant 'Failed password'.
    """
    regex_ip = r"(\d{1,3}(?:\.\d{1,3}){3})"
    ips = []

    for ligne in lignes:
        if "Failed password" in ligne:
            match = re.search(regex_ip, ligne)
            if match:
                ips.append(match.group(1))
    
    return ips

def compter_ips(ips):
    """
    Retourne un dictionnaire avec le nombre d’occurrences de chaque IP.
    """
    return dict(Counter(ips))

def afficher_resultats(compteur_ip):
    """
    Affiche les IPs triées par nombre décroissant d’occurrences.
    """
    print("\n--- Résultat : IPs avec le plus d’échecs ---")
    for ip, nb in sorted(compteur_ip.items(), key=lambda x: x[1], reverse=True):
        print(f"{ip} : {nb} fois")

# --- Zone de test / exécution ---
if __name__ == "__main__":
    chemin = r"C:\Users\abila\Desktop\Python IRS\auth.log"

    lignes = lire_log(chemin)
    ips = extraire_ips_failed_password(lignes)
    compteur = compter_ips(ips)
    afficher_resultats(compteur)
