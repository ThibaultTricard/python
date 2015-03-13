#!/usr/bin/env python
# coding: utf-8

from Tkinter import Button
import Tkinter as tk
import time


class Accueil():
    def __init__(self, ADRESSE, PORT):
        self.ADRESSE = ADRESSE
        self.PORT = PORT


        def donnee():
            self.ADRESSE = adresse_input.get()
            self.PORT = int(port_serveur.get())
            self.NOM = pseudo_input.get()
            validation = tk.Label(fenetre, text='Connexion de ' + self.NOM + ' a ' + self.ADRESSE + ":" + str(
                self.PORT) + " en cours", height=5, fg="navy")
            validation.pack()

            fenetre.update()

            time.sleep(1)
            fenetre.quit()

        #on cree une fenêtre
        fenetre = tk.Tk()
        #on donne un titre a la fenêtre
        fenetre.title("Tetris")
        #on donne une taille et une position
        fenetre.geometry("500x500+0+0")
        #on creer un titre
        titre_principal = tk.Label(fenetre, text="Tetris Connexion")
        #on affiche ce titre
        titre_principal.pack()

        espace = tk.Label(fenetre, text="")
        espace.pack()


        adresse_label = tk.Label(fenetre, text='Adresse du serveur :', width=20, height=3, fg="navy")
        adresse_label.pack()
        adresse_input = tk.StringVar()
        adresse_input.set("127.0.0.1")  # on assigne une valeur de base au chanp

        saisie_default = tk.Entry(textvariable=adresse_input, width=30)
        saisie_default.pack()

        port_label = tk.Label(fenetre, text='Port du serveur :', width=20, height=3, fg="navy")
        port_label.pack()
        port_serveur = tk.StringVar()
        port_serveur.set("8888")  # facultatif: assigne une valeur ? la variable
        saisie_port = tk.Entry(textvariable=port_serveur, width=30)
        saisie_port.pack()

        pseudo_label = tk.Label(fenetre, text='Pseudo :', width=20, height=3, fg="navy")
        pseudo_label.pack()
        pseudo_input = tk.StringVar()  # definition d'une variable-chaine pour recevoir la saisie d'un texte
        pseudo_input.set("Joueur")  # facultatif: assigne une valeur ? la variable
        saisie_peusdo = tk.Entry(textvariable=pseudo_input, width=30)
        saisie_peusdo.pack()

        #on creer un boutton valider avec un fonction a executer au clic
        b = Button(fenetre, text="Connexion", command=donnee)
        espace.pack()
        #on afficher
        b.pack()

        #on lance la boucle du programme
        fenetre.mainloop()

        fenetre.destroy()
