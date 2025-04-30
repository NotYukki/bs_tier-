import main

def menu():
    " Afficahge graphique qui donne tout les fonction de main.py affichage graphique imh consolle"
    while True:
        print("\n--- MENU DE GESTION DES BRAWLERS ---")
        print("1. Trier par Movement Speed")
        print("2. Trier par Attack Damage")
        print("3. Trier par Max Health")
        print("4. Trier par Brawler")
        print("5. Trier par Rarity")
        print("6. Trier par Tier")
        print("7. Trier par Attack Range")
        print("8. Trier par Projectile Speed")
        print("9. Ajouter un Brawler")
        print("10. Supprimer un Brawler")
        print("11. Quitter")
        print("12. Rechercher un perso")
        print("13. Perso aléatoire")
        print("14 jouer au quizz")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            main.trier_movement_speed()
            print("Tri par Movement Speed terminé.")
        elif choix == "2":
            main.trier_attack_damage()
            print("Tri par Attack Damage terminé.")
        elif choix == "3":
            main.trier_max_health()
            print("Tri par Max Health terminé.")
        elif choix == "4":
            main.trier_brawler()
            print("Tri par Brawler terminé.")
        elif choix == "5":
            main.trier_rarity()
            print("Tri par Rarity terminé.")
        elif choix == "6":
            main.trier_tier()
            print("Tri par Tier terminé.")
        elif choix == "7":
            main.trier_attack_range()
            print("Tri par Attack Range terminé.")
        elif choix == "8":
            main.trier_projectile_speed()
            print("Tri par Projectile Speed terminé.")
        elif choix == "9":
            main.ajouter_brawler()
        elif choix == "10":
            main.supprimer_brawler()
        elif choix == "12":
            main.rechercher_brawler()
        elif choix == "11":
            print("Au revoir !")
            print("Merci d'avoir utilisé notre programme de tri des Brawlers.")
            break
        elif choix == "13":
            main.brawler_aleatoire()
        elif choix == "14":
            main.quizz_brawler()

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
