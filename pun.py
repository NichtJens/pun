#!/usr/bin/env python
import argparse

from collect import collect
#from jsonext import json_save
from analyzer import Analyzer
from printing import itemize


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("folder")
    parser.add_argument("-i", "--ignore", nargs="*")
    parser.add_argument("-t", "--targets", nargs="*")

    clargs = parser.parse_args()

    res = collect(clargs.folder, clargs.ignore)

#    json_save(res, "res.json")

    ana = Analyzer(res)

    targets = clargs.targets
    for target in targets:
         ana.follow(target)

    seen = ana.seen
    unused = ana.unused

    print(itemize(seen, "seen"))
    print(itemize(unused, "unused"))





if __name__ == "__main__":
    main()



