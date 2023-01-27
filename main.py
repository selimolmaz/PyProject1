from models.Homan import Homan
from modules.SayHallo import SayHallo
from modules.PostRequest import Post
from modules.GetRequst import getRequest
from modules.Threading import thread_single, threads_multiple

def main():
    h = Homan("selim", "OLMAZ")
    function1 = h.eat()
    function2 = h.move()
    # thereading 
    threads_multiple(function1, function2)
    #thread_single(print(getRequest("http://api.plos.org/search?q=title:DNA")))
    
    thread_single(Post("key1", "selam çukulatam"))
    
    #Post("say1", h.__str__())
    #print(getRequest("http://api.plos.org/search?q=title:DNA"))
    #bu asenkron çalışsın


if __name__ == "__main__":
    main()