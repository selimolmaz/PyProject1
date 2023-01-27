from models.Animals import Animals
"""
        @Author: Selim The Magnificent
        @Date: 01.24.2023
        @Credit: ["Selim OLMAZ", [Bayram Kuliev]]
        @Links: selimolmazz@gmail.com
"""
# Polimorphism
class Homan(Animals):
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.lastName = last_name 
    def __repr__(self):
        return print(f"Homan({self.name}, {self.lastName})")
    
    def __str__(self):
        return print(f"hey there my name is: {self.name} {self.lastName}, i appreciate to let me alive!")
    