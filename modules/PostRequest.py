import requests
from modules.Threading import run_in_thread

url = 'http://ptsv3.com/t/selam/post/'
data = {}

@run_in_thread
def Post(key, message):
    data[key] = message
    response = requests.post(url, data=data)
    # Cevabın JSON verisini yazdırır
    # print(response.json()) 
    # HTTP cevabının durum kodunu yazdırır
    return print(response.status_code)