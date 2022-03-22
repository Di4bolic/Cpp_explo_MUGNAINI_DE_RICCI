# Importations

import random
from tabnanny import check
import time

# Def de la classe mère

class Poisson:
    def __init__(self,nom):
        # Nom
        self.nom = nom
        # Affection
        self.affection = 0
        # Faim
        self.faim = 0
        # Fatigue
        self.fatigue = 0
        self.endormi = False
        # PV
        self.pv = 10

    def affiche(self):
        print("\nStatistiques de " + self.nom + " :\n\nPV : " + str(self.pv) + " :\nAffection : " + str(self.affection) + "\nFaim : " + str(self.faim) + "\nFatigue : " + str(self.fatigue) + "\nEndormi : " + str(self.endormi) + "\n")

    def getName(self):
        return poisson.nom

    def testMort(self):
        if self.pv <= 0:
            return True
        else:
            return False

    def nourrir(self, typeNourriture):
        if self.endormi == True:
            print(self.nom + " dort , tu ne peux pas le nourrir ...")
        else:
            if typeNourriture == 1:
                self.faim -= 2
                self.affection += 4
            elif typeNourriture == 2:
                self.faim -= 3
                self.affection += 3
            else:
                self.faim -= 6
                self.affection += -3
            if self.faim < 0:
                self.faim = 0

    def caresser(self):
        self.affection += 10

    def actionFin(self):
        # Fatigue
        if self.endormi == True:
            self.endormi = False
        if self.fatigue >= 10:
            self.endormi = True
            self.fatigue = 0
        # Faim
        if self.faim >= 10:
            self.pv -= 2
        

# Def du poisson de base

class BlobFish(Poisson):
    def __init__(self,nom):
        Poisson.__init__(self,nom)
        self.maxAffection = 100
        # Cri
        self.cri = "Blob blob blob"
        self.tauxCri = 2
        # PV
        self.pv = 10

# Def du poisson rare

class PoissonVipère(Poisson):
    def __init__(self,nom):
        Poisson.__init__(self,nom)
        self.maxAffection = 500
        # Cri
        self.cri = "Crr crr !"
        self.tauxCri = 4
        # PV
        self.pv = 20

# Def du poisson épique

class BaudroieAbyssale(Poisson):
    def __init__(self,nom):
        Poisson.__init__(self,nom)
        self.maxAffection = 1000
        # Cri
        self.cri = "*Hurlements*"
        self.tauxCri = 4
        # PV
        self.pv = 50

    def actionDebut(self):
        # Fatigue
        if random.randint(1,2) == 1:
            self.fatigue += 1
        # Faim
        if random.randint(1,2) == 1:
            self.faim += random.randint(1,5)
        # Affection
        if random.randint(1,5) == 1:
            self.affection -= random.randint(1,10)


# Choix du poisson

choix = int(input("\nChoisissez votre poisson :\n\n1) Blob fish\n2) Poisson-vipère\n3) Baudroie abyssale\n\nEcrivez ici votre choix : "))
time.sleep(1)
nom = input("\nDonnez un nom à votre nouvel ami : ")
time.sleep(1)

if choix == 1:
    poisson = BlobFish(nom)
elif choix == 2:
    poisson = PoissonVipère(nom)
else:
    poisson = BaudroieAbyssale(nom)

# Boucle principale

poisson.affiche()
print("Pour le moment tout va bien , vous devrez maintenant prendre soin de " + poisson.getName() + "en le nourissant et en le cajolant pour parvenir à le domestiquer !")
time.sleep(3)

while poisson.testMort() == False:
    poisson.actionDebut()
    poisson.affiche()
    time.sleep(1)
    print("Que voulez vous faire ?")
    time.sleep(1)
    print("\n1) Le nourrir")
    time.sleep(1)
    print("2) Le carresser")
    time.sleep(1)
    choix = int(input("\nEcrivez ici votre choix : "))
    time.sleep(1)
    if choix == 1:
        print("\nQuel type de nourriture utilisez-vous ?")
        time.sleep(1)
        print("\n1) Des granulés")
        time.sleep(1)
        print("2) Un steack")
        time.sleep(1)
        print("3) De la drogue en bonne quantité")
        time.sleep(1)
        choix = int(input("\nEcrivez ici votre choix : "))
        poisson.nourrir(choix)
        time.sleep(1)
    else:
        poisson.caresser()
    poisson.actionFin()
