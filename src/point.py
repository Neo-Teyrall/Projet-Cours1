from vector import Vector3
import traceback 
class Point():
    """Description"""
    nb_points =  0
    
    def __init__(self,X,Y,Z):
        self.position = Vector3(X= X, Y= Y ,Z= Z)
        Point.nb_points += 1
        self.num_point = Point.nb_points
        self.voisins = []
        self.occuped = False
        pass

    def connect(self, voisin) -> None:
        if voisin == self:
            return 
        if voisin in self.voisins:
            return
        self.voisins.append(voisin)
        voisin.connect(self)


    def dist_to(self, point):
        if isinstance(point, Vector3):
            return self.position.dist_to(point)
        elif isinstance(point, Point):
            return self.position.dist_to(point.position)
        else:
            traceback.print_stack()
            exit("ERROR : Impossible to evaluate the distance withe the {} Only Vecteur3, Point".format(type(point)))


    def __convert_vec_to_self(self,vec):
        self.x = a.x
        self.y = a.y
        self.z = a.z
        return self


    def __del__(self):
        pass


if __name__ == "__main__" :
    print(type(1))
    a = Point(1,1,1)
    a.dist_to(2)
   
    pass
