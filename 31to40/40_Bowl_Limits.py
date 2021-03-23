# DomirScire

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoopes = 3

    def __init__(self, *new_scoopes):
        self.scoops = []

    def add_scoops(self, *new_scoopes):
        for one_scoop in new_scoopes:
            if len(self.scoops) < Bowl.max_scoopes:
                self.scoops.append(one_scoop)

    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

if __name__ == "__main__":
    s1 = Scoop('chocolate')
    s2 = Scoop('vanilla')
    s3 = Scoop('persimmon')
    s4 = Scoop('flavor 4')
    s5 = Scoop('flavor 5')

    b = Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    b.add_scoops(s4, s5)
    print(b)
