import os
import time
from datetime import datetime
import sys

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
os.system('cls')
print('*'*73)
show_time=time.localtime()
print('||||.............WELCOME TO SANDEEP KUMAR PATEL Project..............||||')
print('||||...................TIME IN.- {0}............................||||'.format(current_time))
print('*'*73)
print()
print("Pleace give me some time..")
for remaining in range(3, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining....".format(remaining))
    sys.stdout.flush()
    time.sleep(1)
print()
print('*'*73)
print('Plasce Given Some Information like........')
print()
User_F_name = input("Plsece Enter your Fist Name :- ")
User_M_name = input("Plsece Enter your Midle Name :- ")
User_L_name = input("Plsece Enter your Last Name :- ")
print('Fist Name is :-',User_F_name)
print('Midel Name is :-',User_M_name)
print('Last Name is :-',User_L_name)
Full_Name=User_F_name+' '+User_M_name+' '+User_L_name
print('*'*73)
print("Hello Mr. ",Full_Name)
print('*'*73)
print(f"..........WELCOME TO WORD of ...SANDEEP KUMAR PATEL Project ...................")
print('*'*73)

for remaining in range(5, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)
