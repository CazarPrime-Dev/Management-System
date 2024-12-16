from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
import sqlite3

# creation des fonctions d'usage
def Retour():
    root.destroy()
    call(["python", "main.py"])


def Ajouter():
    matricule = txtNumero.get()
    client = txtfournisseur.get()
    telephone = txtTelephone.get()
    produit = comboproduit.get()
    prix = txtPrix.get()
    quantite = txtQuantite.get()
    maBase = sqlite3.connect("database.db")
    meConnect = maBase.cursor()
    try:
        sql = "INSERT INTO tb_vente (code, client, telephone, produit, prix_vente, quantite) VALUES (?, ?, ?, ?, ?, ?)"
        val = (matricule, client, telephone, produit, prix, quantite)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("INFORMATION", "Vente ajoutée")
        ModiferAchat()
        root.destroy()
        call(["python", "Ventes.py"])
    except Exception as e:
        print(e)
        maBase.rollback()
    finally:
        maBase.close()


def Modifer():
    matricule = txtNumero.get()
    client = txtfournisseur.get()
    telephone = txtTelephone.get()
    produit = comboproduit.get()
    prix = txtPrix.get()
    quantite = txtQuantite.get()
    maBase = sqlite3.connect("database.db")
    meConnect = maBase.cursor()

    try:
        sql = "UPDATE tb_vente SET client=?, telephone=?, produit=?, prix_vente=?, quantite=? WHERE code=?"
        val = (client, telephone, produit, prix, quantite, matricule)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("INFORMATION", "Vente modifiée")
        root.destroy()
        call(["python", "Ventes.py"])
    except Exception as e:
        print(e)
        maBase.rollback()
    finally:
        maBase.close()


def ModiferAchat():
    produit = comboproduit.get()
    quantite = txtQuantite.get()
    maBase = sqlite3.connect("database.db")
    meConnect = maBase.cursor()

    try:
        sql = "UPDATE tb_achat SET quantite = quantite - ? WHERE produit = ?"
        val = (quantite, produit)
        meConnect.execute(sql, val)
        maBase.commit()
    except Exception as e:
        print(e)
        maBase.rollback()
    finally:
        maBase.close()


