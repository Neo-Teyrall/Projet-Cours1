import atom
import protein
from vector import Vector3
from para import TH
class AcideAmine:
    """Acide Amine Partie de la protein contenant les atomes """


    def __init__(self, list_atomes):
        protein.Protein.Prot.acide_amines.append(self)
        self.accessibility = 0 
        self.atoms = []
        self.__add_atoms(list_atomes)
        #TH.sema.release()
        pass


    def __add_atoms(self,list_atoms):
        """Ajoute tout les atome de l'acide aminé"""
        for i, i_atom in enumerate(list_atoms):
            new_atom = atom.Atom(self,i_atom)
            self.atoms.append(new_atom)


    def calc_accesibility(self):
        """calcule l'accessibilité et la retourn"""
        for i in self.atoms :
            self.accessibility += i.calc_accesibility()

        return self.accessibility / len(self.atoms)   



    def __del__(self):
        #print("free AcideAmine")
        pass


if __name__ == "__main__" :
    
    pass
