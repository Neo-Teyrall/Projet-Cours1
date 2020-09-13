#! /usr/bin/python3.8
import protein
import Bio
import Bio.PDB

import acide_amine as aa
import atom
import protein
import sphere

if __name__ == "__main__" :
    """TODO:: INFO """
    print("ok")
    prot = protein.Protein("../data/4yu3.pdb")
    access = prot.calc_accesibility()
    print("final access", access)
    pass
