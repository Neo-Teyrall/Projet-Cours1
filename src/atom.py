import sphere
import protein.Protein

class Atom:
    """Description"""


    Atom.nb_points = 96
    def __init__(self,self_aa,position :  Vec):
        protein.Protein.Prot.Atoms.append(self)
        self.self_aa = self_aa
        self.self_aa.Atoms.append(self)
        self.position = position
        self.points
        self.__creat_points()
        pass

    def __creat_points(self, pos : int) -> None:
        self.points = sphere.calc_points(self.nb_points,self.position)

    def __del__(self):
        print("free atom")
        pass
