from Halka import Halka

class BolumHalkasi(Halka):
    bolumHalkasi_defination = """
        Bölüm Halkası:
        1) Birimli
        2) Tersinir
    """
    def __init__(self):
        self.defination = BolumHalkasi.bolumHalkasi_defination
    def __str__(self):
        return self.defination
    

bh = BolumHalkasi()
print(bh.halka_defination)
print(bh.bolumHalkasi_defination)

