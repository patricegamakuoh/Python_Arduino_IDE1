from Arduino import Arduino
import time
'''旋钮程序 '''

board = Arduino(port="COM14")#COM口根据实际情况修改
while 1:
      flag=board.pinMode('A0', "INPUT")#旋钮电阻信号线连接ARDUINO “A0”脚  
      if flag==1:
             print('Start')
             break         
                              
while 1:
   print(board.analogRead('A0'))
   #time.sleep(1)
#board.close()
