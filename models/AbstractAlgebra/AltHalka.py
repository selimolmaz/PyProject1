from models.AbstractAlgebra.Halka import Halka

class AltHalka(Halka):
    altHalka_defination = """
        Alt Halka:
        A bir althalka <-> ∀a,b ∈ A için
            a-b ∈ A
            ab ∈ A
    """
    def __init__(self):
        self.defination = AltHalka.altHalka_defination
    def __str__(self):
        return self.defination
    


