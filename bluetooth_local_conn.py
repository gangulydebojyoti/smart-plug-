import urllib,httplib
import Adafruit_BBIO.GPIO as GPIO 
import time 
import serial
import Adafruit_BBIO.UART as UART

GPIO.setup("P8_10",GPIO.OUT) 		
UART.setup("UART1")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=38400)
ser.close()
ser.close()
def startconn():
		global ser
	   	print 'serial is open'
		#ser.write("AT+VERSION?\r\n")
   		ser.write("\r\n+STWMOD=0\r\n")		   ##slave0
   		ser.write("\r\n+STNA=ani\r\n")	   
   		ser.write("\r\n+STPIN=0000\r\n")       	    ##pincode
   		ser.write("\r\n+STOAUT=1\r\n")        ##permit to coonn 
   		ser.write("\r\n+STAUTO=1\r\n") ## Auto-connection forbid
   		ser.write("\r\n+INQ=1\r\n")    ##inquirabl
		time.sleep(2)
		##UART.cleanup()
		ser.flush()
ser.open()
startconn()
	

while True:
 conn = httplib.HTTPConnection("api.thingspeak.com:80")
 conn.request("GET","/channels/27455/fields/1/last?key=CIG83HG9MKW6EUJL")
 response=conn.getresponse()
 data = response.read()

 if (data=='1'):
	print 'Temp senson on'
	GPIO.output("P8_10", GPIO.HIGH)
	ser.write("o")

	##time.sleep(0.5)

 if (data=='0'):
	print 'Temp sensor off'
	GPIO.output("P8_10", GPIO.LOW)
	ser.write("f")
    	##time.sleep(0.5) 


conn.close()

 
