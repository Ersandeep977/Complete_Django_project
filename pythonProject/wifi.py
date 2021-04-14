import sys
import os

command_1 = 'cd/'
c = os.system(command_1)
print(c)
command_2 ='netsh wlan show profile'
command_2 ='netsh wlan show profile Provoke IT Solutions key=clear'
d = os.system(command_2)
#sys.stdout=open("test.txt","w")
print(d)
#sys.stdout.close()