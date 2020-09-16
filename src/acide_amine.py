import atom
import protein
from vector import Vector3
from para import TH


class AcideAmine:

    """
    Acide Amine : partie de la protéine contenant les atomes
    """
    def __init__(self, list_atomes):
        protein.Protein.Prot.acide_amines.append(self)
        self.atoms = []
        self.res = ""
        self.accessibility_num = 0
        self.__add_atoms(list_atomes)
        #TH.sema.release()

    def __add_atoms(self, list_atoms):
        """
        Ajoute tous les atomes de l'acide aminé
        et attribue à l'AA son code 3 lettres.
        """
        for i, i_atom in enumerate(list_atoms):
            new_atom = atom.Atom(self, i_atom)
            self.atoms.append(new_atom)

        self.res = list_atoms[0]["AAtype"]

    def calc_accesibility(self):
        """Calcul l'accessibilité et la retourne"""
        area = 0
        area_backbone = 0
        for i, atom in enumerate(self.atoms):
            access_num, area_temp = atom.calc_accesibility()
            self.accessibility_num += access_num
            area += area_temp
            if i in range(4):
                area_backbone += access_num

        str_f = "{}{:10.3f}{:10.3f}{:10.3f}{:10.3f}\n\n"
        protein.Protein.Prot.chain_out += str_f.format(self.res,
                                                       area_backbone,
                                                       self.accessibility_num - area_backbone,
                                                       self.accessibility_num,
                                                       self.accessibility_num/area)
        return (self.accessibility_num, area)


if __name__ == "__main__":

    pass
