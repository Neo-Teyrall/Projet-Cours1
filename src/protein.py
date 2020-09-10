import acide_amine.AcideAmine

class Protein:
    """protein """
    Prot = None
    
    def __init__(self, pdb_file :str):
        Protein.Prot = self
        self.acide_amines = []
        self.Atoms = []
        pass
    

    def __del__(self):
        print("free protein")
        pass
