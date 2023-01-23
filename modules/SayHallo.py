from models.Homan import Homan
"""
        @Author: Selim The Magnificent
        @Date: 01.24.2023
        @Credit: ["Selim OLMAZ", [Bayram Kuliev]]
        @Links: selimolmazz@gmail.com
"""
def SayHallo(homanObject):
    if not type(homanObject) == Homan:
        "your parameters is not correct"
    else:
        return print("Hallo my name is " + str(homanObject.name))

