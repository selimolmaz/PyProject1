from models.Homan import Homan
from modules.SayHallo import SayHallo
from modules.PostRequest import Post
from modules.GetRequst import getRequest

def main():
    h = Homan("selim", "OLMAZ")
    SayHallo(h)
    print(h.__repr__())
    print(h.__str__())
    print(h.eat())
    Post("say1", h.__str__())
    print(getRequest("http://api.plos.org/search?q=title:DNA"))
    #bu asenkron çalışsın

if __name__ == "__main__":
    main()