
class Analyzer:

    def __init__(self, data):
        self.data = data
        self.seen = set()


    def follow(self, target, level=0):
        arrow = make_arrow(level)

        if target in self.seen:
            print(arrow, target, "[SEEN]")
            return

        self.seen.add(target)

        try:
            start = self.data[target]
        except KeyError:
            print(arrow, target, "[UNKNOWN]")
            raise

        print(arrow, target)

        for i in start["import"]:
            self.follow(i, level=level+1)

        for m, n in start["from"]:
            try:
                self.follow(f"{m}.{n}", level=level+1)
            except KeyError:
                self.follow(m, level=level+1)


    @property
    def unused(self):
        return self.every - self.seen

    @property
    def every(self):
        res = set()
        for v in self.data.values():
            for i in v["import"]:
                res.add(i)
            for m, n in v["from"]:
                res.add(m)
                res.add(f"{m}.{n}")
        return res



def make_arrow(lvl):
    if lvl == 0:
        return "@"
    bar = "---" * lvl
    return bar[:-1] + ">"



