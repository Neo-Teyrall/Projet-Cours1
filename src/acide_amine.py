import atom
import protein
from vector import Vector3
from para import TH
class AcideAmine:
    """Acide Amine : partie de la protéine contenant les atomes """


    def __init__(self, list_atomes):
        protein.Protein.Prot.acide_amines.append(self)
        self.accessibility_rel = 0
        self.accessibility_num = 0
        self.atoms = []
        self.res = ""
        self.__add_atoms(list_atomes)
        #TH.sema.release()
        pass

    def __add_atoms(self,list_atoms):
        """Ajoute tous les atomes de l'acide aminé"""
        for i, i_atom in enumerate(list_atoms):
            new_atom = atom.Atom(self,i_atom)
            self.atoms.append(new_atom)
        #print(i_atom["AAtype"])
        #print(list_atoms[0]["AAtype"])
        self.res = list_atoms[0]["AAtype"]
        #self.res = i_atom["AAtype"]


    def calc_accesibility(self):
        """Calcul l'accessibilité et la retourne"""
        area = 0
        for atom in self.atoms :
            #print("ID atom from AA", atom.id)
            access_rel, access_num, area_temp = atom.calc_accesibility()
            self.accessibility_rel += access_rel
            self.accessibility_num += access_num
            area += area_temp

        protein.Protein.Prot.filout.write("{:1}\t{:6.4f}\t{:10.4f}\n\n".format(self.res,self.accessibility_rel/len(self.atoms), self.accessibility_num))
        return (self.accessibility_rel / len(self.atoms), self.accessibility_num, area)



    def __del__(self):
        #print("free AcideAmine")
        pass


if __name__ == "__main__" :
    
    pass
