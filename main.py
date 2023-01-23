from models.Homan import Homan
from modules.SayHallo import SayHallo


def main():
    h = Homan("selim", "OLMAZ")
    SayHallo(h)
    print(h.__repr__())
    print(h.__str__())
if __name__ == "__main__":
    main()