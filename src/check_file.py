import os
import sys

def verify_arg(sys_args):
    """
    La fonction qu'un fichier a été pris en argument et qu'il peut être lu
    """
    if len(sys_args) != 2:
        exit("ERROR: NEEDS 1 PDB FILE AS ARGUMENT")
    if (os.path.exists(sys_args[1]) == False) :
        exit("ERROR: FILE DOES NOT EXIST")
    return sys_args[1]