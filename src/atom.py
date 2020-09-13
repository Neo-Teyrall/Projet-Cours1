import protein
from vector import Vector3
import copy
import time
import math
from point import Point
# from para import TH
# import threading as th 

class Atom:
    """Atom résolue dont l'occupation sphérique est résolue par la des points positionner pseudo uniformément sur sa surface."""
    nb_points = 96                         # nombre de point composant la sphere
    voisin_rayon = 5                   # rayon pour déterminer les atoms voisins
    graph_d = 0.5          # rayon pour déterminer les point de la sphere voisin
    def __init__(self,self_aa, position :  Vector3, graph = True, local = False):
        if not local:                  # condition pour tester la class en local
            protein.Protein.Prot.atoms.append(self)                    # protein
            self.self_aa = self_aa              # acide amine que l'atom compose
            self.self_aa.atoms.append(self) 

        self.position = position
        self.voisins = []                                     # voisin de l'atom
        self.points = []                                    # point de la sphere
        self.rayon = 1                                 # rayon de l'atom + sonde
        # t = th.Thread(target = self.__t)
        # TH.sema.acquire()
        # t.start()
        self.__calc_points()
        if graph : 
            self.__make_graph()

    # def __t(self):
    #     print("tbegin")
    #     self.__calc_points() 
    #     self.__make_graph()
    #     print("tend")
    #     TH.sema.release()


    def __calc_points(self, angle = None):
        """ calcule la posiiton des points de surface de l'atom
        reprise de l'algoryhtme de sphère de saff copié et modifié depuis le
        packet anti_lib_progs"""
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
        """création d'un graphe de point a la surface de la sphère  """
        for i, ipoint in enumerate(self.points) :
            for j , jpoint in enumerate(self.points[i+1:]):
                d =  ipoint.dist_to(jpoint)
                if d < 0.5:
                    ipoint.connect(jpoint)


    def get_all_voisin(self) -> None:
        """récupère tout les atomes de la protéine et les assigne en tant que voisin"""
        self.voisins = copy.copy(protein.Protein.Prot.atoms)
        self.voisins.remove(self)


    def calc_voisin(self) -> None:
        """discrimine les voisin les plus éloigné afin de conserver uniquement
        les voisin qui sont dans le voisinage de l'atome"""
        tmp_voisins = copy.copy(self.voisins)
        z = len(self.voisins)
        for i in range(len(self.voisins)):
            if self.position.dist_to(self.voisins[i].position) > Atom.voisin_rayon :
                self.voisins[i].voisins.remove(self)
                tmp_voisins.remove(self.voisins[i])

        self.voisins = tmp_voisins
        print("apres nb voisin = {}           ".format(len(self.voisins)),end = '')


    def calc_accesibility(self):
        """Calcule et retourne l'accessibilité de l'atome"""
        accessibility = 0
        return accessibility
        pass


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


    def __del__(self):
        pass


if __name__ == "__main__" :
    # from acide_amine import AcideAmine
    p = Atom(None, Vector3(0,0,0), local = True)
    p.print_atom()
