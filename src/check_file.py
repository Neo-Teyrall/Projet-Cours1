import os
import sys

def verify_arg(sys_args):
    """
    Vérifie qu'un fichier de lecture et un fichier de sortie
    ont été pris en arguments et que le pdb peut être lu.
    """
    if len(sys_args) < 2 or len(sys_args) > 3:
        exit("ERROR: NEEDS AT LEAST 1 PDB FILE AS ARGUMENT (OPTION : OUTPUT FILE)")

    if (os.path.exists(sys_args[1]) == False) :
        exit("ERROR: PDB FILE DOES NOT EXIST")

    return sys_args