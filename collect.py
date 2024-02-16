from ast_read import ast_read
from collector import Collector
from scripts import find_scripts, fn_to_module


def collect(path, ignore):
    res = {}

    fnames = find_scripts(path)
    for fn in fnames:
#        print(fn)

        tree = ast_read(fn)

        scr = fn_to_module(path, fn)
        print("<<<", scr)

        coll = Collector(scr, ignore=ignore)
        coll.visit(tree)
        coll.report()

        print("-"*10)

        scr = scr if not scr.endswith(".__init__") else scr[:-len(".__init__")]

        res[scr] = coll.collected

    return res



