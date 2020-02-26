from Arduino import Arduino
import time
'''
Voice recognition Module
'''
board = Arduino(port="COM14")                #COM口根据实际情况修改
while  1:
         ak=board.BettertreeVoice.init(10,11)#(RX,TX)
         print(ak)
         if ak==1:
            print("Ok")  
            break   
while True:
    value=board.BettertreeVoice.GetSpeech()    # listens to the voice input command
    #compare ='7777'
    if value:                                  #compare the value
       board.BettertreeVoice.Passed("0777")    #if =="0777" then voice feedback command
       print(value)                            #print the receive command
    #else:                                     #if no command print not
       #print("not detected")
