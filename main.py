from subprocess import call
from tkinter import *

#fonction Achats
def Achats():
    root.destroy()
    call(["python","Achats.py"])

def Ventes():
    root.destroy()
    call(["python","Ventes.py"])


#fenétre
root = Tk()
root.title("GESTION DES ACHATS ET VENTES")
root.geometry("600x200+400+100")
root.resizable(False, False)
root.configure(background="#808080")
# titre
labtitre = Label(root,borderwidth=3,relief= SUNKEN, text="GESTION DES ACHATS ET VENTES", font=("Sans Serif",25),background="#0023F5",foreground="black")
labtitre.place(x = 0, y = 0, width = 600)

# les differents boutons

# bouton Achats
btn_enregistrement = Button(root, text="ACHATS", font=("Arial",24), bg="#0023F5",fg="black", command=Achats)
btn_enregistrement.place(x=100,y=100,width=200)
#bouton Ventes
btn_enregistrement = Button(root, text="VENTES", font=("Arial",24), bg="#0023F5",fg="black", command=Ventes)
btn_enregistrement.place(x=330,y=100,width=200)


#excution fenêtre
root.mainloop()
