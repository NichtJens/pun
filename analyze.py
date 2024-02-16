from analyzer import Analyzer
from printing import itemize


def analyze(data, targets):
    ana = Analyzer(data)

    for target in targets:
         ana.follow(target)

    print(itemize(ana.seen, "seen"))
    print(itemize(ana.unused, "unused"))



