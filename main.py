import urequests, dht
from machine impor Pin

s = dht.DHT11(Pin(14))

s.measure()

temp = s.temperature() 
hum = s.humidity()

temp2 = str(temp)
hum2 = str(hum)
dato = "humeda=" + hum2 + "&temperatura=" + temp2
headers = {'Content-type':"application/x-www-form-urlencoded"}
data = dato

try:
  resp = urequests.post(url, data=data, headers=headers)
  print(resp.status_code)
except:
  pass


