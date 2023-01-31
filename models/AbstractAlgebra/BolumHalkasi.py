from Halka import Halka

class BolumHalkasi(Halka):
    bolumHalkasi_defination = """
        Bölüm Halkası:
        1) Birimli
        2) Tersinir
    """
    def __init__(self):
        self.defination = self.bolumHalkasi_defination
    def __str__(self):
        return self.defination
    


