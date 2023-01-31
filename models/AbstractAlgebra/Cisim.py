from BolumHalkasi import BolumHalkasi

class Cisim(BolumHalkasi):
    cisim_defination = """
        Cisim:
        1) Bölüm halkası
        2) Değişmeli
    """
    cisim_examples = """
        Zp, Q, R, C
    """
    cisim_note1 = """
        Her cisim bir Tamlık Bölgesidir!
    """
    def __init__(self):
        self.defination = Cisim.cisim_defination
        self.examples = Cisim.cisim_examples

    def __str__(self):
        return self.defination 

