import sphere
import protein
from vector import Vector3
import copy
import time


class Atom:
    """Description"""
    nb_points = 96
    voisin_rayon = 3

    def __init__(self,self_aa,position :  Vector3,a_type = 'C'):
        protein.Protein.Prot.atoms.append(self)
        self.self_aa = self_aa
        self.self_aa.atoms.append(self)
        self.position = position
        self.voisins = []
        self.points = []
        self.accessibility = 0
        self.rayon = 1
        self.a_type = a_type
        self.__creat_points()
        self.set_rayon()


    def __creat_points(self) -> None:
        self.points = sphere.calc_points(self.nb_points,self.position,None,self.rayon)

        
    def get_all_voisin(self) -> None:
        self.voisins = copy.copy(protein.Protein.Prot.atoms)
        self.voisins.remove(self)

    def set_rayon(self):
        dict_vdw = { "H" : 1.20,
                 "O" : 1.52,
                 "C" : 1.70,
                 "N" : 1.55,
                 "P" : 1.80,
                 "F" : 1.47,
                 "S" : 1.80
                 }
        self.rayon = self.rayon * dict_vdw[self.a_type[0]] + dict_vdw["O"]


    def calc_voisin(self) -> None:
        tmp_voisins = copy.copy(self.voisins)
        z = len(self.voisins)
        for i in range(len(self.voisins)):
            #print("add rayon :",(self.voisins[i].rayon + self.rayon) )
            #print("dist entre atome", self.position.dist_to(self.voisins[i].position))
            if self.position.dist_to(self.voisins[i].position)  > (self.voisins[i].rayon + self.rayon) :
                tmp_voisins.remove(self.voisins[i])
                self.voisins[i].voisins.remove(self)
        self.voisins = tmp_voisins
        print("apres nb voisin = {}           ".format(len(self.voisins)),end = '')

    def calc_accesibility(self):
        access = 0
        for point in self.points:
            for voisin in self.voisins:
                dist = voisin.position.dist_to(point)
                #print("distance = ", dist, end = " ")
                #print("rayon =", voisin.rayon)
                if (dist < voisin.rayon):
                    #print("done")
                    access += 1
                    continue
        #if access == self.nb_points:
        #    print("access = ", access, end =" ")
        access = 1.0 - (access/self.nb_points)
        
        return access

    def __del__(self):
       # print("free atom")
        pass
