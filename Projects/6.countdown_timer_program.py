#This is python project number 6
#TITLE:COUNTDOWN TIMER PROGRAM

#It's a countdown timer program using python

import time

my_time = int(input("Enter the time in seconds you would like to countdown: "))

for i in (range(my_time,0,-1)):
    seconds = i % 60
    minutes = int(i/60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)


print("TIME'S UP!")