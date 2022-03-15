# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:44:40 2022

@author: JDQS
"""
# https://github.com/JosephDqs/CorrectionTD2IN200
############################
#        Import            #
############################

import random

############################
#       Exercice 1         #
############################


def exercice_1():
    list_notes = []
    # On ouvre le fichier
    notes = open("notes.txt", "r")
    while(True):
        # On lit les lignes
        new_line = notes.readline()
        # Si on lit une ligne vide, o arrette
        if(new_line == ""):
            break
        # on split la ligne dans une liste
        splitted_line = new_line.split()
        sum_notes = 0
        # on fait la somme
        for i in range(1, len(splitted_line)):
            sum_notes += int((splitted_line[i]))
        # on fait la moyenne
        mean_notes = sum_notes / (i)
        # on ajoute la moyenne à la fin de notre ligne
        splitted_line.append(mean_notes)
        # on ajoute cette liste à notre liste de listes
        list_notes.append(splitted_line)
    # On pense bien à fermer le fichier
    notes.close()
    # On ré-écrit nos notes dans le fichier
    ecrire_notes = open("moyennes.txt", "w")
    for listes in list_notes:
        for elem in listes:
            # On re-écrit les éléements de notre liste
            ecrire_notes.write(f"{elem} ")
        # On oublie pas le retour à la ligne
        ecrire_notes.write("\n")
    ecrire_notes.close()


############################
#       Exercice 2         #
############################


def nb_lignes(nom_fichier):
    fichier = open(nom_fichier, "r")
    lines = fichier.readlines()
    fichier.close()
    return(len(lines))


def ecrit_liste_mots(n):
    fichier1 = open("words.txt", "r")
    fichier2 = open(f"words{n}.txt", "w")
    while(True):
        new_line = fichier1.readline()
        if(new_line == ""):
            break
        if(len(new_line) == n+1):
            fichier2.write(f"{new_line}")
    fichier1.close()
    fichier2.close()


def melange_mots(nom_fichier):
    fichier1 = open(f"{nom_fichier}.txt", "r")
    fichier2 = open(f"{nom_fichier}.mel", "w")
    mots1 = fichier1.readlines()
    random.shuffle(mots1)
    fichier1.close()
    for mot in mots1:
        fichier2.write(mot)
    fichier2.close()


def compare_mots(m1, m2):
    m1 = m1.strip("\n")
    n = len(m1)
    profil = [-1] * n
    copy_m2 = list(m2)
    for i in range(0, n):  # on verifie d'abord les similaires
        if(m1[i] == m2[i]):
            profil[i] = 1
            copy_m2.remove(m1[i])
    for i in range(0,n):  # puis les mal placées
        if(profil[i] == -1 ):
            if(m1[i] in copy_m2):
                profil[i] = 2
                copy_m2.remove(m1[i])
            else:
                profil[i] = 0
    return profil


def ecrit_liste_compatible(fic, m, profil):
    fichier1 = open(f"{fic}.txt", "r")
    fichier2 = open(f"{fic}.comp", "w")
    mots = fichier1.readlines()
    for m2 in mots:
        if(compare_mots(m, m2) == profil):
            fichier2.write(m2)
    fichier1.close()
    fichier2.close()


def exercice_2():
    taille = input('Entrez la taille du mot mystere : \n')
    taille = int(taille)
    solution = [0] * taille
    ecrit_liste_mots(taille)
    mot = " " * taille
    while(solution.count(1) != taille):
        ecrit_liste_compatible(f"words{taille}", mot, solution)
        mot = input('Entrez le mot choisi : ')
        solution = list(input('Entrez le profil obtenu : '))
        solution = list(map(int, solution))
    print("Bravo vous avez trouvez !")


############################
#         Main             #
############################


def main():
    exercice_1()
    exercice_2()


if __name__ == '__main__':
    main()
