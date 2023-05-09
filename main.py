def rendre_monnaie(montant, liste_monnaie, caisse):
    liste_monnaie.sort(reverse=True)
    rendu = []
    for valeur in liste_monnaie:
        while montant >= valeur and caisse.get(valeur, 0) > 0:
            rendu.append(valeur)
            montant -= valeur
            caisse[valeur] -= 1
    if montant == 0:
        return rendu
    else:
        return None

montant_a_rendre = 25698
liste_monnaie = [500, 200, 100, 50, 20, 10, 5, 2, 1]
caisse = {500: 5, 200: 10, 100: 20, 50: 50, 20: 100, 10: 200, 5: 500, 2: 1000, 1: 2000}

rendu = rendre_monnaie(montant_a_rendre, liste_monnaie, caisse)
print(rendu)
