class Noeud2:
    idl : int
    idr : int
    enfantG: int
    enfantM: int
    enfantD: int

    def __init__(self, idl, idr, enfantG=None, enfantM=None, enfantD=None) -> None:
        self.idl = idl
        self.idr = idr
        self.enfantG = enfantG
        self.enfantM = enfantM
        self.enfantD = enfantD

    ## Si feuille retourne True sinon retourne False.
    def estfeuille(self):
        return self.enfantG is None and self.enfantM is None and self.enfantD is None

    ## Verifie si valeur présent dans arbre
    def contient(self, valeur):
        if self.idl == valeur or self.idr == valeur:
            return True
        elif self.estfeuille():
            return False
        elif valeur < self.idl:
            return self.enfantG.contient(valeur)
        elif self.idr is not None:
            if valeur < self.idr:
                return self.enfantM.contient(valeur)
            else:
                return self.enfantD.contient(valeur)
        else:
            return self.enfantD.contient(valeur)

    ## Insertion valeur dans arbre: si TRUE insertion réussi, si FALSE insertion impossible
    def insertValeur(self, valeur):
        if valeur == self.contient(valeur):
            return False
        
    def findFeuilleInsertion(self, valeur):
        if valeur < self.idl:
            if valeur < self.enfantG:
                return
            else:
                return
        elif self.idr is not None:
            if valeur < self.idr:
                if valeur < self.enfantG:
                    return
                elif valeur < self.enfantM:
                    return
                else:
                    return
            elif valeur < self.idr:
                return self.enfantD.contient(valeur)
        else:
            return self.enfantD.contient(valeur)
    
    def insertIntoNoeud(self, valeur):
        return