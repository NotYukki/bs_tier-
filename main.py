import csv


def charger_brawlers():
    "Cette fonction est une dérivé de  notre fonction de base qui corrige les erreurs de 0 et O car on en avait bcp trop" 
    brawlers = []
    colonnes_numeriques = ["Movement Speed", "Max health", "Attack Range", "Attack Damage", "Projectile Speed"]
    
    with open("info.csv", newline='', encoding='utf-8') as fichier:
        lecteur = csv.DictReader(fichier)
        
        for index, ligne in enumerate(lecteur, start=2):  # start=2 pour sauter l'en-tête (ligne 1)
            propre = {}
            ligne_valide = True

            for cle, val in ligne.items():
                if val is None:
                    print(f"[Erreur] Valeur manquante ligne {index}, colonne '{cle}'")
                    ligne_valide = False
                    break

                val = val.strip().replace('O', '0')  # Corrige les erreurs comme "52O0" → "5200"
                if cle in colonnes_numeriques:
                    try:
                        propre[cle.strip()] = float(val)
                    except ValueError:
                        print(f"[Erreur] Conversion impossible ligne {index}, colonne '{cle}': '{val}'")
                        ligne_valide = False
                        break
                else:
                    propre[cle.strip()] = val

            if ligne_valide:
                brawlers.append(propre)
            else:
                print(f"[Ignorée] Ligne {index} incorrecte : {ligne}")

    return brawlers


def sauvegarder_brawlers(brawlers, nom_fichier):
    "Fonction pour sauvergarder un perso spécifique" 
    with open(nom_fichier, "w", newline='') as f:
        titres = brawlers[0].keys()
        writer = csv.DictWriter(f, fieldnames=titres)
        writer.writeheader()
        writer.writerows(brawlers)

def ajouter_brawler():
    "Ajouter un perso dans le fichier csv elle demande à l'utilisateur toute les colonnes" 
    brawler = {}
    brawler["Brawler"] = input("Nom du Brawler : ")
    brawler["Rarity"] = input("Rareté : ")
    brawler["Tier"] = input("Tier : ")
    brawler["Movement Speed"] = input("Vitesse de déplacement : ")
    brawler["Max health"] = input("Santé maximale : ")
    brawler["Attack Range"] = input("Portée d'attaque : ")
    brawler["Attack Damage"] = input("Dégâts d'attaque : ")
    brawler["Projectile Speed"] = input("Vitesse du projectile : ")

    try:
        with open("info.csv", "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=brawler.keys())
            writer.writerow(brawler)
        print("Brawler ajouté avec succès.")
    except Exception as e:
        print("Erreur lors de l'ajout :", e)

def supprimer_brawler():
    "suprrimer le perso mais si il n y est pas ne rien suprimer" 
    nom = input("Nom du Brawler à supprimer : ").strip().lower()
    brawlers = charger_brawlers()
    nouveaux = [b for b in brawlers if b["Brawler"].strip().lower() != nom]

    if len(nouveaux) == len(brawlers):
        print("Aucun Brawler trouvé avec ce nom.")
    else:
        sauvegarder_brawlers(nouveaux, "info.csv")
        print("Brawler supprimé avec succès.")

def trier_brawler():
    "Trie des perso en fonction de le ordre alphabétique"
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

def trier_rarity():
    "trier par leur tier" 
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

def trier_tier():
    "trier par tier list"
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
    "par vitesse" 
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
