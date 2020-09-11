import atom
import protein
from vector import Vector3
class AcideAmine:
    """Acide Amine Partie de la protein contenant les atomes """


    def __init__(self, list_atomes):
        protein.Protein.Prot.acide_amines.append(self)
        self.accessibility = 0 
        self.atoms = []
        self.__add_atoms(list_atomes)
        pass


    def __add_atoms(self,list_atoms):
        for i, i_atom in enumerate(list_atoms):
            new_atom = atom.Atom(self,Vector3(X = i_atom["x"],
                                              Y = i_atom["y"],
                                              Z = i_atom["z"]))
            self.atoms.append(new_atom)


    def calc_accesibility(self):
        for i in self.atoms :
            self.accessibility += i.calc_accesibility()
        return self.accessibility    
        pass


    def __del__(self):
        #print("free AcideAmine")
        pass
