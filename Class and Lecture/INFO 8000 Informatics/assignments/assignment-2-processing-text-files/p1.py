# Program 1
# The data folder contains a file named p1.txt
# Write a program that opens this file and displays its contents using the "print" function, but it should skip any line that begins with #.  

data = open("data/p1.txt") #do not modify this line, which opens the file
#insert your code here
s = data.readlines()
i = ""
 
for line in s:
    for c in line:
        if(c == '#'):   #check every character if it is a '#' or not.
            break
        elif (c=='\n' or c == ' '): # remove extra newline and space to get rid of indentation/ presentation error in output.
            continue
        else:
            print(c)


data.close() #good practice to close files you open