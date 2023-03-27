from noeud2 import Noeud2

class Arbre:
    def __init__(self, racine=None):
        self.racine = racine

    def inserer(self, valeur):
        if self.racine is None:
            self.racine = Noeud2(valeur, valeur)
        else:
            # Trouver la feuille d'insertion et conserver le chemin
            chemin = []
            noeud = self.racine
            while not noeud.estfeuille():
                chemin.append(noeud)
                if valeur < noeud.idl:
                    noeud = noeud.enfantG
                elif noeud.idr is not None and valeur < noeud.idr:
                    noeud = noeud.enfantM
                else:
                    noeud = noeud.enfantD

            # Insérer la valeur dans la feuille d'insertion
            if noeud.enfantG is None:
                noeud.enfantG = Noeud2(valeur, valeur)
            elif noeud.enfantM is None:
                noeud.enfantM = Noeud2(valeur, valeur)
            elif noeud.enfantD is None:
                noeud.enfantD = Noeud2(valeur, valeur)
            else:
                # Si la feuille est pleine, appeler récursivement la fonction d'insertion sur le parent
                parent = chemin.pop()
                self.inserer_valeur_parent(parent, valeur)

    def inserer_valeur_parent(self, parent, valeur):
        if parent.enfantG is None:
            parent.enfantG = Noeud2(valeur, valeur)
        elif parent.enfantM is None:
            parent.enfantM = Noeud2(valeur, valeur)
        elif parent.enfantD is None:
            parent.enfantD = Noeud2(valeur, valeur)
        else:
            # Si le parent est également plein, appeler récursivement la fonction d'insertion sur le parent suivant
            noeud = parent
            while not noeud.estfeuille():
                if valeur < noeud.idl:
                    noeud = noeud.enfantG
                elif noeud.idr is not None and valeur < noeud.idr:
                    noeud = noeud.enfantM
                else:
                    noeud = noeud.enfantD
            parent_suivant = chemin.pop()
            self.inserer_valeur_parent(parent_suivant, valeur)
