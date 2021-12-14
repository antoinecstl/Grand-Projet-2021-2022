# -*- coding: utf-8 -*-
"""
Fenêtre de gestion des étudiants
Par Geoffrey VENANT et Antoine CASTEL
En classe 2PD2
"""
import tkinter as tk
import definition as df 
import Tkinter_GE_ajt as tkgeajt


def open_ge(fenetre_parent):
    
    #Initialisation des paramètres de la fenêtre
    
    fenetre_GE = tk.Toplevel(fenetre_parent)
    fenetre_GE.iconbitmap("logo_chapeau.ico")
    fenetre_GE.geometry("1100x650")
    fenetre_GE.title('Gestion Etudiants')
    fenetre_GE.configure(bg="#313131")
    df.tree_etud_merge(fenetre_GE)


    #Label principal
    
    label2 = tk.Label(fenetre_GE, text = "Gestion des étudiants", font = ("arial",20), relief = "raised", bg = "#646464", bd = "6", fg = "white" )
    label2.place(relx = -0.08, rely = 0.05, relwidth = 1.16, relheight = 0.12)
    
    #Boutton Refresh de l'affichage du CSV
    
    reload_button = tk.PhotoImage(file = "reload1.png")
    Butaff = tk.Button(fenetre_GE, image = reload_button, font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : df.tree_etud_merge(fenetre_GE), bg = "#646464", fg = "white")
    Butaff.place(relx = 0.322, rely = 0.222, relwidth = 0.025, relheight = 0.04)

    #Boutton menant à la fenêtre d'ajout d'étudiant
    
    Butajt = tk.Button(fenetre_GE, text = "Ajouter un étudiant", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgeajt.open_ge_ajt(fenetre_GE), bg = "#646464", fg = "white")
    Butajt.place(relx = 0.1, rely = 0.3, relwidth = 0.15, relheight = 0.07)
    
    #Boutton menant à la fenêtre de modification d'étudiant
    
    Butmod = tk.Button(fenetre_GE, text = "Modifier un étudiant", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgeajt.open_ge_mod(fenetre_GE), bg = "#646464", fg = "white")
    Butmod.place(relx = 0.1, rely = 0.45, relwidth = 0.15, relheight = 0.07)
    
    #Boutton menant à la fenêtre de suppression d'étudiant
    
    Butsup = tk.Button(fenetre_GE, text = "Supprimer un étudiant", font = ("arial",10), overrelief = "groove", activebackground = "grey", command = lambda : tkgeajt.open_ge_supp(fenetre_GE), bg = "#646464", fg = "white")
    Butsup.place(relx = 0.1, rely = 0.6, relwidth = 0.15, relheight = 0.07)
    
    #Boutton de fermeture de la fenêtre
    
    ReturnGE = tk.Button(fenetre_GE, text = "Retour", font = ("arial",10), overrelief = "groove", command = lambda : df.close(fenetre_GE), activebackground = "red",  bg = "#8BA0AC")
    ReturnGE.place(relx = 0.12, rely = 0.8, relwidth = 0.11, relheight = 0.0475)
    
    #Lancement de la fenêtre
    
    fenetre_GE.mainloop()