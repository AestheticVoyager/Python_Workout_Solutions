# DomirScire

class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

    def create_scoops(self):
        scoops = [Scoop('chocolate'),
                  Scoop('vanilla'),
                  Scoop('persimmon')]
        for scoop in scoops:
            print(scoop.flavor)

if __name__ == "__main__":
    a=Scoop('vanilla')
    a.create_scoops()
