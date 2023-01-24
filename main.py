from models.Homan import Homan
from modules.SayHallo import SayHallo
from modules.Poster import Post

def main():
    h = Homan("selim", "OLMAZ")
    SayHallo(h)
    print(h.__repr__())
    print(h.__str__())
    print(h.eat())
    Post("say1", h.__str__())

if __name__ == "__main__":
    main()