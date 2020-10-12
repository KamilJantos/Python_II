"""docstring dla modułu"""

class Pojazd:
    """ docstring dla klasy """
    sygnal = "Piiib piiib"

    def __init__(self, kolor, marka):
        self.kolor = kolor
        self.marka = marka
        pass

    def hamuj(self):
        """
         zatrzymaj samochód
         """
        return "hamuję..."

    def jedz(self):
        """
        jedziemy dalej
        """
        return "%s jedzie dalej" % self.marka


class Opel_Omega(Pojazd):
    def hamuj(self):
        return "hamuje dość szybko..."


pojazd = Pojazd("niebieski", "Ford")
print(pojazd.hamuj())
print(pojazd.jedz())

opel = Opel_Omega("zielony", "Opel")
print(opel.hamuj())
print(opel.jedz())
