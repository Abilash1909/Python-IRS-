import pandas as pd              # Pour manipuler des tableaux de données
import matplotlib.pyplot as plt  # Pour générer des graphiques

def convertir_en_dataframe(compteur_ip):
    """
    Convertit un dictionnaire {IP: nombre} en DataFrame pandas.
    Cela permet de trier, filtrer, et visualiser les données.
    """
    df = pd.DataFrame(compteur_ip.items(), columns=["IP", "Nombre d'échecs"])
    df = df.sort_values(by="Nombre d'échecs", ascending=False)
    return df

def afficher_top(df, n=5):
    """
    Affiche les n premières lignes du DataFrame (Top IPs).
    """
    print(f"\n--- Top {n} des adresses IP ---")
    print(df.head(n).to_string(index=False))

def tracer_graphique(df, n=5):
    """
    Trace un graphique en barres des n IPs les plus fréquentes.
    """
    top_n = df.head(n)

    plt.figure(figsize=(10, 6))  # Taille du graphique
    plt.bar(top_n["IP"], top_n["Nombre d'échecs"], color='darkred')
    plt.title(f"Top {n} des IPs ayant échoué à se connecter", fontsize=14)
    plt.xlabel("Adresse IP", fontsize=12)
    plt.ylabel("Nombre d’échecs", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
