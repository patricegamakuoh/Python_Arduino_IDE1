#!/usr/bin/env python
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import logging
import itertools
import platform
from .Lib import serial
import time

from .Lib.serial.tools import list_ports
if platform.system() == 'Windows':
    import winreg as winreg 
else:
    import glob


log = logging.getLogger(__name__)


def enumerate_serial_ports():
    
    path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
    except WindowsError:
        raise Exception
  
    for i in itertools.count():
        try:
            val = winreg.EnumValue(key, i)
            yield (str(val[1]))  # , str(val[0]))
        except EnvironmentError:
            break


def build_cmd_str(cmd, args=None):
    
    if args:
        args = '%'.join(map(str, args))
    else:
        args = ''
    return "@{cmd}%{args}$!".format(cmd=cmd, args=args)


def find_port(baud, timeout):
    
    if platform.system() == 'Windows':
        ports = enumerate_serial_ports()
    elif platform.system() == 'Darwin':
        ports = [i[0] for i in list_ports.comports()]
    else:
        ports = glob.glob("/dev/ttyUSB*") + glob.glob("/dev/ttyACM*")
    for p in ports:
        log.debug('Found {0}, testing...'.format(p))
        try:
            sr = serial.Serial(p, baud, timeout=timeout)
        except (serial.serialutil.SerialException, OSError) as e:
            log.debug(str(e))
            return str(e)
            continue
        time.sleep(2)
        version = get_version(sr)
        if version != 'version':
            log.debug('Bad version {0}. This is not a Shrimp/Arduino!'.format(
                version))
            sr.close()
            continue
        log.info('Using port {0}.'.format(p))
        if sr:
            return sr
    return None

