from models.AbstractAlgebra.EsasIdealHalkasi import EsasIdealHalkası
from models.AbstractAlgebra.TamlikBolgesi import TamlikBolgesi

class EsasIdealBolgesi(EsasIdealHalkası, TamlikBolgesi):
    esas_ideal_bogesi_defination = """
        Esas İdeal Bölgesi:
        1) Esas ideal halksı
        2) Tamlık Bölgesi 
    """
    def __init__(self):
        self.defination = EsasIdealBolgesi.esas_ideal_bogesi_defination
    def __str__(self):
        return self.defination
    
