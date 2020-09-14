import acide_amine
import re
# from para import TH
# import threading as th
from  datetime import datetime
class Protein:
    """protein """
    Prot = None


    def __init__(self, pdb_file :str):
        Protein.Prot = self
        self.acide_amines = []
        self.atoms = []
        self.Atypes = []
        self.load_protein(pdb_file)
        print("all atom type = : \n ", self.Atypes)
        self.accessibility  = 0
        self.voisin_organisation()
        self.calc_accesibility()
        
        pass


    def load_protein(self, pdb_file : str) -> None:
        """charge la proteine"""
        AAindex = -1
        liste_Atom_AA = []
        print("\ncreation de la protein")
        t_i  = datetime.now()
        with open(pdb_file,"r") as fillin:
            lines = fillin.readlines()

            for i, line in enumerate(lines):
                print("\r {} / {}".format(i,len(lines)),end = "")

                if not re.match("^ATOM",line) :
                    continue

                atom = self.__parse(line)
                if atom["AAnum"] != AAindex:
                    AAindex = atom["AAnum"]

                    if len(liste_Atom_AA) != 0:
                        # t1 = th.Thread(target=acide_amine.AcideAmine,
                        #                args = (liste_Atom_AA,))
                        # TH.sema.acquire()
                        # t1.start()
                        acide_amine.AcideAmine(liste_Atom_AA)

                    liste_Atom_AA = []

                liste_Atom_AA.append(atom)

        print(" temp = {}".format(datetime.now()-t_i))


    def voisin_organisation(self):
        """calcule des Atom les plus proche entre eux (voisin) """
        print("\n copy des voisin")
        for i,atom in enumerate(self.atoms):
            print("\r {}/{}     ".format(i,len(self.atoms)),end="")
            atom.get_all_voisin()

        print("\n evaluation des voisin")
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
        if not splitted_line["Atom"] in self.Atypes:
            self.Atypes.append(splitted_line["Atom"])
        return splitted_line
        pass


    def calc_accesibility(self):
        print("\n  calc acces : ") 
        for i, acide_amine in enumerate(self.acide_amines):
            print("\r {} / {}".format(i,len(self.acide_amines)),end = "")
            self.accessibility +=  acide_amine.calc_accesibility()

        acc = self.accessibility / len(self.acide_amines)
        print("final access", acc)
        return acc


    def __del__(self):
        Protein.Prot = None
        print("free protein")
        pass
