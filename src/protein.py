import acide_amine
import re
# from para import TH
# import threading as th
from  datetime import datetime
class Protein:

    """
    Protéine : classe principale depuis laquelle est calculé l'accessibilité
    """
    Prot = None
    def __init__(self, pdb_file :str, filename = None):
        Protein.Prot = self
        self.acide_amines = []
        self.atoms = []
        self.Atypes = []
        self.filename = filename
        self.chain_out = "{:3}{:>10}{:>10}{:>10}{:>10}\n".format("RES","backbone","sidechain","total","%")
        self.load_protein(pdb_file)
        print("all atom type = : \n ", self.Atypes)
        self.accessibility_num = 0
        self.voisin_organisation()
        self.calc_accesibility()


    def load_protein(self, pdb_file : str) -> None:
        """Charge la proteine"""
        AAindex = -1
        liste_Atom_AA = []
        print("\ncréation de la protéine")
        t_i  = datetime.now()
        with open(pdb_file,"r") as fillin:
            lines = fillin.readlines()
            for i, line in enumerate(lines):
                print("\r {} / {}".format(i+1,len(lines)),end = "")
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

        print(" temps = {}".format(datetime.now()-t_i))


    def voisin_organisation(self):
        """Calcule des atomes les plus proches entre eux (voisins) """
        print("\n copie des voisins")
        t_i  = datetime.now()
        for i,atom in enumerate(self.atoms):
            print("\r {}/{}     ".format(i+1,len(self.atoms)),end="")
            atom.get_all_voisin()

        print(" temps = {}".format(datetime.now()-t_i))

        print("\n évaluation des voisins")
        t_i  = datetime.now()
        for i, atom in enumerate(self.atoms):
            print("\r {}/{}     ".format(i+1,len(self.atoms)),end="")
            atom.calc_voisin()

        print(" temps = {}".format(datetime.now()-t_i))


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


    def calc_accesibility(self):
        print("\n  calc access : ")
        t_i  = datetime.now()
        area = 0
        for i, acide_amine in enumerate(self.acide_amines):
            print("\r {} / {}".format(i+1,len(self.acide_amines)),end = "")
            access_num, area_temp = acide_amine.calc_accesibility()
            self.accessibility_num += access_num
            area += area_temp

        print(" temps = {}\n".format(datetime.now()-t_i))
        acc_rel = self.accessibility_num / area

        self.chain_out += "\n------------------------------\n\n"
        self.chain_out += "Final access %   : {:.4f}\n".format(acc_rel)
        self.chain_out += "Final access Å^2 : {:.4f}\n\n".format(self.accessibility_num)
        self.chain_out += "\n------------------------------\n\n"

        if self.filename is not None:
            with open(self.filename, "w") as filout:
                filout.write(self.chain_out)
        else:
            print(self.chain_out)

        return (acc_rel, self.accessibility_num)


    def __del__(self):
        Protein.Prot = None
        print("free protein")
