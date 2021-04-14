# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

# import time
#
# t = time.localtime()
# current_time = time.strftime("%H:%M:%S", t)
# print(current_time)
# import time
# import sys
#
# for remaining in range(20, 0, -1):
#     sys.stdout.write("\r")
#     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
#     sys.stdout.flush()
#     time.sleep(1)
#
# sys.stdout.write("\rComplete!            \n")


# # import the time module
# import time
# # define the countdown func.
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#
#     print('Fire in the hole!!')
#
#
# # input time in seconds
# t = input("Enter the time in seconds: ")
#
# # function call
# countdown(int(t))
