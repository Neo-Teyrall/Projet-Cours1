import argparse
import sys

import check_file as cf
from info import Info
import protein


if __name__ == "__main__":
    """TODO:: INFO """
    # para threading
    # TH.sema = th.Semaphore(20)

    parser = argparse.ArgumentParser(description='Calculation of the surface accessible to the solvent.')
    parser.add_argument('pdb_file', type=str,
                        help='an input file (pdb format)')
    parser.add_argument('--file_out', type=str,
                        help='an output file to store the results')
    parser.add_argument('--probe', type=float,
                        help='radius of the probe (Å)')
    args = parser.parse_args()
    cf.verify_arg(args.pdb_file)

    if args.probe is not None:
        if args.probe > 0:
            Info.rayonH20 = args.probe
        else:
            exit("ERROR: Radius is negative")

    print("Lancement du programme")
    prot = protein.Protein(args.pdb_file, args.file_out)
