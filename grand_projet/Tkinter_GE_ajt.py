# -*- coding: utf-8 -*-
"""
Regroupement des 3 fenêtres (ajout, modification, suppression) de gestion des étudiants
Par Geoffrey VENANT et Antoine CASTEL
En classe 2PD2
"""

import tkinter as tk
import definition as df
from tkinter import ttk 

#Fenêtre d'ajout étudiant
def open_ge_ajt (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_ge_ajt = tk.Toplevel(fenetre_parent)
    fenetre_ge_ajt.iconbitmap("logo_chapeau.ico")
    fenetre_ge_ajt.geometry("600x800")
    fenetre_ge_ajt.title("Ajout d'un étudiant")
    fenetre_ge_ajt.configure(bg="#313131")
    
    #Label principal
    
    TitreLabel = tk.Label(fenetre_ge_ajt, text = "Ajouter un étudiant", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    TitreLabel.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.10)
    
    #Prénom de l'étudiant
    
    prenomlabel = tk.Label(fenetre_ge_ajt, text = "Prénom", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    prenomlabel.place(relx = 0.36, rely = 0.21, relwidth = 0.28, relheight = 0.03)
    prenomentry = tk.Entry(fenetre_ge_ajt, bg = "white", relief = "ridge")
    prenomentry.place(relx = 0.36, rely = 0.26, relwidth = 0.28, relheight = 0.03)
    
    #Nom de l'étudiant
    
    Nomlabel = tk.Label(fenetre_ge_ajt, text = "Nom", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Nomlabel.place(relx = 0.36, rely = 0.32, relwidth = 0.28, relheight = 0.03)
    Nomentry = tk.Entry(fenetre_ge_ajt, bg = "white", relief = "ridge")
    Nomentry.place(relx = 0.36, rely = 0.37, relwidth = 0.28, relheight = 0.03)
    
    #Email de l'étudiant
    
    emaillabel = tk.Label(fenetre_ge_ajt, text = "E-mail", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    emaillabel.place(relx = 0.36, rely = 0.43, relwidth = 0.28, relheight = 0.03)
    emailentry = tk.Entry(fenetre_ge_ajt, bg = "white", relief = "ridge")
    emailentry.place(relx = 0.36, rely = 0.48, relwidth = 0.28, relheight = 0.03)
    
    #Genre de l'étudiant(e)
    
    genrelabel = tk.Label(fenetre_ge_ajt, text = "Genre", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    genrelabel.place(relx = 0.36, rely = 0.54, relwidth = 0.28, relheight = 0.03)
    
    GenreValue = tk.StringVar() 
    GenreFemme = tk.Radiobutton(fenetre_ge_ajt, text = "Femme",
                             variable=GenreValue, value = "F") 
    GenreHomme = tk.Radiobutton(fenetre_ge_ajt, text = "Homme",
                             variable=GenreValue, value = "M") 
    
    GenreFemme.place(relx = 0.36, rely = 0.59)
    GenreHomme.place(relx = 0.525, rely = 0.59)
    
    GenreFemme.deselect()
    GenreHomme.deselect()
    
    #Classe de l'étudiant
    
    Classelabel = tk.Label(fenetre_ge_ajt, text = "Classe", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Classelabel.place(relx = 0.36, rely = 0.65, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_ge_ajt, 
                            values=[
                                    "ANG1",
                                    "ANG2",
                                    "2PA1", 
                                    "2PA2",
                                    "2PB1",
                                    "2PB2",
                                    "2PC1",
                                    "2PC2",
                                    "2PD1",
                                    "2PD2",
                                    "2PE1",
                                    "2PE2",
                                    "2PF1",
                                    "2PF2",
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.70, relwidth = 0.28, relheight = 0.03)
    
    #Boutton d'application de la def de vérification
    
    ConfimerGE = tk.Button(fenetre_ge_ajt, text = "Confirmer", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC",
                           command = lambda : [df.verif_ajt(GenreValue, Nomentry, prenomentry, emailentry, ComboClasse),df.close(fenetre_ge_ajt)], activebackground = "blue")
    ConfimerGE.place(relx = 0.18, rely = 0.84, relwidth = 0.22, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGE = tk.Button(fenetre_ge_ajt, text = "Retour", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC",
                         command = lambda : df.close(fenetre_ge_ajt), activebackground = "red")
    ReturnGE.place(relx = 0.60, rely = 0.84, relwidth = 0.22, relheight = 0.07)
 
    
#Fenêtre de modification étudiant
def open_ge_mod (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_ge_mod = tk.Toplevel(fenetre_parent) 
    fenetre_ge_mod.iconbitmap("logo_chapeau.ico")
    fenetre_ge_mod.geometry("600x800")
    fenetre_ge_mod.title("Modification d'un profil étudiant")
    fenetre_ge_mod.configure(bg="#313131")
    
    #Label principal
        
    TitreLabel = tk.Label(fenetre_ge_mod, text = "Modifier un étudiant", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    TitreLabel.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.10)
    
    #Id de l'étudiant
    
    Idlabel = tk.Label(fenetre_ge_mod, text = "ID de l'étudiant", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.21, relwidth = 0.28, relheight = 0.03)  
    Identry = tk.Entry(fenetre_ge_mod, bg = "white", relief = "ridge")
    Identry.place(relx = 0.36, rely = 0.25, relwidth = 0.28, relheight = 0.03)
    
    #Prenom de l'étudiant
    
    prenomlabel = tk.Label(fenetre_ge_mod, text = "Prénom", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    prenomlabel.place(relx = 0.36, rely = 0.31, relwidth = 0.28, relheight = 0.03)
    prenomentry = tk.Entry(fenetre_ge_mod, bg = "white", relief = "ridge")
    prenomentry.place(relx = 0.36, rely = 0.35, relwidth = 0.28, relheight = 0.03)
    
#Nom de l'étudiant   

    Nomlabel = tk.Label(fenetre_ge_mod, text = "Nom", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Nomlabel.place(relx = 0.36, rely = 0.41, relwidth = 0.28, relheight = 0.03)
    Nomentry = tk.Entry(fenetre_ge_mod, bg = "white", relief = "ridge")
    Nomentry.place(relx = 0.36, rely = 0.45, relwidth = 0.28, relheight = 0.03)
    
#Email de l'étudiant

    emaillabel = tk.Label(fenetre_ge_mod, text = "E-mail", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    emaillabel.place(relx = 0.36, rely = 0.51, relwidth = 0.28, relheight = 0.03)    
    emailentry = tk.Entry(fenetre_ge_mod, bg = "white", relief = "ridge")
    emailentry.place(relx = 0.36, rely = 0.55, relwidth = 0.28, relheight = 0.03)

#Genre de l'étudiant
    
    genrelabel = tk.Label(fenetre_ge_mod, text = "Genre", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    genrelabel.place(relx = 0.36, rely = 0.61, relwidth = 0.28, relheight = 0.03)
    
    GenreValue = tk.StringVar() 
    GenreFemme = tk.Radiobutton(fenetre_ge_mod, text = 'Femme',
                             variable=GenreValue, value="F") 
    GenreHomme = tk.Radiobutton(fenetre_ge_mod, text = 'Homme',
                             variable=GenreValue, value="M") 
    GenreFemme.deselect()
    GenreHomme.deselect()
    
    GenreFemme.place(relx = 0.36, rely = 0.65)
    GenreHomme.place(relx = 0.525, rely = 0.65)
    
    #Classe de l'étudiant
    
    Classelabel = tk.Label(fenetre_ge_mod, text = "Classe", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Classelabel.place(relx = 0.36, rely = 0.69, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_ge_mod, 
                            values=[
                                    "ANG1",
                                    "ANG2",
                                    "2PA1", 
                                    "2PA2",
                                    "2PB1",
                                    "2PB2",
                                    "2PC1",
                                    "2PC2",
                                    "2PD1",
                                    "2PD2",
                                    "2PE1",
                                    "2PE2",
                                    "2PF1",
                                    "2PF2",
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.73, relwidth = 0.28, relheight = 0.03)
    
    #Boutton d'application de la def de vérification
    
    ConfimerGE = tk.Button(fenetre_ge_mod, text = "Confirmer", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC", activebackground = "blue",
                           command = lambda : [df.verif_mod_ge(Identry, GenreValue, Nomentry, prenomentry, emailentry, ComboClasse),df.close(fenetre_ge_mod)])
    ConfimerGE.place(relx = 0.18, rely = 0.85, relwidth = 0.22, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGE = tk.Button(fenetre_ge_mod, text = "Retour", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC", command = lambda : df.close(fenetre_ge_mod), activebackground = "red")
    ReturnGE.place(relx = 0.60, rely = 0.85, relwidth = 0.22, relheight = 0.07)
 
    
#Fenêtre de suppresion étudiant
def open_ge_supp (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_ge_supp = tk.Toplevel(fenetre_parent)   
    fenetre_ge_supp.iconbitmap("logo_chapeau.ico") 
    fenetre_ge_supp.geometry("400x200")
    fenetre_ge_supp.title("Supprimer un étudiant")
    fenetre_ge_supp.configure(bg="#313131")
    
    #Label principal
    
    TitreLabel = tk.Label(fenetre_ge_supp, text = "Supprimer un étudiant", font = ("arial",18), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    TitreLabel.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.20)
    
    #Id de l'étudiant
    
    Idlabel = tk.Label(fenetre_ge_supp, text = "ID de l'étudiant", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.30, relwidth = 0.28, relheight = 0.13)
    Identry = tk.Entry(fenetre_ge_supp, bg = "white", relief = "ridge")
    Identry.place(relx = 0.43, rely = 0.52, relwidth = 0.14, relheight = 0.12)
    
    #Boutton d'application de la def de vérification
    
    ConfimerGE = tk.Button(fenetre_ge_supp, text = "Confirmer", font = ("arial",10), overrelief = "groove", bg = "#8BA0AC", activebackground = "blue",
                           command = lambda : [df.verif_supp_ge(Identry),df.close(fenetre_ge_supp)])
    ConfimerGE.place(relx = 0.18, rely = 0.80, relwidth = 0.22, relheight = 0.12)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGE = tk.Button(fenetre_ge_supp, text = "Retour", font = ("arial",10), overrelief = "groove", bg = "#8BA0AC", command = lambda : df.close(fenetre_ge_supp), activebackground = "red")
    ReturnGE.place(relx = 0.60, rely = 0.80, relwidth = 0.22, relheight = 0.12)
    
    