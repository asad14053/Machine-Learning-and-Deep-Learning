# this is how I generated the data for p3.  You should not run this, otherwise it will generate new data
import random
sensornames = ["Sensor1","Sensor2","Sensor3"]
sensor_last_times = [0,0,0]

f = open("data/p3.txt","w")
for i in range(0,1000):
    #pick a random sensor
    sensor_num = random.choice(range(0,len(sensornames)))
    sensor_time = sensor_last_times[sensor_num] + random.random()*2
    sensor_last_times[sensor_num] = sensor_time
    f.write(f"{sensornames[sensor_num]}\n")
    f.write(f"{sensor_time}\n")
    f.write(f"{random.random()*10}\n")

    