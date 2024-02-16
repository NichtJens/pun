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
    every = get_every(res)
    unused = every - seen

    print(itemize(seen, "seen"))
    print(itemize(unused, "unused"))


def get_every(collected):
    every = set()
    for v in collected.values():
        for i in v["import"]:
            every.add(i)
        for m, n in v["from"]:
            every.add(m)
            every.add(f"{m}.{n}")
    return every





if __name__ == "__main__":
    main()



