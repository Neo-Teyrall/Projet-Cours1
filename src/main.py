import sys

import check_file as cf
import protein

if __name__ == "__main__" :
    """TODO:: INFO """
    # para threading
    # TH.sema = th.Semaphore(20)
    print("Lancement du programme")
    filename = cf.verify_arg(sys.argv)
    if len(filename) < 3:
    	prot = protein.Protein(filename[1])
    else:
    	prot = protein.Protein(filename[1], filename[2])
    pass
