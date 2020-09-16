import os


def verify_arg(file):
    """
    Vérifie qu'un fichier de lecture et un fichier de sortie
    ont été pris en arguments et que le pdb peut être lu.
    """
    if (os.path.exists(file) == False):
        exit("ERROR: PDB file does not exist")
