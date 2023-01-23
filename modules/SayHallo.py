from models.Homan import Homan

def SayHallo(homanObject):
    if not type(homanObject) == Homan:
        "your parameters is not correct"
    else:
        return print("Hallo my name is" + str(homanObject.name))

