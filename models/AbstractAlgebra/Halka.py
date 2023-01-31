class Halka:
    halka_defination = """
        Halka:
        R1) (R,+) değişmeli grup
        R2) a(bc) = (ab)c
        R3) a(b+c) = ab + ac
        (a+b)c = ac + bc
        """
    halka_examples = """
        Z, Q, R, C
    """
    def __init__(self):
        self.defination = Halka.halka_defination
        self.example = Halka.halka_examples
    
    def __str__(self):
        return self.defination
    
    def char_defination():
        return "n*a = 0 (n ∈ N, a ∈ R) için en küçük n"
    
    def sifir_bolensiz():
        return "a*b = 0 için ya a = 0 ya b = 0 olmalı"
    
