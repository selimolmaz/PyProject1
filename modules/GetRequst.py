import requests

def getRequest(url):
    response = requests.get(url)
    httpCode = response.status_code # HTTP cevabının durum kodunu yazdırır
    json = response.json() # Cevabın JSON verisini yazdırır
    return json