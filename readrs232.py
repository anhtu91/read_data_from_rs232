import serial
import web
from serial import SerialException

#For webserver
urls = (
    '/', 'index'
)


class index:
    def GET(self):
        try:
            #Define port serial
            port =serial.Serial(
            '/dev/ttyUSB0', #Get current using usb port: python -m serial.tools.list_ports
            baudrate=9600,
            parity=serial.PARITY_EVEN,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.SEVENBITS,
            timeout=None, xonxoff=0)
            print("Port is open: "+str(port.isOpen()))
            print("Port is readable: "+str(port.readable()))
            if(port.isOpen() and port.readable()):
                b = port.readline()  # read a byte string
                str_decode = b.decode()  # decode byte string into Unicode
                str_result = str_decode.strip("\n").strip("\r").replace("11", "").strip()
                flt_result = float(str_result)/100
                print("Result: "+str(flt_result).replace('.', ','))
                return str(flt_result).replace('.',',')
            else:
                return "Port is not opened"
        except (IOError, OSError) as e:
            return "Error in config input port "+e
        except serial.SerialException as e:
            return "Error in port "+e
        except TypeError as e:
            return "Error "+e
        
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()