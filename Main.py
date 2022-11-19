import random
import time

print()
print("Entrez le nombre de joueurs réels")
nb_joueurs_n = int(input())
print("Entrez le nombre d'IA")
nb_ia = int(input())

nb_joueurs = nb_joueurs_n + nb_ia

decks = {}
for i in range(nb_joueurs):
    decks[i] = []
pile = []

nombres = [nb for nb in range(10)]

couleurs = ["Rouge", "Vert", "Bleu", "Jaune"]

tour = 0


def test_jouer(carte):
    if carte[0] == carte_actuelle[0] or carte[1] == carte_actuelle[1] or carte[0] == "+4" or carte[0] == "Joker":
        return True
    return False


def cardToString(carte):
    return str(carte[0]) + " de couleur " + carte[1]


def reset_pile():
    for couleur in couleurs:
        for n in range(1, 10):
            pile.append((n, couleur))
            pile.append((n, couleur))
        pile.append((0, couleur))
        pile.append(("+2", couleur))
        pile.append(("+2", couleur))
        pile.append(("Inversion", couleur))
        pile.append(("Inversion", couleur))
        pile.append(("Skip", couleur))
        pile.append(("Skip", couleur))
        pile.append(("Joker", couleur))
        pile.append(("+4", couleur))

    random.shuffle(pile)


def inputColor():
    print("Choisissez une couleur")
    for i in range(len(couleurs)):
        print(i, "-", couleurs[i])
    color = int(input())
    return couleurs[color]


reset_pile()
random.shuffle(pile)

for n in range(7):
    for i in range(nb_joueurs):
        decks[i].append(pile.pop(0))

carte_actuelle = ("?", "?")
while not carte_actuelle[0] in nombres:
    carte_actuelle = pile.pop(0)
    print("Carte actuelle :", cardToString(carte_actuelle))

sens = True

time.sleep(2)

while True:
    if sens:
        tour += 1
    else:
        tour -= 1
    if tour not in decks.keys():
        if sens:
            tour = 0
        else:
            tour = list(decks)[-1]
    print()
    print("    Au tour du joueur", tour + 1)
    time.sleep(2)
    if tour < nb_joueurs_n:
        print("Votre deck :")
        for nb_carte in range(len(decks[tour])):
            string = ""
            string = string + str(nb_carte) + " - " + cardToString(decks[tour][nb_carte]) + "    "
            print(string)
    print()
    i = 0
    choix = True
    if tour < nb_joueurs_n:
        choix = False
        canPlay = False
        for i in range(len(decks[tour])):
            if test_jouer(decks[tour][i]):
                canPlay = True
        if canPlay:
            print("Choisissez la carte (Carte actuelle : " + cardToString(carte_actuelle) + ")")
            i = int(input())
            print("\n" * 100)
            print("Le joueur", tour + 1, "joue la carte", cardToString(decks[tour][i]))
            carte_actuelle = decks[tour][i]
            del (decks[tour][i])
            if carte_actuelle[0] == "Inversion":
                sens = not sens
                print("Changement de sens !")
            if carte_actuelle[0] == "Skip":
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                print("Le joueur", tour + 1, "passe son tour")
            if carte_actuelle[0] == "+2":
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                print("Le joueur", tour + 1, "pioche 2 cartes")
            if carte_actuelle[0] == "Joker":
                best_couleur = inputColor()
                carte_actuelle = (carte_actuelle[0], best_couleur)
                print("Il a choisi la couleur " + best_couleur)
            if carte_actuelle[0] == "+4":
                best_couleur = inputColor()
                carte_actuelle = (carte_actuelle[0], best_couleur)
                print("Il a choisi la couleur " + best_couleur)
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                print("Le joueur", tour + 1, "pioche 4 cartes")
        else:
            print("Le joueur", tour + 1, "pioche une carte")
            decks[tour].append(pile.pop(0))
    while choix:
        if i >= len(decks[tour]):
            print("Le joueur", tour + 1, "pioche une carte")
            decks[tour].append(pile.pop(0))
            choix = False
        elif test_jouer(decks[tour][i]):
            print("Le joueur", tour + 1, "joue la carte", cardToString(decks[tour][i]))
            carte_actuelle = decks[tour][i]
            del (decks[tour][i])
            if carte_actuelle[0] == "Inversion":
                sens = not sens
                print("Changement de sens !")
            if carte_actuelle[0] == "Skip":
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                print("Le joueur", tour + 1, "passe son tour")
            if carte_actuelle[0] == "+2":
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                print("Le joueur", tour + 1, "pioche 2 cartes")
            if carte_actuelle[0] == "Joker":
                nb_couleurs = {"Rouge": 0, "Bleu": 0, "Vert": 0, "Jaune": 0}
                for c in decks[tour]:
                    nb_couleurs[c[1]] += 1
                best = 0
                best_couleur = ""
                for (couleur, nombre) in nb_couleurs.items():
                    if nombre > best:
                        best = nombre
                        best_couleur = couleur
                carte_actuelle = (carte_actuelle[0], best_couleur)
                print("Il a choisi la couleur " + best_couleur)
            if carte_actuelle[0] == "+4":
                nb_couleurs = {"Rouge": 0, "Bleu": 0, "Vert": 0, "Jaune": 0}
                for c in decks[tour]:
                    nb_couleurs[c[1]] += 1
                best = 0
                best_couleur = ""
                for (couleur, nombre) in nb_couleurs.items():
                    if nombre > best:
                        best = nombre
                        best_couleur = couleur
                carte_actuelle = (carte_actuelle[0], best_couleur)
                print("Il a choisi la couleur " + best_couleur)
                if sens:
                    tour += 1
                else:
                    tour -= 1
                if tour not in decks.keys():
                    if sens:
                        tour = 0
                    else:
                        tour = list(decks)[-1]
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                decks[tour].append(pile.pop(0))
                print("Le joueur", tour + 1, "pioche 4 cartes")
            choix = False
        i += 1
    choix = True
    if len(decks[tour]) == 1:
        print("UNO")
    if len(decks[tour]) == 0:
        print("Le joueur", tour + 1, "a gagné !")
        break
    if len(pile) == 0:
        reset_pile()
    time.sleep(1)
time.sleep(60)