def Supprimer():
    matricule = txtNumero.get()
    maBase = sqlite3.connect("database.db")
    meConnect = maBase.cursor()

    try:
        sql = "DELETE FROM tb_vente WHERE code = ?"
        val = (matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        messagebox.showinfo("INFORMATION", "Vente supprimée")
        root.destroy()
        call(["python", "Ventes.py"])
    except Exception as e:
        print(e)
        maBase.rollback()
    finally:
        maBase.close()


# Ma fenetre
root = Tk()

root.title("MENU DES VENTES")
root.geometry("1350x700+0+0")
root.resizable(True, True)
root.configure(background="#808080")

# Ajouter le titre
lbltitre = Label(root, borderwidth=3, relief=SUNKEN, text="GESTION DES VENTES", font=("Sans Serif", 25), background="#0023F5", fg="black")
lbltitre.place(x=0, y=0, width=1350, height=100)

# Detail code
# Matricule
LblNumero = Label(root, text="MATRICULE", font=("Arial", 18), bg="#808080", fg="white")
LblNumero.place(x=0, y=150, width=150)
txtNumero = Entry(root, bd=4, font=("Arial", 14))
txtNumero.place(x=180, y=150, width=150)

# Fournisseur
Lblfournisseur = Label(root, text="CLIENT_NAME", font=("Arial", 18), bg="#808080", fg="white")
Lblfournisseur.place(x=-17, y=200, width=200)
txtfournisseur = Entry(root, bd=4, font=("Arial", 14))
txtfournisseur.place(x=180, y=200, width=300)

# Telephone
LblTelephone = Label(root, text="TELEPHONE", font=("Arial", 18), bg="#808080", fg="white")
LblTelephone.place(x=0, y=250, width=150)
txtTelephone = Entry(root, bd=4, font=("Arial", 14))
txtTelephone.place(x=180, y=250, width=300)

# Produit
Lblproduit = Label(root, text="PRODUIT", font=("Arial", 18), bg="#808080", fg="white")
Lblproduit.place(x=500, y=150, width=150)
comboproduit = ttk.Combobox(root, font=("Arial", 14))
comboproduit['values'] = []
comboproduit.place(x=650, y=150, width=150)

# Prix
LblPrix = Label(root, text="PRIX VENTE", font=("Arial", 18), bg="#808080", fg="white")
LblPrix.place(x=500, y=200, width=150)
txtPrix = Entry(root, bd=4, font=("Arial", 14))
txtPrix.place(x=650, y=200, width=150)

# Quantite
lblQuantite = Label(root, text="QUANTITE", font=("Arial", 18), bg="#808080", fg="white")
lblQuantite.place(x=500, y=250, width=150)
txtQuantite = Entry(root, bd=4, font=("Arial", 14))
txtQuantite.place(x=650, y=250, width=150)

# Enregistrer
btnenregistrer = Button(root, text="Enregistrer", font=("Arial", 16), bg="green", fg="white", command=Ajouter)
btnenregistrer.place(x=900, y=140, width=200)

# Modifier
btnmodofier = Button(root, text="Modifier", font=("Arial", 16), bg="#48308B", fg="white", command=Modifer)
btnmodofier.place(x=900, y=190, width=200)

# Supprimer
btnSupprimer = Button(root, text="Supprimer", font=("Arial", 16), bg="red", fg="white", command=Supprimer)
btnSupprimer.place(x=900, y=240, width=200)

# Retour
btnRetour = Button(root, text="Back", font=("Arial", 16), bg="#B22222", fg="white", command=Retour)
btnRetour.place(x=1150, y=240, width=100)

# Ajouter le titre
LblTitretTable = Label(root, borderwidth=3, relief=SUNKEN, text="TABLE ACHATS", font=("Sans Serif", 18), bg="#0023F5", fg="black")
LblTitretTable.place(x=0, y=300, width=400)

# TableAchats
table = ttk.Treeview(root, columns=(1, 2, 3), height=10, show="headings")
table.place(x=0, y=330, width=400, height=600)

# Entete
table.heading(1, text="PRODUIT")
table.heading(2, text="PRIX")
table.heading(3, text="QUANTITE")

# Definir les dimensions des colonnes
table.column(1, width=200)
table.column(2, width=50)
table.column(3, width=100)

# Afficher les informations de la table_achat
maBase = sqlite3.connect("database.db")
meConnect = maBase.cursor()
meConnect.execute("SELECT produit, prix, quantite FROM tb_achat")

for row in meConnect:
    table.insert('', END, values=row)
maBase.close()

# Ajouter le titre
LblTitretVente = Label(root, borderwidth=3, relief=SUNKEN, text="TABLE VENTES", font=("Sans Serif", 18), background="#0023F5", fg="black")
LblTitretVente.place(x=450, y=300, width=900)

# TableVentes
tableVentes = ttk.Treeview(root, columns=(1, 2, 3, 4, 5, 6), height=10, show="headings")
tableVentes.place(x=450, y=330, width=850, height=500)

# Entete
tableVentes.heading(1, text="CODE")
tableVentes.heading(2, text="CLIENTS")
tableVentes.heading(3, text="TELEPHONE")
tableVentes.heading(4, text="PRODUIT")
tableVentes.heading(5, text="PRIX_VENTES")
tableVentes.heading(6, text="VENDU")

# Definir les dimensions des colonnes
tableVentes.column(1, width=50)
tableVentes.column(2, width=150)
tableVentes.column(3, width=150)
tableVentes.column(4, width=100)
tableVentes.column(5, width=50)
tableVentes.column(6, width=50)

# Afficher les informations de la table_vente
maBase = sqlite3.connect("database.db")
meConnect = maBase.cursor()
meConnect.execute("SELECT * FROM tb_vente")

for row in meConnect:
    tableVentes.insert('', END, values=row)
maBase.close()

# Execution
root.mainloop()
