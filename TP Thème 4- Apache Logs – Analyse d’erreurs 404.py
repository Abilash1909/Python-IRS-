import re
import pandas as pd
import matplotlib.pyplot as plt

log_path = r"C:\Users\abila\Desktop\Python IRS\access.log"

# Nouveau regex adapté à TON format
log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<datetime>[^\]]+)\] '
    r'"(?P<method>\S+)\s(?P<url>\S+)\sHTTP/\d.\d" '
    r'(?P<status>\d{3}) "(?P<user_agent>[^"]*)"'
)

parsed_data = []
with open(log_path, 'r', encoding='utf-8', errors='ignore') as file:
    for line in file:
        match = log_pattern.match(line)
        if match:
            parsed_data.append(match.groupdict())

# Vérification et traitement
if not parsed_data:
    print("Erreur : aucune ligne reconnue dans le fichier.")
    exit()

df = pd.DataFrame(parsed_data)
df['status'] = pd.to_numeric(df['status'], errors='coerce')
df.dropna(subset=['status'], inplace=True)
df['status'] = df['status'].astype(int)

# Filtrer les erreurs 404
df_404 = df[df['status'] == 404]

# Top 5 IPs fautives
top_5 = df_404['ip'].value_counts().head(5)
print("Top 5 IPs avec erreurs 404 :")
print(top_5)

# Génération du graphique
output_img = r"C:\Users\abila\Desktop\Python IRS\top_5_ips_404.png"
plt.figure(figsize=(8, 5))
top_5.plot(kind='bar', color='red')
plt.title('Top 5 des IPs générant des erreurs 404')
plt.xlabel('Adresse IP')
plt.ylabel("Nombre d'erreurs 404")
plt.tight_layout()
plt.savefig(output_img)
plt.close()
print(f"Graphique enregistré ici : {output_img}")

# Détection de bots
bot_keywords = ['bot', 'crawler', 'spider']
df_bots = df_404[df_404['user_agent'].str.contains('|'.join(bot_keywords), case=False, na=False)]
percent_bot = round(len(df_bots) / len(df_404) * 100, 2) if len(df_404) > 0 else 0

print("IPs suspectes (bots détectés) :", df_bots['ip'].unique())
print("Pourcentage d'erreurs 404 causées par des bots :", percent_bot, "%")
