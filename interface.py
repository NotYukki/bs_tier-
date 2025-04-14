import tkinter as tk
from tkinter import messagebox
import main  # ← on importe main.py

def lancer_tri_movement():
    main.trier_movement_speed()
    messagebox.showinfo("trop fort gg", "Tri par Mv Speed fini !")

def lancer_tri_attack():
    main.trier_attack_damage()
    messagebox.showinfo("Succès", "Tri par Damage terminé !")

def lancer_tri_health():
    main.trier_max_health()
    messagebox.showinfo("Succès", "Tri par Vie terminé !")

def lancer_tri_brawler():
    main.trier_brawler()
    messagebox.showinfo("Succès", "Tri par nom terminé !")

def lancer_tri_rarity():
    main.trier_rarity()
    messagebox.showinfo("Succès", "Tri par rareté terminé !")

def lancer_tri_tier():
    main.trier_tier()
    messagebox.showinfo("Succès", "Tri par tier terminé !")

def lancer_tri_range():
    main.trier_attack_range()
    messagebox.showinfo("Succès", "Tri par range terminé !")

def lancer_tri_projectile():
    main.trier_projectile_speed()
    messagebox.showinfo("Succès", "Tri par projectile speed terminé !")

fenetre = tk.Tk()
fenetre.title("Tri Brawlers - IMH")
fenetre.geometry("350x400")

tk.Button(fenetre, text="1. Trier par Movement Speed", command=lancer_tri_movement).pack(pady=5)
tk.Button(fenetre, text="2. Trier par Attack Damage", command=lancer_tri_attack).pack(pady=5)
tk.Button(fenetre, text="3. Trier par Max Health", command=lancer_tri_health).pack(pady=5)
tk.Button(fenetre, text="4. Trier par Brawler", command=lancer_tri_brawler).pack(pady=5)
tk.Button(fenetre, text="5. Trier par Rarity", command=lancer_tri_rarity).pack(pady=5)
tk.Button(fenetre, text="6. Trier par Tier", command=lancer_tri_tier).pack(pady=5)
tk.Button(fenetre, text="7. Trier par Attack Range", command=lancer_tri_range).pack(pady=5)
tk.Button(fenetre, text="8. Trier par Projectile Speed", command=lancer_tri_projectile).pack(pady=5)

fenetre.mainloop()
