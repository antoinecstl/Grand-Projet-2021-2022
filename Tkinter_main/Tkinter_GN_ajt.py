# -*- coding: utf-8 -*-
"""
Regroupement des 3 fenêtres (ajout, modification, suppression) de gestion des notes
Par Geoffrey VENANT et Antoine CASTEL
En classe 2PD2

"""

import tkinter as tk
import definition as df
from tkinter import ttk



#Fenêtre d'ajout des notes
def open_gn_ajt (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_gn_ajt = tk.Toplevel(fenetre_parent)
    fenetre_gn_ajt.geometry("500x700")
    fenetre_gn_ajt.title("Ajout d'une note")
    fenetre_gn_ajt.configure(bg="#313131")
    
    #Label principal
    
    label = tk.Label(fenetre_gn_ajt, text = "Ajouter une note", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    label.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.10)
    
    #Id de l'étudiant
    
    Idlabel = tk.Label(fenetre_gn_ajt, text = "ID de l'étudiant", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.21, relwidth = 0.28, relheight = 0.03)
    Identry = tk.Entry(fenetre_gn_ajt, bg = "white", relief = "ridge")
    Identry.place(relx = 0.36, rely = 0.26, relwidth = 0.28, relheight = 0.03)
    
    #Année scolaire
    
    Idlabel = tk.Label(fenetre_gn_ajt, text = "Année scolaire", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.34, relwidth = 0.28, relheight = 0.03)
    Identry1 = tk.Entry(fenetre_gn_ajt, bg = "white", relief = "ridge")
    Identry1.place(relx = 0.36, rely = 0.39, relwidth = 0.28, relheight = 0.03)
    
    #Matière de la note
    
    Classelabel = tk.Label(fenetre_gn_ajt, text = "Matière", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Classelabel.place(relx = 0.36, rely = 0.47, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_gn_ajt, 
                            values=[
                                    "Mathematique",
                                    "Aeronautique",
                                    "Informatique",
                                    "Anglais",
                                    "Electronique",
                                    "Physique",
                                    "Mecanique",
                                    "Grand Projet"
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.52, relwidth = 0.28, relheight = 0.03)
    
    #Note
    
    Idlabel = tk.Label(fenetre_gn_ajt, text = "Note", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.60, relwidth = 0.28, relheight = 0.03)
    Identry2 = tk.Entry(fenetre_gn_ajt, bg = "white", relief = "ridge")
    Identry2.place(relx = 0.36, rely = 0.65, relwidth = 0.28, relheight = 0.03)
    
    #Boutton d'application de la def de vérification
    
    ConfimerGE = tk.Button(fenetre_gn_ajt, text = "Confirmer", font = ("arial",8), overrelief = "groove", activebackground = "blue", bg = "#8BA0AC",
                           command = lambda : [df.verif_ajt_note(Identry, Identry1, ComboClasse , Identry2), df.close(fenetre_gn_ajt)])
    ConfimerGE.place(relx = 0.18, rely = 0.82, relwidth = 0.22, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGN = tk.Button(fenetre_gn_ajt, text = "Retour", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC", command = lambda : df.close(fenetre_gn_ajt), activebackground = "red")
    ReturnGN.place(relx = 0.60, rely = 0.82, relwidth = 0.22, relheight = 0.07)
 
    
#Fenêtre de modification des notes
def open_gn_mod (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_gn_mod = tk.Toplevel(fenetre_parent)
    fenetre_gn_mod.geometry("500x700")
    fenetre_gn_mod.title("Modification d'une note")
    fenetre_gn_mod.configure(bg="#313131")
    
    #Label principal
    
    label = tk.Label(fenetre_gn_mod, text = "Modifier une note", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    label.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.10)
    
    #Id de l'étudiant
    
    Idlabel = tk.Label(fenetre_gn_mod, text = "ID de l'étudiant", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.21, relwidth = 0.28, relheight = 0.03)
    Identry = tk.Entry(fenetre_gn_mod, bg = "white", relief = "ridge")
    Identry.place(relx = 0.36, rely = 0.26, relwidth = 0.28, relheight = 0.03)
    
    #Année scolaire
    
    Idlabel = tk.Label(fenetre_gn_mod, text = "Année scolaire", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.34, relwidth = 0.28, relheight = 0.03)
    Identry1 = tk.Entry(fenetre_gn_mod, bg = "white", relief = "ridge")
    Identry1.place(relx = 0.36, rely = 0.39, relwidth = 0.28, relheight = 0.03)
    
    #Matière
    
    Classelabel = tk.Label(fenetre_gn_mod, text = "Matière", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Classelabel.place(relx = 0.36, rely = 0.47, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_gn_mod, 
                            values=[
                                    "Mathematique",
                                    "Aeronautique",
                                    "Informatique",
                                    "Anglais",
                                    "Electronique",
                                    "Physique",
                                    "Mecanique",
                                    "Grand Projet"
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.52, relwidth = 0.28, relheight = 0.03)
    
    #Note
    
    Idlabel = tk.Label(fenetre_gn_mod, text = "Note", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.60, relwidth = 0.28, relheight = 0.03)
    Identry2 = tk.Entry(fenetre_gn_mod, bg = "white", relief = "ridge")
    Identry2.place(relx = 0.36, rely = 0.65, relwidth = 0.28, relheight = 0.03)
    
    #Boutton d'application de la def de vérification

    ConfimerGE = tk.Button(fenetre_gn_mod, text = "Confirmer", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC",
                           command = lambda : [df.verif_mod_note(Identry, Identry1, ComboClasse, Identry2),df.close(fenetre_gn_mod)],activebackground = "blue")
    ConfimerGE.place(relx = 0.18, rely = 0.82, relwidth = 0.22, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGN = tk.Button(fenetre_gn_mod, text = "Retour", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC", command = lambda : df.close(fenetre_gn_mod), activebackground = "red")
    ReturnGN.place(relx = 0.60, rely = 0.82, relwidth = 0.22, relheight = 0.07)
    
    
#Fenêtre de suppression des notes
def open_gn_supp (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_gn_supp = tk.Toplevel(fenetre_parent)
    fenetre_gn_supp.geometry("500x700")
    fenetre_gn_supp.title("Supression d'une note")
    fenetre_gn_supp.configure(bg="#313131")

    #Label principal
    
    label = tk.Label(fenetre_gn_supp, text = "Supprimer une note", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    label.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.10)
    
    #Id de l'étudiant
    
    Idlabel = tk.Label(fenetre_gn_supp, text = "ID de l'étudiant", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.21, relwidth = 0.28, relheight = 0.03)
    Identry = tk.Entry(fenetre_gn_supp, bg = "white", relief = "ridge")
    Identry.place(relx = 0.36, rely = 0.26, relwidth = 0.28, relheight = 0.03)
    
    #Année scolaire    
    
    Idlabel = tk.Label(fenetre_gn_supp, text = "Année scolaire", font = ("arial",10), relief = "groove", bg = "#646464", fg = "white")
    Idlabel.place(relx = 0.36, rely = 0.34, relwidth = 0.28, relheight = 0.03)
    Identry1 = tk.Entry(fenetre_gn_supp, bg = "white", relief = "ridge")
    Identry1.place(relx = 0.36, rely = 0.39, relwidth = 0.28, relheight = 0.03)
    
    #Matière
    
    Classelabel = tk.Label(fenetre_gn_supp, text = "Matière", font = ("arial", 10), relief = "groove", bg = "#646464", fg = "white")
    Classelabel.place(relx = 0.36, rely = 0.47, relwidth = 0.28, relheight = 0.03)
    
    ComboClasse = ttk.Combobox(fenetre_gn_supp, 
                            values=[
                                    "Mathematique",
                                    "Aeronautique",
                                    "Informatique",
                                    "Anglais",
                                    "Electronique",
                                    "Physique",
                                    "Mecanique",
                                    "Grand Projet"
                                    ],
                            state = "readonly")
    
    ComboClasse.place(relx = 0.36, rely = 0.52, relwidth = 0.28, relheight = 0.03)
    
    #Boutton d'application de la def de vérification
    
    ConfimerGE = tk.Button(fenetre_gn_supp, text = "Confirmer", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC",
                           command = lambda : [df.verif_supp_note(Identry, Identry1, ComboClasse),df.close(fenetre_gn_supp)], activebackground = "blue")
    ConfimerGE.place(relx = 0.18, rely = 0.82, relwidth = 0.22, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGN = tk.Button(fenetre_gn_supp, text = "Retour", font = ("arial",8), overrelief = "groove", bg = "#8BA0AC", command = lambda : df.close(fenetre_gn_supp), activebackground = "red")
    ReturnGN.place(relx = 0.60, rely = 0.82, relwidth = 0.22, relheight = 0.07)