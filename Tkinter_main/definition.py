# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:54:42 2021

@author: antoi
"""
import tkinter as tk
from tkinter.constants import END, NO, RIGHT, VERTICAL, W, Y
from lib_commun import ouverture_fichier_csv, ecriture_fichier_csv
import time as t
import tkinter.ttk as ttk


def close (x):
    
    """
    Cette fonction a pour objectif de fermer
    IN : La page que l'on souhaite fermer
    OUT : Aucun retour
    """
    
    t.sleep(0.2)
    x.destroy()
    return


def tree_note_merge(fenetre):

    """
    Cette fonction a pour objectif de creer un tableau d'affichage des données du CSV "notes" via tree
    IN : La fenetre d'application de la frame
    OUT : Aucun retour
    """

    frametree = tk.Frame(fenetre, borderwidth = 2, relief = "groove")
    frametree.place(relx = 0.50, rely = 0.22, relheight = 0.73, relwidth = 0.47) 
    scrollbary = tk.Scrollbar(frametree, orient=VERTICAL)
    tree = ttk.Treeview(frametree, columns=("ANNEE", "ID_ETUDIANT", "MATIERE", "NOTE"), height=100, selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('ANNEE', text="ANNEE", anchor=W)
    tree.heading('ID_ETUDIANT', text="ID_ETUDIANT", anchor=W)
    tree.heading('MATIERE', text="MATIERE", anchor=W)
    tree.heading('NOTE', text="NOTE", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    
    tree.pack()

    data_notes = ouverture_fichier_csv("notes.csv")
            
    for i in range(1, len(data_notes)):
        ANNEE = data_notes[i][1]
        ID_ETUDIANT = data_notes[i][2]
        MATIERE = data_notes[i][3]
        NOTE = data_notes[i][4]
        tree.insert("", END, values=(ANNEE,ID_ETUDIANT,MATIERE,NOTE))


def tree_etud_merge(fenetre):

    """
    Cette fonction a pour objectif de creer un tableau d'affichage des données du CSV "Etudiants" via tree
    IN : La fenetre d'application de la frame
    OUT : Aucun retour
    """

    frametree = tk.Frame(fenetre, borderwidth = 2, relief = "groove")
    frametree.place(relx = 0.35, rely = 0.22, relheight = 0.73, relwidth = 0.62)
    scrollbary = tk.Scrollbar(frametree, orient=VERTICAL)
    tree = ttk.Treeview(frametree, columns=("ID", "GENRE", "NOM", "PRENOM","EMAIL", "CLASSE"), height=400, selectmode="extended", yscrollcommand=scrollbary.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    tree.heading('ID', text="ID", anchor=W)
    tree.heading('GENRE', text="GENRE", anchor=W)
    tree.heading('NOM', text="NOM", anchor=W)
    tree.heading('PRENOM', text="PRENOM", anchor=W)
    tree.heading('EMAIL', text="EMAIL", anchor=W)
    tree.heading('CLASSE', text="CLASSE", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=50)
    tree.column('#2', stretch=NO, minwidth=0, width=50)
    tree.column('#3', stretch=NO, minwidth=0, width=150)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=250)
    
    tree.pack()

    data_etudiants = ouverture_fichier_csv("etudiants.csv")
            
    for i in range(1, len(data_etudiants)):
        ID = data_etudiants[i][0]
        GENRE = data_etudiants[i][1]
        NOM = data_etudiants[i][2]
        PRENOM = data_etudiants[i][3]
        EMAIL = data_etudiants[i][4]
        GROUPE = data_etudiants[i][5]
        tree.insert("", END, values=(ID,GENRE,NOM,PRENOM,EMAIL,GROUPE))



def ajoutEtudiant(*donneesEtudiant) :
    
    """
    Cette fonction à pour objectif d'ajouter un étudiant au CSV étudiant
    IN : Données de l'étudiant
    OUT : Aucun retour
    """
    
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    ajout = [len(data)]
    for i in range(0,len(donneesEtudiant)):
        ajout.append(donneesEtudiant[i]) 

    data.append(ajout)
    ecriture_fichier_csv(data, nomfichier)
    
    return


def modificationEtudiant(*donneesEtudiant) :
    
    """
    Cette fonction à pour objectif de modifier les données de l'étudiant dans le CSV
    IN : Données de l'étudiant
    OUT : Aucun retour
    """
    
    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in range(0, len(data)):
        if donneesEtudiant[0] == data[i][0] :
            data[i][1] = donneesEtudiant[3]
            data[i][2] = donneesEtudiant[2]
            data[i][3] = donneesEtudiant[1]
            data[i][4] = donneesEtudiant[4]
            data[i][5] = donneesEtudiant[5]
            print("modificationEtudiant")
            ecriture_fichier_csv(data, nomfichier)
    return
    
def suppressionEtudiant(etudiant) :
    
    """
    Cette fonction à pour objectif de supprimer un étudiant et ses données dans le CSV
    IN : ID de l'étudiant
    OUT : Aucun retour
    """

    nomfichier = "etudiants.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in range(1,len(data)):
        if data[i][0] == etudiant :
            del data[i]
            ecriture_fichier_csv(data, "etudiants.csv")
            return
    return 
    

def ajoutNote(*donneesNote) :
    
    """
    Cette fonction à pour objectif d'ajouter une note au CSV Note
    IN : Données de la note
    OUT : Aucun retour
    """
    
    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    ajout = [len(data)]
    for i in range(0,len(donneesNote)):
        ajout.append(donneesNote[i]) 

    for j in range(1,len(data)):
        if ajout[3] == data[j][3] and ajout[2] == data[j][2]:
            print("la note existe deja")
        
    data.append(ajout)
    ecriture_fichier_csv(data, nomfichier)
    
    return
    
def modificationNote(*donneesNote) :
    
    """
    Cette fonction a pour objectif de modifier une note du CSV Note
    IN : Données de la note
    OUT : Aucun retour
    """

    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in range(0, len(data)):
        if data[i][2] == donneesNote[0] and data[i][1] == donneesNote[1] and data[i][3] == donneesNote[2] :  
            data[i][4] = donneesNote[3]
            ecriture_fichier_csv(data, nomfichier)
    return

def suppressionNote(*donneesNote) :
    
    """
    Cette fonction a pour objectif de supprimer une note du CSV Note
    IN : ID de la note, Année, Matière
    OUT : Aucun retour
    """

    nomfichier = "notes.csv"
    data = ouverture_fichier_csv(nomfichier)
    for i in range(1,len(data)):
        if data[i][1] == donneesNote[1] and data[i][2] == donneesNote[0] and data[i][3] == donneesNote[2] :
            del data[i]
            ecriture_fichier_csv(data, "notes.csv")
            return
    return


def verif_ajt(genre, nom, prenom, email, groupe):
    
    """
    Cette fonction à pour objectif de faire des vérification de doublon d'étudiant et de données manquante avant d'ajouter un élève au CSV étudiant
    IN : Genre, nom, prenom, email, groupe
    OUT : Aucun retour
    """
    
    csvdata = ouverture_fichier_csv("etudiants.csv")
    for i in range(1 , len(csvdata)):
        if str(csvdata[i][4]) == email.get():
            tk.messagebox.showerror(title = "Erreur",message = "L'étudiant existe déja")
            return
    if (prenom.get() == "") or (nom.get == "") or (email.get() == "") or (groupe.get() == "") or (genre.get() == ""):
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    else:
        ajoutEtudiant(genre.get(), nom.get(), prenom.get(), email.get(), groupe.get())
        
        return
    
    
    
def verif_mod_ge(id_, prenom, nom, genre, email, groupe):
    
    """
    Cette fonction à pour objectif de faire des vérification de données manquante et de l'existance de l'étudiant avant de modifier les données de l'élève
    IN : id_, prenom, nom, genre, email, groupe
    OUT : Aucun retour
    """
    
    if (prenom.get() == "") or (nom.get == "") or (email.get() == "") or (groupe.get() == "") or (genre.get() == "") or (id_.get() == "") :
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    else :
        csvdata = ouverture_fichier_csv("etudiants.csv")
        for i in range (1, len(csvdata)):
            if csvdata[i][0] == id_.get():
                modificationEtudiant(id_.get(),genre.get(), nom.get(), prenom.get(), email.get(), groupe.get())
                return
        tk.messagebox.showerror("Erreur","Id non-existant")
        return
    
    
def verif_supp_ge(id_):
    
    """
    Cette fonction a pour objectif de faire des vérifications de données manquantes et de l'existance de l'étudiant avant de le supprimer 
    IN : id_
    OUT : Aucun retour
    """
    
    if (id_.get() == "") :
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    else :
        csvdata = ouverture_fichier_csv("etudiants.csv")
        for i in range (1, len(csvdata)):
            if csvdata[i][0] == id_.get():
                suppressionEtudiant(id_.get())
                return
        tk.messagebox.showerror("Erreur","Id non-existant")
        return
    
def verif_ajt_note(id_, annee, matiere, note):
    
    """
    Cette fonction à pour objectif de faire des vérifications de données manquantes, de doublon de note et d'existence de l'ID avant de l'ajouter au CSV des notes
    IN : id_, annee, matiere, note
    OUT :Aucun retour
    """
    
    csvdata = ouverture_fichier_csv("notes.csv")
    csvdataetudiant = ouverture_fichier_csv("etudiants.csv")
    find = False
    if (id_.get() == "") or (annee.get() == "") or (matiere.get() == "") or (note.get() == ""):
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    for j in range(1, len(csvdataetudiant)):
        if csvdataetudiant[j][0] == id_.get():
            for i in range (1, len(csvdata)):
                if csvdata[i][2] == id_.get() and csvdata[i][3] == matiere.get() and csvdata[i][1] == annee.get():
                    tk.messagebox.showerror("Erreur","Cette note existe déja")
                    find = True
                    return
            if find == False:
                ajoutNote(annee.get(), id_.get(), matiere.get(), note.get())
                return
    tk.messagebox.showerror("Erreur","Id non-existant")
    return       
     

def verif_mod_note(id_, annee, matiere, note):
    
    """
    Cette fonction à pour objectif de faire des vérifications de données manquantes, de doublon de note et d'existance de l'ID avant de la modifier dans le CSV Note
    IN : id_, annee, matiere, note
    OUT : Aucun retour
    """
    
    csvdata = ouverture_fichier_csv("notes.csv")
    csvdataetudiant = ouverture_fichier_csv("etudiants.csv")
    find =False
    if (id_.get() == "") or (annee.get() == "") or (matiere.get() == "") or (note.get() == ""):
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    for j in range(1, len(csvdataetudiant)):
        if csvdataetudiant[j][0] == id_.get():
            for i in range (1, len(csvdata)):
                if csvdata[i][2] == id_.get() and csvdata[i][3] == matiere.get() and csvdata[i][1] == annee.get() and csvdata[i][4] == note.get():
                    tk.messagebox.showerror("Erreur","Cette note existe déja")
                    find =True
                    return
            if find == False:
                modificationNote(id_.get(), annee.get(), matiere.get(), note.get())
                return   
    tk.messagebox.showerror("Erreur","Id non-existant")
    return      
     
def verif_supp_note(id_, annee, matiere):
    
    """
    Cette fonction à pour objectif de faire des vérifications de données manquantes et d'ID non-existant avant de supprimer la note du CSV Note
    IN : id_, annee, matiere
    OUT : Aucun retour
    """
    
    csvdataetudiant = ouverture_fichier_csv("etudiants.csv")
    if (id_.get() == "") or (annee.get() == "") or (matiere.get() == ""):
        tk.messagebox.showerror("Erreur","Données manquantes")
        return
    for j in range(1, len(csvdataetudiant)):
        if csvdataetudiant[j][0] == id_.get():
            suppressionNote(id_.get(), annee.get(), matiere.get())
            return
    tk.messagebox.showerror("Erreur","Id non-existant")
    return
    
