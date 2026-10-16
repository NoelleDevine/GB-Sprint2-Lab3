import json
from easytello import tello
from time import sleep

my_drone = tello.Tello()

#this will be a dictionary
myData = {}

my_drone.takeoff()
sleep(.5)

for loc in range (4):
    #go reads the dictionary for the x, y, and z values
    my_drone.go(myData["x"][loc], myData["y"][loc], myData["z"][loc], 25)
    sleep(.5)
    #the append adds to the dictionary 
    myData["pressure"].append(my_drone)
    sleep(.5)
    myData["temp"].append(my_drone)

my_drone.land()
#json_string = json.dumps(myData)
#we should see our new pressure and temperature values in the dictionary 
print(myData)