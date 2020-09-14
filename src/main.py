#! /usr/bin/python3.8
import protein

if __name__ == "__main__" :
    """TODO:: INFO """
    # para threading
    #TH.sema = th.Semaphore(20)
    print("lancement du programe")
    prot = protein.Protein("../data/4yu3.pdb")
    access = prot.calc_accesibility()
    print("final access", access)
    pass
