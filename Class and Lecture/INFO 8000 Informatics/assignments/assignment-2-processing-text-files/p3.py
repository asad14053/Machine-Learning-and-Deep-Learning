# Once again, you'll be reading a text file, but this time, the file is a bit more structured. 
# The data is contained in p3.txt
# It contains sensor values from a system, organized in groups of 3 lines, sensor_id, time, reading
# Your goal is to determine two things about each sensor: the average value and the average time between readings
# You should work in stages to do this, as described belo

# First, open the file, i.e. data = open("data/p3.txt")

# now, create an empty dictionary called "sensors", i.e. sensors = {}

# Next, start a "while" loop that never ends e.g. while True:
    # within that loop, read exactly 1 line into a variable called sensor_name
    # if that value is empty "break" out of the while loop, i.e. if sensor_name == '': break
    # otherwise, read the time and the value with two more calls to readline (make sure you convert them to floats!)
    # next, if the sensor name is not a key in the dictionary, add it and two empty lists for the times and values, i.e. if sensor_name not in sensors.keys(): sensors[sensor_name] = {"times":[],"values":[]}
    # next append the time and value to the designated list, e.g. sensors[sensor_name]["times"].append(time)

# Once you have your sensors dictionary, compute the requested values and print them.  Your solution should be:
#Sensor1: Average value = 4.89, Average Time Delta = 1.05
#Sensor2: Average value = 4.93, Average Time Delta = 0.98
#Sensor3: Average value = 4.94, Average Time Delta = 1.02

# Note that to get sorted output, you need to iterate through the key names in sorted order.  You can get a sorted list of names with keys = sorted(sensors.keys())
# To get time deltas, you can use the following list expression, which assumes ts is the list of times for a particular sensor:   deltas = [ts[i]-ts[i-1] for i in range(1,len(ts))]

data = open("data/p3.txt")  # load data file
sensors ={}
c =1
while True:
    sensor_name = data.readline();   # load sensor name
    if sensor_name =='':        # EOF
        break

    times = float(data.readline());  # load sensor time
    values = float(data.readline())
      # load sensor value
    if sensor_name not in sensors.keys():
        sensors[sensor_name] = {"times":[],"values":[]}  # mapped the new sensor value

    sensors[sensor_name]["times"].append(times)  # append in previous sensor time
    sensors[sensor_name]["values"].append(values)  # append in previous sensor value
    
    keys = sorted(sensors.keys())
    for key in keys:
        deltas = [sensors[key]["times"][i]-sensors[key]["times"][i-1] for i in range(1,len(sensors[key]["times"]))]
        avg = float(sum(sensors[key]["times"])/c)
        print(key,": Average value = ", "Average Time Delta = "+deltas)
    c+=1

