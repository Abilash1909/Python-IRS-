import psutil
import os
import time
import platform
import csv
from datetime import datetime

# ───── Partie 1 : Test des fonctions psutil ─────
def test_psutil_functions():
    print("=== Découverte des fonctions psutil ===")
    print("CPU % :", psutil.cpu_percent(interval=1))
    print("Mémoire :", psutil.virtual_memory())
    print("Disque / :", psutil.disk_usage('/'))
    print("Réseau :", psutil.net_io_counters())
    input("\nAppuyez sur Entrée pour passer au tableau de bord...")

# ───── Utilitaire : effacer l'écran ─────
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# ───── Barre ASCII ─────
def ascii_bar(percentage, length=30):
    filled = int(length * percentage / 100)
    return '█' * filled + '-' * (length - filled)

# ───── Sauvegarde CSV ─────
def save_to_csv(cpu, mem_used, mem_avail, net_sent, net_recv):
    with open("system_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().isoformat(),
            cpu,
            mem_used,
            mem_avail,
            net_sent,
            net_recv
        ])

# ───── Tableau de bord ─────
def display_dashboard():
    try:
        while True:
            clear_screen()
            print("=" * 50)
            print("🖥️  TABLEAU DE BORD - MÉTRIQUES SYSTÈME")
            print("=" * 50)

            # CPU
            print("\n[UTILISATION CPU]")
            cpu_percents = psutil.cpu_percent(percpu=True)
            for i, p in enumerate(cpu_percents):
                print(f"  Cœur {i+1:2}: {p:5.1f}% | {ascii_bar(p)}")
            total_cpu = psutil.cpu_percent()
            print(f"  Total    : {total_cpu:5.1f}% | {ascii_bar(total_cpu)}")

            # Mémoire
            mem = psutil.virtual_memory()
            print("\n[MÉMOIRE RAM]")
            print(f"  Totale   : {mem.total // (1024**2)} Mo")
            print(f"  Utilisée : {mem.used // (1024**2)} Mo")
            print(f"  Disponible : {mem.available // (1024**2)} Mo")

            # Disque
            print("\n[UTILISATION DISQUE]")
            for part in psutil.disk_partitions():
                try:
                    usage = psutil.disk_usage(part.mountpoint)
                    print(f"  {part.device} ({part.mountpoint}): {usage.percent}% utilisé")
                except PermissionError:
                    continue

            # Réseau global
            net = psutil.net_io_counters()
            print("\n[ACTIVITÉ RÉSEAU]")
            print(f"  Octets envoyés : {net.bytes_sent // 1024} Ko")
            print(f"  Octets reçus   : {net.bytes_recv // 1024} Ko")

            # Réseau par interface
            print("\n[INTERFACES RÉSEAU]")
            net_per_iface = psutil.net_io_counters(pernic=True)
            for iface, stats in net_per_iface.items():
                print(f"  {iface}: Envoyés = {stats.bytes_sent // 1024} Ko | Reçus = {stats.bytes_recv // 1024} Ko")

            # Température CPU (Bonus 1)
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if temps:
                    print("\n[TEMPÉRATURE CPU]")
                    for name, entries in temps.items():
                        for entry in entries:
                            print(f"  {name} - {entry.label or 'core'} : {entry.current} °C")

            # Bonus 3 : export CSV
            save_to_csv(
                total_cpu,
                mem.used,
                mem.available,
                net.bytes_sent,
                net.bytes_recv
            )

            # Quitter
            print("\nTapez 'quit' pour quitter ou attendez 5 secondes...")
            print(">>> ", end='', flush=True)
            try:
                # Entrée utilisateur avec timeout
                import sys, select
                i, _, _ = select.select([sys.stdin], [], [], 5)
                if i:
                    if sys.stdin.readline().strip().lower() == "quit":
                        break
            except KeyboardInterrupt:
                break

    except KeyboardInterrupt:
        print("\nArrêté par l'utilisateur.")

# ───── Main ─────
if __name__ == "__main__":
    test_psutil_functions()
    # En-tête CSV
    if not os.path.exists("system_log.csv"):
        with open("system_log.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Horodatage", "CPU (%)", "RAM utilisée", "RAM dispo", "Octets envoyés", "Octets reçus"])
    display_dashboard()
