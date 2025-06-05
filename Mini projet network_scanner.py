import socket

def scanner_ports(ip, ports=[22, 80, 443], timeout=1):
    """
    Scanner les ports spécifiés sur une IP donnée.
    Retourne un dictionnaire {port: True/False} selon qu’il est ouvert ou non.
    """
    resultat = {}
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            code = sock.connect_ex((ip, port))
            resultat[port] = (code == 0)
            sock.close()
        except:
            resultat[port] = False
    return resultat

def afficher_resultats_scan(ip, resultat):
    """
    Affiche les résultats du scan pour une IP.
    """
    print(f"\n--- Résultat du scan pour {ip} ---")
    for port, ouvert in resultat.items():
        statut = "OUVERT" if ouvert else "fermé"
        print(f"Port {port} : {statut}")

# ========================
# Partie interactive (exécution directe)
# ========================
if __name__ == "__main__":
    print("Bienvenue dans le scanner de ports Python.")
    ip_cible = input("Tapez l’adresse IP à analyser : ").strip()

    ports_test = [22, 80, 443]  # Ports standards : SSH, HTTP, HTTPS
    print(f"\nAnalyse des ports {ports_test} en cours sur {ip_cible}...")

    resultats = scanner_ports(ip_cible, ports=ports_test)
    afficher_resultats_scan(ip_cible, resultats)
