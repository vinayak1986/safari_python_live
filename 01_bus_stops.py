from urllib import request
from xml.etree.ElementTree import XML

url = 'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22'
u = request.urlopen(url)
data = u.read()
doc = XML(data)
for pt in doc.findall('.//pt'):
    print(pt.text) 
