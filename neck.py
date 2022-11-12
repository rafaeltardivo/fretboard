

class Neck:
    """Guitar neck text generator."""

    def __init__(self, fret_count:int=21, string_count:int=6):
        self.fret_count = fret_count
        self.string_count = string_count

    def generate_frets(self, fret_distance:int, fret_count:int):
        return ("-" * fret_distance + "|") * fret_count

    def generate(self):
         
        print("\\")
        for _ in range(self.string_count):
            base = self.generate_frets(5, 12)
            octaves = self.generate_frets(3, self.fret_count - 12)
            print(" |" + base + octaves)
        print("/")

if __name__ == "__main__":
    n = Neck(21)
    n.generate()

    