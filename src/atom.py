import sphere
import protein
from vector import Vector3
import copy
import time


class Atom:
    """Description"""
    nb_points = 96
    voisin_rayon = 5
    def __init__(self,self_aa,position :  Vector3):
        protein.Protein.Prot.atoms.append(self)
        self.self_aa = self_aa
        self.self_aa.atoms.append(self)
        self.position = position
        self.voisins = []
        self.points = []
        self.__creat_points()



    def __creat_points(self) -> None:
        self.points = sphere.calc_points(self.nb_points,self.position)

        
    def get_all_voisin(self) -> None:
        self.voisins = copy.copy(protein.Protein.Prot.atoms)
        self.voisins.remove(self)


    def calc_voisin(self) -> None:
        tmp_voisins = copy.copy(self.voisins)
        z = len(self.voisins)
        for i in range(len(self.voisins)):
            if self.position.dist_to(self.voisins[i].position)  > Atom.voisin_rayon :
                tmp_voisins.remove(self.voisins[i])
                self.voisins[i].voisins.remove(self)
        self.voisins = tmp_voisins
        print("apres nb voisin = {}           ".format(len(self.voisins)),end = '')


    def calc_accesibility(self):
        accessibility = 0 
        return accessibility
        pass


    def __del__(self):
       # print("free atom")
        pass
