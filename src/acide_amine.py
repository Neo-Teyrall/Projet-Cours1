import atom.Atom
import protein.Protein
class AcideAmine:
    """Acide Amine Partie de la protein contenant les atomes """


    def __init__(self):
        protein.Protein.acide_amines.append(self)
        self.Atoms = []
        pass




    def __del__(self):
        print("free AcideAmine")
        pass
