import csv

def charger_brawlers():
    brawlers = []
    colonnes_numeriques = ["Movement Speed", "Max health", "Attack Range", "Attack Damage", "Projectile Speed"]
    with open("info.csv", newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        for index, ligne in enumerate(lecteur, start=2):
            propre = {}
            ligne_valide = True
            for cle, val in ligne.items():
                if val is None:
                    ligne_valide = False
                    break
                val = val.strip().replace('O', '0')
                if cle in colonnes_numeriques:
                    try:
                        propre[cle.strip()] = float(val)
                    except ValueError:
                        ligne_valide = False
                        break
                else:
                    propre[cle.strip()] = val
            if ligne_valide:
                brawlers.append(propre)
    return brawlers

def sauvegarder_brawlers(brawlers, nom_fichier):
    with open(nom_fichier, "w", newline='') as f:
        titres = brawlers[0].keys()
        writer = csv.DictWriter(f, fieldnames=titres)
        writer.writeheader()
        writer.writerows(brawlers)

def ajouter_brawler():
    brawler = {
        "Brawler": input("Nom du Brawler : "),
        "Rarity": input("Rareté : "),
        "Tier": input("Tier : "),
        "Movement Speed": input("Vitesse de déplacement : "),
        "Max health": input("Santé maximale : "),
        "Attack Range": input("Portée d'attaque : "),
        "Attack Damage": input("Dégâts d'attaque : "),
        "Projectile Speed": input("Vitesse du projectile : ")
    }
    try:
        with open("info.csv", "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=brawler.keys())
            writer.writerow(brawler)
        print("Brawler ajouté avec succès.")
    except Exception as e:
        print("Erreur lors de l'ajout :", e)

def supprimer_brawler():
    nom = input("Nom du Brawler à supprimer : ").strip().lower()
    brawlers = charger_brawlers()
    nouveaux = [b for b in brawlers if b["Brawler"].strip().lower() != nom]
    if len(nouveaux) == len(brawlers):
        print("Aucun Brawler trouvé avec ce nom.")
    else:
        sauvegarder_brawlers(nouveaux, "info.csv")
        print("Brawler supprimé avec succès.")

def trier_brawler():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Brawler"].lower() > valeur["Brawler"].lower():
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Brawler.csv")

def trier_rarity():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Rarity"].lower() > valeur["Rarity"].lower():
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Rarity.csv")

def trier_tier():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Tier"].upper() > valeur["Tier"].upper():
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Tier.csv")

def trier_movement_speed():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Movement Speed"] > valeur["Movement Speed"]:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Movement_Speed.csv")

def trier_max_health():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Max health"] > valeur["Max health"]:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Max_health.csv")

def trier_attack_range():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Attack Range"] > valeur["Attack Range"]:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Attack_Range.csv")

def trier_projectile_speed():
    brawlers = charger_brawlers()
    for i in range(1, len(brawlers)):
        valeur = brawlers[i]
        j = i - 1
        while j >= 0 and brawlers[j]["Projectile Speed"] > valeur["Projectile Speed"]:
            brawlers[j + 1] = brawlers[j]
            j -= 1
        brawlers[j + 1] = valeur
    sauvegarder_brawlers(brawlers, "trie_Projectile_Speed.csv")

def trier_attack_damage():
    brawlers = charger_brawlers()
    for i in range(len(brawlers) - 1):
        min_i = i
        for j in range(i + 1, len(brawlers)):
            if brawlers[j]["Attack Damage"] < brawlers[min_i]["Attack Damage"]:
                min_i = j
        brawlers[i], brawlers[min_i] = brawlers[min_i], brawlers[i]
    sauvegarder_brawlers(brawlers, "trie_Attack_Damage.csv")

def rechercher_brawler():
    nom = input("Nom du Brawler à rechercher : ").strip().lower()
    brawlers = charger_brawlers()
    trouve = False
    for b in brawlers:
        if b["Brawler"].strip().lower() == nom:
            print("\n--- Brawler trouvé ---")
            for cle, val in b.items():
                print(f"{cle} : {val}")
            trouve = True
            break
    if not trouve:
        print("Aucun Brawler trouvé avec ce nom.")
