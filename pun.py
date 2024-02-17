#!/usr/bin/env python
import argparse

from analyze import analyze
from collect import collect
#from utils import json_save


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("folder")
    parser.add_argument("-i", "--ignore", nargs="*")
    parser.add_argument("-t", "--targets", nargs="*")

    clargs = parser.parse_args()

    res = collect(clargs.folder, clargs.ignore)

#    json_save(res, "res.json")

    analyze(res, clargs.targets)





if __name__ == "__main__":
    main()



