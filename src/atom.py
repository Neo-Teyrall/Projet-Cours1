import copy
import math
import time

from info import Info
from para import TH
from point import Point
import protein
import threading as th 
from vector import Vector3

class Atom:

    """
    Atome dont l'occupation sphérique est résolue par des points 
    positionnés pseudo-uniformément sur sa surface.
    """
    nb_points = 96                        # nombre de points composant la sphère
    graph_d = 0.5        # rayon pour déterminer les points de la sphère voisine
    def __init__(self,self_aa, info, graph = True, local = False):
        if not local:                 # condition pour tester la classe en local
            protein.Protein.Prot.atoms.append(self)                   # protéine
            self.self_aa = self_aa        # acide aminé dont fait partie l'atome

        self.id = info["ATnum"]
        self.position = Vector3(info["x"], info["y"], info["z"])
        self.voisins = []                                   # voisins de l'atome
        self.points = []                                   # points de la sphère
        self.rayon = Info.rayon_vdw[info["Atom"]] + Info.rayonH20      # rayon de l'atome + sonde
        self.area = 4*math.pi*(self.rayon**2)                  # aire de l'atome
        #t = th.Thread(target = self.__t)
        #TH.sema.acquire()
        #t.start()
        self.__calc_points()
        #if graph : 
        #    self.__make_graph()


    #def __t(self):
        #print("tbegin")
        #self.__calc_points() 
        #self.__make_graph()
        #print("tend")
        #TH.sema.release()


    def __calc_points(self, angle = None):
        """ Calcule la position des points de surface de l'atome.
        Reprise de l'algorithme de création de sphère de saff,
        copié et modifié depuis le packet anti_lib_progs (librairie antiprism)"""
        points = []
        use_angle = angle is not None
        if use_angle:
            ang = (angle * math.pi/180) % (2*math.pi)

        N = self.nb_points
        for k in range(1, N + 1):
            h = -1 + 2 * (k - 1) / float(N - 1)
            theta = math.acos(h)
            if k == 1 or k == N:
                phi = 0

            elif use_angle:
                phi += ang

            else:
                phi += 3.6 / math.sqrt(N * (1 - h * h))

            new_point = Point(X = math.sin(phi) * math.sin(theta),
                              Y = math.cos(phi) * math.sin(theta),
                              Z = -math.cos(theta))
            new_point.position *= self.rayon
            new_point.position += self.position
            points.append(new_point)
            phi %= 2*math.pi

        self.points = points


    def __make_graph(self):
        """Création d'un graphe de points à la surface de la sphère  """
        for i, ipoint in enumerate(self.points) :
            for j , jpoint in enumerate(self.points[i+1:]):
                d =  ipoint.dist_to(jpoint)
                if d < (1.4): # 
                    ipoint.connect(jpoint)


    def get_all_voisin(self) -> None:
        """Récupère tous les atomes de la protéine et les assigne en tant que voisin"""
        self.voisins = copy.copy(protein.Protein.Prot.atoms)
        self.voisins.remove(self)


    def calc_voisin(self) -> None:
        """Discrimine les voisins les plus éloignés afin de conserver uniquement
        les voisins qui sont dans le voisinage de l'atome"""
        tmp_voisins = copy.copy(self.voisins)
        z = len(self.voisins)
        for i in range(len(self.voisins)):

            if self.position.dist_to(self.voisins[i].position) > (self.rayon + self.voisins[i].rayon) :
                self.voisins[i].voisins.remove(self)
                tmp_voisins.remove(self.voisins[i])

        self.voisins = tmp_voisins


    def calc_accesibility(self):
        """Calcule les accessibilités relatives (rel) et quantitatives (num) de l'atome"""
        access_rel = 0
        for point in self.points:
            for voisin in self.voisins:
                dist = voisin.position.dist_to(point.position)
                if (dist < voisin.rayon):
                    access_rel += 1
                    break

        access_rel = 1.0 - (access_rel/self.nb_points)
        access_num = access_rel*self.area
        return (access_num,self.area)


    def print_atom(self):
        """Print les points de l'atome au format pdb"""
        self.__print_hetam()
        self.__print_connect()


    def __print_hetam(self):
        for i, point in enumerate(self.points) :
            p=point.position
            print("{:6s}{:5d}{:^4s}{:1s}{:3s} {:1s}{:4d}{:>4s}{:8.3f}{:8.3f}{:8.3f}"
                  .format("HETATM", point.num_point,
                          "O", "", "HOH", "A", point.num_point , "  ",
                          p.x, p.y, p.z))


    def __print_connect(self):
        for i, point in enumerate(self.points):
            if len(point.voisins) == 0 :
                continue

            print("CONECT",end = "")
            print("{:>5}".format(point.num_point), end ="")
            for j, voisin in enumerate(point.voisins):
                print("{:>5}".format(voisin.num_point), end = "")

            print()



if __name__ == "__main__" :
    p = Atom(None, {"x":0, "y":0,"z":0,"Atom":'P'}, local = True)
    p.print_atom()

