class Produkt:
    def __init__(self, namn, pris, lager):
        self.namn = namn
        self.pris = pris
        self.lager = lager

    def salj(self):
        if self.lager > 0:
            self.lager -= 1
        else:
            print("Produkten är slut i lager!")

    def visa_info(self):
        print("Produkt:", self.namn)
        print("Pris:", self.pris, "kr")
        print("Lager:", self.lager)

    def fyll_pa(self, antal):
        self.lager += antal


produkt1 = Produkt("Tangentbord", 399, 10)
produkt2 = Produkt("Mus", 199, 5)
produkt1.salj()
produkt1.visa_info()
produkt1.fyll_pa(5)
produkt1.visa_info()
