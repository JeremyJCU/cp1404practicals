from musician import Musician

class Band:
    def __init__(self, name = "", musicians = None):
        if musicians is None:
            musicians = []
        self.musicians = musicians
        self.name = name

    def __str__(self):
        band_string = ""
        band_string += self.name
        for musician in self.musicians:
            band_string += " " + str(musician)
        return band_string

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        musician_string = ""
        for musician in self.musicians:
            musician_string += musician.play() + "\n"
        return musician_string

from guitar import Guitar

if __name__ == "__main__":
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    print(nuno)
    band.add(nuno)
    print(band)