class Arduino(object):

    def __init__(self, baud=9600, port=None, timeout=2, sr=None):
        
        if not sr:
            if not port:
                sr = find_port(baud, timeout)
                if not sr:
                    raise ValueError("Could not find port.")
            else:
                sr = serial.Serial(port, baud, timeout=timeout)
        sr.flush()
        self.sr = sr
        self.Servos = Servos(self)
        self.Gyro = Gyro(self)
        self.SpeechRecognition= SpeechRecognition(self)
        self.LatticeLED=LatticeLED(self)  
        self.BettertreeVoice=BettertreeVoice(self)

    def digitalWrite(self, pin, val):
        
        if val == "LOW":
            pin_ = -pin
        else:
            pin_ = pin
        cmd_str = build_cmd_str("dw", (pin_,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
           
          
    def analogWrite(self, pin, val):
        
        if val > 255:
            val = 255
        elif val < 0:
            val = 0
        cmd_str = build_cmd_str("aw", (pin, val))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass

    def analogRead(self, pin):
       
        if pin=='A0':
            pin=20
        elif pin=='A1':
            pin=21
        elif pin=='A2':
            pin=22
        elif pin=='A3':
            pin=23
        elif pin=='A4':
            pin=24
        elif pin=='A5':
            pin=25        
        cmd_str = build_cmd_str("ar", (pin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        rd = self.sr.readline()
        rd=rd.decode('gb18030')
        try:
            return int(rd)
        except:
            return 0

    def pinMode(self, pin, val):

        if val == "INPUT":
            if pin=='A0' :
                pin_=20
            elif pin=='A1' :
                pin_=21 
            elif pin=='A2' :
                pin_=22
            elif pin=='A3' :
                pin_=23
            elif pin=='A4' :
                pin_=24
            elif pin=='A5' :
                pin_=25
            else:  
               pin_ = -pin
        else:
            pin_ = pin
        cmd_str = build_cmd_str("pm", (pin_,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            return 0
            pass
        re = self.sr.readline()
        re=re.decode('gb18030')
        try:
            if re!='':
                return 1
        except:
            return 0

    def close(self):
        if self.sr.isOpen():
            self.sr.flush()
            self.sr.close()
            
    def fade_led(self,ledPin):

        cmd_str = build_cmd_str("fd", (ledPin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass

    def Distance_Sense(self,trig,echo):  
        cmd_str = build_cmd_str("ds", (trig,echo,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
       	rd = self.sr.readline()
        rd=rd.decode('gb18030')
        try:
            if rd:
               return rd
        except:
            return 0


    def digitalRead(self, pin):
        
        cmd_str = build_cmd_str("dr", (pin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
    
        rd = self.sr.readline()
       
        rd=rd.decode('gb18030')
        try:
            if rd:
               return int(rd)
        except:
            return 0   

    def tone(self, pin, frequency, durations):
      
        cmd_str = build_cmd_str("tone", (pin, frequency, durations))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
       
    
    def notone(self, pin):
        
        cmd_str = build_cmd_str("notone", (pin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass


    def muBegin(self, type):
       
        if type == "VISION_COLOR_DETECT":
            cmd_str = build_cmd_str("mubegin", (1,))

        elif type == "VISION_COLOR_RECOGNITION":
            cmd_str = build_cmd_str("mubegin", (2,))

        elif type == "VISION_BALL_DETECT":
            cmd_str = build_cmd_str("mubegin", (3,))

        elif type == "VISION_BODY_DETECT":
            cmd_str = build_cmd_str("mubegin", (4,))

        elif type == "VISION_SHAPE_CARD_DETECT":
            cmd_str = build_cmd_str("mubegin", (5,))

        elif type == "VISION_TRAFFIC_CARD_DETECT":
            cmd_str = build_cmd_str("mubegin", (6,))

        elif type == "VISION_NUM_CARD_DETECT":
            cmd_str = build_cmd_str("mubegin", (7,))
            

        else:
            return 0
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
            
        except:
            pass
        
        re = self.sr.readline()
       
        re=re.decode('gb18030')
        try:
            if re:
                return 1
        except:
            return 0

    def muVisionColorSet(self, type):
        
        if type == "MU_COLOR_BLACK":
            cmd_str = build_cmd_str("mucolor", (1,))  

        elif type == "MU_COLOR_WHITE":
            cmd_str = build_cmd_str("mucolor", (2,))  

        elif type == "MU_COLOR_RED":
            cmd_str = build_cmd_str("mucolor", (3,))   

        elif type == "MU_COLOR_YELLOW":
            cmd_str = build_cmd_str("mucolor", (4,))    

        elif type == "MU_COLOR_GREEN":
            cmd_str = build_cmd_str("mucolor", (5,))    

        elif type == "MU_COLOR_CYAN":
            cmd_str = build_cmd_str("mucolor", (6,))

        elif type == "MU_COLOR_BLUE":
            cmd_str = build_cmd_str("mucolor", (7,))
            
        elif type == "MU_COLOR_PURPLE":
            cmd_str = build_cmd_str("mucolor", (8,))    

        else:
            return 0
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
            
        except:
            pass
        
        re = self.sr.readline()
       
        re=re.decode('gb18030')
        try:
            if re:
                return re
        except:
            return 0
    

    def muGetValue(self, type):
       
        if type == "VISION_COLOR_DETECT":
            cmd_str = build_cmd_str("muvalue", (1,))

        elif type == "VISION_COLOR_RECOGNITION":
            cmd_str = build_cmd_str("muvalue", (2,))

        elif type == "VISION_BALL_DETECT":
            cmd_str = build_cmd_str("muvalue", (3,))

        elif type == "VISION_BODY_DETECT":
            cmd_str = build_cmd_str("muvalue", (4,))

        elif type == "VISION_SHAPE_CARD_DETECT":
            cmd_str = build_cmd_str("muvalue", (5,))

        elif type == "VISION_TRAFFIC_CARD_DETECT":
            cmd_str = build_cmd_str("muvalue", (6,))

        elif type == "VISION_NUM_CARD_DETECT":
            cmd_str = build_cmd_str("muvalue", (7,))

        else:
            return 0

        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass

        re = self.sr.readline()
       
        re=re.decode('gb18030')
        try:
            if re:
               return re
        except:
            return 0

    
    def IRstart(self, pin):
      
        cmd_str = build_cmd_str("irstart", (pin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        
        rd = self.sr.readline()
       
        rd=rd.decode('gb18030')
        try:
            if rd:
               return 1
        except:
            return 0

    
    def IRrecv(self, pin):
       
        cmd_str = build_cmd_str("irrecv", (pin,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        
        rd = self.sr.readline()
        try:
            if rd:
               return rd.strip()
        except:
            return 0
               

class Shrimp(Arduino):

    def __init__(self):
        Arduino.__init__(self)

class LatticeLED(object):

    def __init__(self, board):
     
        self.board = board
        self.sr = board.sr
        
    def start(self,pin1,pin2):
        cmd_str = build_cmd_str("ldstart", (pin1, pin2))
      
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        
        rd = self.sr.readline()     
        
        rd=rd.decode('gb18030')
        try:
            if rd:
               return 1
            
        except:
            return 0

        
def display(self,data):
        cmd_str = build_cmd_str("display", (data,))
      
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
      
class Gyro(object):

    def __init__(self, board):
        self.board = board
        self.sr = board.sr
      
    def begin(self):
        
        cmd_str = build_cmd_str("gyrst", (1, ))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
    
        rd = self.sr.readline()
        
        rd=rd.decode('gb18030')
        try:
            if rd:
               return rd
            
        except:
            return 0
      

    def read(self,type):
    
        if type == "x":
            cmd_str = build_cmd_str("gyrdx", (1,))

        elif type == "y":
            cmd_str = build_cmd_str("gyrdy", (2,))

        elif type == "z":
            cmd_str = build_cmd_str("gyrdz", (3,))

        else:
            return 0
      
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        
        rd = self.sr.readline()
            
        rd=rd.decode('gb18030')
        try:
            if rd:
               return rd
            
        except:
            return 0        

class SpeechRecognition(object):

    def __init__(self, board):
     
        self.board = board
        self.sr = board.sr
        
    def begin(self,p1,p2):    
        cmd_str = build_cmd_str("vrset", (p1, p2))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
       
        rd = self.sr.readline()
        
        try:
            if rd:
               return 1
            
        except:
            return 0


    def read(self):
      
        cmd_str = build_cmd_str("vrd", (1,))
      
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        
        rd = self.sr.readline()
        
        rd=rd.decode('gb18030')
        try:
            if rd:
               return rd
            
        except:
            return 0

class BettertreeVoice(object):
    
    def __init__(self, board):
     
        self.board = board
        self.sr = board.sr
        
    def init(self,p1,p2):    
        cmd_str = build_cmd_str("vrinit", (p1, p2))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass
        rd = self.sr.readline()   
        try:
            if rd:
               return 1          
        except:
            return 0

    def GetSpeech(self):
        cmd_str = build_cmd_str("vrget", (1,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass   
        rd = self.sr.readline()  
        rd=rd.decode('gb18030')
        try:
            if rd:
               return rd   
        except:
            return 0

    def Passed(self,feedback):    
        cmd_str = build_cmd_str("vrp", (feedback,))
        try:
            cmd_str=cmd_str.encode()
            self.sr.write(cmd_str)
            self.sr.flush()
        except:
            pass    
        rd = self.sr.readline()
        try:
            if rd:
               return 1     
        except:
            return 0

class Wires(object):
    """
    Class for Arduino wire (i2c) support
    """
    def __init__(self, board):
        self.board = board
        self.sr = board.sr

class Servos(object):
    """
    Class for Arduino servo support
    0.03 second delay noted
    """
    def __init__(self, board):
        self.board = board
        self.sr = board.sr
        self.servo_pos = {}

    def attach(self, pin, min=544, max=2400):
        cmd_str = build_cmd_str("sva", (pin, min, max))

        while True:
            self.sr.write(str.encode(cmd_str))
            self.sr.flush()
            rd = self.sr.readline().decode("utf-8").replace("\r\n", "")
            if rd:
                break
            else:
                log.debug("trying to attach servo to pin {0}".format(pin))
        position = int(rd)
        self.servo_pos[pin] = position
        return 1

    def detach(self, pin):
        position = self.servo_pos[pin]
        cmd_str = build_cmd_str("svd", (position,))
        try:
            self.sr.write(str.encode(cmd_str))
            self.sr.flush()
        except:
            pass
        del self.servo_pos[pin]

    def write(self, pin, angle):
        position = self.servo_pos[pin]
        cmd_str = build_cmd_str("svw", (position, angle))

        self.sr.write(str.encode(cmd_str))
        self.sr.flush()

    def writeMicroseconds(self, pin, uS):
        position = self.servo_pos[pin]
        cmd_str = build_cmd_str("svwm", (position, uS))

        self.sr.write(str.encode(cmd_str))
        self.sr.flush()

    def read(self, pin):
        if pin not in self.servo_pos.keys():
            self.attach(pin)
        position = self.servo_pos[pin]
        cmd_str = build_cmd_str("svr", (position,))
        try:
            self.sr.write(str.encode(cmd_str))
            self.sr.flush()
        except:
            pass
        rd = self.sr.readline().decode("utf-8").replace("\r\n", "")
        try:
            angle = int(rd)
            return angle
        except:
            return None




