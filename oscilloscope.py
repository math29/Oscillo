#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, Frame

from screen import Screen
from timebase import TimeBase
from generator import Generator


class Oscilloscope(Frame):
    """ 
    Modele d'Oscilloscope 

    time : valeur de la base de temps
    signal : liste de couples, (temps,elongation) ou (elongation X, elongation Y)  de signaux
    view : visualisation de signaux
    control_X : controle d'un signal
    control_time : controle de la base de temps
    """
    def __init__(self, parent=None, width=800, height=800):
        """ 
        Initialisation

        parent : une application
        width,height : dimension de l'oscilloscpe
        """
        Frame.__init__(self)
        self.master.title("Oscilloscope")
        # Hauteur & largeur
        self.width = width
        self.height = height
        # Modele
        self.time = 0
        self.signal = None
        # Vues
        self.view = Screen(parent=self)
        # Controleurs
        self.control_time = TimeBase(parent=self)
        self.control_X = Generator(parent=self)
        # Affichage Vues, Controleurs
        self.view.pack()
        self.control_time.pack()
        self.control_X.pack()
        self.configure(width=width, height=height)

    def get_time(self):
        """
        recuperer la valeur courante de la base de temps
        """
        return self.control_time.get_time()

    def update_time(self, time):
        """
        calcul de signal si modification de la base de temps

        time : nouvelle valeur de la base de temps
        """
        if self.time != time:
            self.time = time
            self.control_X.update_signal(None)

    def update_view(self, name="X", signal=None):
        """ demande d'affichage de signal

        name : nom de la courbe (X,Y, X-Y)
        signal : liste des couples (temps,elongation) ou (elongation X, elongation Y)
        """
        print("Base de Temps :", self.get_time())
        msdiv = self.get_time()
        if signal :
            signal = signal[0:(len(signal)/msdiv) + 1]
            signal = map(lambda (x, y): (x*msdiv, y), signal)
            self.view.plot_signal(name, signal)
        return signal

if __name__ == "__main__":
    root = Tk()
    oscillo = Oscilloscope(root)
    root.mainloop()
