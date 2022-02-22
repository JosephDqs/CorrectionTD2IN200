# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:44:40 2022

@author: JDQS
"""
############################
#        Import            #
############################

import sys


############################
#       Exercices          #
############################


def exercice_1():
    list_notes = []
    notes = open("notes", "r")
    new_line = notes.readline().split()
    list_notes.append(new_line)
    while(new_line):
        new_line = notes.readline().split()
        list_notes.append(new_line)
    # utilisez readline() pour lire la ligne suivante
    print(list_notes)
    pass


def main():
    if(len(sys.argv) < 2):
        print("Erreur : pas assez d'arguments. \nEntrez le numéro d'exercice")
        return(0)
    elif(int(sys.argv[1]) not in [1, 2]):
        print("Erreur : mauvais argument")
        return(0)
    else:
        globals()[f'exercice_{sys.argv[1]}']()



if __name__ == '__main__':

    main()