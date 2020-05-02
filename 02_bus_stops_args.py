#!/home/balavinayak/safari_python_live/safari_live/bin/python3
import sys
from urllib import request
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    raise SystemExit('Usage : ./02_bus_stops_args.py route stopid')
route = sys.argv[1]
stopid = sys.argv[2]
url = f'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={stopid}&route={route}'
u = request.urlopen(url)
data = u.read()
doc = XML(data)
for pt in doc.findall('.//pt'):
    print(pt.text)

#test
