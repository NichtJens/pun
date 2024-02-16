
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



