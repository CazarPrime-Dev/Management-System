# Bibliotheque
from tkinter import *
from tkinter import ttk, Tk
from subprocess import call
from tkinter import messagebox
import sqlite3


def main():
    root.destroy()
    call(["python", "main.py"])


def enregistrer():
    print("Enregistrer")
    matricule = txt_numero.get()
    fournisseur = txt_fournisseur.get()
    telephone = txt_tel.get()
    produit = combo_produit.get()
    prix_achat = txt_prix.get()
    quantite = txt_quantite.get()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        sql = "INSERT INTO tb_achat(code, fournisseur, telephone, produit, prix, quantite) VALUES (?, ?, ?, ?, ?, ?)"
        val = (matricule, fournisseur, telephone, produit, prix_achat, quantite)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("INFORMATION", "Achat ajouter")
        root.destroy()
        call(["python", "Achats.py"])

    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def modifier():
    print("modifier")
    matricule = txt_numero.get()
    fournisseur = txt_fournisseur.get()
    telephone = txt_tel.get()
    produit = combo_produit.get()
    prix_achat = txt_prix.get()
    quantite = txt_quantite.get()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        sql = "UPDATE tb_achat SET fournisseur = ?, telephone = ?, produit = ?, prix = ?, quantite = ? WHERE code = ?"
        val = (fournisseur, telephone, produit, prix_achat, quantite, matricule)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("information", "Achat modifier")
        root.destroy()
        call(["python", "Achats.py"])
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


def supprimer():
    print("supprimer")
    matricule = txt_numero.get()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        sql = "DELETE FROM tb_achat WHERE code = ?"
        val = (matricule,)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo("information", "Achat supprimer")
        root.destroy()
        call(["python", "Achats.py"])
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        conn.close()


# Fenêtre
root = Tk()
root.title("MENU ACHATS")
root.geometry("1270x700+0+0")
root.resizable(True, True)
root.configure(background="#808080")

# Titre
titre = Label(root, borderwidth=3, relief=SUNKEN, text="GESTION DES ACHATS", font=("Sans Serif", 25), bg="#0023F5",
              fg="#000000")
titre.place(x=-50, y=0, width=1350, height=100)

# Matricule
numero_label = Label(root, text="MATRICULE", font=("Arial", 18), bg="#808080", fg="white")
numero_label.place(x=20, y=150, width=150)
txt_numero = Entry(root, bd=4, font=("Arial", 14))
txt_numero.place(x=220, y=150, width=150)

# Fournisseur
fournisseur_label = Label(root, text="FOURNISSEUR", font=("Arial", 18), bg="#808080", fg="white")
fournisseur_label.place(x=-10, y=200, width=250)
txt_fournisseur = Entry(root, bd=4, font=("Arial", 14))
txt_fournisseur.place(x=220, y=200, width=250)

# Téléphone
tel_label = Label(root, text="TELEPHONE", font=("Arial", 18), bg="#808080", fg="white")
tel_label.place(x=26, y=250, width=150)
txt_tel = Entry(root, bd=4, font=("Arial", 14))
txt_tel.place(x=220, y=250, width=250)

# Produit
produit_label = Label(root, text="PRODUIT", font=("Arial", 18), bg="#808080", fg="white")
produit_label.place(x=500, y=150, width=150)
combo_produit = ttk.Combobox(root, font=("Arial", 14))
combo_produit['values'] = ["kss", "kdskq", "kdqkd"]
combo_produit.place(x=650, y=150, width=150)

# Prix
prix_label = Label(root, text="PRIX", font=("Arial", 18), bg="#808080", fg="white")
prix_label.place(x=500, y=200, width=150)
txt_prix = Entry(root, bd=4, font=("Arial", 14))
txt_prix.place(x=650, y=200, width=150)

# Quantité
quantite_label = Label(root, text="QUANTITE", font=("Arial", 18), bg="#808080", fg="white")
quantite_label.place(x=500, y=250, width=150)
txt_quantite = Entry(root, bd=4, font=("Arial", 14))
txt_quantite.place(x=650, y=250, width=150)

# Boutons
bouton_enregistrer = Button(root, text="ENREGISTRER", font=("Arial", 16), bg="green", fg="black", command=enregistrer)
bouton_enregistrer.place(x=900, y=140, width=200)

bouton_modifier = Button(root, text="MODIFIER", font=("Arial", 16), bg="#483088", fg="white", command=modifier)
bouton_modifier.place(x=900, y=190, width=200)

bouton_supprimer = Button(root, text="SUPPRIMER", font=("Arial", 16), bg="red", fg="black", command=supprimer)
bouton_supprimer.place(x=900, y=240, width=200)

bouton_retour = Button(root, text="BACK", font=("Arial", 16), bg="#B22222", fg="white", command=main)
bouton_retour.place(x=1150, y=240, width=100)

# Table
table = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
table.place(x=0, y=290, width=1280, height=700)

# Entête
table.heading(1, text="CODE_ACHAT")
table.heading(2, text="FOURNISSEUR")
table.heading(3, text="TELEPHONE")
table.heading(4, text="PRODUIT")
table.heading(5, text="PRIX")
table.heading(6, text="QUANTITE")

# Redimension des colonnes
table.column(1, width=50)
table.column(2, width=150)
table.column(3, width=100)
table.column(4, width=150)
table.column(5, width=50)
table.column(6, width=50)

# Information de la table
try:
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tb_achat")
    rows = cursor.fetchall()
    for row in rows:
        table.insert('', END, values=row)
except sqlite3.Error as err:
    root.destroy()
    messagebox.showinfo("ERROR", f"Erreur de connexion: {err}")
    exit(1)
finally:
    conn.close()

# Exécution de la fenêtre
root.mainloop()
