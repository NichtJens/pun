
class Analyzer:

    def __init__(self, data):
        self.data = data
        self.seen = set()

    def follow(self, target):
        if target in self.seen:
            return
        print(">>>", target)
        self.seen.add(target)
        start = self.data[target]
        for i in start["import"]:
            self.follow(i)
        for m, n in start["from"]:
            try:
                self.follow(f"{m}.{n}")
            except Exception as e:
                print("error:", e)
                self.follow(m)
        print()

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



