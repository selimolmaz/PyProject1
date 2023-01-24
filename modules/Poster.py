import requests
url = 'http://ptsv3.com/t/selam/post/'
data = {}

def Post(key, message):
    data[key] = message
    response = requests.post(url, data=data)
    # Cevabın JSON verisini yazdırır
    # print(response.json()) 
    # HTTP cevabının durum kodunu yazdırır
    return print(response.status_code)