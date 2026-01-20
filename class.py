class Mashina:
    def __init__(self, rang, model, tezlik):
        self.rang = rang
        self.model = model
        self.tezlik = tezlik
#     Metod yaratamiz
#     1 - metod gaz_ber
    def gaz_ber(self, miqdor):
        self.tezlik += miqdor

#      2 - metod tormozla metodi
    def tormozla(self, miqdor):
        self.tezlik -= miqdor
        if self.tezlik < 0:
            self.tezlik = 0

gentra = Mashina("Qora", "Gentra", 200)
nexia = Mashina("Oq", "Nexia 3", 180)
damas = Mashina("Oq", "Damas 2", 300)

damas.gaz_ber(50)
damas.tormozla(400)
print(f"Damas modeli: {damas.model}\nDamas rangi: {damas.rang}\nDamas tezliki: {damas.tezlik} km/s")
print("---------------------------------------------")
nexia.gaz_ber(30)
nexia.tormozla(200)
print(f"Nexia modeli: {nexia.model}\nNexia rangi: {nexia.rang}\nNexia tezliki: {nexia.tezlik} km/s")
print("---------------------------------------------")
gentra.gaz_ber(40)
gentra.tormozla(300)
print(f"Gentra modeli: {gentra.model}\nGentra rangi: {gentra.rang}\nGentra tezliki: {gentra.tezlik} km/s")