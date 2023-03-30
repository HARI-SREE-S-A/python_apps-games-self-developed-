import random
import autopy
import datetime




time = int(input("enter the loop in x 100 ")
lock = int(input("enetr t- sec your screen lock time ")

           
x = list(range(200,700))
y  = list(range(300,500))


ctime = datetime.datetime.now()

for i in range(time):
    x1 = random.choice(x)
    y1 = random.choice(y)
    autopy.mouse.move(x1,y1)
    time.sleep(2)



print(ctime.time())



