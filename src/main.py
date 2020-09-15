#! /usr/bin/python3.8
import sys

import check_file as cf
import protein

if __name__ == "__main__" :
    """TODO:: INFO """
    # para threading
    # TH.sema = th.Semaphore(20)
    print("lancement du programe")
    filename = cf.verify_arg(sys.argv)
    prot = protein.Protein(filename[1], filename[2])
    pass
