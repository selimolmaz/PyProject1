import asyncio
from models.AbstractAlgebra.EsasIdealBölgesi import EsasIdealBolgesi

from modules.GetRequst import get

def main():
    #result = get("http://api.plos.org/search?q=title:DNA")
    #print(result)
    eib = EsasIdealBolgesi()
    print(eib.ideal_defination)

if __name__ == "__main__":
    main()