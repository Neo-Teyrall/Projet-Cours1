import acide_amine
import Bio
import Bio.PDB
import re
class Protein:
    """protein """
    Prot = None
    
    def __init__(self, pdb_file :str):
        Protein.Prot = self
        self.acide_amines = []
        self.atoms = []
        self.load_protein(pdb_file)
        self.accessibility  = 0 
        self.voisin_organisation()
        pass

    
    def load_protein(self, pdb_file : str) -> None:
        """charge la proteine"""
        AAindex = -1
        liste_Atom_AA = []
        with open(pdb_file,"r") as fillin:
            for i in fillin:
                if not re.match("^ATOM",i) :
                    continue
                atom = self.__parse(i)
                if atom["AAnum"] != AAindex:
                    AAindex = atom["AAnum"]
                    
                    if len(liste_Atom_AA) != 0:
                        acide_amine.AcideAmine(liste_Atom_AA)
                    liste_Atom_AA = []
                liste_Atom_AA.append(atom)


    def voisin_organisation(self):
        """calcule des Atom les plus proche entre eux (voisin) """
        for i,atom in enumerate(self.atoms):
            print("\r {}/{}     ".format(i,len(self.atoms)),end="")
            atom.get_all_voisin()
        for i, atom in enumerate(self.atoms):
            print("\r {}/{}     ".format(i,len(self.atoms)),end="")
            atom.calc_voisin()


    def __parse(self, line : str) -> list:
        """parse le document pdb """
        splitted_line = {"type" : line[:6].split()[0].replace(" ",""),
                         "ATnum" : int(line[6:11].split()[0].replace(" ","")),
                         "Atype" : line[12:16].split()[0].replace(" ",""),
                         "AAtype" : line[17:20].split()[0].replace(" ",""),
                         "chain" : line[21].replace(" ",""),
                         "AAnum" : int(line[22:26].split()[0].replace(" ","")),
                         "x" : float(line[30:38].replace(" ","")),
                         "y" : float(line[38:46].replace(" ","")),
                         "z" : float(line[46:54].replace(" ","")),
                         "occupancy": float(line[54:60].replace(" ","")),
                         "TF":float(line[60:66].replace(" ","")),
                         "Atom" : line[76:78].replace(" ",""),
                         "charge": line[78:80].replace(" ","")}
        return splitted_line
        pass


    def calc_accesibility():
        for i in self.acide_amines:
           self.accessibility +=  i.calc_accesibility()


    def __del__(self):
        Protein.Prot = None
        print("free protein")
        pass
