import re

# Expression régulière stricte pour les adresses IPv4
regex_ip = re.compile(
    r'^('
    r'(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}'
    r'(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})$'
)

def est_adresse_ip(valeur):
    # Vérifie le format général avec regex
    if not regex_ip.match(valeur):
        return False

    # Rejeter les octets avec des zéros en trop
    parties = valeur.split('.')
    for part in parties:
        if len(part) > 1 and part.startswith('0'):
            return False
    return True

# Boucle interactive
while True:
    ip = input("Entrez une adresse IP (ou tapez 'exit' pour quitter) : ")
    if ip.lower() == 'exit':
        break
    if est_adresse_ip(ip):
        print(f"{ip} est une adresse IP VALIDE ;) ")
    else:
        print(f"{ip} est une adresse IP INVALIDE :'( ")
