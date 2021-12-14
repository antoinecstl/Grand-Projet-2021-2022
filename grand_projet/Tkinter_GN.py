# -*- coding: utf-8 -*-
"""
Fenêtre de gestion des notes
Par Geoffrey VENANT et Antoine CASTEL
En classe 2PD2
"""
import tkinter as tk
import definition as df
import Tkinter_GN_ajt as tkgnajt





def open_gn (fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_GN = tk.Toplevel(fenetre_parent)
    fenetre_GN.iconbitmap("logo_chapeau.ico")
    fenetre_GN.geometry("800x600")
    fenetre_GN.title("Gestion Notes")
    fenetre_GN.configure(bg="#313131")
    df.tree_note_merge(fenetre_GN)
    

    #Label principal    
    
    label1 = tk.Label(fenetre_GN, text = "Gestion des notes", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    label1.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.12)
    
    #Boutton Refresh de l'affichage du CSV
    
    reload_button = tk.PhotoImage(file = "reload1.png")
    Butaff = tk.Button(fenetre_GN, image = reload_button, font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : df.tree_note_merge(fenetre_GN), bg = "#646464", fg = "white")
    Butaff.place(relx = 0.47, rely = 0.222, relwidth = 0.025, relheight = 0.042)
    
    #Boutton menant à la fenêtre d'ajout de note
    
    Butajt = tk.Button(fenetre_GN, text = "Ajouter une note", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgnajt.open_gn_ajt(fenetre_GN), bg = "#646464", fg = "white")
    Butajt.place(relx = 0.15, rely = 0.3, relwidth = 0.2, relheight = 0.07)
    
    #Boutton menant à la fenêtre de modification de note
    
    Butmod = tk.Button(fenetre_GN, text = "Modifier une note", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgnajt.open_gn_mod(fenetre_GN), bg = "#646464", fg = "white")
    Butmod.place(relx = 0.15, rely = 0.45, relwidth = 0.2, relheight = 0.07)
    
    #Boutton menant à la fenêtre de suppression de note
    
    Butsup = tk.Button(fenetre_GN, text = "Supprimer une note", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgnajt.open_gn_supp(fenetre_GN),  bg = "#646464", fg = "white")
    Butsup.place(relx = 0.15, rely = 0.6, relwidth = 0.2, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGN = tk.Button(fenetre_GN, text = "Retour", font = ("arial",10), overrelief = "groove", command = lambda : df.close(fenetre_GN), activebackground = "red", bg = "#8BA0AC")
    ReturnGN.place(relx = 0.17, rely = 0.8, relwidth = 0.16, relheight = 0.05)

    #Lancement de la fenêtre
    
    fenetre_GN.mainloop()