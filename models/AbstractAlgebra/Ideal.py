from models.AbstractAlgebra.AltHalka import AltHalka

class Ideal(AltHalka):
    ideal_defination = """
        İdeal: 
        S < R <->  ∀a,b ∈ S için (a - b) ∈ S
        ∀a ∈ S ve ∀r ∈ R için ar, ra ∈ S 
        sağlanmalı.
    """
    X_ile_uretilen_ideal = """
        X ile üretilen ideal: 
        ∩Ai = (X) şeklinde gösterilir Ai idealleri X kümesini kapsar!
    """
    esas_ideal = """
        Esas İdeal:
        X = { a }  ise (X) = (a) 
    """
    def __init__(self):
        self.defination = Ideal.ideal_defination

    def __str__(self):
        return self.defination
