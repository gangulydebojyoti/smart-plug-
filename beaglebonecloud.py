import Adafruit_BBIO.ADC as ADC
import time
import urllib
import httplib
 
sensor_pin = 'P9_40'
 
ADC.setup()
 
while True:
    reading = ADC.read(sensor_pin)
    millivolts = reading * 1800  # 1.8V reference = 1800 mV
    temp = (millivolts ) / 10
    params = urllib.urlencode({'field1': temp,'key':'AWNXLEXQRNKN8HH6 '})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    conn.close() 
    print('mv=%d C=%d ' % (millivolts, temp))
    time.sleep(1)
