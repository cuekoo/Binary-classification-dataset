#!/usr/bin/python

def usage():
    print ""
    print "Generate 2D points and save as a .csv file"
    print "  \'n\': change mode"
    print "  \'c\': clear data"
    print "  \'d\': save as csv file"

import ptsgen2d as p2
import matplotlib.pyplot as plt


def generate_dataset():

    usage()

    f = plt.figure()
    a = p2.PtsGen2d(f)
    plt.show()


from matplotlib.colors import ListedColormap
cm_bright = ListedColormap(['#0000FF', '#FF0000'])

def show_dataset(data):

    plt.scatter(data[:, 1], data[:, 2], c=data[:, 0], cmap=cm_bright)
    plt.show()

import argparse as ap
import numpy as np

def main():

    parser = ap.ArgumentParser(description="2D dataset for machine learning\
            utilities")

    parser.add_argument("--show", help="show dataset (.csv)")
    parser.add_argument("--generate", 
                        help="save result as eps",
                        action="store_true")
    args = parser.parse_args()

    if args.generate:
        generate_dataset()
        return

    if args.show:
        data = np.loadtxt(args.show, delimiter=',')
        show_dataset(data)
        return

if __name__ == "__main__":
    main()

