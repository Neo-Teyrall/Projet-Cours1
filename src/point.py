from vector import Vector3

class Point(Vector3):

    """Description"""


    def __init__(self,X,Y,Z):
        super().__init__(X= X, Y= Y, Z= Z)
        self.occuped = False
        pass




    def __del__(self):
        pass
