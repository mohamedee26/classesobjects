class Temperatursensor:
    def __init__(self, plats, temperatur):
        self.plats = plats
        self.temperatur = temperatur

    def oka_temperatur(self):
        self.temperatur += 1

    def minska_temperatur(self):
        self.temperatur -= 1

    def visa_temperatur(self):
        print(self.plats + ": " + str(self.temperatur) + " grader")


sensor1 = Temperatursensor("Köket", 20)
sensor2 = Temperatursensor("Sovrummet", 18)
sensor1.oka_temperatur()
sensor1.oka_temperatur()
sensor2.minska_temperatur()
sensor1.visa_temperatur()
sensor2.visa_temperatur()