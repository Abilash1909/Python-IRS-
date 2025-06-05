from log_parser import lire_log, extraire_ips_failed_password, compter_ips
from data_analyzer import convertir_en_dataframe, afficher_top, tracer_graphique

# Chemin du fichier log
chemin = r"C:\Users\abila\Desktop\Python IRS\auth.log"

# Étape 1 : Lecture et extraction
lignes = lire_log(chemin)
ips = extraire_ips_failed_password(lignes)
compteur = compter_ips(ips)

# Étape 2 : Traitement avec pandas
df = convertir_en_dataframe(compteur)
afficher_top(df, n=5)

# Étape 3 : Visualisation
tracer_graphique(df, n=5)
