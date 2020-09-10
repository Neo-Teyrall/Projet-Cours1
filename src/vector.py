import math

class Vector3():
    "class de vecteur a trois dimmension"

    def __init__(self,X=0,Y=0,Z=0, random = False):
        """initialisation"""
        self.x = float(X)
        self.y = float(Y)
        self.z = float(Z)
        pass


    def __str__(self):
        """ sortie str """
        return "({}\t{}\t{})".format(self.x,self.y,self.z)


    def __add__(self,add):
        """ addition de vector 3 """
        if isinstance(add, int) or isinstance(add, float):
            return Vector3(self.x + add,
                        self.y + add,
                        self.z + add)
        else : 
            return Vector3(self.x + add.x,
                        self.y + add.y,
                        self.z + add.z)


    def __sub__(self,sub):
        """ soustraction de vector 3 """
        if isinstance(sub, int) or isinstance(sub, float):
            return Vector3(self.x - sub,
                        self.y - sub,
                        self.z - sub)
        return Vector3(self.x - sub.x,
                    self.y - sub.y,
                    self.z - sub.z)


    def __mul__(self,mul):
        """ multiplication de vector 3 """
        if isinstance(mul, int) or isinstance(mul, float):
            return Vector3(self.x * mul,
                        self.y * mul,
                        self.z * mul)
        return Vector3(self.x * mul.x,
                    self.y * mul.y,
                    self.z * mul.z)

    def __floordiv__(self, fdiv):
        """ division   de vector 3 """
        print("floodiv",fdiv)
        if isinstance(fdiv, int) or isinstance(fdiv, float):
            return Vector3(self.x // fdiv,
                        self.y // fdiv,
                        self.z // fdiv)
        return Vector3(self.x // fdiv.x,
                    self.y // fdiv.y,
                    self.z // fdiv.z)

    def __truediv__(self, tdiv):
        """ division vrais de vector 3 """
       # print("truediv",tdiv)
        if isinstance(tdiv, int) or isinstance(tdiv, float):
            return Vector3(self.x / tdiv,
                        self.y / tdiv,
                        self.z / tdiv)
        return Vector3(self.x / tdiv.x,
                    self.y / tdiv.y,
                    self.z / tdiv.z)


    def __pow__(self,p):
        """ puissance de vector 3 """
        if isinstance(p, int) or isinstance(p, float):
            return Vector3(self.x ** p,
                        self.y ** p,
                        self.z ** p)
        exit( "Erreur, impossible de faire la puissance")


    def dist_to(self,point):
        "calcule de la distance entre 2 vecteur3"
        return math.sqrt((self.x - point.x)**2
                         + (self.y - point.y)**2
                         + (self.z - point.z)**2 )
    def norm(self):
        "Calcule de la norm du vecteur3"
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)


if __name__ ==  "__main__":
    a = Vector3(1,2,3)
    b = Vector3(3,2,1)
    print("*", a + b )
    print("-", a - b )
    print("*", a * b )
    print("/", a / b )

    print("*", a + 1 )
    print("-", a - 1 )
    print("*", a * 2 )
    print("/", a / 2.26 )
    pass

