class Fahrzeug:
    # Konstruktormethode
    def __init__(self, bez="(leer)",ge=0):
        self.bezeichnung=bez
        self.geschwindigkeit=ge
    
    # Destruktormethode
    def __del__(self):
        print("Objekt", self.bezeichnung, "entfernt")

    def beschleunigen(self,wert):
        self.geschwindigkeit +=wert
        self.ausgabe()

    def ausgabe(self):
        print(self.bezeichnung, self.geschwindigkeit,"km/h")


# Objekte der Klasse erzeugen
opel = Fahrzeug("Opel Admiral",40)
volvo = Fahrzeug("Volvo Amazon")
ford = Fahrzeug("Ford Mondeo")
mercedes = Fahrzeug(ge=60)

# Objekte betrachten
opel.ausgabe()
volvo.ausgabe()
ford.ausgabe()
mercedes.ausgabe()

# Objektmethoden
opel.beschleunigen(40)
ford.beschleunigen(-3)


# Objekte betrachten
opel.ausgabe()
ford.ausgabe()

# Destruktor aufrufen
#del opel
#del mercedes

# aufruf nicht mehr möglich
opel.ausgabe()