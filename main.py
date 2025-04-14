import csv

def charger_brawlers():
    with open("info.csv", newline='') as fichier:
        lecteur = csv.DictReader(fichier)
        brawlers = list(lecteur)
    for i in range(len(brawlers)):
        propre = {}
        for cle, val in brawlers[i].items():
            propre[cle.strip()] = val.strip()
        brawlers[i] = propre
    return brawlers

def sauvegarder_brawlers(brawlers, nom_fichier):
    with open(nom_fichier, "w", newline='') as f:
        titres = brawlers[0].keys()
        writer = csv.DictWriter(f, fieldnames=titres)
        writer.writeheader()
        writer.writerows(brawlers)

# Tri par Brawler (alphabétique)
def trier_brawler():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = b["Brawler"].lower()
        j = i - 1
        while j >= 0 and brawlers[j]["Brawler"].lower() < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Brawler.csv")

# Tri par Rarity (alphabétique)
def trier_rarity():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = b["Rarity"].lower()
        j = i - 1
        while j >= 0 and brawlers[j]["Rarity"].lower() < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Rarity.csv")

# Tri par Tier (alphabétique)
def trier_tier():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = b["Tier"].upper()
        j = i - 1
        while j >= 0 and brawlers[j]["Tier"].upper() < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Tier.csv")

def trier_movement_speed():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = float(b["Movement Speed"])
        j = i - 1
        while j >= 0 and float(brawlers[j]["Movement Speed"]) < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Movement_Speed.csv")

def trier_max_health():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        try:
            v = float(b["Max health"].replace('O', '0'))
        except ValueError:
            continue
        j = i - 1
        while j >= 0 and float(brawlers[j]["Max health"].replace('O', '0')) < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Max_health.csv")

def trier_attack_range():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = float(b["Attack Range"])
        j = i - 1
        while j >= 0 and float(brawlers[j]["Attack Range"]) < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Attack_Range.csv")

def trier_attack_damage():
    brawlers = charger_brawlers()
    for i in range(len(brawlers)):
        max_i = i
        for j in range(i + 1, len(brawlers)):
            if float(brawlers[j]["Attack Damage"]) > float(brawlers[max_i]["Attack Damage"]):
                max_i = j
        brawlers[i], brawlers[max_i] = brawlers[max_i], brawlers[i]
    sauvegarder_brawlers(brawlers, "trie_Attack_Damage.csv")

def trier_projectile_speed():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        b = brawlers[i]
        v = float(b["Projectile Speed"])
        j = i - 1
        while j >= 0 and float(brawlers[j]["Projectile Speed"]) < v:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = b
    sauvegarder_brawlers(brawlers, "trie_Projectile_Speed.csv")
