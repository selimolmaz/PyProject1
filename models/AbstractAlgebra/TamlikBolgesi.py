from Halka import Halka

class TamlikBolgesi(Halka):
    tamlikBolgesi_defination = """
        Tamlık Bölgesi:
        1) Birimli
        2) Değişmeli
        3) Sıfır Bölensiz
    """
    def __init__(self):
        self.defination = TamlikBolgesi.tamlikBolgesi_defination
    
    def __str__(self):
        return self.defination
    
tb = TamlikBolgesi()

print(tb.defination)
