from models.AbstractAlgebra.Ideal import Ideal

class EsasIdealHalkası(Ideal):
    esas_ideal_halkasi_defination = f"""
        R halkasının bütün idealleri bir esas ideal ise ({Ideal.esas_ideal}) bu halkaya
        esas ideal halkası denir (Proper Ideal Ring). 
    """
    def __init__(self):
        self.defination = EsasIdealHalkası.esas_ideal_halkasi_defination
    def __str__(self):
        return self.defination

