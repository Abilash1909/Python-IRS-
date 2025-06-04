import socket
from concurrent.futures import ThreadPoolExecutor
import csv

def scan_port(ip, port, timeout=1):
    """Tente de se connecter à un port TCP sur une IP donnée avec un délai d'attente."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))  # 0 si le port est ouvert
            return (port, result == 0)
    except Exception:
        return (port, False)

def main():
    print("=== Scanner de ports TCP ===")
    print("Ce programme vous permet de scanner une adresse IP sur une plage de ports.")
    
    # Demander à l'utilisateur l'adresse IP à scanner
    ip = input("Entrez l'adresse IP à scanner : ").strip()

    # Demander les bornes de la plage de ports
    try:
        start_port = int(input("Port de début : "))
        end_port = int(input("Port de fin : "))
    except ValueError:
        print("Erreur : Les ports doivent être des nombres entiers.")
        return

    # Demander si l'utilisateur souhaite voir aussi les ports fermés
    verbose_input = input("Souhaitez-vous afficher les ports fermés également ? (o/n) : ").lower()
    verbose = verbose_input == "o"

    print(f"\nLancement du scan sur {ip} de port {start_port} à {end_port}...\n")

    results = []

    # Utilisation de threads pour accélérer le scan
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port, is_open = future.result()
            if is_open:
                print(f"[OUVERT] Port {port}")
                results.append((port, "ouvert"))
            elif verbose:
                print(f"[FERMÉ] Port {port}")
                results.append((port, "fermé"))

    # Enregistrement des résultats dans un fichier CSV
    output_path = r"C:\Users\abila\Desktop\Python IRS\TP3.csv"
    try:
        with open(output_path, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Port", "Statut"])
            writer.writerows(results)
        print(f"\nRésultats enregistrés dans le fichier : {output_path}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")

if __name__ == "__main__":
    main()
