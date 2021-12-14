
# -*- coding: utf-8 -*-
"""
Fenêtre principale de la Gestion scolaire
Par Geoffrey VENANT et Antoine CASTEL
En classe 2PD2
"""
import tkinter as tk
import Tkinter_GE as tkge
import Tkinter_GN as tkgn
import definition as df


#Initialisation des paramètres de la fenêtre

fenetre1 = tk.Tk()
fenetre1.iconbitmap("logo_chapeau.ico")
fenetre1.title("Gestion de scolarité")
fenetre1.geometry("1050x500")
fenetre1.configure(bg="#313131") 

#Label principal

label = tk.Label(fenetre1, text = "Gestion de scolarité", font = ("arial",24), relief = "raised", bg = "#646464", bd = "8", fg = "white" )
label.place(relx = -0.08, rely = 0.07, relwidth = 1.16, relheight = 0.2)

#Boutton menant à la fenêtre de gestion étudiant

GestEtud = tk.Button(fenetre1, text = "Gestion des étudiants", font = ("arial",13), overrelief = "groove", relief = "raised", command = lambda : tkge.open_ge(fenetre1), bg = "#646464", activeforeground = "white", activebackground = "grey", fg = "white")
GestEtud.place(relx = 0.2, rely = 0.5, relwidth = 0.16, relheight = 0.08)

#Boutton menant à la fenêtre de gestion des notes

GestNote = tk.Button(fenetre1, text = "Gestion des notes", font = ("arial",13), overrelief = "groove", relief = "raised", command = lambda : tkgn.open_gn(fenetre1), bg = "#646464", activeforeground = "white" , activebackground = "grey",  fg = "white")
GestNote.place(relx = 0.65, rely = 0.5, relwidth = 0.15, relheight = 0.08)

#Boutton de fermeture de la fenêtre

Quit = tk.Button(fenetre1, text = "Fermer", font = ("arial",11), overrelief = "groove", command = lambda : df.close(fenetre1), bg = "#8BA0AC", activebackground = "red", fg ='black')
Quit.place(relx = 0.45, rely = 0.8, relwidth = 0.1, relheight = 0.07)

#Lancement de la fenêtre

fenetre1.mainloop()  
